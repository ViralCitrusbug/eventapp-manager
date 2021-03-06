# Generated by Django 4.0.3 on 2022-03-23 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0002_eventslot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(blank=True, db_column='t', null=True)),
                ('mod', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cv_alloc_times',
                'ordering': ('time',),
            },
        ),
        migrations.AddField(
            model_name='eventslot',
            name='time',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='eventapp.time'),
            preserve_default=False,
        ),
    ]
