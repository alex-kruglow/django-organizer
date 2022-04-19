from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(),
        name='login',
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout',
    ),
    path(
        'password-change/',
        auth_views.PasswordChangeView.as_view(),
        name='password-change',
    ),
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(),
        name='password-reset',
    ),
    path(
        'password-reset-done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password-reset-done',
    ),
    path(
        'reset/<uid64>/<token/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='reset',
    ),
    path(
        'reset-done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='reset-done',
    ),
    path(
        'register/',
        views.register,
        name='register',
    ),
]
