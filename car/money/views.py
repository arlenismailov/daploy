from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class CarorSparepartsView(ModelViewSet):
    queryset = CarorSpareparts.objects.all()
    serializer_class = CarorSparepartsSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['price', 'brand', 'model']
    search_fields = ['title']


