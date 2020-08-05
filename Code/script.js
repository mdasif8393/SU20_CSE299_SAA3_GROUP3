//iphone + button work
var iphonePlusButton=document.getElementById('iphonePlusButton');
iphonePlusButton.addEventListener('click',function(){
   iphoneNumberPositive ("iphoneNumber");
   // var iphoneNumber = document.getElementById("iphoneNumber").value;
   // var floatIphoneNumber = parseFloat(iphoneNumber.replace(/,/g, ''));
   // document.getElementById("iphoneNumber").value = floatIphoneNumber +1;
   iphonePricePositive("iphonePrice");
   // var iphonePrice = document.getElementById("iphonePrice").innerText;
   // var floatIphonePrice = parseFloat(iphonePrice.replace(/,/g, ''));
   // document.getElementById("iphonePrice").innerText = floatIphonePrice + 1219 ;
   iphoneSubTotalPositive("subTotal");

   iphoneTotalPositive("total");

});

//iphone case + button work
var iphoneCasePlusButton=document.getElementById('iphoneCasePlusButton');
iphoneCasePlusButton.addEventListener('click',function(){
   iphoneCaseNumberPositive ("iphoneCaseNumber");
   
   iphoneCasePricePositive("iphoneCasePrice");

   iphoneCaseSubTotalPricePositive("subTotal");

   iphoneCaseTotalPricePositive("total");
   
});

//iphone - button work
var iphoneMinusButton = document.getElementById('iphoneMinusButton');
iphoneMinusButton.addEventListener('click',function(){
   // var number = document.getElementById("iphoneNumber").value;
   // var floatNumber = parseFloat(number.replace(/,/g, ''));
   // document.getElementById("iphoneNumber").value = floatNumber -1;
   iphoneNumberNegative("iphoneNumber");
   // var Price = document.getElementById("iphonePrice").innerText;
   // var floatPrice = parseFloat(Price.replace(/,/g, ''));
   // document.getElementById("iphonePrice").innerText = floatPrice - 1219 ;
   iphonePriceNegative("iphonePrice");

   iphoneSubTotalNegative("subTotal");

   iphoneTotalPriceNegative("total");
});

 //iphone case - button work
 var iphoneCaseMinusButton = document.getElementById('iphoneCaseMinusButton');
 iphoneCaseMinusButton.addEventListener('click',function(){
   
   iphoneCaseNumberNegative("iphoneCaseNumber");
   
   iphoneCasePriceNegative("iphoneCasePrice");

   iphoneCaseSubTotalPriceNegative("subTotal");

   iphoneCaseTotalPriceNegative("total");

});




//functions
//iphone number positive count function
function iphoneNumberPositive (id){
   var iphoneNumber = document.getElementById(id).value;
   var floatIphoneNumber = parseFloat(iphoneNumber.replace(/,/g, ''));
   document.getElementById(id).value = floatIphoneNumber +1;
}
//iphone positive price count function
function iphonePricePositive (id){
   var iphonePrice = document.getElementById(id).innerText;
   var floatIphonePrice = parseFloat(iphonePrice.replace(/,/g, ''));
   document.getElementById(id).innerText = floatIphonePrice + 1219 ;
}
//subtotal iphone positive price count function
function iphoneSubTotalPositive (id){
   var iphonePrice = document.getElementById(id).innerText;
   var floatIphonePrice = parseFloat(iphonePrice.replace(/,/g, ''));
   document.getElementById(id).innerText = floatIphonePrice + 1219 ;
}
//total iphone positive price count function
function iphoneTotalPositive (id){
   var iphonePrice = document.getElementById(id).innerText;
   var floatIphonePrice = parseFloat(iphonePrice.replace(/,/g, ''));
   document.getElementById(id).innerText = floatIphonePrice + 1219 ;
}

