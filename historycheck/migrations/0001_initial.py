# Generated by Django 2.1.3 on 2020-04-15 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('task_description', models.TextField(max_length=1200)),
                ('accepted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
