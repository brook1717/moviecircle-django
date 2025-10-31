from django.contrib import admin
from movielist_app.models import CollectionList, StreamPlatform, Review

# Register your models here.
admin.site.register(CollectionList)
admin.site.register(StreamPlatform)
admin.site.register(Review)