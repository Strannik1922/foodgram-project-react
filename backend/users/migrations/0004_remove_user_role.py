from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20221017_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]
