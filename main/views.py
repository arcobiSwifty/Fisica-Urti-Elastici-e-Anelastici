from django.shortcuts import render, redirect

from django.views import View


class UrtoElastico(View):
    def get(self, request):
        return render(request, "elastico.html")

class UrtoAnelastico(View):
    def get(self, request):
        return render(request, "anelastico.html")

class Home(View):
    def get(self, request):
        return render(request, "home.html")
