<<<<<<< HEAD
# Generated by Django 3.2.13 on 2022-11-16 15:42
=======
# Generated by Django 3.2.13 on 2022-11-17 00:38
>>>>>>> c5029a766c710ae73d24d3dc546651c1926af4b5

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Trade_type', models.IntegerField(choices=[(1, '팝니다'), (2, '삽니다')])),
                ('title', models.CharField(max_length=80)),
                ('content', models.TextField(max_length=500)),
                ('price', models.IntegerField(default=0)),
                ('status_type', models.IntegerField(choices=[(1, '거래중'), (2, '거래완료')], default=1)),
                ('keyboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.keyboard')),
                ('marker', models.ManyToManyField(related_name='jjim', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trade_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('trade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade.trades')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='media/')),
                ('trade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade.trades')),
            ],
        ),
    ]
