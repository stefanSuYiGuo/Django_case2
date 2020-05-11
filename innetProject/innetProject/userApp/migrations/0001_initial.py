# Generated by Django 3.0.6 on 2020-05-11 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('userID', models.BigIntegerField(primary_key=True, serialize=False)),
                ('userAccount', models.CharField(max_length=50, unique=True)),
                ('userPass', models.CharField(max_length=30)),
                ('userBirth', models.DateField()),
                ('userGender', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'userInfoTable',
            },
        ),
    ]
