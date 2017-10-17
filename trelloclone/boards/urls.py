from django.conf.urls import url
from .views import BoardView, CardAddView, CommentAddView, SingleListView, ListAddView

urlpatterns = [
    url(r'^board/', BoardView.as_view(), name="board"),
    url(r'^addlist/', ListAddView.as_view(), name="listadd"),
    url(r'^addcard/(?P<list_id>(\d)+)/', CardAddView.as_view(), name="cardadd"),
    url(r'^addcomment/(?P<card_id>(\d)+)/', CommentAddView.as_view(), name="commentadd"),
    url(r'^list/(?P<list_id>(\d)+)/', SingleListView.as_view(), name="singlelistview"),
]