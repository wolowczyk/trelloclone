from django.shortcuts import redirect, render
from django.views import View
from .forms import CardAddForm, ListAddForm
from .models import Card, List


class BoardView(View):

    def get(self, request):
        l_list = List.objects.all()

        ctx = {
            'l_list': l_list,
        }
        return render(request, 'boards/board.html', ctx)


class ListAddView(View):

    def get(self, request):
        form = ListAddForm()
        return render(request, 'boards/list_form.html', {'form': form})

    def post(self, request):
        form = ListAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request)
            return redirect('/board')
        else:
            form = ListAddForm()
        return render(request, 'boards/list_form.html', {'form': form})


class CardAddView(View):

    def get(self, request):
        form = CardAddForm()
        return render(request, 'boards/card_form.html', {'form': form})

    def post(self, request):
        form = CardAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request)
            return redirect('/board')
        else:
            form = CardAddForm()
        return render(request, 'boards/card_form.html', {'form': form})
