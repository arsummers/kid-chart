# Generated by Django 3.0.7 on 2020-07-14 21:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0003_auto_20200708_2233'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Kid',
            new_name='Kids',
        ),
        migrations.RenameModel(
            old_name='Rule',
            new_name='Rules',
        ),
        migrations.CreateModel(
            name='RuleInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this rule', primary_key=True, serialize=False)),
                ('rules', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chart.Rules')),
            ],
        ),
    ]
