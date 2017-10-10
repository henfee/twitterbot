package main

import (
	"github.com/ChimeraCoder/anaconda"
)

func main() {
	anaconda.SetConsumerKey(consumerKey)
	anaconda.SetConsumerSecret(consumerSecret)
	api := anaconda.NewTwitterApi(tokenKey, tokenSecret)
}
