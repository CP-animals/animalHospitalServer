from django.db import models

class Data(models.Model):
    id = models.IntegerField(primary_key=True)
    phone_number = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    location_x = models.FloatField(db_column='location_X', blank=True, null=True)  # Field name made lowercase.
    location_y = models.FloatField(db_column='location_Y', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data'