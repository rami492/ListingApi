from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api1 import views
from knox import views as knox_views
#from rest_framework.urlpatterns import format_suffix_patterns

# Create a router and register our ViewSets with it.
router = DefaultRouter()

router.register(r'listings', views.ListingViewSet, basename='listing')
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'register', views.RegisterViewSet, basename='register')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path(r'login/', views.LoginView.as_view(), name='knox_login'),
    path(r'logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path(r'logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    
]