//Exercise 1
let family = {
    mom: "Vika",
    grandfather: "Eduard",
    grandmother: "Valentina"
};

console.log(Object.keys(family)) //Display only the properties
console.log(Object.values(family)) //Display only the values

//Exercise 2
var building = {
    number_levels: 4,
    number_of_apt_by_level: {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    name_of_tenants: ["Sarah", "Dan", "David"],
    number_of_rooms_and_rent: {
        "Sarah": [3, 2000],
        "Dan": [4, 1000],
        "David": [1, 10],
    },
}

console.log("The number of levels in the building: ", building.number_levels)
console.log(building.number_of_apt_by_level[1] + building.number_of_apt_by_level[3]) //Display how many apartments are on level 1 and 3. Do the sum of these apartments
console.log("The name of the second tenant: ", building.name_of_tenants[1], ", number of rooms he has in his apartment: ", building.number_of_rooms_and_rent["Dan"][0])

sum = building.number_of_rooms_and_rent["Sarah"][1] + building.number_of_rooms_and_rent["David"][1]
if (sum > building.number_of_rooms_and_rent["Dan"][1]) {
    console.log("Dear owner, you have to inscrease the rent of Dan ");
    building.number_of_rooms_and_rent["Dan"][1] = 1500
}
console.log(building.number_of_rooms_and_rent["Dan"][1])

//Exercise 3
let person1 = {
    fullName: "Dannis",
    mass: 70,
    height: 175,
    bmi: function () {
        BMI = this.mass / Math.pow((this.height / 100), 2);
        console.log(BMI.toFixed(0))
    }
};


let person2 = {
    fullName: "Max",
    mass: 89,
    height: 190,
    bmi: function () {
        BMI = this.mass / Math.pow((this.height / 100), 2);
        console.log(BMI.toFixed(0))
    }
};


if (person1.bmi > person2.bmi) {
    console.log(person1.fullName, " has the biigest BMI")
} else {
    console.log(person2.fullName, " has the biigest BMI")
}
