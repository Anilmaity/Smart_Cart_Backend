from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated
from api.models import Cart


class location_Update(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print(request.data)
        cart_id = request.POST["cart_token"]
        latitude = request.POST["latitude"]
        longitude = request.POST["longitude"]

        cart = Cart.objects.all().filter(cart_id=cart_id).exists()
        print(cart)

        if cart:
            cart = Cart.objects.get(cart_id=cart_id)
            cart.latitude = latitude
            cart.longitude = longitude
            cart.save()
            response = {'Status': 'Location updated'}
            return JsonResponse(response, safe=False)
        else:
            response = {'Status': 'Location not updated'}
            return JsonResponse(response, safe=False)
