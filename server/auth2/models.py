from django.db import models
from auth2.enum import Roles


# Given the role name return the corresponding Role Object. If no matching role name return basic user Role Object
def getRoleValue(role):
    for user_type in Roles:
        if user_type.name == role:
            return user_type.value


# Create your models here.

# Scarborough Dining User
class SDUser(models.Model):
    nickname = models.CharField(max_length=30, null=True, default='')
    name = models.CharField(max_length=50, default='')
    picture = models.CharField(max_length=200, default='')
    last_updated = models.CharField(max_length=200, default='')
    email = models.EmailField(primary_key=True, default='')
    email_verified = models.BooleanField(default=False)
    role = models.CharField(max_length=5, choices=[(role, role.value) for role in Roles])

    # Constructs & Saves User to DB
    @classmethod
    def signup(cls, nickname, name, picture, updated, email, verified, role):
        user_role = getRoleValue(role)
        user = cls(nickname=nickname, name=name, picture=picture, last_updated=updated, email=email,
                   email_verified=verified, role=user_role)
        user.save()
        return user

    # Reassigns the Role as the User to the given Role
    def reassign_role(self, role):
        user_role = getRoleValue(role)
        if self.role != user_role:
            self.role = user_role
            self.save(update_fields=["role"])
        return self
