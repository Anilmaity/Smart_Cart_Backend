from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated
from api.models import Cart


class Cart_login(APIView):

    permission_classes = [AllowAny]
    def post(self, request):
        print(request.data)
        cart_id = request.POST["cart_token"]



        cart = Cart.objects.all().filter(cart_id=cart_id).exists()


        if cart:
            response = {'Status': 'Login successful'}
            return JsonResponse(response, safe=False)
        else:
            response = {'Status': 'Login failed'}
            return JsonResponse(response, safe=False)
