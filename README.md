# Geek-Jokes

## A Flask RESTful API to get random geek jokes
[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)
[![forthebadge](http://forthebadge.com/images/badges/gluten-free.svg)](http://forthebadge.com)

## What is the Geek-Jokes-api?
The Geek Jokes RESTful API lets you fetch a random geeky/programming related joke for use in all sorts of applications.

## Why the Geek-Jokes-api?
The Geek Jokes api is for any developer needing some random (geeky) jokes in their life or application.

## URL
```
GET: https://geek-jokes.herokuapp.com/api
```

## Usage
Just do a GET request on the API URL.
```
GET: https://geek-jokes.herokuapp.com/api
```

## Examples

### cURL
```
curl -X GET \
'https://geek-jokes.herokuapp.com/api'
```

### Python
```Python
import requests

requests.get('https://geek-jokes.herokuapp.com/api')
```

### Node.js (es6)
```Javascript
var request = require('request');

let options = {
    url: 'https://geek-jokes.herokuapp.com/api',
    method: 'GET'
}

request(options, (err, response, body) => {
    if(!err && response.statusCode == 200)
        console.log(body)
});
```

## License
MIT

## Contact
Contact me here: [sameer18051998@gmail.com](mailto:sameer18051998@gmail.com)
