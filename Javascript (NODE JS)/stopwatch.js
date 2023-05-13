const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

stops = 0
start_stops = 0
time_table = []
rl.on('line', (line) => {
    if(stops == 0){
        stops = parseInt(line)
        start_stops = stops
    }
    else{
        time_table.push(parseInt(line))
        stops --
    }
    
    if(stops == 0){
        if(start_stops == 0){
            console.log(0)
        }
        else if(time_table.length % 2 == 1){
            console.log("still running")
        }
        else{
            seconds = 0
            for(i = 1; i < time_table.length; i+=2){
                previous = time_table[i-1]
                current = time_table[i]
                seconds += current-previous
            }
            console.log(seconds)
        }
    }
});
