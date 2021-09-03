from django.contrib.auth import models
from django.contrib.auth.models import User, Group
from django.db.models import fields
from rest_framework import serializers
from .models import *

# A serializer class is very similar to a Django Form class, and includes similar validation flags on the various fields,
"""
In the same way that Django provides both Form classes and ModelForm classes, REST framework includes both Serializer classes, and ModelSerializer classes.
"""
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url' , 'username' , 'email' , 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url' , 'name']


class SnippetSerializer(serializers.Serializer):
    #  The first part of the serializer class defines the fields that get serialized/deserialized.
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(required = False,allow_blank=True, max_length=100)
    """
    The {'base_template': 'textarea.html'} flag above is equivalent to using widget=widgets.Textarea on a Django Form class. 
    """
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    # The create() and update() methods define how fully fledged instances are created or modified when calling serializer.save()
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

class SnippetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = '__all__'