from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Development
from .serializers import DevelopmentSerializer

class DevelopmentListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        developments = Development.objects.all()
        serializer = DevelopmentSerializer(developments, many=True)
        return Response(serializer.data)
