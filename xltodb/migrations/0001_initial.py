# Generated by Django 3.0.7 on 2020-06-23 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruction_ID', models.IntegerField()),
                ('case_ref_no', models.CharField(max_length=20)),
                ('client_name', models.CharField(max_length=50)),
                ('candidate_name', models.CharField(max_length=50)),
                ('complete_address', models.TextField()),
                ('period_od_stay', models.DateField()),
            ],
        ),
    ]
