# Generated by Django 5.1.3 on 2024-11-20 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTypeFlow', '0008_alter_mbtidescription_subtipo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mbtidescription',
            name='tipo',
            field=models.TextField(max_length=46),
        ),
    ]
