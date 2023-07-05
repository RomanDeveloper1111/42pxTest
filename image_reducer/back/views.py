from rest_framework.viewsets import GenericViewSet, mixins
from back.serializers import ReduceSerializer
from rest_framework import status
from rest_framework.response import Response
from django.db import IntegrityError
from back.models import Reducer


class ReducerViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = ReduceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                res = serializer.save()
            except IntegrityError:
                instance = Reducer.objects.get(natural_image_name=request.data['image'])
                return Response(f'http://localhost:8000/media/{instance.image}', status=status.HTTP_200_OK)
            return Response({'link': f'http://localhost:8000/media/{res}'}, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
