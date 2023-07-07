# Generated by Django 4.2.3 on 2023-07-07 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr_department', '0002_personeducation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personeducation',
            name='academy_diploma_id',
            field=models.CharField(blank=True, max_length=50, verbose_name='Akademiýanyň diplom belgisi'),
        ),
        migrations.CreateModel(
            name='WasHeAbroad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_country', models.CharField(max_length=100, verbose_name='Ýurduň ady')),
                ('date', models.DateField(verbose_name='Senesi')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persons', to='hr_department.personinformation', verbose_name='Işgär')),
            ],
            options={
                'verbose_name': 'Daşary ýurtda bolandygy barada maglumat',
                'verbose_name_plural': 'Daşary ýurtda bolandygy barada maglumatlar',
            },
        ),
    ]
