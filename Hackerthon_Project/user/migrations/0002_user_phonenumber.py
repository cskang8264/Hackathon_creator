# Generated by Django 2.2.1 on 2019-07-16 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=30, verbose_name='전화번호'),
        ),
    ]
