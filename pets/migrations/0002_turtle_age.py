# Generated by Django 3.2.7 on 2021-09-25 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turtle',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]