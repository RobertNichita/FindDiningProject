from django.core.exceptions import ValidationError
from django.test import TestCase, Client
from auth2.models import SDUser
from auth2.enum import Roles

# Create your tests here.


class SDUserTestCases(TestCase):

    def setUp(self):
        SDUser.objects.create(nickname="TesterB", name="Tester", picture="picB", last_updated="2020-06-26T14:07:39.888Z", email="B@mail.com", email_verified=True, role=Roles.RO.name)
        SDUser.objects.create(nickname="TesterC", name="Tester", picture="picC", last_updated="2020-06-26T14:07:39.888Z", email="C@mail.com", email_verified=True, role=Roles.BU.name)
        SDUser.objects.create(nickname="TesterD", name="Tester", picture="picD", last_updated="2020-06-26T14:07:39.888Z", email="D@mail.com", email_verified=True, role=Roles.BU.name)
        SDUser.objects.create(nickname="TesterE", name="Tester", picture="picE", last_updated="2020-06-26T14:07:39.888Z", email="E@mail.com", email_verified=True, role=Roles.BU.name)
    def test_signup(self):
        SDUser.signup("TesterA", "Tester", "picA", "2020-06-26T14:07:39.888Z", "A@mail.com", True, "BU")
        actual = SDUser.objects.get(pk="A@mail.com")
        expected = SDUser(nickname="TesterA", name="Tester", picture="picA", last_updated="2020-06-26T14:07:39.888Z", email="A@mail.com", email_verified=True, role="BU")
        self.assertEqual(actual, expected)

    def test_signup_invalid_role(self):
        self.assertRaises(ValidationError, SDUser.signup, "TesterF", "Tester", "picF", "2020-06-26T14:07:39.888Z", "F@mail.com", True, "Random")

    def test_reassign_RO_to_BU(self):
        user = SDUser.objects.get(pk="B@mail.com")
        user = user.reassign_role("BU")
        actual = SDUser.objects.get(pk="B@mail.com").role
        expected = Roles.BU.name
        self.assertEqual(actual, expected)

    def test_reassign_BU_to_RO(self):
        user = SDUser.objects.get(pk="C@mail.com")
        user = user.reassign_role("RO")
        actual = SDUser.objects.get(pk="C@mail.com").role
        expected = Roles.RO.name
        self.assertEqual(actual, expected)

    def test_reassign_redundant(self):
        user = SDUser.objects.get(pk="D@mail.com")
        user = user.reassign_role("BU")
        actual = SDUser.objects.get(pk="D@mail.com").role
        expected = Roles.BU.name
        self.assertEqual(actual, expected)

