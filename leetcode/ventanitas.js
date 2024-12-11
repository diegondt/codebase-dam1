const esquina1 = "╔" 
const esquina2 = "╗" 
const esquina3 = "╚" 
const esquina4 = "╝" 
const vertical = "║" 
const horizontal = "═"

//superior

let top = esquina1

for(let i = 0; i < 10; i++){
    top += horizontal
}

top += esquina2

//medio

let middle = vertical

for(let i = 0; i < 10; i++){
    middle += " "
}

middle += vertical

//inferior

let bottom = esquina3

for(let i = 0; i < 10; i++){
    bottom += horizontal
}

bottom += esquina4


// imprimir la ventana

console.log(top)

for(let i = 0; i < 10; i++){
    console.log(middle)
}

console.log(bottom)