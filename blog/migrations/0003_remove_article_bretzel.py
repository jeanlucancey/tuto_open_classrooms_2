# Generated by Django 2.0 on 2018-08-23 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_bretzel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='bretzel',
        ),
    ]
