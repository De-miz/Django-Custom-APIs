from django.db import models


def _list():
    return []


class MyRecipeBook(models.Model):
    
    dish_name = models.CharField(max_length=255)
    
    primary_image_url = models.CharField(max_length=255)
    
    images_url = models.JSONField(default=_list)
    
    ingredients = models.JSONField(default=_list)
    
    def __str__(self) -> str:
        return self.dish_name