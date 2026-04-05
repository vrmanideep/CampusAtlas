from django.urls import path
from django.contrib.auth import views as auth_views # ADD THIS LINE
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='home'), # Pointing home to dashboard
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('api/search/', views.search_location_api, name='search_location_api'),
    path('profile/', views.profile_view, name='profile'),
    
    # Password Change URLs
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='main/password_change.html'), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='main/password_change_done.html'), name='password_change_done')
]