function writeInNDecimals(N, decimals){
    N*= Math.pow(10, decimals)
    N = Math.round(N)
    N /= Math.pow(10, decimals)
    return N.toFixed(3)
}

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

testcases = 0
rl.on('line', (line) => {
    if(testcases == 0){
        testcases = parseInt(line)
    }
    else{
        split = line.split(" ")
        len = parseInt(split[0])
        l = []
        total = 0
        for(i = 1; i <= len; i++){
            score = parseInt(split[i])
            l.push(score)
            total += score
        }
        avg = total/len
        over_avg = 0
        for(i = 0; i < l.length; i++){
            if(l[i] > avg){
                over_avg ++
            }
        }
        percent = 100*(over_avg / l.length)
        //console.log(percent)
        console.log(writeInNDecimals(percent, 3) + "%")
        testcases --
        
    }
});
