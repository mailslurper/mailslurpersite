package main

import (
	"flag"
	"fmt"
	"log"
	"net/http"
)

var port = flag.Int("port", 8889, "Port to bind this server to")

func main() {
	flag.Parse()

	fileServer := http.FileServer(http.Dir("./"))
	http.Handle("/", fileServer)

	log.Println("Serving content for MailSlurperSite on port", *port)
	log.Println(http.ListenAndServe(fmt.Sprintf(":%d", *port), nil))
}
