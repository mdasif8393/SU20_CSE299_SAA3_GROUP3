var update_btns = document.getElementsByClassName('update-cart');

for(var i =0; i < update_btns.length; i++){
    update_btns[i].addEventListener('click', function(){
        var product_id = this.dataset.product
        var action = this.dataset.action

       
            update_user_order(product_id, action)
        
    })
}

function update_user_order(product_id, action){
    var url = '/update_item/';

    fetch(url,{
        method: POST,
        headers:{
            'Content-Type' : 'application/json',
            'X-CSRFTOKEN'  :  csrftoken,
        },
        body:JSON.stringify({ 'product_id': product_id, 'action': action })
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data:', data)
        location.reload()
    })

}