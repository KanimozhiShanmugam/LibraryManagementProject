# Generated by Django 4.1.4 on 2023-01-19 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Student_password',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='issue_book',
            name='End_Date',
            field=models.DateField(default=0),
        ),
        migrations.AlterField(
            model_name='issue_book',
            name='Start_Date',
            field=models.DateField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='Student_Phno',
            field=models.BigIntegerField(default=0),
        ),
    ]