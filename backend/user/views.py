from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from user.models import User
from user.serializers import UserSerializers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    @action(detail=True, methods=['post'])
    def change_password(self, request, *args, **kwargs):
        user = self.get_object()
        data = request.data
        if user.check_password(data.get('new_password')):
            return JsonResponse({'message': False, "error": "Your password cannot be the same as your current password!"},
                                status=status.HTTP_400_BAD_REQUEST)
        if user.check_password(data.get('old_password')):
            user.set_password(data.get('new_password'))
            user.save()
            return JsonResponse({'message': True}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'message': False, "error": "Your current password does not match!"},
                                status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def me(self, request):
        serializer = UserSerializers(request.user, context=self.get_serializer_context())
        return Response(serializer.data)
