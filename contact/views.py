from django.shortcuts import render


def form_view(request):
    return render(request, "contact/form.html")
