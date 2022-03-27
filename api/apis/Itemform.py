from django.http import JsonResponse
from rest_framework.views import APIView

from api.models import items


class Itemform(APIView):


    def post(self, request):

        name = request.POST["name"]
        price = request.POST["price"]
        manufacturer = request.POST["manufacturer"]
        description = request.POST["description"]
        category = request.POST["category"]
        barcode = request.POST["barcode"]
        barcode_type = request.POST["barcode_type"]


        item = items(name=name, price=price, manufacturer=manufacturer, description=description, category=category, barcodedata=barcode, barcode_type=barcode_type)
        item.save()


        response = {'Status': 'Item added sucessfully',
                    'item_no': str(item.id)},
        return JsonResponse(response)
