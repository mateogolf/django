"""Books views.py"""
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Author,Book,Review
from ..users.models import User
# Create your views here.
def index(request):
    #Users-id,alias, Recent Reviews (3), Other Books with reviews

    user = User.objects.get(id=request.session['id'])
    context = {
        # 'id': user.id,
        'alias': user.alias,
        'reviews': Review.objects.order_by('-created_at')[:3],
        'other_books': Book.objects.filter(reviews__isnull=False),
        'rating': 'xxxxx'
    }
    print context['reviews']
    print context['other_books']
    # #Find 3 most recent reviews
    # # context['reviews'] = Review.objects.order_by('-created_at')[:3]
    # # context['other_books'] = Book.objects.filter(reviews_isnull=False)

    # Removes books already on recent from this list
    for recent in context['reviews']:
        context['other_books'] = context['other_books'].exclude(id=recent.book.id)
        # print context['reviews'][i].book.id
        # context['other_books'].exclude(id=context['reviews'][i].book.id)

    return render(request,'books/index.html',context)

def new(request):
    context ={'authors': Author.objects.all()}
    return render(request, 'books/edit.html',context)

def create(request):
    if request.method == "POST":
        errors = Review.objects.basic_validator(request.POST)
        if len(errors):
            context = {
                'title': request.POST['title'],
                'author_name': request.POST['author_name'],
                'content': request.POST['content'],
            }
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
                print tag + ": " + error
            return render(request, 'books/edit.html', context)
        else:
            #Create author,book, review and save after each
            user = User.objects.get(id=request.session['id'])
            if request.POST['author_name']:
                author = Author(name=request.POST['author_name'])
                author.save()
                # author = Author.objects.get(name=request.POST['author_name'])
            else:
                author = Author.objects.get(id=request.POST['author_id'])
            newBook = Book(title = request.POST['title'],author = author)
            newBook.save()
            print newBook
            newReview = Review(
                user=user,
                book=newBook,
                content=request.POST['content'],
                rating=request.POST['rating']
            )
            newReview.save()

            return redirect('/books')
    else:
        return redirect('/books')


def show(request,book_id):
    #Book title and author, reviews
    book = Book.objects.get(id=book_id)
    context={
        'id': book.id,
        'title': book.title,
        'author': book.author.name,
        'reviews': book.reviews.all(),
        'rating': 'xxxxx'
    }
    return render(request,'books/book.html',context)


def createReview(request,book_id):
    if request.method == "POST":
        book = Book.objects.get(id=book_id)
        errors = Review.objects.review_validator(request.POST)
        if len(errors):
            context = {
                'id': book.id,
                'title': book.title,
                'author': book.author.name,
                'reviews': book.reviews.all(),
                'content': request.POST['content'],
                'rating': 'xxxxx'
            }
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
                print tag + ": " + error
            return render(request, 'books/book.html', context)
        else:
            #Create author,book, review and save after each
            user = User.objects.get(id=request.session['id'])
            newReview = Review(
                user=user,
                book=book,
                content=request.POST['content'],
                rating=request.POST['rating']
            )
            newReview.save()

            return redirect('/books/'+book_id)
    else:
        return redirect('/books/'+book_id)

def destroyReview(request,book_id,review_id):
    review = Review.objects.get(id=review_id)
    review.delete()
    return redirect('/books/{{book_id}}')
