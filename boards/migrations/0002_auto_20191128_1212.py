# Generated by Django 2.2.7 on 2019-11-28 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='post',
            name='message',
        ),
        migrations.RemoveField(
            model_name='post',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='board',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='starter',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='subject',
        ),
    ]
