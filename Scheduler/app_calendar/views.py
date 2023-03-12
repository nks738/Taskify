from abc import abstractmethod, ABCMeta

from django.shortcuts import render, HttpResponse, redirect
from .models import UserInfo, TaskInfo
from .myform import HelloForm
import MySQLdb

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import Books
from .serializer import BooksSerializer, UserSerializer, TaskSerializer

@api_view(['GET', 'POST', 'PUT'])
def user(request):
    if request.method == 'GET':
        users = UserInfo.objects.all()

        user_id = request.query_params.get('id')
        if user_id is not None:
            users = UserInfo.objects.filter(id=user_id)

        user_name = request.query_params.get('user_name')
        password = request.query_params.get('password')
        if user_name is not None:
            if password is not None:
                users = UserInfo.objects.filter(user_name=user_name, password=password)

        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        user_data = {'user_name': request.POST.get('user_name'),
                     'password': request.POST.get('password')}
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        user_id = request.POST.get('id')
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        data = {}
        if user_name:
            if password:
                data = {'id': user_id,
                        'user_name': user_name,
                        'password': password}
            else:
                data = {'id': user_id,
                        'user_name': user_name}
        elif password:
            data = {'id': user_id,
                    'password': password}

        user_search = UserInfo.objects.filter(id=user_id)
        if not user_search:
            return JsonResponse({"message": "id error"}, status=status.HTTP_400_BAD_REQUEST)

        user_data = UserInfo.objects.get(id=user_id)
        user_serializer = UserSerializer(instance=user_data, data=data, partial=True)

        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskInfo.objects.all()
    serializer_class = TaskSerializer


class UserLogin(APIView):
    def get(self, request, *args, **kwargs):
        user_name = request.GET.get("user_name")
        password = request.GET.get('password')
        users = UserInfo.objects.filter(user_name=user_name, password=password)
        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)


class GetTasks(APIView):
    def get(self, request, *args, **kwargs):
        user_id = request.GET.get("user_id")
        tasks = TaskInfo.objects.filter(Task_owner_user=user_id)
        tasks_serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(tasks_serializer.data, safe=False)

# html, current-app-dir/templates/
# search order as settings.py: INSTALLED_APPS
def cal_main(request, null=None):
    # user_id = ''
    c = Calendar('Tom')
    if request.method == "GET":
        return render(request, 'calendar.html', {"data_list": c.get_schedular()})
    scheduler_name = request.POST.get("Scheduler name")
    operation_type = request.POST.get("type")

    if operation_type == "add":
        c.add_schedular(scheduler_name)

    if operation_type == "delete":
        if c.search_schedular(scheduler_name):
            c.delete_schedular(scheduler_name)
            return HttpResponse("delete success")
        else:
            return HttpResponse("This Scheduler does not exist")


# user template
def user_template(request):
    UserInfo.objects.create(user_id='123', user_name='123', password='123')

    UserInfo.objects.filter(user_id=1).delete()  # delete data

    data_list = UserInfo.objects.all()  # return type:QuerySet .first()
    for obj in data_list:
        print(obj.user_id, obj.user_name, obj.user_password)

    UserInfo.objects.filter(user_id=1).update()  # update data

    return HttpResponse("success")
