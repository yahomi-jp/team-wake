# Generated by Django 3.2.6 on 2021-08-19 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12, verbose_name='名前')),
            ],
            options={
                'db_table': 'members',
            },
        ),
        migrations.CreateModel(
            name='Wake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Wake名')),
                ('member', models.ManyToManyField(related_name='wakes', related_query_name='wake', to='group.Member')),
            ],
            options={
                'db_table': 'wakes',
            },
        ),
    ]
