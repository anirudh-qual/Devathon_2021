# Generated by Django 3.2.7 on 2021-09-17 21:27

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='address',
        ),
        migrations.RemoveField(
            model_name='student',
            name='caste',
        ),
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='phone_no',
        ),
        migrations.RemoveField(
            model_name='student',
            name='program',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_profile',
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='branch',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Cse', 'Cse'), ('Ece', 'Ece'), ('Eee', 'Eee'), ('Mech', 'Mech'), ('Chem', 'Chem'), ('Civil', 'Civil'), ('Bio', 'Bio'), ('Mme', 'Mme')], max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='caste',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Oc', 'Oc'), ('Obc', 'Obc'), ('Sc', 'Sc'), ('St', 'St')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='closingtime',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='openingtime',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='program',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Btech', 'Btech'), ('Mtech', 'Mtech'), ('PHD', 'PHD')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(blank=True, choices=[('Cse', 'Cse'), ('Ece', 'Ece'), ('Eee', 'Eee'), ('Mech', 'Mech'), ('Chem', 'Chem'), ('Civil', 'Civil'), ('Bio', 'Bio'), ('Mme', 'Mme')], max_length=100, null=True),
        ),
    ]