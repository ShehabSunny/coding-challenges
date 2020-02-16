package main

import "fmt"

func main() {
	fmt.Println("hello")
	a := "abcc"
	b := "acbc"
	print(buddyString(a, b))
}

func buddyString(a string, b string) bool {
	if len(a) != len(b) {
		return false
	}

	return false
}
