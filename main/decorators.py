from django.shortcuts import redirect
from django.urls import reverse

def anonymous_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('base'))
        else:
            return view_func(request, *args, **kwargs)
    return wrapped_view
