# Generated by Django 3.2.6 on 2021-08-19 12:55

from django.db import migrations, models
import django.db.models.deletion


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
            ],
            options={
                'db_table': 'wakes',
            },
        ),
        migrations.CreateModel(
            name='MemberWakes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.member')),
                ('wake_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.wake')),
            ],
            options={
                'db_table': 'member_wakes',
            },
        ),
    ]