//iphone case number positive count function
function iphoneCaseNumberPositive (id){
   var iphoneNumber = document.getElementById(id).value;
   var floatIphoneNumber = parseFloat(iphoneNumber.replace(/,/g, ''));
   document.getElementById(id).value = floatIphoneNumber +1;
}
//iphone case positive price count function
function iphoneCasePricePositive (id){
   var iphonePrice = document.getElementById(id).innerText;
   var floatIphonePrice = parseFloat(iphonePrice.replace(/,/g, ''));
   document.getElementById(id).innerText = floatIphonePrice + 59 ;
}
//subtotal iphone case positive price count function
function iphoneCaseSubTotalPricePositive (id){
   var iphonePrice = document.getElementById(id).innerText;
   var floatIphonePrice = parseFloat(iphonePrice.replace(/,/g, ''));
   document.getElementById(id).innerText = floatIphonePrice + 59 ;
}
//total iphone case positive price count function
function iphoneCaseTotalPricePositive (id){
   var iphonePrice = document.getElementById(id).innerText;
   var floatIphonePrice = parseFloat(iphonePrice.replace(/,/g, ''));
   document.getElementById(id).innerText = floatIphonePrice + 59 ;
}

//iphone number negative count function
function iphoneNumberNegative (id){
   var iphoneNumber = document.getElementById(id).value;
   var floatIphoneNumber = parseFloat(iphoneNumber.replace(/,/g, ''));
   if(floatIphoneNumber<1){
      alert("Choose one item");
   }
   else{
      document.getElementById(id).value = floatIphoneNumber -1;
   }
      
   
   
   
}
//iphone negative price count function
function iphonePriceNegative (id){
   var iphonePrice = document.getElementById(id).innerText;
   var floatIphonePrice = parseFloat(iphonePrice.replace(/,/g, ''));
   if(floatIphonePrice<1219){
      document.getElementById(id).innerText = 0 ;
   }
   else{
      document.getElementById(id).innerText = floatIphonePrice - 1219 ;
   }
      
   
   
}
//subtotal iphone negative price count function
function iphoneSubTotalNegative (id){
   var iphonePrice = document.getElementById(id).innerText;
   var floatIphonePrice = parseFloat(iphonePrice.replace(/,/g, ''));
   if(floatIphonePrice<1219){
      document.getElementById(id).innerText = floatIphonePrice ;
   }
   else{
      document.getElementById(id).innerText = floatIphonePrice - 1219 ;
   }
      
   
   
}
//total iphone negative price count function
function iphoneTotalPriceNegative (id){
   var iphonePrice = document.getElementById(id).innerText;
   var floatIphonePrice = parseFloat(iphonePrice.replace(/,/g, ''));
   if(floatIphonePrice<1219){
      document.getElementById(id).innerText = floatIphonePrice ;
   }
   else{
      document.getElementById(id).innerText = floatIphonePrice - 1219 ;
   }
   
}

//iphone case number negative count function
function iphoneCaseNumberNegative (id){
   var iphoneNumber = document.getElementById(id).value;
   var floatIphoneNumber = parseFloat(iphoneNumber.replace(/,/g, ''));
   if(floatIphoneNumber<1){
      alert("Choose one item");
   }
   else{
      document.getElementById(id).value = floatIphoneNumber -1;
   }
      
   
   
}
//iphone case negative price count function
function iphoneCasePriceNegative (id){
   var iphonePrice = document.getElementById(id).innerText;
   var floatIphonePrice = parseFloat(iphonePrice.replace(/,/g, ''));
   if(floatIphonePrice<59){
      document.getElementById(id).innerText = 0 ;
   }
   else{
      document.getElementById(id).innerText = floatIphonePrice - 59 ;
   }
      
   
   
}
//subtotal iphone case negative price count function
function iphoneCaseSubTotalPriceNegative (id){
   var iphonePrice = document.getElementById(id).innerText;
   var floatIphonePrice = parseFloat(iphonePrice.replace(/,/g, ''));
   if(floatIphonePrice<59){
      document.getElementById(id).innerText = floatIphonePrice ;
   }
   else{
      document.getElementById(id).innerText = floatIphonePrice - 59 ;
   }
   
}
//total iphone case negative price count function
function iphoneCaseTotalPriceNegative (id){
   var iphonePrice = document.getElementById(id).innerText;
   var floatIphonePrice = parseFloat(iphonePrice.replace(/,/g, ''));
   if(floatIphonePrice<59){
      document.getElementById(id).innerText = floatIphonePrice;
   }
   else{
      document.getElementById(id).innerText = floatIphonePrice - 59 ;
   }
   
}