# Generated by Django 4.0.3 on 2022-03-05 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('unitManagement', '0002_delete_check'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=48)),
                ('county', models.CharField(max_length=25)),
                ('zip', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_name', models.CharField(max_length=50)),
                ('address_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='unitManagement.address')),
            ],
        ),
        migrations.CreateModel(
            name='Leasing_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leasing_type', models.CharField(max_length=50)),
                ('is_sub_leasing_allowed', models.BooleanField()),
                ('application_fee', models.DecimalField(decimal_places=2, max_digits=20)),
                ('security_deposit', models.DecimalField(decimal_places=2, max_digits=20)),
                ('monthly_rent_1month_lease', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('monthly_rent_6month_lease', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('monthly_rent_12month_lease', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('is_lease_termination_allowed', models.BooleanField()),
                ('lease_termination_cost', models.DecimalField(decimal_places=2, max_digits=20)),
                ('additional_leasing_clauses', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnitType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_Type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_bedrooms', models.IntegerField()),
                ('num_of_bathrooms', models.IntegerField()),
                ('num_of_balcony', models.IntegerField()),
                ('is_available', models.BooleanField(default=False)),
                ('is_reserved', models.BooleanField(default=False)),
                ('unit_availability_start_date', models.DateField(null=True)),
                ('unit_availability_end_date', models.DateField(null=True)),
                ('unit_description', models.TextField(blank=True, null=True)),
                ('living_area_sf', models.IntegerField()),
                ('unit_number', models.IntegerField(null=True)),
                ('unit_at_floor', models.IntegerField(null=True)),
                ('address_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='unitManagement.address')),
                ('community_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='unitManagement.community')),
                ('leasing_info_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='unitManagement.leasing_info')),
                ('unit_type_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='unitManagement.unittype')),
            ],
        ),
    ]
