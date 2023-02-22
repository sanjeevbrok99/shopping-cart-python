from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .models import CartItem

@method_decorator(csrf_exempt, name='dispatch')
class ShoppingCart(View):
    def post(self, request):

        data = json.loads(request.body.decode("utf-8"))
        p_name = data.get('product_name')
        p_price = data.get('product_price')
        p_quantity = data.get('product_quantity')

        product_data = {
            'product_name': p_name,
            'product_price': p_price,
            'product_quantity': p_quantity,
        }

        cart_item = CartItem.objects.create(**product_data)

        data = {
            "message": f"New item added to Cart with id: {cart_item.id}"
        }
        return JsonResponse(data, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class ShoppingCart(View):

    def post(self, request):
        ...

    def get(self, request):
        items_count = CartItem.objects.count()
        items = CartItem.objects.all()

        items_data = []
        for item in items:
            items_data.append({
                'product_name': item.product_name,
                'product_price': item.product_price,
                'product_quantity': item.product_quantity,
            })

        data = {
            'items': items_data,
            'count': items_count,
        }

        return JsonResponse(data)