# Generated by Django 3.2 on 2022-04-11 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.post')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_name', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
