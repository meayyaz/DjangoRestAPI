from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'pixels', views.PixelViewSet)
router.register(r'pixels_post', views.PixelPostDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
