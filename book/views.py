from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .models import Author, Books, Category
from rest_framework.response import Response
from . serializer import BooksSerializer
from rest_framework import viewsets
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist


class BooksViewSet(viewsets.ModelViewSet):

	"""
	Viewset to get and post books
	"""
	model = Books
	serializer_class = BooksSerializer

	def get_queryset(self, *args, **kwargs):	
		queryset = Books.objects.all()
		query = self.request.GET.get('author_name')
		query1 = self.request.GET.get('categories_value')
		try:
			if query:
				author_obj = Author.objects.get(name__exact=query)
				if query1:
					cat_obj = Category.objects.get(category__exact=query1)
					return queryset.filter(author_name=author_obj, categories=cat_obj)		
				return queryset.filter(author_name=author_obj)				
			elif query1:
				cat_obj = Category.objects.get(category__exact=query1)
				return queryset.filter(categories=cat_obj)	
			else:
				return queryset
		except ObjectDoesNotExist:
			print "Opps ! objects you are looking doesnot exists"

	def create(self, *args, **kwargs):

		# print self.request.data
		"""
		data = {'title': self.request.data.get('title'),
		'categories': self.request.data.get('categories'),
		'author_name': self.request.data.get('author_name')
		}
		"""
	
		serializer = BooksSerializer(data=self.request.data)
		if not serializer.is_valid():
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		data = serializer.data
		title = Books.objects.create(title =data.get('title')) 
		cat = Category.objects.get(id=int(data.get('categories')))
		auth = Author.objects.get(id=int(data.get('author_name')))
		
		title.save()
		
		title.categories.add(cat)
		title.author_name.add(auth)
		return Response({'msg': 'created'})

	def retrieve(self, request, pk=None):

		queryset = get_object_or_404(self.model, pk=pk)
		serializer = BooksSerializer(queryset)
		return Response(serializer.data)



"""
	@api_view(['GET','POST'])
	def AllBookList(request):
		books = Books.objects.all()
		serializer = BooksSerializer(books,many=True)
		return Response(serializer.data)

	queryset = Books.objects.all()
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



self.serializer_class = BooksSerializer
		item = get_object(pk=pk)
		serializer = self.serializer_class(item)
		data = serializer.data
		return Response(data)

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

"""