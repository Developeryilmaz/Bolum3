from rest_framework.permissions import IsAuthenticated
from api.models import Profile, StatusMessage
from api.serializers import ProfileSerializer, StatusMessageSerializer, ProfilePhotoSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, generics
from api.permissions import OwnProfileOrReadOnly, OwnStatusOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter


class ProfileViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, OwnProfileOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['city']


class StatusMessageViewSet(ModelViewSet):
    serializer_class = StatusMessageSerializer
    permission_classes = [IsAuthenticated, OwnStatusOrReadOnly]

    def get_queryset(self):
        queryset = StatusMessage.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(profile__user__username=username)
        return queryset

    def perform_create(self, serializer):
        profile = self.request.user.profile
        serializer.save(profile=profile)


class ProfilePhotoUpdateView(generics.UpdateAPIView):
    serializer_class = ProfilePhotoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object
