# Generated by Django 3.0.7 on 2021-07-15 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0008_auto_20210714_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='date_created',
            field=models.DateTimeField(auto_created=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
