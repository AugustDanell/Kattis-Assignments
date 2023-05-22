const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


rl.on('line', (line) => {
   split = line.split(" ")
   a = parseInt(split[0])
   b = parseInt(split[1])
   c = parseInt(split[2])
   
   if(a == 1 || (b == 2 && c == 2) || c == 1){
       console.log("What an excellent example!")
   }
   else{
       console.log("Oh look, a squirrel!")
   }
});
