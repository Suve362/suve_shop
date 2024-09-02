from suve_main.models import Routes


def get_menu_context(request):
    urls = Routes.objects.filter(pk__in=[1, 2, 3, 4])
    return {'routes': urls}
