# Generated by Django 3.1 on 2020-08-19 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.TextField(max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='address',
            field=models.TextField(max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='email',
            field=models.EmailField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='full_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='full_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='phone_number',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
    ]
