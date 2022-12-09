const config = require('config')

var express = require('express')
var app = express()

app.set('port', (process.env.PORT || 5000))
app.use(express.static(__dirname + '/public'))

app.get('/env', (request, response) => {
  if (config.util.getEnv("NODE_ENV") === "Testing") {
    response.send('<b>You are working in the <em>TEST</em> environment.</b>')
  } else if (config.util.getEnv("NODE_ENV") === "Heroku Test") {
    response.send('<b>You are working in the <em>TEST</em> environment that is in Heroku.</b>')
  } else if (config.util.getEnv("NODE_ENV") === "Production") {
    response.send('<b>You are working in Production</b>')
  } else {
    response.send('<b>Environment is unknown</b>')
  }
})

app.listen(app.get('port'), function() {
  console.log("Node app is running at localhost:" + app.get('port'))
})
