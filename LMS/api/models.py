from django.db import models
from django.contrib.auth.models import User, Group


# Create your models here.

class AppUser(models.Model):
    permission_choices = [
        ('ADMIN', 'ADMIN'),
        ('LIBRARIAN', 'LIBRARIAN'),
        ('SUPPLIER', 'SUPPLIER'),
        ('MEMBER', 'MEMBER')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='app_user')
    permission_level = models.CharField(choices=permission_choices, default='MEMBER', max_length=20)
    # item_no = models.ForeignKey("Items", on_delete=models.CASCADE, null=True, related_name='app_users')


#     email
# password
# name
# tp
# addres


class Items(models.Model):
    item_choices = [
        ('BOOK', 'BOOK'),
        ('PASS_PAPER', 'PASS_PAPER'),
        ('MAGAZINE', 'MAGAZINE'),
        ('DVD', 'DVD'),
        ('COMICS', 'COMICS')

    ]
    condition_choices = [
        ('NORMAL', 'NORMAL'),
        ('GOOD', 'GOOD'),
        ('WEEK', 'WEEK')
    ]
    item_type = models.CharField(choices=item_choices, default="BOOK", max_length=20)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='app_user')
    takeaway = models.BooleanField(default=True)
    author = models.CharField(default="BOOK", max_length=20)
    name = models.CharField(default="BOOK", max_length=20)
    # title = models.CharField(default="BOOK", max_length=20) shoud be  choice field
    # publisher
    #  lanuge
    # url
    isbn = models.CharField(default="BOOK", max_length=20)
    # due_date = models.IntegerField(default=14)  choci field normal high
    condition = models.CharField(default="normal", choices=condition_choices, max_length=20)


#     vedio -> duration
#     smmster
# year
# programme
# exame date
# voluem


class ItemGroup(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='transfer__item')
#     quntity
# avalbel_ quntity


class Transfer(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='app_user')
    item = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='transfer__item')
    has_fine = models.BooleanField(default=False)
    fine = models.DecimalField(max_digits=100, decimal_places=3, default=0)
    # borrow_date = models.DateTimeField()
