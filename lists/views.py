from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from lists.models import Todo
from lists.serializers import CreateTodoSerializer, TodoListSerializer


@permission_classes([IsAuthenticated])
class TodoListView(APIView):
    def post(self, request):
        """할일 등록"""
        serializer = CreateTodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """할일 조회"""
        todo_lists = Todo.objects.filter(user=request.user)
        serializer = TodoListSerializer(todo_lists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class TodoView(APIView):
    def put(self, request, todo_id):
        """할일 수정"""
        todo = get_object_or_404(Todo, id=todo_id)
        if request.user == todo.user:
            serializer = CreateTodoSerializer(todo, data=request.data)
            print(request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, todo_id):
        """할일 삭제"""
        todo = get_object_or_404(Todo, id=todo_id)
        if request.user == todo.user:
            todo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)
