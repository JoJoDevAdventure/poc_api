from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NewItemSerializer
from .models import Item
from .serializers import ItemSerializer

class NewItemView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = NewItemSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "Ben is processing this, don't worry"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AddItemView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Item added successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FetchItemsView(APIView):
    def get(self, request, *args, **kwargs):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)