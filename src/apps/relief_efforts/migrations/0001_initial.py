# Generated by Django 3.0.4 on 2020-03-28 09:43

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReliefEfforts',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('relief_name', models.CharField(max_length=999)),
                ('contact_details', models.TextField(blank=True, default='N/A')),
                ('severity_urgency', models.CharField(default='N/A', max_length=50)),
                ('status', models.CharField(default='N/A', max_length=50)),
                ('needs', models.TextField(default='N/A')),
                ('org_type', models.CharField(choices=[('hospital', 'hospital'), ('organization', 'organization'), ('business', 'business'), ('supplier', 'supplier'), ('research', 'research'), ('facility', 'facility'), ('lgu', 'lgu'), ('personal', 'personal'), ('other', 'other')], default='other', max_length=50)),
                ('relief_type', models.CharField(choices=[('frontliner', 'frontliner'), ('families', 'families'), ('public', 'public'), ('supplier', 'supplier'), ('testing kit for PUI', 'testing kit for PUI'), ('other service personel', 'other service personel'), ('other', 'other')], default='other', max_length=999)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('link_for_more_info', models.TextField(default='N/A')),
                ('other_info', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Relief Efforts',
                'ordering': ('-update_date',),
            },
        ),
    ]
