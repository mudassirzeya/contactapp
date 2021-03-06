# Generated by Django 3.2.5 on 2022-02-21 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_remove_contact_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email_2_label',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email_3_label',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email_label',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_2_is_whatsapp',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_2_label',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_3_is_whatsapp',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_3_label',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_4_is_whatsapp',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_4_label',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_5_is_whatsapp',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_5_label',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_is_whatsapp',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone_label',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
