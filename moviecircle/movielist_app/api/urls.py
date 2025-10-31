from django.urls import path, include
# from movielist_app.api.views import movie_list, movie_details
from rest_framework.routers import DefaultRouter
from movielist_app.api.views import CollectionListAV, CollectionDetailAV, StreamListAV, StreamDetailAV, ReviewList, ReviewDetail, ReviewCreate, StreamListVS


router = DefaultRouter()
router.register('stream', StreamListVS,basename='streamplatform')




urlpatterns = [
    # path('list/', movie_list, name='movie-list'),
    # path("stream/", StreamListAV.as_view(), name='stream-list'),
    # path('stream/<int:pk>', StreamDetailAV.as_view(), name='stream-details'),
    
    
    
    path('', include(router.urls)),
    
    
    
    path('list/', CollectionListAV.as_view(), name='movie-list'),
    
    path('list/<int:pk>', CollectionDetailAV.as_view(), name='movie-details'),
    
    # path('review', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
    
    
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    
    path('stream/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
    
    
    
]
