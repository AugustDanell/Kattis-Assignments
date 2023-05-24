const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

N = 0
Q = 0
people_map = {}
restart_sum = "0"

rl.on('line', (line) => {
    split = line.split(" ")
    if(N == 0 && Q == 0){
        N = parseInt(split[0])
        Q = parseInt(split[1])
    }
    else{
        if(split[0] == "SET"){
            people_map[split[1]] = split[2]
        }
        else if(split[0] == "RESTART"){
            restart_sum = split[1]
            people_map = {}
        }
        else{
            if(split[1] in people_map){
                console.log(people_map[split[1]])
            }
            else{
                console.log(restart_sum)
            }
        }
        Q --
    }
});
