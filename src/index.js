const express = require("express");

const app = express();
const cors = require("cors");
const path = require("path");

//settings
app.set('port', process.env.PORT || 5002);

//middleware
app.use(cors());
app.use(express.urlencoded({ extended: false }));
app.use(express.json());

//routes
app.use('/api/test', require(path.join(__dirname, '/routes/test')));

//starting the server
app.listen(app.get('port'), () => {
  console.log(` The server has started successfully on port: ${app.get('port')} !!`);
});