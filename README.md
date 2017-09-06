# Paxos Full Stack Engineer Coding Assignment
Jason Shen



# Instructions for running the code:

### Prior to running:

* Download repository
* Download and install Python
* Download and install MongoDB (Required for Problem 1)
  https://docs.mongodb.com/manual/installation/

### Problem 1

* Change to your MongoDB directory and start the primary Mongo daemon process:

Example:

``` 
$ C/MongoDB/Server/3.4/bin
$ ./mongod
```
* In a separate terminal window, change directory to question1 in the Paxos repository and start npm

```
$ cd Paxos/question1
$ npm start
```
* The web service should now be up and running, and now, as per the spec you should be able to make the POST and GET requests to your localhost:3000

``` 
$ curl -X POST -H "Content-Type: application/json" -d '{"message": "foo"}' localhost:3000/messages

{"digest": "2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae"}
```

```
$ curl localhost:3000/messages/2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae

{"message": "foo"}
```

```
$ curl -i localhost:3000/messages/rickfox

HTTP/1.1 404 Not Found
X-Powered-By: Express
Content-Type: text/plain; charset=utf-8
Content-Length: 9
ETag: W/"9-0gXL1ngzMqISxa6S1zx3F4wtLyg"
Date: Wed, 06 Sep 2017 22:47:55 GMT
Connection: keep-alive

Not Found
```

### Problem 2

* Change directory to Paxos/question2

```
cd Paxos/question2
```
* The prices.txt file contains the list of items and prices. By default, the list is exactly the one provided in the spec. Feel free to change it as necessary for testing.

* The default driver program is main.py and it calls upon the implementations provided in helper.py. To run the program:

``` 
$ python main.py prices.txt 2500

(('Candy Bar', 500), ('Earmuffs', 2000))
```

* An optional fourth argument can be provided to run the bonus question:
``` 
$ python main.py prices.txt 2500 triple

(('Candy Bar', 500), ('Earmuffs', 2000))
```


