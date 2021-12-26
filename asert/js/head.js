var lastScrollTop = 0;
            head = document.getElementById("header");
        window.addEventListener("scroll", function(){

            var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            if (scrollTop > lastScrollTop){
                head.style.top="-10rem";
            }else{
                head.style.top="0";
            }

            lastScrollTop = scrollTop;
    })


var MenuItems = document.getElementById("Items");
MenuItems.style.maxHeight = ("0px")
function menutoggle(){
    if (Items.style.maxHeight == "0px"){
        Items.style.maxHeight = "100%"
    }
    else
    {
        Items.style.maxHeight = "0px"
    }
}