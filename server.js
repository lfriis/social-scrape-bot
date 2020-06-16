/*

Express Server to run python scrape on cron job

*/

try
{
    var express    = require('express');
    var app        = express();
    var cron       = require("node-cron");
    var shell      = require('shelljs');
    var nodemailer = require("nodemailer");
    var port       = 8080;
    var date       = new Date();

    console.log("\nAll necessary packages included...");
}
catch(e) { console.log("Errors including packages: " + (e)); };

// Including required middleware
app.use(express.json());

// Cron job running scrape running everyday at 8:55AM ET
console.log("Cron scheduler ready...");
cron.schedule("02 23 * * *", function() 
{
  console.log("---------------------");
  console.log("Running cron job...");

  let transporter = nodemailer.createTransport({
    service: "gmail",
    auth: {
      user: "****",
      pass: "****"
    }
  });

  let mailOptions = {
    from: "larsenfriis1@gmail.com",
    to: "larsenfriis@icloud.com",
    subject: `Cron Job Failed on ` + date.toLocaleTimeString(),
    text: `Error inserting data into Google Sheet, please check server logs...`
  };
  
  if (shell.exec("python scrape.py").code !== 0) {
    console.log("Cron job did not successfully run at " + date.toLocaleTimeString());

    transporter.sendMail(mailOptions, function(error, info) {
      if (error) {
        throw error;
      } else {
        console.log("Email successfully sent at " + date.toLocaleTimeString());
      }
    });
  }
});

// Listening to requests sent by client
app.listen(port, function() 
{
  console.log('Server deployed...\n' + 'Listening at address localhost:' + port + '\n');
});