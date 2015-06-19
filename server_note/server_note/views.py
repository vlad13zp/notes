from rest_framework import generics
from django.db.models import Q
import serializers
import models

# Tag Classes


class SaveTag(generics.CreateAPIView):
    serializer_class = serializers.TagSerializer

    def get_queryset(self):
        queryset = models.Tag.objects.all()
        return queryset


class TagGetAccess(generics.ListAPIView):
    serializer_class = serializers.TagSerializer

    def get_queryset(self):
        queryset = models.Tag.objects.all()
        access_id = self.kwargs.get('pk')
        return queryset.filter(Q(access=0) | Q(access=access_id))

# Color Classes


class SaveColor(generics.CreateAPIView):
    serializer_class = serializers.ColorSerializer

    def get_queryset(self):
        queryset = models.Color.objects.all()
        return queryset


class ColorGetAccess(generics.ListAPIView):
    serializer_class = serializers.ColorSerializer

    def get_queryset(self):
        queryset = models.Color.objects.all()
        access_id = self.kwargs.get('pk')
        return queryset.filter(Q(access=0) | Q(access=access_id))

# Category Classes


class SaveCat(generics.CreateAPIView):
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        queryset = models.Category.objects.all()
        return queryset


class CategoryGetAccess(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        queryset = models.Category.objects.all()
        access_id = self.kwargs.get('pk')
        return queryset.filter(Q(access=0) | Q(access=access_id))


# Note Classes

class NoteGetByUser(generics.ListAPIView):
    serializer_class = serializers.NoteSerializer

    def get_queryset(self):
        queryset = models.Note.objects.all()
        return queryset.filter(id_user__id=self.kwargs.get('pk'))


class NoteGetByCat(generics.ListAPIView):
    serializer_class = serializers.NoteSerializer

    def get_queryset(self):
        queryset = models.Note.objects.all()
        return queryset.filter(
            id_user__id=self.kwargs.get('pk')
        ).filter(id_category=self.kwargs.get('lg'))


class AddNote(generics.CreateAPIView):
    serializer_class = serializers.NoteSerializer

    def get_queryset(self):
        queryset = models.Note.objects.all()
        return queryset


class DelNoteById(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.NoteSerializer

    def get_queryset(self):
        queryset = models.Note.objects.all()
        return queryset.filter(id=self.kwargs.get('pk'))

# User Classes


class UserGetById(generics.ListAPIView):
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        queryset = models.User.objects.all()
        return queryset.filter(
            password=self.kwargs.get('key')
        )


class UserGetAll(generics.ListAPIView):
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        queryset = models.User.objects.all()
        return queryset.exclude(
            id=self.kwargs.get('pk')
        )


class SaveNewUser(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        queryset = models.User.objects.all()
        return queryset
