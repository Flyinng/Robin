# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alldata(models.Model):
    idalldata = models.AutoField(db_column='idAllData', primary_key=True)  # Field name made lowercase.
    store = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    price = models.CharField(max_length=1000)
    changeableprice = models.FloatField(db_column='changeablePrice')  # Field name made lowercase.
    installmentprice = models.CharField(db_column='installmentPrice', max_length=1000)  # Field name made lowercase.
    changeableinstallmentprice = models.FloatField(db_column='changeableInstallmentPrice')  # Field name made lowercase.
    link = models.CharField(db_column='Link', max_length=1000)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=1000)  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=1000)  # Field name made lowercase.
    logo = models.CharField(db_column='Logo', max_length=1000)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1000)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=1000)  # Field name made lowercase.
    format = models.CharField(db_column='Format', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    interface = models.CharField(db_column='Interface', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    capacity = models.CharField(db_column='Capacity', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    ddr = models.CharField(db_column='DDR', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    frequency = models.CharField(db_column='Frequency', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    platform = models.CharField(db_column='Platform', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'alldata'
