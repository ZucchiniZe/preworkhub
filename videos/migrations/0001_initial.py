# Generated by Django 2.0a1 on 2017-10-07 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('videos', '0001_initial'), ('videos', '0002_auto_20171007_0018')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PreworkVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created', models.DateField(auto_now_add=True)),
                ('subject', models.CharField(choices=[('calc', 'Calculus'), ('stat', 'Statistics')], max_length=4)),
                ('video_link', models.CharField(max_length=100)),
                ('class_num', models.SmallIntegerField()),
                ('video_num', models.SmallIntegerField(default=1)),
                ('slug', models.SlugField()),
                ('notes', models.TextField(blank=True)),
            ],
        ),
    ]
