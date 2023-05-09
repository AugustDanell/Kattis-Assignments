// Repeating Javascript, a solution to the problem: https://open.kattis.com/problems/ofugsnuid

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

size = 0;
stack = [];

rl.on('line', (line) => {
  num = parseInt(line);
  if(size == 0){
    size = num;
  }
  else{
    stack.push(num);
  }
  
  if(stack.length == size){
    for(i = stack.length-1; i >= 0; i--){
      console.log(stack[i]);
    }
  }
});
