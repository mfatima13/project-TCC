# Generated by Django 3.0.5 on 2020-10-22 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0006_auto_20200616_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='team.Team'),
        ),
    ]
