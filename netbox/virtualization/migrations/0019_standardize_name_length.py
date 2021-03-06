# Generated by Django 3.1 on 2020-10-15 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualization', '0018_custom_field_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clustergroup',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='clustergroup',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='clustertype',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='clustertype',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
