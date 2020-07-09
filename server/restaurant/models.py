from djongo import models
from bson import ObjectId
from restaurant.cuisine_dict import load_dict
from RO.models import Restaurant


path = 'cuisine_dict/dishes.csv'
# Model for the Food Items on the Menu
class Food(models.Model):

    _id = models.ObjectIdField()
    name = models.CharField(max_length=50)
    restaurant_id = models.CharField(max_length=24, editable=False, blank=False) # To be changed when restaurant is implemented
    description = models.CharField(max_length=200, blank=True, default='')
    picture = models.CharField(max_length=200, blank=True, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    tags = models.ListField(default=[])
    specials = models.CharField(max_length=51, blank=True)


    class Meta:
        unique_together = (("name", "restaurant_id"),)

    @classmethod
    def add_dish(cls, food_data):
        dish = Food.objects.create(**food_data)
        return dish


# Model for Manual Tags
class ManualTag(models.Model):
    _id = models.ObjectIdField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=[  # Use enum later
        ("promo", "promo"),
        ("allergy", "allergy"),
        ('cuisine', 'cuisine'),
        ('dish', 'dish')
    ])
    value = models.CharField(max_length=50, unique=True)
    foods = models.ListField(default=[])

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
        tag = ManualTag.objects.find(value=value, category=category)
        if not tag:
            tag = cls(value=value, category=category, foods=[food._id])
            tag.full_clean()
        else:
            tag.foods.append(food._id)
        tag.save()
        return tag

    @classmethod
    def auto_tag_food(cls, _id):
        c_dict = load_dict.read(path)
        desc_dict = {}
        dish = Food.objects.get(_id=ObjectId(_id))[0]
        for food in dish.description.split(' '):
            desc_dict.add(''.join(e for e in food if e.isalnum()).lower())
        for item in desc_dict:
            if item in c_dict:
                cls.add_tag(cls, dish.name, dish.restaurant, 'dish', item)

    def __eq__(self, other):
        return self.food == other.food and self.category == other.category and self.value == other.value
