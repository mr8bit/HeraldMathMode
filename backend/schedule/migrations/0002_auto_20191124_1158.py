# Generated by Django 2.1.7 on 2019-11-24 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AnswerOnHelpSerializer',
            new_name='AnswerOnIssueSerializer',
        ),
    ]