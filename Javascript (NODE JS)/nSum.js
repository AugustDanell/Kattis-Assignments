// Repeating easy exercies for JS, this one here: https://open.kattis.com/problems/nsum

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

size = 0;
stack = [];

rl.on('line', (line) => {
  if(size == 0){
    size = parseInt(line);
  }
  else{
    split = line.split(" ");
    for(i = 0; i < size; i++){
      stack.push(split[i]);
    }
  }
  
  if(stack.length == size){
    s = 0;
    for(i = 0; i < size; i++){
      s += parseInt(stack[i]);
    }
    console.log(s);
  }
});
