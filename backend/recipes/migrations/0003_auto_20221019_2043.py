from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20221019_1927'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shoping_card',
            new_name='ShopingCard',
        ),
    ]
