// Exercise 1
function isEven() {
	var x;
	x = prompt("Give me some number:");

	if (Number(x) % 2 == 0){
		alert(x + " is an even number")
	}else{
		alert(x + " is not an even number")
	}
}

// Exercise 2
var x, y;

function isBigger(x, y) {
	if (x > y){
		console.log(x + " is bigger than " + y)
	}else{
		console.log(y + " is bigger than " + x)
	}
}

// Exercise 3
var language;
language = prompt("Which language you speak?")

switch(language) {
  case 'French':
    alert("Bonjour");
    break;
  case 'English':
    alert("Hello");
    break;
   case 'Hebrew':
    alert("Shalom");
    break;
  default:
    alert(";)")
}

// Exercise 4
function gradeAssigner(){
	var score;
	score = prompt("What is your grade?")

	if (Number(score) >= 90){
		console.log('A')
	}else if (Number(score) >= 80){
		console.log('B')
	}else if (Number(score) >= 70){
		console.log('C')
	}else {
		console.log('D')
	}
}