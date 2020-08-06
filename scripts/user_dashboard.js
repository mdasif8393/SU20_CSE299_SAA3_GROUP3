/*************  USER DASHBOARD PAGE *************/

var sidebar_menu_options = document.getElementById("menu-sidebar"),
    main_body = document.getElementById("main"),
    profile_info = document.getElementById("my-profile"),
    past_user_orders = document.getElementById("my-orders"),
    wish_list = document.getElementById("wish-list"),
    user_favourites = document.getElementById("favourites"),
    user_settings = document.getElementById("settings"),
    edit_profile = document.getElementById("edit-profile"),
    reset_password = document.getElementById("reset-password");

sidebar_menu_options.style.display = "none"; 
profile_info.style.display = "block"; 
past_user_orders.style.display = "none"; 
wish_list.style.display = "none"; 
user_favourites.style.display = "none"; 
user_settings.style.display = "none"; 
edit_profile.style.display = "none"; 
reset_password.style.display = "none"; 

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
  edit_profile.style.display = "none"; 
  wish_list.style.display = "none";
  reset_password.style.display = "none"; 
}

function my_orders_page(){
  profile_info.style.display = "none"; 
  past_user_orders.style.display = "block"; 
  user_favourites.style.display = "none";
  user_settings.style.display = "none"; 
  edit_profile.style.display = "none"; 
  wish_list.style.display = "none";
  reset_password.style.display = "none"; 
}

function wish_list_page(){
  profile_info.style.display = "none"; 
  past_user_orders.style.display = "none"; 
  user_favourites.style.display = "none";
  user_settings.style.display = "none"; 
  edit_profile.style.display = "none"; 
  wish_list.style.display = "block";
  reset_password.style.display = "none";    
}

function favourites_page(){
  profile_info.style.display = "none"; 
  past_user_orders.style.display = "none"; 
  user_favourites.style.display = "block";
  user_settings.style.display = "none"; 
  edit_profile.style.display = "none"; 
  wish_list.style.display = "none";
  reset_password.style.display = "none"; 
}

function settings_page(){
  profile_info.style.display = "none"; 
  past_user_orders.style.display = "none"; 
  user_favourites.style.display = "none";
  user_settings.style.display = "block"; 
  edit_profile.style.display = "none"; 
  wish_list.style.display = "none";
  reset_password.style.display = "none";   
}

function edit_profile_page(){
  profile_info.style.display = "none"; 
  past_user_orders.style.display = "none"; 
  user_favourites.style.display = "none";
  user_settings.style.display = "none"; 
  edit_profile.style.display = "block"; 
  wish_list.style.display = "none";
  reset_password.style.display = "none"; 
}

function change_password_page(){
  profile_info.style.display = "none"; 
  past_user_orders.style.display = "none"; 
  user_favourites.style.display = "none";
  user_settings.style.display = "none"; 
  edit_profile.style.display = "none"; 
  wish_list.style.display = "none";
  reset_password.style.display = "block"; 
}