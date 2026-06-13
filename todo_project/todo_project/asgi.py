"""
ASGI config for todo_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
>>>>>>> fcf9742ac05b04750c6d4b1aaf812762669dddd9
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_project.settings')
=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo_project.settings")
>>>>>>> fcf9742ac05b04750c6d4b1aaf812762669dddd9

application = get_asgi_application()
