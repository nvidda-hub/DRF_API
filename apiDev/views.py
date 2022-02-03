from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from apiDev.models import Article
from apiDev.serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets




# function based views 

# # @csrf_exempt
# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == "GET":
#         articles = Article.objects.all()
#         # serializing articles which is query set
#         serializer = ArticleSerializer(articles, many=True)
#         # return JsonResponse(serializer.data, safe=False)
#         return Response(serializer.data)                    # because using api_view()
    
#     elif request.method == "POST":
#         # data = JSONParser().parse(request)
#         # serializer = ArticleSerializer(data=data)
#         serializer = ArticleSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             # return JsonResponse(serializer.data, status = 201)  # 201 -> means created
#             return Response(serializer.data, status = status.HTTP_201_CREATED)  # 201 -> means created
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(["GET", "PUT", "DELETE"])
# def article_detail(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
    
#     # to update the article data
#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return JsonResponse(serializer.errros, status=status.HTTP_404_NOT_FOUND)

#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# generic viewsets

# class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()


# Modal viewsets

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    


# generic view

# class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()
#     # authentication_classes = [SessionAuthentication, BasicAuthentication]
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     lookup_field = 'id'

#     def get(self, request, id=None):
#         if id:
#             return self.retrieve(request)
#         else:
#             return self.list(request)

#     def post(self, request):
#         return self.create(request)

#     def put(self, request, id):
#         return self.update(request, id)
    

#     def delete(self, request):
#         return self.destroy(request, id)

# class based view

# class ArticleAPIView(APIView):

#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)  
    
#     def post(self, request):
        
#         serializer = ArticleSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)  # 201 -> means created
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ArticleDetailView(APIView):

#     def object_id(self, id):
#         try:
#             return Article.objects.get(id=id)
#         except Article.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
#     def get(self, request, id):
#         article = self.object_id(id)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)        

#     def put(self, request, id):
#         article = self.object_id(id)
#         serializer = ArticleSerializer(article, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errros, status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request, id):
#         article = self.object_id(id)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)