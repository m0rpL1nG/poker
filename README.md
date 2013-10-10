Python Poker
================

This program receive poker n hands and return the winner.

Description
----------

1 Deck have 52 cards divided into 4 suits 1 suit have 13 ranks.

*Suit
	*S = Spade
	*H = Heart
	*D = Diamond
	*C = Club

*Rank
	*A = Ace
	*K = King
	*Q = Queen
	*J = Jack
	*T = 10

Requirement
-------

* [Python 2.7.5](http://www.python.org/download/releases/2.7.5/) - another version might work.

<img src="http://i.imgur.com/d5HZAmg.jpg" alt="poker">

Usage
-----

First set you terminal to run the script.

	bash$ python poker.py

Then the program would ask you how many poker hand do you want.(input must be __integer__)

	how much hand do you want? : 2

Then you should be able to input your poker hand.(input must be __list of string__)

	hand 1 : ['5H', '5S', '5D', '8C', '8S']
	hand 2 : ['6H', '6S', '6D', '7C', 'KS']

And then the result would came out.

	winner is : [['5H', '5S', '5D', '8C', '8S']]	

Example
------

	bash$ python poker.py
	how much hand do you want? :  3
	hand 1 : ['JS', 'TS', '9S', '8S', '7S']
	hand 2 : ['5S', '3H', '9D', '8C', '8S']
	hand 3 : ['4S', '4H', '7D', '3C', '3S']
	winner is : [['JS', 'TS', '9S', '8S', '7S']]
