from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_author_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='book',
            name='edition',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_year',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
