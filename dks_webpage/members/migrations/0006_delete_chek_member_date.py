# Generated by Django 4.1.7 on 2023-04-20 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_rename_clock_chek'),
    ]

    operations = [
        migrations.DeleteModel(
            name='chek',
        ),
        migrations.AddField(
            model_name='member',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
