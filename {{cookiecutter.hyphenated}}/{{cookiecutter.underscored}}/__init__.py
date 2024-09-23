import django_plugins


@django_plugins.hookimpl
def installed_apps():
    # A list of app strings to add to INSTALLED_APPS:
    return []


@django_plugins.hookimpl
def urlpatterns():
    # A list of URL patterns to add to urlpatterns:
    return []


@django_plugins.hookimpl
def settings(current_settings):
    # Make changes to the Django settings.py globals here
    pass


@django_plugins.hookimpl
def middleware():
    # A list of middleware class strings to add to MIDDLEWARE:
    # Wrap strings in django_plugins.Before("middleware_class_name") or
    # django_plugins.After("middleware_class_name") to specify before or after
    return []
