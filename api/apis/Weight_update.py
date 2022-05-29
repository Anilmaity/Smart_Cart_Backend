from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated
from api.models import Cart


class location_Update(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print(request.data)
        cart_id = request.POST["cart_id"]
        weight = request.POST["weight"]

        cart = Cart.objects.all().filter(cart_id=cart_id).exists()
        print(cart)

        if cart:
            cart = Cart.objects.get(cart_id=cart_id)
            cart.weight = weight
            cart.save()
            response = {'Status': 'weight updated'}
            return Response(response, status=200)
        else:
            response = {'Status': 'weight not updated'}
            return Response(response, status=200)
