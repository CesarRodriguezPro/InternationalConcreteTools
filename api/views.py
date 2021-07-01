# todo/api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from accounts.models import User
from tools.models import Tool, Type
from .serializers import ToolSerializer, ToolTypeSerializer, UserSerializer


#  User Authentication
class UserRecordView(APIView):

    permission_classes = [IsAdminUser]

    def get(self, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )


#  Tools Section
class ToolListApiView(APIView):


    def get(self, request, *args, **kwargs ):
        tools = Tool.objects.all()
        serializer = ToolSerializer(tools, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'code' :request.data.get('code'),
            'type' :request.data.get('type'),
            'tags' :request.data.get('tags'),
            'quantity' :request.data.get('quantity'),
            'active' :request.data.get('active'),
            'current_user' :request.data.get('current_user'),
            'current_location' :request.data.get('current_location'),
            'date_updated' :request.data.get('date_updated'),
        }
        serializer = ToolSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToolDetailApiView(APIView):


    def get_object(self, todo_id):
        try:
            return Tool.objects.get(id=todo_id)
        except Tool.DoesNotExist:
            return None

    def get(self, request, tool_code,  *args, **kwargs):
        todo_instance = self.get_object(tool_code)

        if todo_instance:
            serializer = ToolSerializer(todo_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(
            {"res": "Object with todo id does not exists"},
            status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, tool_code, *args, **kwargs):

        todo_instance = self.get_object(tool_code)
        if todo_instance:

            data = {
                'type': request.data.get('type'),
                'tags': request.data.get('tags'),
                'quantity': request.data.get('quantity'),
                'active': request.data.get('active'),
                'current_user': request.data.get('current_user'),
                'current_location': request.data.get('current_location'),
                'date_updated': request.data.get('date_updated'),
            }

            serializer = ToolSerializer(instance=todo_instance, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            {"res": "Object with todo id does not exists"},
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, todo_id, *args, **kwargs):
        todo_instance = self.get_object(todo_id)
        if todo_instance:
            todo_instance.delete()
            return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)
        return Response({"res": "Object with todo id does not exists"},status=status.HTTP_400_BAD_REQUEST)


# Types Sections
class ToolTypesListApiView(APIView):


    def get(self, request, *args, **kwargs):
        types = Type.objects.all()
        serializer = ToolTypeSerializer(types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
        }
        serializer = ToolTypeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToolTypesDetailApiView(APIView):


    def get_object(self, type_id):
        try:
            return Type.objects.get(id=type_id)
        except Tool.DoesNotExist:
            return None

    def get(self, request, type_id, *args, **kwargs):
        todo_instance = self.get_object(type_id)

        if todo_instance:
            serializer = ToolTypeSerializer(todo_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(
            {"res": "Object with todo id does not exists"},
            status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, type_id, *args, **kwargs):

        todo_instance = self.get_object(type_id)
        if todo_instance:

            data = {
                'name': request.data.get('name'),
            }

            serializer = ToolTypeSerializer(instance=todo_instance, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            {"res": "Object with todo id does not exists"},
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, type_id, *args, **kwargs):
        todo_instance = self.get_object(type_id)
        if todo_instance:
            todo_instance.delete()
            return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)
        return Response({"res": "Object with todo id does not exists"}, status=status.HTTP_400_BAD_REQUEST)

