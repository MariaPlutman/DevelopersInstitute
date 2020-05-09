// Ask the user for several words and save them.Check if the words given are strings
let word = prompt("Give me several words:");
function isString() {
    if (typeof wordPrompt === 'string' || word instanceof String) {
        console.log(`${word} is a string`)
    } else { `${word} is NOT a string` }
}

function countLetters() {
    for (let i = 0; i < 3; i++) {
        let word = [];
        let input = prompt("Give me several words:");
        word.push(input)
        let tempArr = word[i].split('');
        let letters = []
        let count = 1;
        for (let i = 0; i < tempArr.length; i++) {
            if (tempArr[i] === tempArr[i + 1]) {
                count++;
            } else {
                let value = `${count}`
                letters = [...letters, value];
                count = 1
            }
        }
        return letters
    }

}

console.log(countLetters())



