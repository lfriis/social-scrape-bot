/*

Express Server to run python scrape on cron job

*/

try
{
    var express = require('express');
    var app     = express();
    var cron    = require("node-cron");
    var shell   = require('shelljs');
    var port    = 8080;

    console.log("\nAll necessary packages included...");
}
catch(e) { console.log("errors including packages: " + (e)); };

// Including required middleware
app.use(express.json());

// Cron job running scrape running everyday at 9AM ET
console.log("Cron scheduler ready...");
cron.schedule("1 * * * * *", function() {
  console.log("Scheduler running cron job...\n");
  if (shell.exec("python scrape.py").code !== 0) {
    console.log("Cron job did not successfully run");
  }
});

// Listening to requests sent by client
app.listen(port, function() 
{
  console.log('Server deployed...\n' + 'Listening at address localhost:' + port + '\n');
});