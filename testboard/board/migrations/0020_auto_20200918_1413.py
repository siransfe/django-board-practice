# Generated by Django 2.2.16 on 2020-09-18 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0019_auto_20200918_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='board.Board'),
        ),
    ]
