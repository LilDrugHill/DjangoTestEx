from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView
# Create your views here.

class TaskDetailView(RetrieveAPIView):
    serializer_class =
