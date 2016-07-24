from django.conf.urls import url, include
from django.contrib import admin
from book import views 
from rest_framework import routers
from book.views import BookList

"""
router = routers.DefaultRouter()
router.register(r'books', BookList)
"""


urlpatterns = [
    url(r'^admin/', admin.site.urls),   
    url(r'^books/', views.BookList.as_view({'get': 'get'})),
     url(r'^books/', views.BookList.as_view({'post': 'post'})),
    #url(r'^books/(?P<author_name>[\w]+)/', views.BookList),
    # url(r'^books/(?P<author_name>[\w]+)/(?P<categories_value>[\w]+)	/', views.BookList), 
    #url(r'^',include(router.urls))
    
    
]