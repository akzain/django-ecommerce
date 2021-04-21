# Generated by Django 3.2 on 2021-04-21 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210420_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='orderitem',
            name='date_added',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='zain', max_length=200),
        ),
        migrations.DeleteModel(
            name='ShippingAddres',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.customer'),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.order'),
        ),
    ]
