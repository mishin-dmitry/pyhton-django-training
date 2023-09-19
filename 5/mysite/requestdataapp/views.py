from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from requestdataapp.forms import UserBioForm

# Create your views here.


def process_get_view(request: HttpRequest) -> HttpResponse:
    a = request.GET.get("a", "")
    b = request.GET.get("b", "")
    result = a + b

    context = {"a": a, "b": b, "result": result}

    return render(request, "requestdataapp/request-query-params.html", context=context)


def user_form(request: HttpRequest) -> HttpResponse:
    context = {
        "form": UserBioForm(),
    }

    return render(request, "requestdataapp/user-bio-form.html", context=context)
