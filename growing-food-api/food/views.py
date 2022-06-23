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


class VegetableView(viewsets.ModelViewSet, ListView):
    model = Vegetable
    serializer_class = VegetableSerializer
    queryset = model.objects.all()


class VegetableCreateView(APIView):
    def post(self, request):
        serializer = VegetableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VegetableDeleteView(APIView):
    def delete(self, request, pk):
        vegetable = Vegetable.objects.get(id=pk)
        try:
            vegetable.delete()
            return Response(status=status.HTTP_204_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class VegetableGetView(APIView):
    def get(self, request, pk):
        try:
            vegetable = Vegetable.objects.get(id=pk)
        except Vegetable.DoesNotExist:
            return Response(
                {"Error": "Vegetable not found."}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = VegetableSerializer(vegetable)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VegetableUpdateView(APIView):
    def put(self, request, pk):
        vegetable = Vegetable.objects.get(id=pk)
        serializer = VegetableSerializer(vegetable, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiUrlsView(APIView):
    def get(self, request):
        api_urls = {
            "List-Vegetable-Type": "/vegetables-type/",
            "List-Vegetable": "/vegetables/",
            "Get": "/vegetable/<int:pk>/",
            "Create": "/vegetable-create/",
            "Update": "/vegetable-update/<int:pk>/",
            "Delete": "/vegetable-delete/<int:pk>/",
        }
        return Response(api_urls)
