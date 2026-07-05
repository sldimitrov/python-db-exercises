import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Blog

blog1 = Blog.objects.create(
    post = "This is my first blog",
    author = "Slavi"
)

blog1.save()

print(Blog.objects.get(id=1))