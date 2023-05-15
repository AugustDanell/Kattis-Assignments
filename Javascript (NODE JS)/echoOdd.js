const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

echo = false
rl.on('line', (line) => {
  if(echo){
      console.log(line)
  }
  echo = !echo
});
