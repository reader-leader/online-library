from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='fanfics'),
    path('tables/', views.tables),
    path('form/', views.form, name='form'),
    path('search/', views.search, name='search'),
    path('tag/', views.tag, name='search_tags'),
    path('<int:id>', views.fanfic_detail, name='fanfic_detail'),
    path('favorites/', views.favorites, name='favorites'),
    path('random/', views.randoms, name='random'),
    path('my/', views.my_fanfics, name='my_fanfics')
]
