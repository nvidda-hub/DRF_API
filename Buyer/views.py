from django.shortcuts import render 
from django.http import HttpResponse, JsonResponse 
from rest_framework.parsers import JSONParser 
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.views import APIView 
from rest_framework import generics, mixins 
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication 
from rest_framework.permissions import IsAuthenticated 
from rest_framework import viewsets 
from apiDev.models import Store
from Buyer.buyer_serializers import StoreSerializer



class StoreDetailView(APIView):     
    def get(self, request, link): 
        store = list(Store.objects.all().filter(store_link=link).values())
        store_serializer = StoreSerializer(store) 

        return Response(store)         