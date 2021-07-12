# Generated by Django 3.0.10 on 2020-10-29 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20201029_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='allproducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('price', models.FloatField()),
                ('quantity', models.CharField(max_length=100, null=True)),
                ('drugs', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='specificproducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products')),
                ('price', models.FloatField()),
                ('minquantity', models.IntegerField()),
                ('available', models.IntegerField()),
                ('cp', models.FloatField()),
                ('quantity', models.CharField(max_length=100, null=True)),
                ('drugs', models.CharField(max_length=200, null=True)),
                ('brand', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='pharmacist',
            name='PharmaAddress',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pharmacist',
            name='PharmaName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pharmacist',
            name='Pharmaimage',
            field=models.ImageField(blank=True, null=True, upload_to='pharmacies'),
        ),
        migrations.CreateModel(
            name='WalkinOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('transaction_id', models.CharField(blank=True, max_length=200, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Pharmacist')),
            ],
        ),
        migrations.CreateModel(
            name='WalkinCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.WalkinOrder')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.specificproducts')),
            ],
        ),
        migrations.AddField(
            model_name='specificproducts',
            name='Pharmacist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Pharmacist'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('delivered', models.BooleanField(default=False, null=True)),
                ('transaction_id', models.CharField(blank=True, max_length=200, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.specificproducts')),
            ],
        ),
    ]
