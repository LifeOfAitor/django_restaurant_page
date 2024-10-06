from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_dishes", "Main Dishes"),
    ("desserts", "Desserts")
)
STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)


class Item(models.Model):
    meal = models.CharField(max_length=500, unique=True)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=200, choices=MEAL_TYPE)
    # User is imported and is a table containing different users, passwords, ...
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=1)
    # item created or last modified date
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.meal
