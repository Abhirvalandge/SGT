# Generated by Django 3.1.5 on 2021-04-03 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgt_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entries',
            name='lr_no',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
