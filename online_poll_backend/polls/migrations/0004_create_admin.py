from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_admin_user(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    
    # Check if admin user already exists
    if not User.objects.filter(username='admin').exists():
        User.objects.create(
            username='admin',
            email='jordisavage90@gmail.com',
            password=make_password('jordi1993'),  # change this password
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_remove_vote_unique_user_vote_and_more'),  # replace with your last migration name if different
    ]

    operations = [
        migrations.RunPython(create_admin_user),
    ]
