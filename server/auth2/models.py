from django.db import models
from auth2.enum import Roles


# Scarborough Dining User
class SDUser(models.Model):
    nickname = models.CharField(max_length=30, null=True, default='')
    name = models.CharField(max_length=50, default='')
    picture = models.CharField(max_length=200, default='')
    last_updated = models.CharField(max_length=200, default='')
    email = models.EmailField(primary_key=True, default='')
    email_verified = models.BooleanField(default=False)
    role = models.CharField(max_length=5, choices=Roles.choices(), default="BU")

    # Constructs & Saves User to DB
    @classmethod
    def signup(cls, nickname, name, picture, updated, email, verified, role):
        if role == "":
            role = "BU"
        user = cls(nickname=nickname, name=name, picture=picture, last_updated=updated, email=email,
                   email_verified=verified, role=role)
        # user.full_clean()
        user.save()
        return user

    # Reassigns the Role as the User to the given Role
    def reassign_role(self, role):
        if self.role != role:
            self.role = role
            self.save(update_fields=["role"])
        return None
