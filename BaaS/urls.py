from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name="baas-register"),
    path('profile/<int:pk>/', views.profile, name="baas-profile"),
    path('profile/subscription/', views.updateSubscription, name="baas-subscription"),
    path('profile/payment/', views.paymentInfo, name="baas-payment"),
    path('profile/payment/delete/<int:pk>/', views.deletePaymentInfo, name="baas-payment-delete"),

    #Default login and logout handlers from Django
    path('login/', auth_views.LoginView.as_view(template_name='BaaS/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),

    path('', views.home, name='baas-home')    
]