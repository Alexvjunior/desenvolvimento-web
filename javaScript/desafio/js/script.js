function carregar() {
    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()
    var minutos = data.getMinutes()
    msg.innerHTML = `Agora são ${hora}:${minutos}`
    if (hora >= 0 && hora < 12) {
        img.src = 'fotos/manha.jpg'
        document.body.style.background = '#ffb46a'
    } else if (hora < 18) {
        img.src = 'fotos/tarde.jpg'
        document.body.style.background = '#5aae8c'
    } else {
        img.src = 'fotos/noite.jpg'
        document.body.style.background = '#00639c'
    }
}