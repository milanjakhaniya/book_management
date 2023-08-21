from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Author, Category, Book
import json

# Author views
@csrf_exempt
def all_authors(request):
    authors = Author.objects.all()
    authors_list = list(authors.values("id", "name"))
    return JsonResponse(authors_list, safe=False)


@csrf_exempt
def add_author(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_author = Author(name=data['name'])
        new_author.save()
        return JsonResponse({'message': 'Author created successfully'}, status=201)


@csrf_exempt
def update_author(request, author_id):
    if request.method == 'POST':
        author = Author.objects.get(id=author_id)
        data = json.loads(request.body)
        author.name = data['name']
        author.save()
        return JsonResponse({'message': 'Author updated successfully'}, status=200)


@csrf_exempt
def delete_author(request, author_id):
    if request.method == 'DELETE':
        author = Author.objects.get(id=author_id)
        author.delete()
        return JsonResponse({'message': 'Author deleted successfully'}, status=200)


# Category views
@csrf_exempt
def all_categories(request):
    categories = Category.objects.all()
    categories_list = list(categories.values("id", "cat_name"))
    return JsonResponse(categories_list, safe=False)


@csrf_exempt
def add_category(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_category = Category(cat_name=data['cat_name'])
        new_category.save()
        return JsonResponse({'message': 'Category created successfully'}, status=201)


@csrf_exempt
def update_category(request, category_id):
    if request.method == 'POST':
        category = Category.objects.get(id=category_id)
        data = json.loads(request.body)
        category.cat_name = data['cat_name']
        category.save()
        return JsonResponse({'message': 'Category updated successfully'}, status=200)


@csrf_exempt
def delete_category(request, category_id):
    if request.method == 'DELETE':
        category = Category.objects.get(id=category_id)
        category.delete()
        return JsonResponse({'message': 'Category deleted successfully'}, status=200)




def all_books(request):
    books = Book.objects.all()
    books_list = list(books.values("id", "book_name", "book_description", "author__name", "categories__cat_name"))
    return JsonResponse(books_list, safe=False)


@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        author = Author.objects.get(id=data['author_id'])
        new_book = Book(book_name=data['book_name'], book_description=data['book_description'], author=author)
        new_book.save()
        for cat_id in data['category_ids']:
            category = Category.objects.get(id=cat_id)
            new_book.categories.add(category)
        return JsonResponse({'message': 'Book created successfully'}, status=201)


@csrf_exempt
def update_book(request, book_id):
    if request.method == 'POST':
        book = Book.objects.get(id=book_id)
        data = json.loads(request.body)
        book.book_name = data['book_name']
        book.book_description = data['book_description']
        book.author = Author.objects.get(id=data['author_id'])
        book.categories.clear()
        for cat_id in data['category_ids']:
            category = Category.objects.get(id=cat_id)
            book.categories.add(category)
        book.save()
        return JsonResponse({'message': 'Book updated successfully'}, status=200)


@csrf_exempt
def delete_book(request, book_id):
    if request.method == 'DELETE':
        book = Book.objects.get(id=book_id)
        book.delete()
        return JsonResponse({'message': 'Book deleted successfully'}, status=200)