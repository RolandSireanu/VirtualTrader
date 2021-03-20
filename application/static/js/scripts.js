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
    var temp = "valBox".concat(compId.slice(1,compId.length))
    console.log(temp)
    document.getElementById(temp).innerHTML=newVal;
}

function buy(compId){
    let id = compId.slice(1,compId.length);
    let howMany = document.getElementById("valBox".concat(id)).innerHTML
    let coin = document.getElementById("c".concat(id)).innerHTML
    let price = document.getElementById("p".concat(id)).innerHTML
    let user = document.getElementById("LoggedInAs").innerHTML

    let entry = {
        quantity: howMany,
        coin: coin,
        price: price,
        action: "buy"
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