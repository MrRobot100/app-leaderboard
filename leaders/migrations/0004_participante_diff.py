# Generated by Django 2.0.7 on 2018-07-14 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaders', '0003_auto_20180714_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='participante',
            name='diff',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]