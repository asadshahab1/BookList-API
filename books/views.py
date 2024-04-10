from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse
from .models import Books
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

@csrf_exempt
def books(request):
    if request.method == 'GET':
        books = Books.objects.all().values()
        return JsonResponse({'books':list(books)})
    elif request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        author = request.POST.get('author')
        inventory = request.POST.get('inventory')
        book = Books(title = title, price=price,author = author,inventory = inventory)
        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'},status=400)
        return JsonResponse(model_to_dict(book),status = 201)