# Generated by Django 3.2 on 2021-04-21 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210421_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
