package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println("          math.Pi:", math.Pi)
	fmt.Println("Nilakantha Series:", pi(5000))
}

func pi(n int) float64 {
	ch := make(chan float64)
	for k := 0; k < n; k++ {
		go term(ch, float64(k))
	}
	f := 3.0
	for k := 0; k < n; k++ {
		f += <-ch
	}
	return f
}

func term(ch chan float64, k float64) {
	ch <- 4 * math.Pow(-1, k) / ((2*k + 2) * (2*k + 3) * (2*k + 4))
}