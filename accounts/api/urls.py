from django.urls import path
from accounts.api import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.UserLogin.as_view(), name='login')
]