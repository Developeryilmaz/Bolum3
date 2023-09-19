from django.urls import path, include
from api.views import ProfileViewSet, StatusMessageViewSet, ProfilePhotoUpdateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'status', StatusMessageViewSet, basename='status')

urlpatterns = [
    path('', include(router.urls)),
    path('profile_photo/', ProfilePhotoUpdateView.as_view(), name='profile-update')
]
