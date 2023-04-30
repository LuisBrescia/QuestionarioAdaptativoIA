// ? Caso seja aprovado, o texto será verde, caso contrário, será vermelho.
window.onload = function() {
    if (document.getElementById("statusColor").textContent === "APROVADO") {
        document.getElementById("statusColor").style.color = "#40FF40";
    } else if (document.getElementById("statusColor").textContent === "REPROVADO") {
        document.getElementById("statusColor").style.color = "#ff4040";
    } else {
        document.getElementById("statusColor").style.color = "#4040ff";
    }       
}

// var respostas = [];
 
// if (request.method == 'POST') {
//     var respostaAluno = request.form['respostaAluno'];
//     respostas.push(respostaAluno);
//     localStorage.setItem('respostas', JSON.stringify(respostas));
// } else {
//     var respostaAluno = '';
// }

// window.onload = function() {
//     if (localStorage.getItem('respostas')) {
//         respostas = JSON.parse(localStorage.getItem('respostas'));
//         var ultimaResposta = respostas[respostas.length - 1];
//         document.getElementById('respostaAluno').value = ultimaResposta;
//     }
// }

