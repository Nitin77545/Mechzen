from rest_framework import generics
from .models import Service,Mechanic,Profile
from .serializers import ServiceSerializer,MechanicSerializer,ProfileSerializer,UserProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from django.contrib.auth.models import User

class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDetailView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = "title"
class MechanicListView(generics.ListAPIView):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializer

class MechanicDetailView(generics.RetrieveAPIView):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializer
    lookup_field = "id"

class PublicProfileUpdate(APIView):
    permission_classes = []  # 🚨 No auth (testing only)

    def put(self, request, user_id= None):
        try:
            profile = Profile.objects.get(user__id=user_id)
        except Profile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=404)

        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)