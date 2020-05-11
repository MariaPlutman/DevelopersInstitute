// Exercise 1
function checkDriverAge() {
    let age = parseInt(prompt("What is your age?"));

    if (age == 18) {
        alert("Congratulations on your first year of driving. Enjoy the ride!");
    }
    else if (age < 18) {
        alert("Sorry, you are too young to drive this car. Powering off")
    }
    else if (age > 18) {
        alert("Powering On. Enjoy the ride!")
    }
}


// Exercise 2
amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}

function checkBasket() {
    let item = prompt("What item to you want?");
    if (item in amazonBasket) {
        return `${item} is in the basket`
    } else {
        return `Sorry, it's not there`
    }
}
