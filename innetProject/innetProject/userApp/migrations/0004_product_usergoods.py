# Generated by Django 3.0.6 on 2020-05-11 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0003_auto_20200511_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('proId', models.BigAutoField(primary_key=True, serialize=False)),
                ('proName', models.CharField(max_length=200)),
                ('proPrice', models.FloatField(default=0.0)),
                ('proImg', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='UserGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='userApp.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='userApp.UserInfo')),
            ],
            options={
                'db_table': 'userGoods',
            },
        ),
    ]
