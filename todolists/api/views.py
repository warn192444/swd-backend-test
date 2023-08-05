from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def getTodoLists(request):
    list = Item.objects.all()
    serializer = ItemSerializer(list, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addTodoList(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateTodoList(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response({'error': 'Item not found'}, status=404)
    
    serializer = ItemSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)