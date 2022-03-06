# Generated by Django 3.2.5 on 2022-02-19 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='company',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='country',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='department',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='designation',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email_2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email_3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='notes',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_2',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_3',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_4',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_5',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='photo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='pin_code',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='state',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='website',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]