from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import AllPosts, AllPostsDetail

app_name = "reports"

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.login_user, name='login_user'),  
    path('activate/<str:uidb64>/<str:token>/', views.activate_account, name='activate'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('sign-up', views.signup, name='register_user'),
    path("welcome", views.welcome, name='welcome'),
    path("activate-email", views.activate_email, name='activate_email'),
    path("all-posts", AllPosts.as_view(), name="all_posts"),
    path('all-posts/<int:pk>', AllPostsDetail.as_view(), name="all_posts_detail"),
    path('logout', views.logout_user, name="logout_user")
]