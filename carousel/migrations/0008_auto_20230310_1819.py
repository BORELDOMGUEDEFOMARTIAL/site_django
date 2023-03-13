# Generated by Django 3.1.2 on 2023-03-10 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carousel', '0007_auto_20230310_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article_paroissiale',
            name='document_pdf',
            field=models.FileField(blank=True, default='default.pdf', max_length=254, null=True, upload_to='public'),
        ),
        migrations.AlterField(
            model_name='article_paroissiale',
            name='document_word',
            field=models.FileField(blank=True, default='default.doc', max_length=254, null=True, upload_to='public'),
        ),
    ]
