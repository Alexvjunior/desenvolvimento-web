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

function verificar() {
    var date = new Date()
    var ano = date.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.getElementById('result')
    if (fano.value.length == 0 || fano.value > ano) {
        window.alert("Verifique os dados e tente novamente!")
    } else {
        var sexo = document.getElementsByName('radsex')
        var idade = ano - fano.value
        var genero = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')

        if (sexo[0].checked) {
            genero = 'Homem'
            if (idade < 10) {
                img.setAttribute('src', 'fotos/bebe-masculino.jpg')
            } else if (idade < 21) {
                img.setAttribute('src', 'fotos/homem-jovem.jpg')
            } else if (idade < 50) {
                img.setAttribute('src', 'fotos/homem-adulto.jpg')
            } else {
                img.setAttribute('src', 'fotos/homem-velho.jpg')
            }
        } else {
            genero = 'Mulher'
            if (idade < 10) {
                img.setAttribute('src', 'fotos/bebe-feminino.jpg')
            } else if (idade < 21) {
                img.setAttribute('src', 'fotos/mulher-jovem.jpg')
            } else if (idade < 50) {
                img.setAttribute('src', 'fotos/mulher-adulto.jpg')
            } else {
                img.setAttribute('src', 'fotos/mulher-velha.jpg')
            }
        }
        res.innerHTML = `Detectamos ${genero} com ${idade} anos \n`
        res.appendChild(img)
    }
}

function tabuada(){
    let num = document.getElementById('txtn')
    let tab = document.getElementById('seltab')
    if (num.value.length == 0){
        window.alert('Por favor digite um número')
    }else{
        let n = Number(num.value)
        let c = 1
        while (c <= 10){
            let item = document.createElement('option')
            item.text = `${n} X ${c} = ${n*c}`
            tab.appendChild(item)
            c++
        }
    }

}