const express = require('express');
const app = express();
const PORT = 8080; 

const fs = require('fs');
var wordArr =[];
var count = '';
fs.readFile('el_GR_n_5.txt', function(err, data) {
    if(err) throw err;
    wordArr = data.toString().replace(/\r\n/g,'\n').split('\n');
    count = wordArr.length;
});

var rightNow = new Date();
var day = rightNow.toISOString().slice(0,10).replace(/-/g,"");

// npm install seedrandom
const seedrandom = require('seedrandom');
const generator = seedrandom(day);
const randomNumber= generator();



app.use((req, res, next) => {
    res.setHeader("Access-Control-Allow-Origin", "http://localhost:3000");
    res.setHeader("Access-Control-Allow-Methods", "POST,GET,OPTIONS");
    if (req.method == "OPTIONS") {
        return res.sendStatus(200);
    }
    next();
});

app.listen(
    PORT,
    () => console.log(`App listening on http://localhost:${PORT}`)
)

app.get('/dailyword', (req,res) => {
    const rand = Math.floor(randomNumber * count);
    res.json({data: wordArr[rand]}
    )
});

app.get('/randomword', (req,res) => {
    const rand = Math.floor(Math.random() * count);
    res.json({data: wordArr[rand]}
    )
})

app.get('/wordlist', (req,res) => {
    res.json({data: wordArr}
    )
})
