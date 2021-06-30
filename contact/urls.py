from django import urls
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('add-contact/', views.add_contact, name='add-contact'),
    path('profile/<str:pk>/', views.contact_profile, name='profile'),
    path('edit-contact/<str:pk>', views.edit_contact, name='edit-contact'),
    path('delete/<str:pk>', views.delete_contact, name='delete-contact')
]
