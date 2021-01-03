#Plain

##Description
Santa has received a letter from his freind Markov. But santa couldn't get what he means
###hint:
Default should be enough !

##Solution
The text we got looks like normal readable text but it makes no sense.
Here we used the Markov Chain to hide the flag
there is already a python implementation on Markov chains we can use it to hide and to extract hidden data 
https://github.com/hmoraldo/markovTextStego
The hint here is to tell that you will get the flag with the commands used in the example in the project repo 
to get the flag use 
`python commandline.py decodeFullText --markovInput data/markovChain.json --wordsPerState 1 encoded.txt output.data`

and we get our flag!