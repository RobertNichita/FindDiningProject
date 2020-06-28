from django.db import models


# Create your models here.

# Scarborough Dining User
class SDUser(models.Model):
    nickname = models.CharField(max_length=30, null=True, default='')
    name = models.CharField(max_length=50, default='')
    picture = models.CharField(max_length=200, default='')
    last_updated = models.CharField(max_length=200, default='')
    email = models.EmailField(primary_key=True, default='')
    email_verified = models.BooleanField(default=False)

    # Constructs & Saves User to DB
    @classmethod
    def signup(cls, nickname, name, picture, updated, email, verified):
        user = cls(nickname=nickname, name=name, picture=picture, last_updated=updated, email=email,
                   email_verified=verified)
        user.save()
        return user
