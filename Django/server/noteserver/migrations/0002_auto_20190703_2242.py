# Generated by Django 2.2.3 on 2019-07-03 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteserver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='data',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='name',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
