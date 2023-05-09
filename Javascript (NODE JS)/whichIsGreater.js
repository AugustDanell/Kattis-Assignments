const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
  let split = line.split(" ");
  let a = parseInt(split[0]);
  let b = parseInt(split[1]);
  
  if(a > b){
    console.log(1);
  }
  else{
    console.log(0);
  }
});
