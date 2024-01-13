from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shoe/<str:pk>/', views.viewShoe, name="shoe"),
    path('login/', views.loginPage , name="login"),
    path('register/', views.register , name="register"),
    path('logout/', views.logoutUser , name="logout"),

]
