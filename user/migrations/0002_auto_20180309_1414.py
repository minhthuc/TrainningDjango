# Generated by Django 2.0.2 on 2018-03-09 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usergroup',
            old_name='groupID',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='usergroup',
            old_name='userID',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='userrole',
            old_name='roleID',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='userrole',
            old_name='userID',
            new_name='user',
        ),
    ]
