# Generated by Django 4.0.2 on 2022-03-17 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_rename_dated_expense_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ('-date',)},
        ),
    ]
