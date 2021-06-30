package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	line, _ := reader.ReadString('\n')
	line = strings.TrimSpace(line)

	splitted := strings.Split(line, " ")
	var paulServes bool = true //Seeing as he starts the serve

	N, _ := strconv.ParseInt(splitted[0], 0, 64)
	P, _ := strconv.ParseInt(splitted[1], 0, 64)
	Q, _ := strconv.ParseInt(splitted[2], 0, 64)

	doneMatches := P + Q
	for doneMatches >= 1000*N {
		doneMatches -= 1000 * N
		paulServes = !paulServes
	}

	for doneMatches >= N {
		doneMatches -= N
		paulServes = !paulServes
	}

	//fmt.Print(N, P, Q)

	if paulServes {
		fmt.Print("paul")
	} else {
		fmt.Print("opponent")
	}

}
