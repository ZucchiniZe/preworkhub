# Generated by Django 2.0a1 on 2017-10-10 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preworkvideo',
            name='class_num',
        ),
        migrations.AddField(
            model_name='preworkvideo',
            name='class_date',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='classes.ClassDate'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='preworkvideo',
            name='subject',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.PROTECT, to='classes.Subject'),
        ),
    ]
