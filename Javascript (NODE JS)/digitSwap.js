const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
  let rev = []
  for(let i = line.length -1; i >= 0; i--){
    rev.push(line[i]);
  }
  console.log(rev.join(""));
  
});
