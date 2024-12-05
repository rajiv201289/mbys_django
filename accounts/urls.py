from django.urls import path , include
from . import views

# Creating urls for accounts app 

app_name = 'accounts'
urlpatterns = [
    # Include default auth urls
    path('',include('django.contrib.auth.urls')),
]
