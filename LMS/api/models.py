from django.db import models
from django.contrib.auth.models import User, Group


# Create your models here.

class AppUser(models.Model):
    permission_choices = [
        ('ADMIN', 'ADMIN'),
        ('LIBRARIAN', 'LIBRARIAN'),
        ('MEMBER', 'MEMBER')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='app_user')
    permission_level = models.CharField(choices=permission_choices, default='MEMBER', max_length=20)
    item_no = models.ForeignKey("Items", on_delete=models.CASCADE, null=True, related_name='app_users')


class Items(models.Model):
    item_choices = [
        ('BOOK', 'BOOK'),
        ('PAPER', 'PAPER'),
        ('MAGAZINE', 'MAGAZINE')
    ]
    condition_choices = [
        ('NORMAL', 'NORMAL'),
        ('GOOD', 'GOOD'),
        ('WEEK', 'WEEK')
    ]
    item_type = models.CharField(choices=item_choices, default="BOOK", max_length=20)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='app_user')
    takeaway = models.BooleanField(default=True)
    due_date = models.IntegerField(default=14)
    condition = models.CharField(default="normal", choices=condition_choices, max_length=20)


class Transfer(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='app_user')
    item = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='transfer__item')
    has_fine = takeaway = models.BooleanField(default=False)
    fine = models.DecimalField(max_digits=100, decimal_places=3, default=0)
