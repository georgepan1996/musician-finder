# Generated by Django 2.1.4 on 2019-04-09 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_core', '0012_auto_20190408_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='name',
        ),
        migrations.AddField(
            model_name='song',
            name='composition',
            field=models.FileField(blank=True, upload_to='uploaded_music'),
        ),
        migrations.AddField(
            model_name='song',
            name='composition_title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
