from models import Tag, Color, Category, User, Note
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'tag_name', 'access')


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ('id', 'color_name', 'hex_stat', 'access')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'category_name', 'access')


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = (
            'id', 'id_user', 'subject', 'message', 'date_create',
            'id_tag', 'id_color', 'id_category', 'files')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'email', 'password',
            'id_tag', 'id_color', 'id_category')
