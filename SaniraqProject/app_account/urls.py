from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from app_account import views

app_name = 'accounts'
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('register/verify/', views.UserVerificationView.as_view(), name='user_register_verify'),

    path('forget-password/', views.UserForgetPassword.as_view(), name='forget_password'),
    path('forget-password/verify/', views.UserVerificationPasswordView.as_view(), name='forget_password_verify'),

    path('change-password/', views.UserChangePassword.as_view(), name='change_password'),

    path('edit-profile/', views.UserEditProfileView.as_view(), name='edit_user'),
]