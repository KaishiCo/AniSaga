from django.urls import path
from . import views



app_name = "anisaga"
urlpatterns = [
	path('', views.AboutView.as_view(), name="home"),
]