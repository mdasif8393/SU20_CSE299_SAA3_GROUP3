var item_info = document.getElementById("item-info"),
    item_review = document.getElementById("item-review");

item_info.style.display = "block";
item_review.style.display = "none";

function item_info_page(){
    item_info.style.display = "block";
    item_review.style.display = "none";
}

function review_page(){
    item_info.style.display = "none";
    item_review.style.display = "block";
}