from django.conf.urls import url
from .views import BoardView, CardAddView, ListAddView

urlpatterns = [
    url(r'^board/', BoardView.as_view(), name="board"),
    url(r'^addlist/', ListAddView.as_view(), name="listadd"),
    url(r'^addCard/', CardAddView.as_view(), name="cardadd"),
]