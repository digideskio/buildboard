from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from django.conf import settings
from django.dispatch import receiver


class AccountManager(models.Manager):
    def get_queryset(self):
        return (
            super(AccountManager, self)
            .get_queryset()
            .order_by('user__first_name', 'user__last_name')
        )


# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.CharField(max_length=200, blank=True)
    avatar = models.URLField(blank=True)
    objects = AccountManager()

    def __str__(self):
        return '{first_name} {last_name} ({email})'.format(
            first_name=self.user.first_name,
            last_name=self.user.last_name,
            email=self.user.email)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_account(sender, instance=None, created=False, **kwargs):
    if created:
        Account.objects.create(user=instance)
