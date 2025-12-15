package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"

	"github.com/corned/advent-of-code/common"
)

var example_data string = `L68
L30
R48
L5
R60
L55
L1
L99
R14
L82`

func part1(moves []int) {
	dial := 50
	counter := 0
	for _, value := range moves {
		dial = (dial + value) % 100
		if dial < 0 {
			dial = 100 + dial
		}

		if dial == 0 {
			counter++
		}
	}

	fmt.Println(counter)
}

func part2(data []int) {

}

func main() {
	filename := "./day01-input.txt"
	var data []string

	if len(os.Args) > 1 && os.Args[1] == "--debug" {
		data = strings.Split(example_data, "\n")
	} else {
		data = common.ReadAndProcessFile(filename)
	}

	moves := make([]int, len(data))
	for i, move := range data {
		steps, _ := strconv.Atoi(move[1:])
		if move[0] == 'L' {
			moves[i] = -steps
		} else {
			moves[i] = steps
		}
	}

	part1(moves)
	part2(moves)

}
