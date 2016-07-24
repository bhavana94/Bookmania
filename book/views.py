from django.shortcuts import render
from rest_framework.views import APIView 
from .models import Author, Books, Category
from rest_framework.response import Response
from . serializer import BooksSerializer
from rest_framework import generics, viewsets

"""
class BookList(APIView):

	def get(self, request):
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
		elif query1:
			cat_obj = Category.objects.get(category=query1)
			serializer = BooksSerializer(
				booklist.filter(categories=cat_obj), many=True)
			return Response(serializer.data)

		else:
			serializer = BooksSerializer(booklist, many=True)
			return Response(serializer.data)

	def post(self, request):
		return "Hellos"



"""
class BooksViewSet(viewsets.ModelViewSet):

	queryset = Books.objects.all()
	serializer_class = BooksSerializer

	def get_queryset(self, *args, **kwargs):	
		queryset = Books.objects.all()
		query = self.request.GET.get('author_name')
		query1 = self.request.GET.get('categories_value')
		if query:
			author_obj = Author.objects.get(name=query)
			if query1:
				cat_obj = Category.objects.get(category=query1)
				return  queryset.filter(author_name=author_obj, categories=cat_obj)					
			
			return queryset.filter(author_name=author_obj)
			
		elif query1:
			cat_obj = Category.objects.get(category=query1)
			return queryset.filter(categories=cat_obj)	
		else:
			return queryset

"""
	def create(self, *args, **kwargs):

		data = { 'title':self.request.title, 
		'categories': self.request.categories, 
		'author_name' : self.request.author_name 
		}
		serializer = BooksSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
	
	"""		



"""
@api_view(['GET','POST'])
def AllBookList(request):
	books = Books.objects.all()
	serializer = BooksSerializer(books,many=True)
	return Response(serializer.data)
"""	
	


