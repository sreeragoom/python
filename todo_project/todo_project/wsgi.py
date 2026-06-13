"""
WSGI config for todo_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
>>>>>>> fcf9742ac05b04750c6d4b1aaf812762669dddd9
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_project.settings')
=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo_project.settings")
>>>>>>> fcf9742ac05b04750c6d4b1aaf812762669dddd9

application = get_wsgi_application()
