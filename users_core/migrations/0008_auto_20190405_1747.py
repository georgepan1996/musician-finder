# Generated by Django 2.1.4 on 2019-04-05 14:47

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users_core', '0007_profile_music_nature'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='music_upload',
            field=models.FileField(blank=True, upload_to='uploaded_music'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='music_category',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Rock', 'Rock'), ('Punk', 'Punk'), ('Pop', 'Pop'), ('Hip-Hop', 'Hip-Hop')], max_length=21),
        ),
        migrations.AlterField(
            model_name='profile',
            name='music_nature',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Drummer', 'Drummer'), ('Τραγουδιστής', 'Τραγουδιστής'), ('Κιθαρίστας', 'Κιθαρίστας'), ('Μπασίστας', 'Μπασίστας'), ('Στιχουργός', 'Στιχουργός')], max_length=52),
        ),
    ]