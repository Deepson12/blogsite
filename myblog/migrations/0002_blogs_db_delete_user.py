# Generated by Django 4.2.1 on 2023-06-11 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogs_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('subtitle', models.TextField()),
                ('tags', models.CharField(max_length=25)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
