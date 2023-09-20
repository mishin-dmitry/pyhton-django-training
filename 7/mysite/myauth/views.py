from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy

# Create your views here.


def login_view(request: HttpRequest):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("/admin/")

        return render(request, "myauth/login.html")

    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)

        return redirect("/admin/")

    return render(request, "myauth/login.html", {"error": "invalid login"})


def set_cookie_view(request: HttpRequest) -> HttpResponse:
    response = HttpResponse("Cookie set")
    response.set_cookie("foo", "bar", max_age=3600)

    return response


def get_cookie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get("foo", "default")

    return HttpResponse(f"Cookie value - {value}")


def set_session_view(request: HttpRequest) -> HttpResponse:
    request.session["foo"] = "bar"

    return HttpResponse("session set")


def get_session_view(request: HttpRequest) -> HttpResponse:
    value = request.session.get("foo", "default")

    return HttpResponse(f"Session value - {value}")


def logout_view(request: HttpRequest):
    logout(request)

    return redirect(reverse("myauth:login"))


class LogoutVew(LogoutView):
    next_page = reverse_lazy("myauth:login")
