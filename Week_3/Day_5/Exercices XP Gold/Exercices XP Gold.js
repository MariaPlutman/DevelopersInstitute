//Exercise 1
var x = 0;
var y = -1;
var z = 4;
if (x > y && x > z) {
    if (y > z) {
        console.log(x + ", " + y + ", " + z);
    }
    else {
        console.log(x + ", " + z + ", " + y);
    }
}
else if (y > x && y > z) {
    if (x > z) {
        console.log(y + ", " + x + ", " + z);
    }
    else {
        console.log(y + ", " + z + ", " + x);
    }
}
else if (z > x && z > y) {
    if (x > y) {
        console.log(z + ", " + x + ", " + y);
    }
    else {
        console.log(z + ", " + y + ", " + x);
    }
}

//Exercise 2
var x = 3;
var y = -7;
var z = 2;
if (x > 0 && y > 0 && z > 0) {
    alert("The sign is +");
}
else if (x < 0 && y < 0 && z < 0) {
    console.log("The sign is +");
}
else if (x > 0 && y < 0 && z < 0) {
    console.log("The sign is +");
}
else if (x < 0 && y > 0 && z < 0) {
    console.log("The sign is +");
}
else {
    console.log("The sign is -");
}

//Exercise 3
let grades = {
    david: 80,
    vinoth: 77,
    divya: 88,
    ishitha: 95,
    thomas: 68,
    lea: 77
}

//Write a program to check which student has the best grade. Console.log the name of the student.
var largest = 0;
for (let i in grades) {
    if (grades[i] > largest) {
        largest = grades[i];
    }
}

const getKeyByValue = (obj, value) =>
    console.log(Object.keys(obj).find(key => obj[key] === value));
getKeyByValue(grades, largest);


//Exercise 4
let i = 0;
while (i < 10) {
    if (i === 7) {
        console.log("seven")
    }
}
