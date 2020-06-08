# Geek-Jokes

## A RESTful API to get random geek jokes written in Flask
[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)
[![forthebadge](http://forthebadge.com/images/badges/gluten-free.svg)](http://forthebadge.com)

## What is the Geek-Jokes-api?
The Geek Jokes RESTful API lets you fetch a random geeky/programming related joke for use in all sorts of applications.

## Why the Geek-Jokes-api?
The Geek Jokes api is for any developer needing some random (geeky) jokes in their life or application.

## URL
```
GET: https://geek-jokes.sameerkumar.website/api?format=json
```

## Usage
Just do a GET request on the API URL.
```
GET: https://geek-jokes.sameerkumar.website/api?format=json
```

## Projects using Geek Jokes API

Repository | Description
---- | ----
[Random. Django. Rango.](https://github.com/powerhouseofthecell/rango) | Random. Django. Rango. An introduction to using Python and Django to build a website.
[tellmejoke](https://github.com/MunafHajir/-tellmeajoke) | VS Code Extension that tells you a joke

Used Geek Jokes API in your project? Check out the [contributing guidelines](https://github.com/sameerkumar18/geek-joke-api/blob/master/contributing.md) for this list and let us know. we love PRs :)

## Examples

### cURL
```
curl -X GET \
'https://geek-jokes.sameerkumar.website/api?format=json'
```

### Python
```Python
import requests

requests.get('https://geek-jokes.sameerkumar.website/api?format=json')
```

### Node.js (es6)
```Javascript
var request = require('request');

let options = {
    url: 'https://geek-jokes.sameerkumar.website/api?format=json',
    method: 'GET'
}

request(options, (err, response, body) => {
    if(!err && response.statusCode == 200)
        console.log(body)
});
```
 ### Any browser
 visit the url: https://geek-jokes.sameerkumar.website/api?format=json to get a joke. Press refresh button for more jokes.

## License
MIT

## Contact
Contact: [sam@sameerkumar.website](mailto:sam@sameerkumar.website)

## Author
Sameer Kumar
https://sameerkumar.website
