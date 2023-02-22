This code consists of two parts:
1. Code for the Pico monitoring the moisture level and making a POST request if the moisture drops too low
2. Code listening for POST requests utilizing AWS Lambda function, which triggers an email notification to be sent out

NOTE: Lambda code will need to be updated with the 'To:' and 'From:' email addresses. if your SES is set up in a sandbox environment BOTH the To and From addresses need to be verified in order for it to execute. Only if you are approved for production access can you send emails to any recipient