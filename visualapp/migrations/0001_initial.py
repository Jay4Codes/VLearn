# Generated by Django 3.1 on 2023-01-21 01:11

from django.db import migrations, models
import visualapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='csvstorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=visualapp.models.path_and_rename_for_resume)),
                ('name', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
    ]
