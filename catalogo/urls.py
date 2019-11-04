from django.urls import path 
from . import views

urlpatterns=[
	path('',views.index,name='index'),
	#path('books/', views.BookListView.as_view(), name='books'),
    #path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
	path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
	path('',views.index,name='index'),
	path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]



urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]


'''
# Add URLConf for librarian to renew a book.
urlpatterns += [
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]


urlpatterns += [   
    path(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
]
'''