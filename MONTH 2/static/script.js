const frases = document.querySelectorAll('.frases p');
let index = 0;

function mostrarFrases() {
    frases.forEach((f, i) => {
        f.style.display = i === index ? 'block' : 'none';
    });
    index = (index + 1) % frases.length;
}
mostrarFrases();
setInterval(mostrarFrases, 4000);
