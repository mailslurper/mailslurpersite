//go:generate esc -o ./assets/www.go -pkg assets -ignore DS_Store|README\.md|LICENSE|www\.go -prefix /assets/ ./assets ./index.html

package main

import (
	"flag"
	"fmt"
	"log"
	"net/http"

	"github.com/mailslurper/mailslurpersite/assets"
)

const DEBUG_ASSETS bool = false

var port = flag.Int("port", 8889, "Port to bind this server to")

func main() {
	flag.Parse()

	fileServer := http.FileServer(assets.FS(DEBUG_ASSETS))
	http.Handle("/", fileServer)

	log.Println("Serving content for MailSlurperSite on port", *port)
	log.Println(http.ListenAndServe(fmt.Sprintf(":%d", *port), nil))
}
