# Generated by Django 2.0a1 on 2017-10-10 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
        ('videos', '0002_add_more_foreignkeys'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('got_it', models.BooleanField(default=False)),
                ('watched', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Student')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.PreworkVideo')),
            ],
        ),
    ]