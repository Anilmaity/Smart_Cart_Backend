from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated
from api.models import Cart


class Cart_form(APIView):

    permission_classes = [AllowAny]
    def post(self, request):
        print(request.data)
        current_user = request.POST["current_user"]
        cart_token = request.POST["cart_token"]
        cart_id = request.POST["cart_id"]
        password = request.POST["password"]



        cart = Cart.objects.all().filter(cart_id=cart_id).exists()


        if cart:
            response = {'Status': 'Cart already exists'},
            return JsonResponse(response, safe=False)
        else:
            if password == "12345":
                Cart.objects.create(current_user=current_user, in_use=True,
                                    cart_id=cart_id, password=password)
                response = {'Status': 'Cart added sucessfully',
                            'item_no': str(Cart.id)},
                return JsonResponse(response, safe=False)
            else:
                response = {'Status': 'Password is incorrect'},
                return JsonResponse(response, safe=False)