from django.urls import path, include
from . import views

app_name = 'user'
app_name = 'saddmin'
urlpatterns = [
    path('index/', views.index),
    path('about/', views.about),
    path('description/<int:id>/', views.propertydetail, name="details"),
    path('contact/', views.contact),
    path('enquiry/<str:id>', views.post_enqiry, name='post'),
]