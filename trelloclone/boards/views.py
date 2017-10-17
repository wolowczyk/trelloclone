from django.shortcuts import redirect, render
from django.views import View
from .forms import CardAddForm, CommentAddForm, ListAddForm
from .models import Card, Comment, List


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

    def get(self, request, list_id):
        form = CardAddForm()
        return render(request, 'boards/card_form.html', {'form': form, 'list_id': list_id})

    def post(self, request, list_id):
        form = CardAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request)
            return redirect('/board')
        else:
            form = CardAddForm()
        return render(request, 'boards/card_form.html', {'form': form, 'list_id': list_id})


class CommentAddView(View):

    def get(self, request, card_id):
        form = CommentAddForm()
        return render(request, 'boards/comment_form.html', {'form': form, 'card_id': card_id})

    def post(self, request, card_id):
        form = CommentAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request)
            return redirect('/board')
        else:
            form = CommentAddForm()
        return render(request, 'boards/comment_form.html', {'form': form, 'card_id': card_id})


class SingleListView(View):

    def get(self, request, list_id):
        list = List.objects.get(id=list_id)
        cards_list = Card.objects.filter(card_list=list)

        ctx = {
            'cards_list': cards_list,
            'list': list,
        }
        return render(request, 'boards/singlelist.html', ctx)