from rest_framework import serializers
from .models import Author, Books, Category


class CategorySerializer(serializers.ModelSerializer):

	class Meta :
		model = Category


class AuthorSerializer(serializers.ModelSerializer):	
	
	class Meta:
		model = Author 


class BooksSerializer(serializers.ModelSerializer):

	categories = CategorySerializer(read_only=True, many=True)
	author_name = AuthorSerializer(read_only=True, many=True)

	class Meta:
		model = Books




"""
	categories = serializers.CharField(required=True)
	author_name = serializers.CharField(required=True)
	title = serializers.CharField(required=True)
"""
