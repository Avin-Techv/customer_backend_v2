from django.db import models

from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Customer(models.Model):
    owner = models.ForeignKey('auth.User', related_name='customer',
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    email = models.EmailField(_('Email'), unique=True)
    address = models.CharField(max_length=500)
    phone_number_regex = RegexValidator(regex=r'^\s*(?:\+?(\d{1,3}))?([-. (]*(\d{3})[-. )]*)?((\d{3})[-. ]*(\d{2,4})(?:[-.x ]*(\d+))?)\s*$',
                                        message="Invalid Phone Number",
                                        code="invalid_phone_number"
                                        )
    phone_number = models.CharField(_("Phone Number"),
                                    validators=[phone_number_regex],
                                    max_length=16, null=True)
