from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):

	category = models.CharField(max_length=200)

	def __str__(self):
		return '%s :'%(self.category)


class Author(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	email = models.EmailField()
	
	def __str__(self):
		return '%s :'%(self.name)

class Books(models.Model):

	title = models.CharField(max_length=200)
	categories = models.ManyToManyField(Category)
	author_name = models.ManyToManyField(Author)

	def __str__(self):
		return '%s :'%(self.title)
