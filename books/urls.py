from django.urls import include, path
from rest_framework import routers

from .views import AuthorViewSet, BookViewSet


router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]