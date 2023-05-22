// Javascript solution to the assignment: https://open.kattis.com/problems/backspace
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


rl.on('line', (line) => {
   stack = []
   for(i = 0; i < line.length; i++){
       if(line[i] == "<"){
           if(stack.length > 0){
               stack.pop()
           }
       }
       else{
           stack.push(line[i])
       }
   }
   console.log(stack.join(""));
});
