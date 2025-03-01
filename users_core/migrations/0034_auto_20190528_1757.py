# Generated by Django 2.1.4 on 2019-05-28 14:57

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users_core', '0033_auto_20190525_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rock',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Classic Rock', 'Classic Rock'), ('Progressive Rock', 'Progressive Rock'), ('Post Rock', 'Post Rock'), ('Rock&Roll', 'Rock&Roll'), ('Psychedelic Rock', 'Psychedelic Rock'), ('Hard Rock', 'Hard Rock'), ('Garage Rock', 'Garage Rock'), ('Surf Rock', 'Surf Rock'), ('Instrumental Rock', 'Instrumental Rock'), ('Rockabilly', 'Rockabilly')], max_length=127),
        ),
    ]
