from django.http import JsonResponse
from .models import Item
from .serializers import ItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'Post'])
def item_list(request):
    #get all drinks, serialize them and return json
    if request.method == 'GET':
        items = Item.objects.all() # list
        serializer = ItemSerializer(items, many=True)
        return JsonResponse({'items': serializer.data})
    
    if request.method == 'POST':
        seializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def item_detail(request, id):
    #DOES ITEM EXIST
    try:
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        pass

    elif request.method == 'DELETE':
        pass