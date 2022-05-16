// JavaScript   
var sourceWord = {{ data|safe }};
var translateTo = ["sample"];
var total = sourceWord.length-1
var count = 0;
var touchWordToChange = 1;

// Display first sourceWord' value when webpage loads:
window.onload = function() {
   document.getElementById('value').innerHTML = sourceWord[0]; 
}

// function to translate word to english if the button is pressed and then back to source if the word is pressed again
// console.log("Before function translateWord is called", touchWordToChange);
function translateWord(){
   console.log("translateWord() function called", touchWordToChange)
   // sourceWord
   if (touchWordToChange < 1){
      document.getElementById('value').innerHTML = sourceWord[count];
      touchWordToChange = 1
      // console.log("End of if statement - touchWordToChange value:", touchWordToChange)
   }
   else {
      // translateTo
      document.getElementById('value').innerHTML = translateTo[count];
      touchWordToChange = 0
      // console.log("End of else statement - touchWordToChange value:", touchWordToChange)
   }
}
// The Prev and Next functions function as a carousel from the initial value of the sourceWord to the last value of sourceWord
// prev function
function Prev(){
   touchWordToChange = 1;
   // console.log("Prev function - touchWordToChange value:", touchWordToChange)
   count--
   if (count < 0 ) {
      count++
   }
   else {
      document.getElementById('value').innerHTML = sourceWord[count];
   }
   // console.log("Prev function - count value after the if and else statement:",count);
}
      
//var count = 0;
// next function
function Next(){
   touchWordToChange = 1;
   // console.log("Next function - touchWordToChange value:", touchWordToChange)
   count++
   if (count > total) {
      count = total;
   } 
   else {
      document.getElementById('value').innerHTML = sourceWord[count];
   }
   // console.log("Next function - count value after the if and else statement:",count);
}



