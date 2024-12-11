from rest_framework import generics, permissions
from .models import Journey
from .serializers import JourneySerializer
from drf_app.permissions import IsOwnerOrReadOnly

# List all public journeys or create a new one
class JourneyListCreateView(generics.ListCreateAPIView):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Retrieve, update, or delete a journey
class JourneyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]