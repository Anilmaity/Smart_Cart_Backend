from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated
from api.models import items


class Itemform(APIView):

    permission_classes = [AllowAny]
    def post(self, request):
        print(request.data)
        name = request.POST["name"]
        price = request.POST["price"]
        manufacturer = request.POST["manufacturer"]
        description = request.POST["description"]
        category = request.POST["category"]
        barcode = request.POST["barcode"]
        barcode_type = request.POST["barcode_type"]
        weight = request.POST["weight"]


        item = items.objects.all().filter(barcodedata=barcode, barcode_type=barcode_type).exists()
        if item:
            response = {'Status': 'Item already exists'},
            return JsonResponse(response, safe=False)
        else:
            item = items(name=name,weight=weight, price=price, manufacturer=manufacturer, description=description, category=category, barcodedata=barcode, barcode_type=barcode_type)
            item.save()
            response = {'Status': 'Item added sucessfully',
                        'item_no': str(item.id)},
            return JsonResponse(response, safe=False)