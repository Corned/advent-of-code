package common

import (
	"os"
	"strings"
)

func ReadAndProcessFile(filename string) []string {
	contents, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}

	return strings.Split(string(contents), "\n")
}
