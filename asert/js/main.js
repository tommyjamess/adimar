

$(document).ready(function(){

    $("li").click( function(){

        $("li").removeClass("active")
        $("li").removeClass("secondary-active")
        $(this).addClass("active")
        $(this).prevAll().addClass("secondary-active")
    });

    $("#log").click(function(){

        $(".log").slideToggle("fast")
    });

    $(document).ready(function(){

        $("a").click(function(){
        
            $(this).addClass("active")
    
            $(this).click(function(){
    
                $("a").removeClass("active")
            });
    
        })
    })

    $("#acc").click(function(){

        $(".acc").slideToggle("fast")
    });

    $("#revButton").click(function(event){

        event.preventDefault()

        $(".see-reviews").slideToggle("fast")
        $(".add-com").slideToggle("fast")
        
    });

    $("#detButton").click(function(event){

        event.preventDefault()

        $(".see-detail").slideToggle("fast")
    });

    $(".filter").click(function(event){

        event.preventDefault()

        $(".sidebar").slideToggle("fast")

        $(this).css("transform: translateX(-30rem)")
            
    });

    $(".sub-button, button").click(function(){
        $(this).addClass("active", "3000");
      
    })
});