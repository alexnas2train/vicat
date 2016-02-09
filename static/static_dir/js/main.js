function check(){
    var foo = document.getElementById("gallery");
    // var switcher = document.getElementById("switcher").childNodes[0];
    var switcher = document.getElementById("switcher");
    if(foo.className === "hidden"){
        foo.className = "";
        switcher.className = "opened";
        switcher.innerHTML = '<img src="/static/img/list_opened.png">';
    }
    else{
        foo.className = "hidden";
        switcher.className = "closed";
        switcher.innerHTML = '<img src="/static/img/list_closed.png">';
    }
}
function initElement(){
    var switcher = document.getElementById("switcher");
    var switch_from_button = document.getElementById("episodes");
    switcher.onclick = check;
    switch_from_button.onclick = check;
}