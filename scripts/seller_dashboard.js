var sidebar_menu_options = document.getElementById("menu-sidebar"),
    main_body = document.getElementById("main"),
    dashboard = document.getElementById("dashboard-homepage"),
    orders = document.getElementById("orders"),
    products = document.getElementById("products"),
    messages = document.getElementById("messages"),
    reviews = document.getElementById("reviews"),
    reports = document.getElementById("reports"),
    refunds = document.getElementById("refunds"),
    transactions = document.getElementById("transactions");
    seller_profile_settings = document.getElementById("seller-settings"),
    seller_edit_profile = document.getElementById("seller-edit-profile"),
    seller_reset_password = document.getElementById("seller-reset-password");

sidebar_menu_options.style.display = "none"; 
dashboard.style.display = "block"; 
orders.style.display = "none"; 
products.style.display = "none"; 
messages.style.display = "none"; 
reviews.style.display = "none"; 
reports.style.display = "none"; 
refunds.style.display = "none"; 
transactions.style.display = "none"; 
seller_profile_settings.style.display = "none"; 
seller_edit_profile.style.display = "none"; 
seller_reset_password.style.display = "none";

function openSidebar() {
    main_body.style.display = "none"; 
    sidebar_menu_options.style.display = "block"; 
  }

function closeSidebar() {
    main_body.style.display = "block"; 
    sidebar_menu_options.style.display = "none"; 
  }

function dashboard_home_page(){
    dashboard.style.display = "block"; 
    orders.style.display = "none"; 
    products.style.display = "none"; 
    messages.style.display = "none"; 
    reviews.style.display = "none"; 
    reports.style.display = "none"; 
    refunds.style.display = "none"; 
    transactions.style.display = "none"; 
    seller_profile_settings.style.display = "none"; 
    seller_edit_profile.style.display = "none"; 
    seller_reset_password.style.display = "none";
    
}

function orders_page(){
    dashboard.style.display = "none"; 
    orders.style.display = "block"; 
    products.style.display = "none"; 
    messages.style.display = "none"; 
    reviews.style.display = "none"; 
    refunds.style.display = "none"; 
    transactions.style.display = "none"; 
    seller_profile_settings.style.display = "none"; 
    seller_edit_profile.style.display = "none"; 
    seller_reset_password.style.display = "none";
     
}

function products_page(){
    dashboard.style.display = "none"; 
    orders.style.display = "none"; 
    products.style.display = "block"; 
    messages.style.display = "none"; 
    reviews.style.display = "none";
    reports.style.display = "none";  
    refunds.style.display = "none"; 
    transactions.style.display = "none"; 
    seller_profile_settings.style.display = "none"; 
    seller_edit_profile.style.display = "none"; 
    seller_reset_password.style.display = "none";
       
}

function favourites_page(){
    dashboard.style.display = "block"; 
    orders.style.display = "none"; 
    products.style.display = "none"; 
    messages.style.display = "none"; 
    reviews.style.display = "none";
    reports.style.display = "none"; 
    refunds.style.display = "none"; 
    transactions.style.display = "none"; 
    seller_profile_settings.style.display = "none"; 
    seller_edit_profile.style.display = "none"; 
    seller_reset_password.style.display = "none";
    
}

function messages_page(){
    dashboard.style.display = "none"; 
    orders.style.display = "none"; 
    products.style.display = "none"; 
    messages.style.display = "block"; 
    reviews.style.display = "none"; 
    reports.style.display = "none"; 
    refunds.style.display = "none"; 
    transactions.style.display = "none"; 
    seller_profile_settings.style.display = "none"; 
    seller_edit_profile.style.display = "none"; 
    seller_reset_password.style.display = "none";
      
}

function reviews_page(){
    dashboard.style.display = "none"; 
    orders.style.display = "none"; 
    products.style.display = "none"; 
    messages.style.display = "none"; 
    reviews.style.display = "block";
    reports.style.display = "none";  
    refunds.style.display = "none"; 
    transactions.style.display = "none"; 
    seller_profile_settings.style.display = "none"; 
    seller_edit_profile.style.display = "none"; 
    seller_reset_password.style.display = "none";
    
}

function reports_page(){
    dashboard.style.display = "none"; 
    orders.style.display = "none"; 
    products.style.display = "none"; 
    messages.style.display = "none"; 
    reviews.style.display = "none";
    reports.style.display = "block";  
    refunds.style.display = "none"; 
    transactions.style.display = "none"; 
    seller_profile_settings.style.display = "none"; 
    seller_edit_profile.style.display = "none"; 
    seller_reset_password.style.display = "none";
    
}

function refunds_page(){
    dashboard.style.display = "none"; 
    orders.style.display = "none"; 
    products.style.display = "none"; 
    messages.style.display = "none"; 
    reviews.style.display = "none";
    reports.style.display = "none";  
    refunds.style.display = "block"; 
    transactions.style.display = "none"; 
    seller_profile_settings.style.display = "none"; 
    seller_edit_profile.style.display = "none"; 
    seller_reset_password.style.display = "none";
    
}

function transactions_page(){
    dashboard.style.display = "none"; 
    orders.style.display = "none"; 
    products.style.display = "none"; 
    messages.style.display = "none"; 
    reviews.style.display = "none";
    reports.style.display = "none";  
    refunds.style.display = "none"; 
    transactions.style.display = "block"; 
    seller_profile_settings.style.display = "none"; 
    seller_edit_profile.style.display = "none"; 
    seller_reset_password.style.display = "none";
    
}

function seller_settings_page(){
    dashboard.style.display = "none"; 
    orders.style.display = "none"; 
    products.style.display = "none"; 
    messages.style.display = "none"; 
    reviews.style.display = "none";
    reports.style.display = "none";  
    refunds.style.display = "none"; 
    transactions.style.display = "none"; 
    seller_profile_settings.style.display = "block"; 
    seller_edit_profile.style.display = "none"; 
    seller_reset_password.style.display = "none";
    
}