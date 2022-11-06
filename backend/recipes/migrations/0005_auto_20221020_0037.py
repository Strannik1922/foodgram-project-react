from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0004_auto_20221020_0020'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShopingCart',
            new_name='ShoppingCart',
        ),
    ]
