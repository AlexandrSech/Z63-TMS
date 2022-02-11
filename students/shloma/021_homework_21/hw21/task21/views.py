from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Person
from .forms import PersonModelForm

# Create your views here.


def index(request):
    persons = Person.objects.all()
    return render(request, "task21/index.html", context={"persons": persons})


def show_one_person(request, person_id: int):
    person = get_object_or_404(Person, id=person_id)
    # person_form = PersonModelForm()

    return render(request, "task21/person_detail.html", {"person": person})


def edit_person(request, person_id: int):
    person = get_object_or_404(Person, id=person_id)

    if request.method == "GET":
        person_form = PersonModelForm()
        return render(request, "task21/person_edit.html", {"person": person, "form": person_form})

    elif request.method == "POST":
        form = PersonModelForm(request.POST)

        if form.is_valid():
            person.firstname = form.cleaned_data.get("firstname")
            person.lastname = form.cleaned_data.get("lastname")
            person.age = form.cleaned_data.get("age")
            person.profession = form.cleaned_data.get("profession")
            person.save()

        return redirect('person_detail', person_id=person.id)

    return HttpResponse('Aaaaaaaaaaaaaaaaaaaaaaaaa')


def delete_person(request, person_id: int):
    person = get_object_or_404(Person, id=person_id)
    person.delete()

    return redirect('index')
