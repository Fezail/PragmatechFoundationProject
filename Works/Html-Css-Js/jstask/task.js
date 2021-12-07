// TASK-1: 2 ededi tipində məlumatı parametr olaraq qəbul edib ededlərin hasilini return edən funksiya yazın
function hasil(x, y) {
    return (x * y)
}
hasiller = hasil(4, 9)
document.write(hasiller)


// TASK-2: 1 eded parametr qəbul edib daxil edilən dəyərin 1 artığını return elətdirən funksiya yazın
let a = 10
function artim(a){
    return a++
}
document.write(a)


// TASK-5: Daxil edilən 5 parametri array formasında return edən funksiya yazın
function meyve() {
    let meyve = ["alma", "armud", "nar", "heyva", "gilas", "tut"]
    meyve = [0, 1, 2, 3, 4, 5]
    console.log(meyve)
    return
}
meyve()


// TASK-8: str daxilində neçə hərf olduğunu ekrana yazdırın
let txt = "Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır";
console.log(txt.length)


// TASK-9: str daxilindəki sözləri ayrı bir massiv içərisində toplayın
netice = txt.split(" ")
console.log(netice)


// TASK-12: str ni vergülə görə ayırıb iki string halına gətirin
netice = txt.split(",")
console.log(netice)