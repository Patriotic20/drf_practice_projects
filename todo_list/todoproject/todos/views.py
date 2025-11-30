from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer

@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        # Get all todos
        todos = Todo.objects.all()
        
        # Filter by completed status if provided
        completed = request.query_params.get('completed')
        if completed is not None:
            todos = todos.filter(completed=completed.lower() == 'true')
        
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # Create new todo
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response({'error': 'Todo not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        # Get single todo
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        # Update todo
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        # Delete todo
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)