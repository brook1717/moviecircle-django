from django.urls import path, include
# from movielist_app.api.views import movie_list, movie_details
from movielist_app.api.views import CollectionListAV, CollectionDetailAV, StreamListAV, StreamDetailAV
urlpatterns = [
    # path('list/', movie_list, name='movie-list'),
    path("stream/", StreamListAV.as_view(), name='stream-list'),
    path('stream/<int:pk>', StreamDetailAV.as_view(), name='stream-details'),
    path('list/', CollectionListAV.as_view(), name='movie-list'),
    
    path('list/<int:pk>', CollectionDetailAV.as_view(), name='movie-details')
]
