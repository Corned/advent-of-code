package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	fmt.Println("Day 1: ...")

	contents, _ := os.ReadFile("./day01-input.txt")
	var data []string = strings.Split(string(contents), "\n")

	for _, value := range data {
		fmt.Println(value)
	}
}
