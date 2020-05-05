var array = ["Banana", "Apples", "Oranges", "Blueberries"];
array.shift() // Remove the Banana from the array.
array.sort() // Sort the array in order.
array.push("Kiwi") // Put “Kiwi” at the end of the array.
array.splice(0,1) // Remove “Apples” from the array.
array.reverse() // Sort the array in reverse order. 
console.log(array) // [“Kiwi”, “Oranges”, “Blueberries”]


var array2 = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
array2[1][1][0] // access “Oranges”.