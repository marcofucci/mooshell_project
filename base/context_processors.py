from django.conf import settings


def load_settings(request):
    return {
			'project_name': settings.PROJECT_NAME,
			'project_status': settings.PROJECT_STATUS,
			'seo_title_pre': settings.SEO_TITLE_HEAD,
			'seo_title_tail': settings.SEO_TITLE_TAIL,
			'title_separator': settings.TITLE_SEPARATOR,
			'WEB_SERVER': request.META['SERVER_NAME']
			}