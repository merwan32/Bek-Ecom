var updatbtns = document.getElementsByClassName('addbtn')

for(var i=0;i<updatbtns.length ; i++){
    updatbtns[i].addEventListener('click',function(){
        var productid = this.dataset.productid;
        var action = this.dataset.action;
        console.log('user : ',user);
        if (user == 'AnonymousUser') {
            console.log('not')
        } else {
            UpdateUserOrder(productid,action);
        }
    })
}

function UpdateUserOrder(productid,action) {
    console.log('user is login, sending data..');
    var  url ='/update_item/';

    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body: JSON.stringify({'productid':productid,'action':action})
    })

    .then((response)=>{
        return response.json()
    })

    .then((data)=>{
        console.log('data', data)
        location.reload()
    })
}