from django.urls import path
from .views import ItemSetView



urlpatterns = [
	path("", ItemSetView.as_view()), 
]

