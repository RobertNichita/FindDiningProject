---
id: backend
title: Backend
---

This section will go over all the backends components of the Scarborough Dining Project.

## Models & Enums

#### Auth2

###### Scarborough Dining User

```python
class SDUser(models.Model):
    nickname = models.CharField(max_length=30, null=True, default='')
    name = models.CharField(max_length=50, default='')
    picture = models.CharField(max_length=200, default='')
    last_updated = models.CharField(max_length=200, default='')
    email = models.EmailField(primary_key=True, default='')
    email_verified = models.BooleanField(default=False)
    role = models.CharField(max_length=5, choices=[(role, role.value) for role in Roles])
```

###### Roles (Enum)

    RO = "Restaurant Owner"
    BU = "Basic User"

#### Restaurant

###### Food Item

```python
class Food(models.Model):
    name = models.CharField(max_length=50)
    restaurant = models.CharField(max_length=50)  # To be changed when restaurant is implemented
    description = models.CharField(max_length=200, blank=True, default='')
    picture = models.CharField(max_length=200, blank=True, default='')
    category = models.CharField(max_length=50, blank=True, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
``` 

###### Manual Tag for Food Item

```python
class ManualTag(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=[("promo", "promo"), ("allergy", "allergy")])
    value = models.CharField(max_length=50)
``` 

## URLs

|     Address     | Required Fields (Field Type)                                                          | Functionality                  |
| :-------------: | :------------------------------------------------------------------------------------ | ------------------------------ |
| /auth/signup/   | nickname, name, picture, updated\_at, email, email\_verified, role **(_Roles_ Name)** | Registers SDUser to DB         |
| /auth/reassign/ | email, role **(_Roles_ Name)**                                                        | Updates Role of SDUser         |
| /tag/add/       | food_name, restaurant, category, value                                                | Adds Tag to a Food Item        |
| /tag/clear/     | food_name, restaurant                                                                 | Clears All Tags on a Food Item |

All requests should be sent in a JSON format.


