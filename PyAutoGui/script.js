const img = document.getElementById("imagem")
img.addEventListener('click', () => {
    if (img.requestFullscreen) {
        img.requestFullscreen();
    }
});