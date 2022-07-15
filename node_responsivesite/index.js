const express = require("express");
const redis = require('redis');
const process = require("process");

const app = express()
const client = redis.createClient({
  host:'redis-server',
  port: 6379
});


client.set('visits', 0);

// app.get('/', (req, res) => {
//   client.get('visits', (err, visits) => {
//     res.send('Number of visits is ' + visits);
//     client.set('visits', parseInt(visits) + 1);
//   });
// });



// delete this part its only for checking perposes 




app.get('/',(req,res)=>{

    // intro error code 
    process.exit(0);

    // res.send("hi there");
    client.get('visits', (err, visits) => {
          res.send('Number of visits is ' + visits);
          client.set('visits', parseInt(visits) + 1);
      
        })
})

app.listen(8080, ()=>{
    console.log("listening on port 8080");
})