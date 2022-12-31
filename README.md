<h1> sqlite3 and sql injection</h1>

<h2> SQL Injection</h2>
<div>
  <p>SQL injection is one of the famous injection techniques which is listed in OWASP Top 10 vulnerabilities</p><br>
  <p>This appliction contains the details of OWASP top 10 vulnerabilites. For page source</p>
  <a href='https://www.reflectiz.com/blog/owasp-top-ten-2022/'>click here</a>
</div>

<div>
  <p>For giving you a glance on SQL injection, this application is developed intentionally vulnerable. Here, in order to access the OWASP top 10 details you have to provide the user name and password. This password section is made vulnerable to injection.</p>
  <p>
</div>
<div>
  <h2>Step 1 : </h2>
  <p>   Clone the repository</p><br>
 <img src='https://user-images.githubusercontent.com/59536508/210131281-2df6ab9b-e2c3-49d4-9818-75c350a77290.png'>
  
  <h2>Step 2 : </h2>
  <p>   Open the directory and execute the program sql_injection.py</p>
  <img src='https://user-images.githubusercontent.com/59536508/210131484-c374b7d5-c29b-472f-aa71-9b9109986cbe.png'>
  
  <h2>Step 3 : </h2>
  <p>Press Enter and you will be asked for username and password</p>
  <p>This application has an "admin" account. So enter the username and along with that add the payload and a random password</p>
  <h6>Payload  :   ' OR 1=1 -- </h6>
  <img src='https://user-images.githubusercontent.com/59536508/210131658-513125e7-2f87-4217-a2e3-395dacb78d64.png'>
  
  

</div>


