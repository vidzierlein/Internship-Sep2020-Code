Exercise 2
Pig Latin is a language game, where you move the first
 letter of the word to the end and add "ay." So "Python" becomes "ythonpay." 
 To write a Pig Latin translator in Python, here are the steps we'll need to take:

Ask the user to input a word in English.
Make sure the user entered a valid word.
Convert the word from English to Pig Latin.
Display the translation result.
First define a variable called pygequal to "ay" and ask the user to 
enter a word. Save the results of raw_input() in a variable called original. 
Then add an ifstatement that checks that len(original) is greater than zero 
AND that the word the user enters contains only alphabetical characters(Note:isalpha() 
returns False since the string contains non-letter characters.). 
If the string actually has some characters in it, 
print the user's word.Otherwise (i.e. an else: statement), 
please print "empty".After that checks create a new variable
 called word that holds the .lower()-case conversion of original. 
 Create a new variable called first that holds word[0], the first letter of word. 
 Create a new variable callednew_wordand set it equal to the concatenation ofword,first, 
 andpyg.Setnew_wordequal to the slice from the 1st index all the way to the end ofnew_word. 
 Use[1:len(new_word)]` to do this.

