//Exercise 1
let person = {
	username: "mariap"
	password: "heyyou45"
}

var database = [person]

//Exercise 2
function isEven() {
	for (let i = 0; i < 16; i++) {
		if (i % 2 == 0){
    		alert(i + " is even");
		}else{
			alert(i + " is odd");
		}
	}	
}

//Exercise 3
var names = ["john", "sarah", 23, "Rudolf",34];
var newNames = []
function isName(){
	for (let i of names){
		if (i != Number(i)){
			newNames.push(i)
		}else{
			continue;
		}
	}
	alert(newNames)
}