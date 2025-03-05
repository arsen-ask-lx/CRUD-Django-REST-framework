from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CRUDView

router = DefaultRouter()
router.register(r'tasks', CRUDView, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
]
