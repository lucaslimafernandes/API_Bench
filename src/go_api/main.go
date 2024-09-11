package main

import (
	"fmt"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	// fmt.Fprintf(w, "Hello, World! You've hit %s\n", r.URL.Path)
	fmt.Fprint(w, "Hello, World!")
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":3000", nil)
}
