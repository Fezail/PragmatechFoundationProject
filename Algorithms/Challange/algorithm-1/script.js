let ChangeBox = function (Letters) {
    let NewLetters = "";
    for (let i = 0; i < Letters.length; i++) {
        if (Letters[i] === Letters[i].toLowerCase()) {
            NewLetters += Letters[i].toUpperCase();
        } else {
            NewLetters += Letters[i].toLowerCase();
        }
    }
    console.log(NewLetters);
    return NewLetters;
}

let text = "UP , down";

let swappedText = ChangeBox(text);