// Repeating Javascript, a solution to the problem: https://open.kattis.com/problems/different

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


rl.on('line', (line) => {
   split = line.split(" ")
   a = parseInt(split[0])
   b = parseInt(split[1])
   
   if (a >= b){
       console.log(a-b)
   }
   else{
       console.log(b-a)
   }
});
