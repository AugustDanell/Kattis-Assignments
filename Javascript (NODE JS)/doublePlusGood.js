function doublePlusGood(expr){
    let uniqueResults = new Map()
    let operands = expr.split("+")
    
    // 1. Iterate over every possible bit string for x operations, ex, 3 operations -> (000 - 111):
    for(let i = 0; i < Math.pow(2, operands.length-1); i++){
        
        // 2. Initiate the bit string:
        let bin_str = i.toString(2)

        // 3. Add padding to the bit string:
        while(bin_str.length < operands.length-1){
            bin_str = "0" + bin_str
        }

        // 4. Calculate a local result:
        numbers = [operands[0]]
        for(let j = 0; j < operands.length-1; j++){
            if(bin_str.charAt(j) == "0"){
                numbers.push(operands[j+1])
            }
            else{
                numbers[numbers.length-1] += operands[j+1]
            }
        }

        // 5. Sum it up:
        let sum = numbers.reduce((x, y) => { return parseInt(x) + parseInt(y) }, 0)
        
        // 6. Add not visited results to the global map:
        if(!uniqueResults.has(sum)){
            uniqueResults.set(sum, true)
        }
    }

    return (uniqueResults.size)
}

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (line) => {
    console.log(doublePlusGood(line))
});
