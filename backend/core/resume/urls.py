from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.Resume_details_view)

urlpatterns = [
    path('', include(router.urls)),
]
