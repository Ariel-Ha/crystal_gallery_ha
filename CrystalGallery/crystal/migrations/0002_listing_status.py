# Generated by Django 3.2.3 on 2021-08-10 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crystal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Closed', 'Closed')], default='Pending', max_length=7),
        ),
    ]