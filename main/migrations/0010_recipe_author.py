# Generated by Django 4.0.1 on 2022-07-27 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_friend_request_customuser_friends_delete_friend_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='author',
            field=models.CharField(default='mr.Fermenter', max_length=500),
            preserve_default=False,
        ),
    ]