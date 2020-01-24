# Generated by Django 2.2.7 on 2019-12-16 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0011_auto_20190418_0137'),
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dat',
            options={'base_manager_name': 'objects'},
        ),
        migrations.RemoveField(
            model_name='dat',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='dat',
            name='file',
        ),
        migrations.RemoveField(
            model_name='dat',
            name='id',
        ),
        migrations.RemoveField(
            model_name='dat',
            name='name',
        ),
        migrations.AddField(
            model_name='dat',
            name='file_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='filer.File'),
            preserve_default=False,
        ),
    ]
