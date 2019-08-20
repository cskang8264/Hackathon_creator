# Generated by Django 2.2.3 on 2019-08-09 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prop',
            name='user',
        ),
        migrations.AddField(
            model_name='prop',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Props', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
