document.addEventListener("DOMContentLoaded", function() {
    var list_id = document.getElementById('list_id');
    list_id.style.display = 'none';
    var el = document.getElementById('id_card_list');
    el.parentNode.style.display = 'none';
    el.children[list_id.innerHTML].setAttribute("selected", "selected");

});