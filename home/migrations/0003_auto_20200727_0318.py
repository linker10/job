# Generated by Django 3.0.8 on 2020-07-26 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200726_2023'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personnel',
            options={'verbose_name_plural': 'personnel'},
        ),
        migrations.AlterField(
            model_name='personnel',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
