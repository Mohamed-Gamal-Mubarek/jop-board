# Generated by Django 3.0.6 on 2022-03-10 14:40

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_job_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='img',
            field=models.ImageField(upload_to=job.models.upload_image),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=100),
        ),
    ]