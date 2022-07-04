from rest_framework import viewsets, status
from django.views.generic.list import ListView

from food.models import Vegetable, VegetableType
from food.serializers import VegetableTypeSerializer, VegetableSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class VegetableTypeView(viewsets.ModelViewSet, ListView):
    model = VegetableType
    serializer_class = VegetableTypeSerializer
    queryset = model.objects.all()


class VegetablesView(viewsets.ModelViewSet, ListView):
    model = Vegetable
    serializer_class = VegetableSerializer
    queryset = model.objects.all()


class VegetableView(APIView):
    def post(self, request, pk=None):
        serializer = VegetableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            vegetable = Vegetable.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        vegetable.delete()
        return Response(status=status.HTTP_204_OK)

    def get(self, request, pk=None):
        try:
            vegetable = Vegetable.objects.get(id=pk)
        except Vegetable.DoesNotExist:
            return Response(
                {"Error": "Vegetable not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = VegetableSerializer(vegetable)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk=None):
        try:
            vegetable = Vegetable.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = VegetableSerializer(vegetable, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
