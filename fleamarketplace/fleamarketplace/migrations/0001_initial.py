from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [("migrations")]

    operations = [
        migrations.AddField("Product", "category", models.ForeignKey(models.Category), False),
    ]