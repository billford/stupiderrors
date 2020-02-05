[![Build Status](https://travis-ci.org/billford/stupiderrors.svg?branch=master)](https://travis-ci.org/billford/stupiderrors)

# stupiderrors -- BETA 
A site that lets you test your code for various http status codes (errors, problems, etc) 


So you're writing some code that calls a bunch of APIs but you need to be able to test
for when those APIs fail. Enter stupiderrors.net. You can use it to write tests against stuff you
KNOW will fail. Make the hostname a variable and you should be all set.

Usage: 

https://stupiderrors.net/any/path/you/want/error_code so an example
https://stupiderrors.net/api/v2/stuff/404 will return a proper 404 to you. 

https://stupiderrors.net/rando will redirect you to a random (well picked from the 'codes' files of http status codes) and redirect you with the random code. 

https://stupiderrors.net/readme will get you here

I know sites like this exist, blah blah blah, it just seemed like an interesting little diversion to build one myself. 
Wanna fight about it? 


Anyway, enjoy! 

