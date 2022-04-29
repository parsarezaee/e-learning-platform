# Generated by Django 4.0.4 on 2022-04-29 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_basecontent_video_text_image_file_content_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderContent',
        ),
        migrations.CreateModel(
            name='OrderedContent',
            fields=[
            ],
            options={
                'ordering': ['created'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('courses.basecontent',),
        ),
    ]
