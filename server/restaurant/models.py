from django.forms import model_to_dict
from djongo import models
from bson import ObjectId
from restaurant.cuisine_dict import load_dict

path = 'cuisine_dict/dishes.csv'


# Model for the Food Items on the Menu
class Food(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=50, default='')
    restaurant_id = models.CharField(max_length=24, editable=False, blank=False)
    description = models.CharField(max_length=200, blank=True, default='')
    picture = models.CharField(max_length=200, blank=True, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    tags = models.ListField(default=[], blank=True)
    specials = models.CharField(max_length=51, blank=True)

    class Meta:
        unique_together = (("name", "restaurant_id"),)

    @classmethod
    def add_dish(cls, food_data):
        dish = cls(
            name=food_data['name'],
            restaurant_id=food_data['restaurant_id'],
            description=food_data['description'],
            picture=food_data['picture'],
            price=food_data['price'],
            specials=food_data['specials'],
        )
        # dish.full_clean()
        dish.save()
        return Food.objects.get(name=food_data['name'], restaurant_id=food_data['restaurant_id'])

    @classmethod
    def get_all(cls):
        response = {'Dishes': []}
        for food in list(Food.objects.all()):
            food._id = str(food._id)
            response['Dishes'].append(model_to_dict(food))
        return response


# Model for Manual Tags
class ManualTag(models.Model):
    _id = models.ObjectIdField()
    category = models.CharField(max_length=20, choices=[  # Use enum later
        ("promo", "promo"),
        ("allergy", "allergy"),
        ('cuisine', 'cuisine'),
        ('dish', 'dish')
    ])
    value = models.CharField(max_length=50, unique=True)
    foods = models.ListField(default=[], blank=True)

    # Clears all the tags off a food item
    @classmethod
    def clear_food_tags(cls, food_name, restaurant):  # To be changed when restaurant is implemented
        food = Food.objects.get(name=food_name, restaurant_id=restaurant)  # To be changed when restaurant is implemented
        for tag_id in food.tags:
            tag = ManualTag.objects.get(_id=tag_id)
            for food_id in tag.foods:
                if food_id == food._id:
                    tag.foods.remove(food_id)
                    tag.save()
        food.tags = []
        food.save()

    # Clears all the tags off a food item
    @classmethod
    def add_tag(cls, food_name, restaurant, category, value):  # To be changed when restaurant is implemented
        food = Food.objects.get(name=food_name,
                                restaurant_id=restaurant)  # To be changed when restaurant is implemented
        try:
            tag = ManualTag.objects.get(value=value, category=category)
        except:
            tag = cls(value=value, category=category, foods=[])
            tag.clean_fields()
            tag.clean
            tag.save()
            tag.refresh_from_db()

        if tag._id not in food.tags:
            food.tags.append(tag._id)
            food.save()
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
