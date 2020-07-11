from django.core.exceptions import ValidationError
from django.test import TestCase
from restaurant.models import Food, ManualTag
from RO.models import Restaurant


class TagTestCases(TestCase):

    def setUp(self):
        restaurant = Restaurant.objects.create(name="RestA", address="123 Road", phone=None, email="RA@mail.com",
                                               city="Toronto",
                                               cuisine="Chinese", pricepoint="?", twitter="?", instagram="?", bio=None,
                                               GEO_location="?", external_delivery_link="?", cover_photo_url="picA",
                                               logo_url="urlA", rating="4.5")

        food = Food.objects.create(name="foodA", restaurant_id=restaurant._id, description="descripA", picture="picA",
                                   category="catA", price=10.99)
        tag = ManualTag.objects.create(food=[food._id], category="promo", value="50% off")
        food.tags = [tag._id]
        food.save()
        Food.objects.create(name="foodB", restaurant_id=restaurant._id, description="descripB", picture="picB",
                            category="catB",
                            price=20.99)

    def test_clear_food_tags(self):
        restaurant = Restaurant.objects.get(name="RestA")
        ManualTag.clear_food_tags(food_name="foodA", restaurant=restaurant._id)
        food = Food.objects.get(name="foodA")
        food_actual = food.tags
        expected = []
        tags_actual = ManualTag.objects.get(food=food._id).food

        self.assertEqual(food_actual, expected)
        self.assertEqual(actual, expected)

    def test_add_tag(self):
        restaurant = Restaurant.objects.get(name="RestA")
        ManualTag.add_tag(food_name="foodB", restaurant_id=restaurant._id, category="promo", value="25% off")
        food = Food.objects.get(name="foodB")
        expected = ManualTag(food=[food._id], category="promo", value="25% off")
        actual = ManualTag.objects.get(food=food)
        self.assertEqual(actual, expected)

    def test_add_tag_invalid_category(self):
        self.assertRaises(ValidationError, ManualTag.add_tag, food_name="foodB", restaurant="restB", category="wrong",
                          value="25% off")


class FoodTestCases(TestCase):

    def setUp(self):
        food = Food.objects.create(name="foodA", restaurant="restA", description="descripA", picture="picA",
                                   category="catA", price=10.99)
        Food.objects.create(name="foodB", restaurant="restB", description="descripB", picture="picB", category="catB",
                            price=20.99)

    def test_get_all_foods(self):
        self.assertJSONEqual(ValidationError, ManualTag.add_tag, food_name="foodB", restaurant="restB",
                             category="wrong", value="25% off")
