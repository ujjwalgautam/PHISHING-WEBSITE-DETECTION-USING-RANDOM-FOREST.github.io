from django.urls import path, include
from . import views

urlpatterns = [
    path('phish/', views.predict),
    path('', views.login_view),
    path('adminpanel/',views.adminpanel),
    path('extractfeat/',views.extractfeat),
    path('predictURL/',views.predictURL)
]
