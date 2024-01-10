from rest_framework import serializers
from note.models import Note


class NotesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
