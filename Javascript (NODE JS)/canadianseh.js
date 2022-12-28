const readline = require('readline');
let canadian = false;

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
  const strLength = line.length;
  var lastLetter = line.charAt(line.length - 1);
  var secondLastLetter = line.charAt(line.length - 2);
  var thirdLastLetter = line.charAt(line.length - 3);
  
  if(lastLetter === "?" && secondLastLetter === "h" && thirdLastLetter === "e"){
    canadian = true;
  }

  if(canadian){
    console.log("Canadian!");
  }
  else{
    console.log("Imposter!");
  }
});
