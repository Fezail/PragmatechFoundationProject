let x=0;

let box=document.querySelector('.slide-items');

function left(){
    x-=1220;
    box.style.left=`${x}px`;
}

function right(){
    x+=1220;
    box.style.left=`${x}px`;
}