from django.contrib.auth import get_user_model
from django.http import HttpResponse


class CheckSubsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/api/products/'):
            if request.user.is_authenticated:
                user_id = request.user.id
                u = get_user_model().objects.get(id=user_id)
                if u.is_active:
                    response = self.get_response(request)
                    return response
            return HttpResponse('Приобретите подписку!!!')
        else:
            response = self.get_response(request)
            return response

