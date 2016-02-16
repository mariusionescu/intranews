# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, null=True)),
                ('component_type', models.CharField(default=b'html', max_length=32, choices=[(b'text', b'Text'), (b'html', b'HTML'), (b'image', b'Image'), (b'video', b'Video'), (b'audio', b'Audio'), (b'script', b'Script'), (b'iframe', b'Iframe')])),
                ('value', models.TextField()),
                ('parent', models.ForeignKey(to='wall.Component', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='component',
            field=models.ForeignKey(to='wall.Component'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
