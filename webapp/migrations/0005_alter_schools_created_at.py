# Generated by Django 4.0.2 on 2022-02-19 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_rewardtasks_alter_schools_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schools',
            name='created_at',
            field=models.CharField(default='2022-19-02 10:29:38.334750', max_length=50),
        ),
    ]
