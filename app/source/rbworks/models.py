import uuid
from django.db import models

# Create your models here.
class DistoributionType(models.Model):
   distribution_type_id = models.SmallIntegerField(primary_key=True)
   distribution_type_name = models.CharField(max_length=10)

class ShopHoliday(models.Model):
   shopHoliday_id = models.SmallIntegerField(primary_key=True)
   shopHoliday_name = models.CharField(max_length=10)

class Printer(models.Model):
   printer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   printer_name = models.CharField(max_length=10)

class Service(models.Model):
   service_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   service_no = models.CharField(max_length=5)
   service_size = models.CharField(max_length=5)
   service_tieup = models.BooleanField()
   service_name = models.CharField(max_length=30)

class Destination(models.Model):
   destination_id = models.SmallIntegerField(primary_key=True)
   destination_name = models.CharField(max_length=100)
   destination_post = models.CharField(max_length=20)
   destination_address = models.CharField(max_length=100)
   destination_tell = models.CharField(max_length=50)

class DeliverySetting(models.Model):
   setting_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   shop_id = models.SmallIntegerField()
   destination_id = models.SmallIntegerField()
   distoribution_type_id = models.SmallIntegerField()
   folding = models.BooleanField()
   notes = models.TextField()
   arrive_offset = models.CharField(max_length=5)
   shipp_offset = models.SmallIntegerField()

class Shop(models.Model):
   shop_id = models.SmallIntegerField(primary_key=True)
   shop_name = models.CharField(max_length=10)
   shopHoliday_id =  models.SmallIntegerField()
   shop_tell = models.CharField(max_length=30)
   shop_fax = models.CharField(max_length=30)
   shop_address = models.CharField(max_length=100)

class ShopSample(models.Model):
   shopsample_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   shop_id = models.SmallIntegerField()
   year = models.SmallIntegerField()
   month = models.SmallIntegerField()
   service_id = models.UUIDField()
   shopsample_number = models.SmallIntegerField()

"""
class Lot(models.Model):
   lot_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   shop_id = models.SmallIntegerField()
   year = models.SmallIntegerField()
   month = models.SmallIntegerField()
   distribution_type_id = models.SmallIntegerField()
   plate_id = models.SmallIntegerField(default=1)
"""