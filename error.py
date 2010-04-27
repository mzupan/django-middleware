from django.conf import settings

import traceback

class AjaxErrorMiddleware:
    def process_exception(self, request, exception):
        if request.META.has_key('HTTP_X_REQUESTED_WITH') and settings.DEBUG:
            print traceback.format_exc() 