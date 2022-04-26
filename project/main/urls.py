from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='fanfics'),
    path('tables/', views.tables),
    path('form/', views.form),
    path('search/', views.search, name='search'),
    path('tag/', views.tag, name='search_tags')

]
