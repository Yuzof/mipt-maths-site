from django.shortcuts import render
from django.core.cache import cache
from . import terms_work
from . import choice_work


def index(request):
    return render(request, "index.html")


def terms_list(request):
    terms = terms_work.get_terms_for_table()
    return render(request, "term_list.html", context={"terms": terms})


def add_term(request):
    return render(request, "term_add.html")


def send_term(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_term = request.POST.get("new_term", "")
        new_definition = request.POST.get("new_definition", "").replace(";", ",")
        context = {"user": user_name}
        if len(new_definition) == 0:
            context["success"] = False
            context["comment"] = "Описание должно быть не пустым"
        elif len(new_term) == 0:
            context["success"] = False
            context["comment"] = "Термин должен быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Ваш термин принят"
            terms_work.write_term(new_term, new_definition)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "term_request.html", context)
    else:
        add_term(request)


def show_stats(request):
    stats = terms_work.get_terms_stats()
    return render(request, "stats.html", stats)

def cover_page(request):
    return render(request, "cover_page.html")

def pricing_page(request):
    return render(request, "pricing_page.html")

def send_choice(request):
    if request.method == "POST":
        cache.clear()
        yourself = request.POST.get("yourself_button")
        online = request.POST.get("online_button")
        tutor = request.POST.get("tutor_button")
        choice_work.write_choice(yourself, online, tutor)
    context = choice_work.get_choice_stats()
    return render(request, "pricing_page.html", context)