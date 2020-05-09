//Exercise 1
num1 = parseInt(prompt("Give me first number:"))
num2 = parseInt(prompt("Give me second number:"))

if ((num1 + num2) < 100) {
    console.log(true)
} else {
    console.log(false)
}

//Exercise 2
console.log(x % y);


//Exercise 3
function dividesEvenly(a, b) {
    if (a % b == 0) {
        return true;
    } else {
        return false;
    }
}
dividesEvenly(98, 7)


//Exercise 4
let arr = [1, 6, 8, 44, 87]
num = parseInt(prompt("Give me some number:"))
if (arr.includes(num)) {
    console.log("True")
} else {
    console.log("False")
}



