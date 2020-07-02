---
id: backend
title: Backend
---
This section will go over all the backends components of the Scarborough Dining Project.
## Models & Enums
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
## URLs

| Address        |      Required Fields (Field Type)      |   Functionality |
| :-------------:  |      :------------------ | ----- |
| /auth/signup/   | nickname, name, picture, updated_at, email, email_verified, role **(_Roles_ Name)** | Register's SDUser to DB |
| /auth/reassign/ |   email, role **(_Roles_ Name)**     |  Updates Role of SDUser in DB | 

All requests should be sent in a JSON format.