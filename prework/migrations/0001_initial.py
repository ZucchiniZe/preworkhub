# Generated by Django 2.0a1 on 2017-10-18 18:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created', models.DateField(default=datetime.date.today, verbose_name='Date created')),
                ('video_link', models.CharField(max_length=100)),
                ('video_num', models.SmallIntegerField(default=1)),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('notes', models.TextField(blank=True)),
                ('class_date', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='videos', to='classes.ClassDate')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='videos', to='classes.Subject')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='videos', to='classes.Unit')),
            ],
            options={
                'ordering': ['-created'],
                'get_latest_by': 'created',
            },
        ),
        migrations.CreateModel(
            name='VideoMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('got_it', models.BooleanField(default=False)),
                ('watched', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Student')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prework.Video')),
            ],
        ),
    ]