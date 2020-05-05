//Exercice 1
//Write a simple JavaScript program to join all elements of the following array into a string.
var me = ["my","favorite","color","is","blue"]
me.toString() // "my,favorite,color,is,blue"


// Exercice 2: MixUp
var a = 'mix';
var b = 'pod';
var newWord = b.slice(0, 2) + a.slice(2) + " " + a.slice(0, 2) + b.slice(2);
console.log(newWord)


// Exercice 3: Calculator
function myCalculator() {
  var x,y,z,oper;
  x=prompt("Type first number");
  y=prompt("Type second number");
  oper=prompt("Type an operator");
  
  if(oper=="+"){
    z=Number(x)+Number(y);
  }
  else if(oper=!null){
    z="Error"
  }
  else if(x=!null){
    z="Error"
  }
  else if(y=!null){
    z="Errore"
  }
  else if(oper=="/"){
    z=Number(x)/Number(y);
  }
  else if(oper=="*"){
    z=Number(x)*Number(y);
  }
  else if(oper=="-"){
    z=Number(x)-Number(y);
  }
  
  return z;
    }
alert(myCalculator())