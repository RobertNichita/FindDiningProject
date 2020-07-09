from django.db import models

# Model for the Food Items on the Menu
class Food(models.Model):
    name = models.CharField(max_length=50)
    restaurant = models.CharField(max_length=50)  # To be changed when restaurant is implemented
    description = models.CharField(max_length=200, blank=True, default='')
    picture = models.CharField(max_length=200, blank=True, default='')
    category = models.CharField(max_length=50, blank=True, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = (("name", "restaurant"),)

# Model for Manual Tags
class ManualTag(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=[("promo", "promo"), ("allergy", "allergy")])
    value = models.CharField(max_length=50)

    # Clears all the tags off a food item
    @classmethod
    def clear_food_tags(cls, food_name, restaurant):  # To be changed when restaurant is implemented
        food = Food.objects.get(name=food_name, restaurant=restaurant)  # To be changed when restaurant is implemented
        ManualTag.objects.filter(food=food).delete()
        return None


    # Clears all the tags off a food item
    @classmethod
    def add_tag(cls, food_name, restaurant, category, value):  # To be changed when restaurant is implemented
        food = Food.objects.get(name=food_name, restaurant=restaurant)  # To be changed when restaurant is implemented
        tag = cls(food=food, category=category, value=value)
        tag.clean_fields()
        tag.clean()
        tag.save()
        return tag

    def __eq__(self, other):
        return self.food == other.food and self.category == other.category and self.value == other.value
