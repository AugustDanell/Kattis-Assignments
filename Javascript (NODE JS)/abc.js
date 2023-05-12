const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

numbers = []
rl.on('line', (line) => {
    if (numbers.length == 0){
        split = line.split(" ")
        for(i = 0; i < split.length; i++){
            numbers.push(parseInt(split[i]))
        }
        numbers = numbers.sort(function(a,b){return a-b;})
        //console.log(numbers)
    }
    else{
        out_list = []
        for(i = 0; i < line.length; i++){
            out_list.push(line.charCodeAt(i) - 65)
        }
        console.log(numbers[out_list[0]], numbers[out_list[1]], numbers[out_list[2]])
    }
});
