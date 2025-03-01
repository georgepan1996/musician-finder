# Generated by Django 2.1.4 on 2019-05-28 23:11

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users_core', '0036_auto_20190528_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='blues',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Blues', 'Blues'), ('Blues Rock', 'Blues Rock'), ('Country Blues', 'Country Blues'), ('Rythm & Blues', 'Rythm & Blues'), ('Electric Blues', 'Electric Blues'), ('Boogie-Woogie', 'Boogie-Woogie'), ('Bluegrass', 'Bluegrass'), ('Delta Blues', 'Delta Blues')], max_length=95),
        ),
        migrations.AlterField(
            model_name='profile',
            name='music_nature',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Drummer', 'Drummer'), ('Τραγουδιστής', 'Τραγουδιστής'), ('Κιθαρίστας', 'Κιθαρίστας'), ('Μπασίστας', 'Μπασίστας'), ('Στιχουργός', 'Στιχουργός '), ('Σαξοφωνίστας', 'Σαξοφωνίστας '), ('Κλαριτζής', 'Κλαριτζής '), ('Dj', 'Dj ')], max_length=78),
        ),
    ]
