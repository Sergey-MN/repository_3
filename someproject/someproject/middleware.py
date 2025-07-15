from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseForbidden

from subscriptions.models import UserSubscription


class CheckSubsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/api/products/'):
            if request.user.is_authenticated:
                if not UserSubscription.objects.filter(user_id=request.user.id).exists():
                    return HttpResponseForbidden('Приобретите подписку!!!')
            else:
                return HttpResponseForbidden('Необходимо авторизоваться!')

        return self.get_response(request)
