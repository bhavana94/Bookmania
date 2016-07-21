from django.conf.urls import url, include
from django.contrib import admin
from book import views 



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^books/', views.BookList),
    url(r'^books/(?P<author_name>[\w]+)/', views.BookList),
    url(r'^books/(?P<author_name>[\w]+)/(?P<categories_value>[\w]+)/', views.BookList)
]