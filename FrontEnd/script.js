window.onload = function() {
    if (document.getElementById("statusColor").textContent === "APROVADO") {
        document.getElementById("statusColor").style.color = "#40FF40";
    } else {
        document.getElementById("statusColor").style.color = "#ff4040";
    }       
}
  
var answer = document.getElementById("answer");