# Generated by Django 3.1.5 on 2021-04-04 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgt_App', '0002_auto_20210403_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entries',
            name='firm_name',
            field=models.CharField(choices=[('new gandhi roadline', 'New Gandhi Roadline'), ('shri ganesh roadline', 'Shri Ganesh Roadline')], default='shri ganesh roadline', max_length=50),
        ),
    ]
