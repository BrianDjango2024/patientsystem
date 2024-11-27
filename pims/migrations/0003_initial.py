# Generated by Django 5.1.3 on 2024-11-22 05:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pims', '0002_remove_record_disease_remove_record_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialist', models.CharField(max_length=20, verbose_name='診療科')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=20, verbose_name='患者氏名')),
                ('birthday', models.CharField(max_length=8, verbose_name='生年月日')),
                ('gender', models.CharField(max_length=4, verbose_name='性別')),
                ('tel_number', models.CharField(max_length=11, verbose_name='電話番号')),
                ('address', models.CharField(max_length=100, verbose_name='住所')),
                ('condition', models.TextField(verbose_name='病状')),
                ('image1', models.ImageField(upload_to='attachment', verbose_name='イメージ１')),
                ('image2', models.ImageField(upload_to='attachment', verbose_name='イメージ2')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='attachment', verbose_name='イメージ3')),
                ('record_at', models.DateTimeField(auto_now_add=True, verbose_name='記録日時')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='担当医')),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pims.specialist', verbose_name='診療科')),
            ],
        ),
    ]
