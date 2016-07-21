from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Author, Books, Category
from rest_framework.response import Response
from . serializer import BooksSerializer
from rest_framework import generics


@api_view(['GET','POST'])
def BookList(request):
	booklist = Books.objects.all()
	query = request.GET.get('author_name')
	query1 = request.GET.get('categories_value')
	if query:
		author_obj = Author.objects.get(name=query)
		if query1:
			cat_obj = Category.objects.get(category=query1)
			serializer = BooksSerializer(
				booklist.filter(author_name=author_obj, categories=cat_obj), many=True)
			return Response(serializer.data)
		serializer = BooksSerializer(
			booklist.filter(author_name=author_obj), many=True)
		return Response(serializer.data)
	else:
		serializer = BooksSerializer(
			booklist.filter(categories=cat_obj), many=True)
		return Response(serializer.data)



	


