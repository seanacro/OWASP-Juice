The tryhackme room "OWASP Juice Shop" has a challenge that has you use Burp to run a dictionary attack on the admin's password but Burp is SLOOOOOOOOOW if you're using the free version. So I wrote this python script to get through it a bit faster. 

Things you may have to change:
The cookies (line 12) don't appear to change if the victim machine times out or is otherwise relaunched with a new IP but maybe they're different for other users?
Line 8 assumes that you're using a particular dictionary located in a specific folder.
