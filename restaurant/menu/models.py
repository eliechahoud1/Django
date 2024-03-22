from django.db import models

class categories(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class items(models.Model):
    category = models.ForeignKey(categories, on_delete=models.PROTECT)
    name = models.CharField(max_length=200 , null=True)
    description= models.TextField(null=True)
    price =models.FloatField(default=0)
    def __str__(self):
        return  f"{self.name} - Description: {self.description} - Price: {self.price}"