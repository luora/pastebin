from dataclasses import fields
from email.policy import default
from turtle import title
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User







class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    class Meta:
        model = Snippet
        fields = ['id', 'owner','title', 'code', 'linenos', 'language']



class UserSerializer(serializers.ModelSerializer):

    # snippets = serializers.PrimaryKeyRelatedField(many = True, queryset = Snippet.objects.all(),)

    snippets = SnippetSerializer(many = True)

    class Meta:
        model = User 
        fields = ['id', 'username', 'snippets']

# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     title = serializers.CharField(required = False, allow_blank = True, max_length = 100)
#     code = serializers.CharField(style = {'base_templete': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices = LANGUAGE_CHOICES, default = 'python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default= 'friendly')


#     def create(self, valifated_data):
#         '''
#         create and return a new 'Snippet' instance 
#         '''
#         return Snippet.objects.create(**valifated_data)
    

#     def update(self, instance, validated_data):

#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)

#         instance.save()

#         return instance

