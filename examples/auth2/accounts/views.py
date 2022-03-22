from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="login/")
def main_view(request):
    if request.method == "GET":

        text = "<p>is_authenticated: {}</p><p>has_perm add user: {}</p><p>has_perm delete user: {}</p>".format(
            request.user.is_authenticated,
            request.user.has_perm("accounts.add_users"),
            request.user.has_perm("accounts.delete_users"),
        )

        return render(
            request,
            "accounts/main.html",
            {"text": text}
        )

    return ""
