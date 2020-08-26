var sidebar_menu_options = document.getElementById("menu-sidebar"),
    main_body = document.getElementById("main");
  

    var divs = ["dashboard-homepage", "orders", "products", "refunds",   "edit-product", "add-product"];
     for(var j=0;j<divs.length;j++){
         if(divs[j]=='dashboard-homepage'){
            document.getElementById(divs[j]).style.display = "block";
            console.log( document.getElementById(divs[j]));
         }
         else{
            document.getElementById(divs[j]).style.display = "none"; 
         }
     }


    function change_content(ids){
    var div = ["dashboard-homepage", "orders", "products", "refunds", "edit-product", "add-product"];
     for(var i=0;i<div.length;i++){
         if(ids==div[i]){
            document.getElementById(div[i]).style.display = "block";
            console.log( document.getElementById(div[i]));
         }
         else{
            document.getElementById(div[i]).style.display = "none"; 
         }
     }
    }

function openSidebar() {
    main_body.style.display = "none"; 
    sidebar_menu_options.style.display = "block"; 
  }

function closeSidebar() {
    main_body.style.display = "block"; 
    sidebar_menu_options.style.display = "none"; 
  }
