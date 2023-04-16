window.onload = function() {
    if (document.getElementById("statusColor").textContent === "APROVADO") {
        document.getElementById("statusColor").style.color = "#40FF40";
    } else if (document.getElementById("statusColor").textContent === "REPROVADO") {
        document.getElementById("statusColor").style.color = "#ff4040";
    } else {
        document.getElementById("statusColor").style.color = "#4040ff";
    }       
}
  
