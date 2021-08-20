from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class SGTEntries(models.Model):
    STATUS_CHOICES = (('pending', 'Pending'), ('done', 'Done'),('cancle', 'Cancle'))
    #FIRM_CHOICES = (('new gandhi roadline', 'New Gandhi Roadline'), ('shri ganesh roadline','Shri Ganesh Roadline'))
    date = models.DateField()
    lr_no = models.IntegerField()
    vehicle_no = models.CharField(max_length=100,db_index=True)
    location = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,db_index=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    cash = models.DecimalField(max_digits=10,decimal_places=2)
    diesel = models.DecimalField(max_digits=10,decimal_places=2)
    rtgs = models.DecimalField(max_digits=10,decimal_places=2)
    company_frade = models.DecimalField(max_digits=10,decimal_places=2)
    frade = models.DecimalField(max_digits=10,decimal_places=2)
    commission = models.DecimalField(max_digits=10,decimal_places=2)
    total_balance = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='done')
    firm_name = models.CharField(max_length=50, default='shri ganesh roadline')
    flag = models.BooleanField(default=True)

    class Meta:
        db_table = 'sgt_entries'

    def __str__(self):
        return self.vehicle_no

    def get_absolute_url(self):
        return reverse('entry_detail', args=[self.lr_no])


