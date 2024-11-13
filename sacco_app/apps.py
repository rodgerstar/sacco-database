# sacco_app/apps.py
from django.apps import AppConfig

class SaccoAppConfig(AppConfig):  # Updated to match settings.py
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sacco_app'
