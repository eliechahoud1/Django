from django.shortcuts import render
from menu.models import categories,items

def create_category():
    a=categories(name='starters')
    a.save()
    b=categories(name='mains')
    b.save()
    c=categories(name='desserts')
    c.save()
 

def create_item():
    a=categories.objects.get(pk=1)
    
    item1=a.items_set.create(name='Bacon Rings',
          description='Bacon rings are a delicious and savory culinary creation made from bacon strips formed into circular shapes',price=15)
    item2=a.items_set.create(name='Blooming Onion',
                               description='A blooming onion is a popular appetizer that features a large onion sliced to resemble a flower and then deep-fried',price=22.5)
    item3=a.items_set.create( name='Caprese Salad',
                               description='Caprese Salad is a classic Italian dish that showcases the flavors of fresh tomatoes, mozzarella cheese, and basil',price=30)
    
    b=categories.objects.get(pk=2)
   
    item4=b.items_set.create(name='bruschetta chicken',
                               description='Bruschetta chicken is a flavorful and delicious dish that combines grilled or baked chicken with a topping inspired by traditional Italian bruschetta',price=45)
    item5=b.items_set.create(name='Ronto Wrap',
                               description='The Ronto Wrap consists of a grilled sausage wrapped in a pita-like bread with various toppings and sauces',price=52.5)
    item6=b.items_set.create(name='Black Pepper Chicken',
                               description='Black pepper chicken is a flavorful and aromatic dish that features tender chicken pieces cooked with a generous amount of black pepper',price=65.75)
    
    c=categories.objects.get(pk=3)
    
    item7=c.items_set.create(name='Atlantic Beach Pie',
                               description='It is a simple yet delicious pie that combines a buttery cracker crust with a tangy and creamy citrus filling',price=33.75)
    item8=c.items_set.create(name='Easy Peach Cobbler',
                               description='Easy Peach Cobbler is a classic dessert that features juicy peaches baked with a sweet and buttery topping',price=35)
    item9=c.items_set.create(name='Sea Salt-Caramel Cake',
                               description='Sea Salt-Caramel Cake is a decadent and indulgent dessert that combines the rich flavors of caramel with a sprinkle of sea salt',price=42)
    

def update_item():
    item1=items.objects.get(pk=1)
    item1.price=20
    item1.save()

    item2=items.objects.get(pk=4)
    item2.name='Veggie pasta bake'
    item2.description='Veggie pasta bake is a delicious and satisfying vegetarian dish that combines pasta, vegetables, and cheese baked to perfection'
    item2.save()

    item3=items.objects.get(pk=9)
    item3.price=35
    item3.save()



def delete_item():
    a=categories.objects.get(pk=1)
    b=categories.objects.get(pk=2)
    
    item1=a.objects.filter(name__startswith='Bacon')
    item1.delete()

    item2=a.objects.filter(price=22.5)
    item2.delete()
    
    item3=b.objects.filter(description__contains="flavorful and aromatic dish ")
    item3.delete()


def display_items():
    instances=items.objects.order_by('name')

    for x in instances:
        print(items.name,items.description,items.price)



def display_categories():
    types=categories.objects.all()

    for x in types:
        print("Category:" , x.name)
        print("Items:")
        meals= x.items_set.all()
        for y in meals:
            print(y.name , y.description , y.price)

        