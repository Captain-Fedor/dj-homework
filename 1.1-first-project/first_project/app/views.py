from django.http import HttpResponse
from django.shortcuts import render, reverse
import os
from datetime import datetime

from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Weapon
from .serializers import WeaponSerializer


# @api_view(['GET', 'POST'])
# def demo(request):
#     if request.method == 'GET':
#         weapons = Weapon.objects.all()
#         ser = WeaponSerializer(weapons, many=True)
#         # data = {'message': 'hello'}
#         return Response(ser.data)
#     if request.method == 'POST':
#         weapons = Weapon.objects.all()
#         ser = WeaponSerializer(weapons, many=True)
#         # data = {'message': 'hello'}
#         return Response(ser.data)
#         # return Response({'status':'oko'})


# class DemoView(APIView):
#     def get(self, request):
#         weapons = Weapon.objects.all()
#         ser = WeaponSerializer(weapons, many=True)
#         # data = {'message': 'hello'}
#         return Response(ser.data)
#
#     def post(self,request):
#         return Response({'status':'ok'})

class DemoView(ListAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

    def post(self,request):
        return Response({'status':'ok'})

class WeaponView(RetrieveAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.now().strftime("%H:%M:%S")
    msg = f'Текущее время: {current_time}'
    print(request)
    return HttpResponse(msg)


def workdir_view(request):
    path = os.getcwd()
    dir_list = os.listdir(path)
    print(reverse('workdir'))
    print(path)
    return HttpResponse(f'Current directory {path}: {dir_list}')
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    # raise NotImplemented
