let x = 0


function plus() {
    x++
    document.getElementById("counter").innerHTML = x
}

function reset() {
    x = 0
    document.getElementById("counter").innerHTML = x
}

function minus() {
    x--
    document.getElementById("counter").innerHTML = x
}