
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

from api.models import items
from api.serilizers import itemsSerializer

import datetime

from rest_framework.views import APIView
from rest_framework.response import Response

class itemslist(APIView):

    def get(self, request):
        print("get")
        item = items.objects.all()
        ser = itemsSerializer(item,many=True)
        if (request.method == "GET"):
            print(ser.data)
            return JsonResponse(ser.data, safe=False)
        else:
            return HttpResponse("Not Found")

