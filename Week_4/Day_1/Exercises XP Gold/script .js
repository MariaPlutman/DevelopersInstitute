var i = 0;
function playTheGame() {
    let answer = confirm("Do you want play the game?");
    if (answer == true) {
        var number = parseInt(prompt("Put a number between 0 and 10: "))
        if (number == isNaN) {
            alert("Sorry Not a number, Goodbye");
        } else if (number < 0 || number > 10) {
            alert("Sorry it's not a good number,Goodbye")
        } else if (0 > number < 10) {
            var computerNumber = Math.floor(Math.random() * 11);
        }
        test(number, computerNumber);
    } else {
        alert("No problem, Goodbye")
    }
}

console.logp(layTheGame())

function test(myNumber, computerNumber) {
    if (myNumber == computerNumber) {
        alert("You won!!!");
        i = 0;
    } else if (number < 0 || number > 10) {
        alert("Sorry it's not a good number,Goodbye");
        i++;
    } else if (myNumber < computerNumber) {
        alert("It's lower. You have to guess again.");
        i++;
    }
    if (i >= 3) {
        alert(`You can't try again. The good number in my mind is ${computerNumber}`);
        i = 0;
    }
}

