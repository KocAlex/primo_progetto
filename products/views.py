from django.shortcuts import render
from django.http import JsonResponse
from products.models import Product, Manufacturer


def product_list(request):
    products = Product.objects.all()
    data  = {"products" : list(products.values())}
    print(type(data))
    response = JsonResponse(data)
    return response

def product_detail(request, pk):
    try: 
        product = Product.objects.get(pk = pk)
        data = {
            "product": {
                "name" : product.name,
                "manufacturer" : product.manufacturer.name,
                "description" : product.description,
                "photo" : product.photo.url,
                "price" : product.price,
                "shipping_cost" : product.shipping_cost,
                "quantity" : product.quantity,
            }
        }
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code" : 404,
                "message" : "Prodotto non trovato!"
            }
        },
        status = 404)
        return response
    
def manufacturer_list(request):
        manufacturers = Manufacturer.objects.all()
        data = {"manufacturers" : list(manufacturers.values())}
        response = JsonResponse(data)
        return response

def manufacturer_detail(request, pk):
     try:
          manufacturer = Manufacturer.objects.get(pk = pk)
          manufacturer_products  = manufacturer.products.all()
          data = {
               "manufacturer": {
                    "name" : manufacturer.name,
                    "location" : manufacturer.location,
                    "active" : manufacturer.active,
                    "products" : list(manufacturer_products.values())
               }
          }
          response = JsonResponse(data)
     except:
          response = JsonResponse({
               "error": {
                    "code" : 404,
                    "message": "Produttore non trovato!"
               }
          }, status = 404)
     return response

     
