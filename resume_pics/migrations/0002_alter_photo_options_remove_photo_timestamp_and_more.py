# Generated by Django 4.0.3 on 2022-04-02 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_pics', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={},
        ),
        migrations.RemoveField(
            model_name='photo',
            name='timestamp',
        ),
        migrations.AlterField(
            model_name='photo',
            name='height',
            field=models.IntegerField(default=25),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='img/%y'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='width',
            field=models.IntegerField(default=25),
        ),
    ]
