from django.conf.urls import url, include
from django.contrib import admin
from book import views 
from rest_framework import routers
from book.views import BooksViewSet

"""
router = routers.DefaultRouter()
router.register(r'books', BookList)
"""


urlpatterns = [
    url(r'^admin/', admin.site.urls),   
    #url(r'^books/(?P<pk>[0-9]+)/$', views.BooksViewSet.as_view({'get': 'retrieve'})),
    url(r'^books/', views.BooksViewSet.as_view({'get': 'list'})),
    #url(r'^books/', views.BookList.as_view()),
    #url(r'^books/(?P<author_name>[\w]+)/', views.BookList),
    # url(r'^books/(?P<author_name>[\w]+)/(?P<categories_value>[\w]+)	/', views.BookList), 
    #url(r'^',include(router.urls))
    
    
]