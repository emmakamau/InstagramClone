$(document).ready(function(){
    $("img.portfolio-img").tooltip()

    $("span#change-photo").click(function(){
        $("div#change-photo-form").toggle()
    })
});

