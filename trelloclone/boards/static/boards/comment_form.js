document.addEventListener("DOMContentLoaded", function() {
    var card_id = document.getElementById('card_id');
    card_id.style.display = 'none';
    var el = document.getElementById('id_comment_card');
    el.parentNode.style.display = 'none';
    el.children[card_id.innerHTML].setAttribute("selected", "selected");

});