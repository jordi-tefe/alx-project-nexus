from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_admin_user(apps, schema_editor):
    # Use your custom user model
    User = apps.get_model('polls', 'User')
    
    # Check if admin user already exists
    if not User.objects.filter(username='admin').exists():
        User.objects.create(
            username='admin',
            email='jordisavage90@gmail.com',
            password=make_password('jordi1993'),  # change this password if needed
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_remove_vote_unique_user_vote_and_more'),  # keep your last migration
    ]

    operations = [
        migrations.RunPython(create_admin_user),
    ]
