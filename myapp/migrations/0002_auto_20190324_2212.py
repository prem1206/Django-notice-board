# Generated by Django 2.1.7 on 2019-03-24 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='name',
            field=models.TextField(blank=True, max_length=4000, null=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='message',
            field=models.TextField(blank=True, max_length=4000, null=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notices', to='myapp.Board'),
        ),
    ]