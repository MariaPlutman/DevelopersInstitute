function hello_mood(name, mood) {
    console.log(`Hello ${name}, you are ${mood} today`)
}
hello_mood("Dan", "happy")

// Exercise 1
function age(my_age) {
    let mom_age = my_age * 2;
    let dad_age = mom_age * 1.2;
    console.log(`My mom is ${mom_age} years old and my dad is ${dad_age.toFixed(0)} years old.`)
}
age(24)


// Exercise 2
function age2(myAge) {
    return myAge * 2;
}
let momAge = age2(24)
console.log(`My mom is ${momAge} years old`)


















function playTheGame() {
    function confirm() {
        let answer = prompt("Do you want play the game? yes/no")
        if (answer == "yes") {
            let num = parseInt(prompt("Put a number between 0 and 10: "))
            if (0 > num > 10) {
                alert("Sorry it's not a good number,Goodbye")
            } else {
                let computerNumber = (Math.random() * 10)
            }
        } else if (answer == "no") {
            prompt("No problem, Goodbye")
        }
    }
}

playTheGame()