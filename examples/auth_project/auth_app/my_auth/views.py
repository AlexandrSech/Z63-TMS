from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from django.views.decorators.csrf import csrf_exempt
from .models import MyUser


@csrf_exempt
def registration(request):
    """
    вьюха для регистрации

    если гет запрос то просто выдаем пустую страницу с формой

    если пост - получаем с этой формы данные от юзера, проверяем,
     что таких же логина и емэйла нет в базе, создаем его в базе,
     читаем базу проверяя что запись появилась
    """
    if request.method == "GET":
        return render(request, "my_auth/registration.html", {})
    elif request.method == "POST":
        # get data from user in form
        users_data = RegistrationForm(request.POST)

        # check db for data like this
        login_check = MyUser.objects.filter(login=users_data.data["login"])
        # print(login_check)
        if login_check:
            return HttpResponse("Login {} already exist".format(users_data.data["login"]))
        email_check = MyUser.objects.filter(login=users_data.data["email"])
        # print(email_check)
        if email_check:
            return HttpResponse("Email {} already exist".format(users_data.data["email"]))

        # create data in db
        users_data.save()

        # check db for new data
        new_user = MyUser.objects.filter(login=users_data.data["login"])

        # return HttpResponse("User {} created: ok.".format(new_user[0].login))
        if new_user:
            return redirect("http://127.0.0.1:8000/login")
        return HttpResponse("Something going wrong...")


@csrf_exempt
def login(request):
    if request.method == "GET":
        # print(request.session.get("visites"))
        return render(request, "my_auth/login.html", {})
    elif request.method == "POST":
        users_data = RegistrationForm(request.POST)

        user = MyUser.objects.filter(login=users_data.data["login"])
        if user:
            if user[0].password == users_data.data["password"]:
                request.session["login"] = users_data.data["login"]
                return redirect("http://127.0.0.1:8000/main")
            else:
                return render(request, "my_auth/login.html", {"error_message": "wrong password"})
        else:
            return render(request, "my_auth/login.html", {"error_message": "no user like this"})


def logout(request):
    if "login" in request.session:
        del request.session["login"]
    print(request.session)
    return redirect("http://127.0.0.1:8000/login")


def main(request):
    """if "visited" in request.session:
        request.session["visited"] += 1
    else:
        request.session["visited"] = 1"""

    """request.session["visites"] = request.session.get("visites", 0) + 1
    print(request.session.get("visites"))"""

    if request.session.get("login", None):
        return render(request, "my_auth/main.html", {})
    return redirect("http://127.0.0.1:8000/login")
