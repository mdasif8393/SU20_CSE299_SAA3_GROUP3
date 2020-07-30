/*************  USER DASHBOARD PAGE *************/

var sidebar_menu_options = document.getElementById("menu-sidebar");
var main_body = document.getElementById("main");

sidebar_menu_options.style.display = "none"; 

function openSidebar() {
    main_body.style.display = "none"; 
    sidebar_menu_options.style.display = "block"; 
  }

function change_form2(){
       exp_form.style.display = "block";
       stay_form.style.display = "none";
  }
