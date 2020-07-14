# Generated by Django 3.0.7 on 2020-07-08 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0002_auto_20200703_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='kid',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='kidinstance',
            name='rules',
            field=models.ManyToManyField(help_text='Select a rule to give to this kid', to='chart.Rule'),
        ),
    ]