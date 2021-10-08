# Generated by Django 3.2.8 on 2021-10-08 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_user_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('contact_method', models.CharField(choices=[('Phone', 'Phone'), ('Email', 'Email')], max_length=6, verbose_name=' Best method for contact')),
                ('time_of_the_day_to_reach', models.CharField(choices=[('Morning', 'Morning'), ('Noon', 'Noon'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening'), ('Night', 'Night')], max_length=20, verbose_name='Best time of the day to reach you')),
                ('how_can_we_help_you', models.TextField()),
                ('additional_notes', models.TextField()),
            ],
        ),
    ]
