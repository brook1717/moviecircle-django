from rest_framework import serializers
from movielist_app.models import CollectionList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
              class Meta:
                  model = Review
                  exclude = ('collectionlist',)
                #   fields = "__all__"
                  
                
                
# Using Model Serializers
class CollectionListSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many = True, read_only=True)
    
    class Meta:
        model = CollectionList
        fields = "__all__"
                

class StreamPlatformSerializer(serializers.ModelSerializer):
    collectionlist = CollectionListSerializer(many = True, read_only = True)
    # collectionlist = serializers.StringRelatedField(many=True)
    # collectionlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # collectionlist = serializers.HyperlinkedRelatedField(many=True, read_only =True, view_name ='movie-details')
    class Meta:
        model = StreamPlatform
        fields = "__all__"     
        
        
        
        
# #Validations
#     def get_len_name(self, object):
#         length = len(object.name)
#         return length

#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name  and Description should be different")
#         else:
#             return data      
        
#     def validate_name(self, value):
#         if len(value)<2:
#             raise serializers.ValidationError("Name is too short")
#         else:
#             return value
    
    
    
    

# def name_length(value):
#     if len(value) <2:
#         raise serializers.ValidationError("Name is too short")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name  and Description should be different")
#         else:
#             return data
        
        
        
        
    # def validate_name(self, value):
    #     if len(value)<2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value
    