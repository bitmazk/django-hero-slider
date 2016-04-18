# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 01:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_libs.models_mixins
import filer.fields.file


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField(blank=True, null=True, verbose_name='Position')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('external_url', models.CharField(blank=True, max_length=512, verbose_name='External URL')),
                ('text_position_top', models.IntegerField(blank=True, null=True, verbose_name='Text position top')),
                ('text_position_bottom', models.IntegerField(blank=True, null=True, verbose_name='Text position bottom')),
                ('text_position_left', models.IntegerField(blank=True, null=True, verbose_name='Text position left')),
                ('text_position_right', models.IntegerField(blank=True, null=True, verbose_name='Text position right')),
            ],
            options={
                'abstract': False,
            },
            bases=(django_libs.models_mixins.TranslationModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SliderItemCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=128, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
            bases=(django_libs.models_mixins.TranslationModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SliderItemCategoryTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='hero_slider.SliderItemCategory')),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'hero_slider_slideritemcategory_translation',
                'db_tablespace': '',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='SliderItemTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, verbose_name='Title')),
                ('description', models.CharField(blank=True, max_length=512, verbose_name='Description')),
                ('link_text', models.CharField(blank=True, max_length=512, verbose_name='Link text')),
                ('is_published', models.BooleanField(default=False, verbose_name='Is published')),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='hero_slider.SliderItem')),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'hero_slider_slideritem_translation',
                'db_tablespace': '',
                'default_permissions': (),
            },
        ),
        migrations.AddField(
            model_name='slideritem',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hero_slider.SliderItemCategory', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='slideritem',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='slideritem',
            name='image',
            field=filer.fields.file.FilerFileField(on_delete=django.db.models.deletion.CASCADE, to='filer.File', verbose_name='Image'),
        ),
        migrations.AlterUniqueTogether(
            name='slideritemtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='slideritemcategorytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
