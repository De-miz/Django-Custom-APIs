from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .models import *
from django.template import loader
import json

# Create your views here.


@csrf_exempt
def my_recipe_book_mobile_app_endpoint(request):
    response_data = {"status": 1, "error": ""}
    req_status_code = 200
    
    if request.method == 'POST':
        data = MyRecipeBook.objects.all()
        response_data['data'] = []
        for i in data:
            response_data['data'].append(
                {
                    "id": i.id, 
                    "name": i.dish_name, 
                    "image": i.primary_image_url, 
                    "images": i.images_url, 
                    "ingredients": i.ingredients
                }
            )
    
    response = JsonResponse(response_data, status=req_status_code)
    return response


@csrf_exempt
def my_recipe_book_mobile_app_custom_admin_dashboard(request):
    response_data = {"status": 0, "error": ""}
    
    if request.method == 'POST': 
        request_data = json.loads(request.body)
        print(request_data)
        
        dishname = request_data.get('dish_name')
        primary_image_url = request_data.get('primary_image')
        other_image_urls = request_data.get('other_image_urls')
        ingredients = request_data.get('ingredients')
        if all([dishname, primary_image_url, other_image_urls, ingredients]):
            MyRecipeBook.objects.create(
                dish_name=dishname, 
                primary_image_url=primary_image_url, 
                images_url=other_image_urls, 
                ingredients=ingredients
            )
        else:
            response_data["error"] = "All parameters are required"
            response_data["status"] = 0
        
        return JsonResponse(response_data)
    
    if request.method == 'GET':
        template = loader.get_template('my_recipe_book.html')
        
        return HttpResponse(template.render({}, request))