from rest_framework import status
from rest_framework.response import Response 
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from movielist_app.models import CollectionList, StreamPlatform
from .serializers import CollectionListSerializer, StreamPlatformSerializer


class StreamListAV(APIView):
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class StreamDetailAV(APIView):
    def get(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)
    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.deleteK()
        return Response({"Congrats": "Deleted Succesfully"})
    
        
        


#Using class based view
class CollectionListAV(APIView):
    def get(self, request):
        movies = CollectionList.objects.all()
        serializer = CollectionListSerializer(movies, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CollectionListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
class CollectionDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = CollectionList.objects.get(pk=pk)
        except CollectionList.DoesNotExist:
            return Response({"Eror": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer=CollectionListSerializer(movie)
        return Response(serializer.data)
    def put(self, request, pk):
        movie = CollectionList.objects.get(pk=pk)
        serializer = CollectionListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        movie = CollectionList.objects.get(pk=pk)
        movie.delete()
        return Response({"Congrats": "Movie Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)
        
        






# # Using Function based views
# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many =True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk = pk)
#         except Movie.DoesNotExist:
#             return Response({'Error': 'Movie not Found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
    
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)