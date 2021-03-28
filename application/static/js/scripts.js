/*!
    * Start Bootstrap - SB Admin v6.0.2 (https://startbootstrap.com/template/sb-admin)
    * Copyright 2013-2020 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */
    (function($) {
    "use strict";

    // Add active state to sidbar nav links
    var path = window.location.href; // because the 'href' property of the DOM element is the absolute path
        $("#layoutSidenav_nav .sb-sidenav a.nav-link").each(function() {
            if (this.href === path) {
                $(this).addClass("active");
            }
        });

    // Toggle the side navigation
    $("#sidebarToggle").on("click", function(e) {
        e.preventDefault();
        $("body").toggleClass("sb-sidenav-toggled");
    });
})(jQuery);

function showVal(newVal, compId){

    let elementToUpdate;
    let rowNumber = compId.slice(2,compId.length);

    if(compId.slice(1,2) === "b"){
        elementToUpdate = "valBoxB".concat(rowNumber)
        let price = document.getElementById("p".concat(rowNumber));
        console.log("price = " + price);
        document.getElementById("moneySpent-"+rowNumber).innerHTML = parseFloat(parseFloat(newVal) * parseFloat(price.innerHTML)).toFixed(2); 
    }
    else
    {
        elementToUpdate = "valBoxS".concat(compId.slice(2,compId.length))
        let price = document.getElementById("p".concat(rowNumber)).innerHTML;
        
        console.log(parseFloat(newVal) * parseFloat(price));
        document.getElementById("moneyGained-"+rowNumber).innerHTML = parseFloat(parseFloat(newVal) * parseFloat(price)).toFixed(2);
    }
    
    document.getElementById(elementToUpdate).innerHTML=newVal;
}

function Transaction(compId){
    let id = compId.slice(1,compId.length);
    let act = 0;
    let howMany;
    let coin = document.getElementById("c".concat(id)).innerHTML
    let price = document.getElementById("p".concat(id)).innerHTML
    let user = document.getElementById("LoggedInAs").innerHTML
    
    console.log(compId.slice(0,1));

    if('s' === compId.slice(0,1)){
        act = "sell"
        console.log("Sell actions")
        howMany = document.getElementById("valBoxS".concat(id)).innerHTML
    }
    else
    {
        console.log("Buy actions")
        howMany = document.getElementById("valBoxB".concat(id)).innerHTML
        act = "buy"
    }

    let entry = {
        quantity: howMany,
        coin: coin,
        price: price,
        action: act
    };

    fetch(`${window.origin}/api`,{
        method: "POST",
        credentials: "include",
        body: JSON.stringify(entry),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    }).then(function(resp){
        if(resp.status !== 200){
            console.log("Return status is not OK ! ");
            return;
        }

        resp.json().then(function (data){
            console.log(data);
        });

        location.reload();
    })
}