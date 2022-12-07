
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.TextField(db_index=True, default='Anonymous', max_length=50, verbose_name='Name'),
        ),
    ]
