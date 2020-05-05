// Exercise 1
let addressNumber = 9
let addressStreet = "Efal"
let country = "Israel"
let global_address = "I live in " + addressStreet + " " + addressNumber + ", in " + country
console.log(global_address)

// Exercise 2
let bd_year = 1995
let future_year = 2022
let age = future_year - bd_year
console.log("I will be " + age + ' in ' + future_year)
alert(`I will be ${future_year - bd_year} in ${future_year}`)

// Exercise 3
let pets = ['cat', 'dog', 'fish', 'rabbit', 'cow']
pets.splice(3, 1, 'horse')
console.log(pets[1], pets.length, pets)
