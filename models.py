# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ForbesBestEmployers2023(models.Model):
    rank = models.TextField(blank=True, null=True)  # This field type is a guess.
    company = models.TextField(blank=True, null=True)  # This field type is a guess.
    industries = models.TextField(blank=True, null=True)  # This field type is a guess.
    country_territory = models.TextField(blank=True, null=True)  # This field type is a guess.
    employees = models.TextField(blank=True, null=True)  # This field type is a guess.
    publish_year = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'forbes_best_employers_2023'
