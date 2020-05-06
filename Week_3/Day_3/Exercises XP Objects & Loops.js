// Exercise 1
let colors = ["blue", "yellow", "red", "green", "pink"];
let end = ''

for (let i = 0; i < colors.length; i++) {
	console.log("My #" + (i + 1) + " choice is " + colors[i]);
}

for (let i = 0; i < colors.length; i++) {
	if (i == 0) {
		end = 'st';
	} else if (i == 1) {
		end = 'nd';
	} else if (i == 2) {
		end = 'rd';
	} else {
		end = 'th'
	}
	console.log("My " + (i + 1) + end + " choice is " + colors[i]);
}

// Exercise 3
var people = ["Greg", "Mary", "Devon", "James"];

for (let i of people) {
	console.log(i);
}

people.shift() // remove “Greg” from the array
people[2] = "Jason" // replace “James” by “Jason”
people.push("Maria") // add my name to the end 
// ["Mary", "Devon", "Jason", "Maria"]

for (i of people) {
	console.log(i);
	if (i == 'Mary') {
		break;
	}
}

people.slice(1, 3) // ["Devon", "Jason"]
people.indexOf('Mary') // 0
people.indexOf('Foo') // -1
people[people.length - 1] //Maria

// Exercise 4
var age = [20, 5, 12, 43, 98, 55];
let even = []
function myFunc(total, num) {
	return total + num;
}
age.reduce(myFunc, 0); // 233

var age = [20, 5, 12, 43, 98, 55];
let even = []
for (i of age) {
	if (i % 2 == 0) {
		even.push(i)
	} else {
		continue;
	}
}
console.log(even)

var age = [20, 5, 12, 43, 98, 55];
Math.max(...age)

