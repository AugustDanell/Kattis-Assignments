const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
  word = [line[0]];
  for(i = 1; i < line.length; i++){
    if(line[i] != line[i-1]){
      word.push(line[i]);
    }
  }
  console.log(word.join(""));
});
