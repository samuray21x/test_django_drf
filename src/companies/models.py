import random
import string
from django.db import models

from uuid import uuid4


def generate_test_int_field():
    return random.randint(0, 123456789)


def generate_test_char_field():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(10, 100)))


class Company(models.Model):

    name = models.CharField(max_length=100, verbose_name='название')
    uuid = models.UUIDField(default=uuid4)
    boolean_1 = models.BooleanField(default=True)
    boolean_2 = models.BooleanField(default=True)
    boolean_3 = models.BooleanField(default=True)
    boolean_4 = models.BooleanField(default=False)
    boolean_5 = models.BooleanField(default=True)
    boolean_6 = models.BooleanField(default=False)
    boolean_7 = models.BooleanField(default=True)
    integer_1 = models.IntegerField(default=generate_test_int_field)
    integer_2 = models.IntegerField(default=generate_test_int_field)
    integer_3 = models.IntegerField(default=generate_test_int_field)
    integer_4 = models.IntegerField(default=generate_test_int_field)
    integer_5 = models.IntegerField(default=generate_test_int_field)
    date_1 = models.DateTimeField(auto_now=True)
    date_2 = models.DateTimeField(auto_now=True)
    date_3 = models.DateTimeField(auto_now=True)
    date_4 = models.DateTimeField(auto_now=True)
    string_1 = models.CharField(default=generate_test_char_field, max_length=110)
    string_2 = models.CharField(default=generate_test_char_field, max_length=110)
    string_3 = models.CharField(default=generate_test_char_field, max_length=110)
    string_4 = models.CharField(default=generate_test_char_field, max_length=110)
    string_5 = models.CharField(default=generate_test_char_field, max_length=110)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'компания'
        verbose_name_plural = 'компании'
