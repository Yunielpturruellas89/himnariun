from django.urls import path
from rest_framework import routers
from .views import HymnViewSet

router = routers.DefaultRouter()
router.register(r'hymns', HymnViewSet) #  'hymns' es el prefijo de la URL
urlpatterns = router.urls