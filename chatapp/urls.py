from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_view, name='base_view'), # Default path
    path('messages/', views.messages_view, name='messages_view'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('user_profile/', views.user_profile_view, name='user_profile_view'),
]

