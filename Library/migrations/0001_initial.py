# Generated by Django 4.0.4 on 2022-05-31 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=12)),
            ],
        ),
    ]
