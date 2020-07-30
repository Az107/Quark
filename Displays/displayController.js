var pid = null
function initSocket(){
    var socket = new WebSocket("ws://localhost:8" + port);
}


socket.onerror = function(){
    alert("socket error")
    socket = new WebSocket("ws://localhost:8" + pid);

} 

socket.onmessage = function(msgevent){
    try {
        eval(msgevent.data)
    } catch (Exception) {
        console.log("error " + msgevent.data)
    }

} 
socket.onopen = function(){

    if (pid != null){
        fun("auth." + pid);
    }
} 
function fun(name){
    if (socket == null){
        alert("connecting")
        socket = new WebSocket("ws://localhost:8" + port);
    }
    alert(name);
    socket.send(name);

    
}   

function load(){

    var all = document.getElementsByTagName("*")
    for (var i=0, max=all.length; i < max; i++) {
        element = all[i];
        
        if (element.nodeName == "BUTTON"){

            if (element.id != ""  && element.id != null){
                element.onclick = function(){
                   
                    fun("click." + this.id);
                } 
            } 
        }else if (element.nodeName == "INPUT"){
            if (element.id != ""  && element.id != null){
                element.onchange = function(){
                    fun("change." + this.id + ":" + this.value)
                } 
            } 
        } 
   }

} 

function b1OnClick(){
    text = document.getElementById("entrada").value
    try{
        socket.send(text);
    }catch (Err){
        socket = new WebSocket("ws://localhost:8765");
        socket.send(text);
    }
}