//Exercise 1
let person = {
	username: "mariap",
	password: "heyyou45"
};

let database = [person];

let newsfeed = [ 
	{
		username: "mariap",
		timeline: "heyyou45"
	},
	{
		username: "mariap",
		timeline: "heyyou45"
	},
	{
		username: "mariap",
		timeline: "heyyou45"
	}
];

//Exercise 2
for (let i = 0; i < 16; i++) {
	if (i % 2 == 0){
    	alert(i + " is even");
	}else{
		alert(i + " is odd");
	}
}	


//Exercise 3
let names = ["john", "sarah", 23, "Rudolf", 34];
let newNames = []
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

for (let i of names){
	if (i != Number(i) && i[0].isUpper){
		continue;
	}
}
i[0] === i[0].toUpperCase()