const express = require('express');
const session = require('express-session');
const bodyParser = require('body-parser');
const api = require('./api/index');

const native = require('bindings')('native');

const config = process.env.NODE_ENV === 'production' ? process.env : require('../../config/config');

const app = express();

app.disable('x-powered-by');

app.use(
  session({
    secret: config.SECRET,
    resave: false,
    saveUninitialized: false,
    cookie: {
      maxAge: 3600000, // one hour
    },
  })
);

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

app.use(express.static(`${__dirname}/../../client/dist/`));

app.use('/api', api);

app.get('*', (req, res) => res.redirect(301, '/'));

module.exports = app;

//csv([[12, 90],[11, 100]], (err, data) => fs.writeFile('./server/local/band1.csv', data, (err) => console.log(err)))
