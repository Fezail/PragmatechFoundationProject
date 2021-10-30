let x = 10
function showBoxLeft(){
    document.querySelector(".box").style.transform=`translate(${x}px, 0px)`
    x += 15
}

function showBoxRight(){
    document.querySelector(".box").style.transform=`translate(${x}px, 0px)`
    x += -15
}

function showBoxUp(){
    document.querySelector(".box").style.transform=`translate(0px, ${x}px)`
    x += -15
}

function showBoxDown(){
    document.querySelector(".box").style.transform=`translate(0px, ${x}px)`
    x += 15
}