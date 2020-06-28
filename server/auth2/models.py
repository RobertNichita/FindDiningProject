from django.db import models


# Create your models here.

# Scarborough Dining User
class SDUser(models.Model):
    nickname = models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=50)
    picture = models.CharField(max_length=200)
    last_updated = models.DateTimeField(null=True)
    email = models.EmailField(primary_key=True)
    email_verified = models.BooleanField()
    _id = models.UUIDField(blank=True)

    # Constructs & Saves User to DB
    @classmethod
    def signup(cls, nickname, name, picture, updated, email, verified):
        user = cls(nickname=nickname, name=name, picture=picture, last_updated=updated, email=email,
                   email_verified=verified)
        user.save()
        return user
