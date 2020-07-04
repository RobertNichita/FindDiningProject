from django.core.exceptions import ValidationError
from django.test import TestCase
from restaurant.models import Food, ManualTag


class SDUserTestCases(TestCase):

    def setUp(self):
        food = Food.objects.create(name="foodA", restaurant="restA", description="descripA", picture="picA", category="catA", price=10.99)
        ManualTag.objects.create(food=food, category="promo", value="50% off")
        Food.objects.create(name="foodB", restaurant="restB", description="descripB", picture="picB", category="catB", price=20.99)

    def test_clear_food_tags(self):
        ManualTag.clear_food_tags(food_name="foodA", restaurant="restA")
        food = Food.objects.get(name="foodA")
        expected = None
        actual = ManualTag.objects.filter(food=food).first()

        self.assertEqual(actual, expected)

    def test_add_tag(self):
        ManualTag.add_tag(food_name="foodB", restaurant="restB", category="promo", value="25% off")
        food = Food.objects.get(name="foodB")
        expected = ManualTag(food=food, category="promo", value="25% off")
        actual = ManualTag.objects.get(food=food)
        self.assertEqual(actual, expected)

    def test_add_tag_invalid_category(self):
        self.assertRaises(ValidationError, ManualTag.add_tag, food_name="foodB", restaurant="restB", category="wrong", value="25% off")
