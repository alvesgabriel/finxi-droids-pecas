from backend.adverts import models, serializers
from backend.adverts.permissions import IsOwner
from rest_framework import generics, permissions, viewsets


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AddressSerializer
    queryset = models.Address.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AdvertViewSet(viewsets.ModelViewSet):
    queryset = models.Advert.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return serializers.AdvertInfoSerializer
        return serializers.AdvertSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AdvertFinalizeDetail(generics.UpdateAPIView):
    serializer_class = serializers.AdvertFinalizeSerializer
    queryset = models.Advert.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwner]
