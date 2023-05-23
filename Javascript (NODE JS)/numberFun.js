const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

cases = 0
rl.on('line', (line) => {
    split = line.split(" ")
    if (cases == 0){
        cases = parseInt(line)
    }
    else{
        operand_one = parseInt(split[0])
        operand_two = parseInt(split[1])
        result = parseInt(split[2])
        
        addition = operand_one + operand_two          == result
        multiplication = operand_one * operand_two    == result  
      
        subtract_one = operand_one - operand_two      == result
        subtract_two = operand_two - operand_one      == result
        subtraction = subtract_one || subtract_two
        
        div_one = (operand_one / operand_two) == result
        div_two = (operand_two / operand_one) == result
        division = div_one || div_two
        
        if(addition || subtraction || multiplication || division){
            console.log("Possible")
        }
        else{
            console.log("Impossible")
        }
    }
});
