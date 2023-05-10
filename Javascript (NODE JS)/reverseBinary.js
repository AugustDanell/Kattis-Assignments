const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    var bin_str = parseInt(line).toString(2);
    var rev_str = ""
    for(var i = bin_str.length-1; i>=0; i--){
        rev_str += bin_str[i]
    }
    console.log(parseInt(rev_str, 2))
});
