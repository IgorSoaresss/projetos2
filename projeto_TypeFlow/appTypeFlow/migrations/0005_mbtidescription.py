# Generated by Django 5.1.1 on 2024-11-16 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTypeFlow', '0004_alter_mbtiresult_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='MBTIDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=4, unique=True)),
                ('description', models.TextField()),
                ('famous_person_image', models.ImageField(blank=True, null=True, upload_to='personalities/')),
                ('primary_color', models.CharField(default='#000000', max_length=7)),
                ('background_color', models.CharField(default='#ffffff', max_length=7)),
            ],
        ),
    ]
