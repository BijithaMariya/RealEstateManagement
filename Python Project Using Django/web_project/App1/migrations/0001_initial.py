# Generated by Django 4.2.7 on 2023-12-05 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('classDetails', models.IntegerField(null=True)),
                ('address', models.TextField()),
            ],
        ),
    ]
