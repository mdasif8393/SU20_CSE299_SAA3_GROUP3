/*************  USER DASHBOARD PAGE *************/

var sidebar_menu_options = document.getElementById("menu-sidebar"),
    main_body = document.getElementById("main"),
    profile_info = document.getElementById("my-profile"),
    past_user_orders = document.getElementById("my-orders"),
    user_favourites = document.getElementById("favourites"),
    user_settings = document.getElementById("settings");

sidebar_menu_options.style.display = "none"; 
profile_info.style.display = "block"; 
past_user_orders.style.display = "none"; 
user_favourites.style.display = "none"; 
user_settings.style.display = "none"; 

function openSidebar() {
    main_body.style.display = "none"; 
    sidebar_menu_options.style.display = "block"; 
  }

function closeSidebar() {
    main_body.style.display = "block"; 
    sidebar_menu_options.style.display = "none"; 
  }

function profile_page(){
  profile_info.style.display = "block"; 
  past_user_orders.style.display = "none"; 
  user_favourites.style.display = "none";
  user_settings.style.display = "none"; 
}

function my_orders_page(){
  past_user_orders.style.display = "block"; 
  profile_info.style.display = "none";
  user_settings.style.display = "none";  
}

function favourites_page(){
  user_favourites.style.display = "block"; 
  past_user_orders.style.display = "none"; 
  profile_info.style.display = "none";
  user_settings.style.display = "none";  
}

function settings_page(){
  user_settings.style.display = "block"; 
  past_user_orders.style.display = "none";
  user_favourites.style.display = "none";  
  profile_info.style.display = "none"; 
}