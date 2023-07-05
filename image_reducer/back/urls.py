from django.urls import path, include
from rest_framework.routers import SimpleRouter
from back.views import ReducerViewSet

router = SimpleRouter()
router.register(r'resize_picture', ReducerViewSet, basename='resize_picture')

urlpatterns = [
    path(r'', include(router.urls)),
]
