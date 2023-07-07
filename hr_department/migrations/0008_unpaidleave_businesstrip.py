# Generated by Django 4.2.3 on 2023-07-07 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr_department', '0007_healthvacation_additionalvacation'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnpaidLeave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Ady')),
                ('order_id', models.CharField(max_length=20, verbose_name='Buýrugyň belgisi')),
                ('order_date', models.DateField(verbose_name='Buýrugyň senesi')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_UnpaidLeave', to='hr_department.personinformation', verbose_name='Işgär')),
            ],
            options={
                'verbose_name': 'Tölegsiz rugsady barada maglumat',
                'verbose_name_plural': 'Tölegsiz rugsady barada maglumatlar',
            },
        ),
        migrations.CreateModel(
            name='BusinessTrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_country', models.CharField(max_length=100, verbose_name='Ýurduň ady')),
                ('order_id', models.CharField(max_length=20, verbose_name='Buýrugyň belgisi')),
                ('order_date', models.DateField(verbose_name='Buýrugyň senesi')),
                ('start_date', models.DateField(verbose_name='Giden senesi')),
                ('end_date', models.DateField(verbose_name='Gelen senesi')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_BusinessTrip', to='hr_department.personinformation', verbose_name='Işgär')),
            ],
            options={
                'verbose_name': 'Iş sapary barada maglumat',
                'verbose_name_plural': 'Iş sapary barada maglumatlar',
            },
        ),
    ]