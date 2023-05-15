const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

echo = true
rl.on('line', (line) => {
  stones = parseInt(line)
  if(stones % 2 == 1){
      console.log("Alice")
  }
  else{
      console.log("Bob")
  }
});
