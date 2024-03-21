from django.shortcuts import render
from .models import categories , Item

def create_category():
    a=categories(name="starters")
    b=categories(name="mains")
    c=categories(name="desserts")
    return a , b, c

item1, item2, item3 = create_category()
item1.save()
item2.save()
item3.save()

def create_item():
    a=