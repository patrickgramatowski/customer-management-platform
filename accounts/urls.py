from django.urls import path

from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    # Create, Login/out, settings and profile user staff 
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user_profile/', views.userProfile, name="user_profile"),
    path('profile_settings/', views.accountSettings, name="profile_settings"),
    
    # main sites
    path('', views.home, name ="home"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk>/', views.customer, name="customer"),

    # CRUD for orders, admin site
    path('createOrder/<str:pk>/', views.createOrder, name="createOrder"),
    path('updateOrder/<str:pk>/', views.updateOrder, name="updateOrder"),
    path('delete/<str:pk>/', views.deleteOrder, name="delete"),


    # SMTP / path to reset password by email
    path('reset_password/', 
    auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), 
    name="reset_password"),
    path('reset_password_sent/', 
    auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'), 
    name="password_reset_done"),
    path('reset/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'), 
    name="password_reset_confirm"),
    path('reset_password_complete/', 
    auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'), 
    name="password_reset_complete"),
]