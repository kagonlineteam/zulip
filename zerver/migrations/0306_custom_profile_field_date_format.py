from django.db import migrations


class Migration(migrations.Migration):
    """
    We previously accepted invalid ISO 8601 dates like 1909-3-5 for
    date values of custom profile fields. Correct them by adding the
    missing leading zeros: 1909-03-05.
    """

    dependencies = [
        ("zerver", "0305_realm_deactivated_redirect"),
    ]

    operations = []
