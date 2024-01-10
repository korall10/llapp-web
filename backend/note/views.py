from rest_framework.viewsets import ModelViewSet
from note.models import Note
from note.serializers import NotesSerializers
from note.filters import NoteFilter
from rest_framework.response import Response


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NotesSerializers
    filterset_class = NoteFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(user=request.user)
        if request.query_params.get("is_trash"):
            is_trash = None
            if request.query_params.get("is_trash") == "true":
                is_trash = True
            elif request.query_params.get("is_trash") == "false":
                is_trash = False
            queryset = queryset.filter(is_trash=is_trash)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)