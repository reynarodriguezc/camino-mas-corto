let numeroSecreto = Math.floor(Math.random() * 10) + 1;
let intentos = 0;

function adivinaElNumero() {
    let adivinanza = parseInt(document.getElementById('adivinanza').value);
    let mensaje = document.getElementById('mensaje');
    let intentosDisplay = document.getElementById('intentos');

    intentos++;

    if (adivinanza < numeroSecreto) {
        mensaje.textContent = "Demasiado bajo. Intenta nuevamente.";
    } else if (adivinanza > numeroSecreto) {
        mensaje.textContent = "Demasiado alto. Intenta nuevamente.";
    } else {
        mensaje.textContent = `¡Felicidades! Adivinaste el número en ${intentos} intentos.`;
    }

    intentosDisplay.textContent = `Intentos: ${intentos}`;
}