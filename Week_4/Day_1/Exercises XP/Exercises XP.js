// Exercise 1
function checkDriverAge(age) {
    //let age = parseInt(prompt("What is your age?"));

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

// Exercise 3
let shoppingList = ['banana', 'orange', 'apple'];

var stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry": 1
}

var prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry": 10
}

function myBill() {
    let total_price = 0;
    for (x of shoppingList) {
        if (stock[x] > 0) {
            stock[x] = stock[x] - 1;
            total_price += prices[x];
        }
    }
    console.log(total_price);
}
myBill();

// Exercise 4
function hotel_cost(nights) {
    return nights * 140 + "$"
}

function plane_ride_cost(city) {
    if (city == "London") {
        return city + ":183$"
    } else if (city == "Paris") {
        return city + ":220$"
    } else {
        return city + ":300$"
    }
}

function rental_car_cost(days) {
    return days * 40 + "$"
}
