from django.urls import path

from app_users import views


urlpatterns = [
    path('', views.MainPageView.as_view(), name='main_page'),
    path('users/login/', views.user_login_view, name='user_login'),
    path('users/another-login/', views.AnotherUserLoginView.as_view(), name='another-user_login'),
]
