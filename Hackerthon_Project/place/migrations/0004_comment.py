# Generated by Django 2.2.3 on 2019-07-27 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0003_place_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=50)),
                ('place_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='place.Place')),
            ],
        ),
    ]
