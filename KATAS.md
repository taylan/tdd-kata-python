Katas
=====

### FizzBuzz

- Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz"
  instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both
  three and five print "FizzBuzz".


### [String Calculator](http://osherove.com/tdd-kata-1/)

- Create a simple String calculator with a method int Add(string numbers)
    - The method can take 0, 1 or 2 numbers, and will return their sum (for an empty string it will return 0) for example “” or “1” or “1,2”
    - Start with the simplest test case of an empty string and move to 1 and two numbers
    - Remember to solve things as simply as possible so that you force yourself to write tests you did not think about
    - Remember to refactor after each passing test
- Allow the Add method to handle an unknown amount of numbers
- Allow the Add method to handle new lines between numbers (instead of commas).
    - the following input is ok:  “1\n2,3”  (will equal 6)
    - the following input is NOT ok:  “1,\n” (not need to prove it - just clarifying)
- Support different delimiters
    - to change a delimiter, the beginning of the string will contain a separate line that looks like this:   “//[delimiter]\n[numbers…]” for example “//;\n1;2” should return three where the default delimiter is ‘;’ .
    - the first line is optional. all existing scenarios should still be supported
- Calling Add with a negative number will throw an exception “negatives not allowed” - and the negative that was passed.if there are multiple negatives, show all of them in the exception message
- Numbers bigger than 1000 should be ignored, so adding 2 + 1001  = 2
- Delimiters can be of any length with the following format:  `//[delimiter]\n` for example: `//[***]\n1***2***3` should return 6
- Allow multiple delimiters like this:  `//[delim1][delim2]\n` for example `//[*][%]\n1*2%3` should return 6.
- make sure you can also handle multiple delimiters with length longer than one char


### Bowling Game

- Gutter game scores zero - When you roll all misses, you get a total score of zero.
- All ones scores 20 - When you knock down one pin with each ball, your total score is 20.
- A spare in the first frame, followed by three pins, followed by all misses scores 16.
- A strike in the first frame, followed by three and then four pins, followed by all misses, scores 24.
- A perfect game (12 strikes) scores 300.


### LCD Digits

<pre>
Your task is to create an LCD string representation of an
integer value using a 3x3 grid of space, underscore, and
pipe characters for each digit. Each digit is shown below
(using a dot instead of a space)

._.   ...   ._.   ._.   ...   ._.   ._.   ._.   ._.   ._.
|.|   ..|   ._|   ._|   |_|   |_.   |_.   ..|   |_|   |_|
|_|   ..|   |_.   ._|   ..|   ._|   |_|   ..|   |_|   ..|


Example: 910

._. ... ._.
|_| ..| |.|
..| ..| |_|
</pre>


### Leap Year

<pre>
Write a function that returns true or false depending on
whether its input integer is a leap year or not.

A leap year is defined as one that is divisible by 4,
but is not otherwise divisible by 100 unless it is
also divisible by 400.

For example, 2001 is a typical common year and 1996
is a typical leap year, whereas 1900 is an atypical
common year and 2000 is an atypical leap year.
</pre>


### Recently Used List

<pre>
Develop a recently-used-list class to hold strings
uniquely in Last-In-First-Out order.

o) The most recently added item is first, the least
   recently added item is last.

o) Items can be looked up by index, which counts from zero.

o) Items in the list are unique, so duplicate insertions
   are moved rather than added.

o) A recently-used-list is initially empty.

Optional extras

o) Null insertions (empty strings) are not allowed.

o) A bounded capacity can be specified, so there is an upper
   limit to the number of items contained, with the least
   recently added items dropped on overflow.
</pre>


### Word Wrap

Create a function which breaks words on specified space with new line. Its nothing but merely similar to word-processor.


### [Bloom Filter](http://codekata.com/kata/kata05-bloom-filters/)

Bloom filters are very simple. Take a big array of bits, initially all zero. Then take the things you want to look up (in our case we’ll use a dictionary of words). Produce ‘n’ independent hash values for each word. Each hash is a number which is used to set the corresponding bit in the array of bits. Sometimes there’ll be clashes, where the bit will already be set from some other word. This doesn’t matter.

To check to see of a new word is already in the dictionary, perform the same hashes on it that you used to load the bitmap. Then check to see if each of the bits corresponding to these hash values is set. If any bit is not set, then you never loaded that word in, and you can reject it.


### [Supermarket Checkout](http://codekata.com/kata/kata09-back-to-the-checkout/)

In a normal supermarket, things are identified using Stock Keeping Units, or SKUs. In our store, we’ll use individual letters of the alphabet (A, B, C, and so on). Our goods are priced individually. In addition, some items are multipriced: buy n of them, and they’ll cost you y cents. For example, item ‘A’ might cost 50 cents individually, but this week we have a special offer: buy three ‘A’s and they’ll cost you $1.30.

Our checkout accepts items in any order, so that if we scan a B, an A, and another B, we’ll recognize the two B’s and price them at 45 (for a total price so far of 95). Because the pricing changes frequently, we need to be able to pass in a set of pricing rules each time we start handling a checkout transaction.

    co = CheckOut.new(pricing_rules)
    co.scan(item)
    co.scan(item)
        :    :
    price = co.total


### [Transitive Dependencies](http://codekata.com/kata/kata18-transitive-dependencies/)

Let’s write some code that calculates how dependencies propagate between things such as classes in a program.

Given the following input, we know that A directly depends on B and C, B depends on C and E, and so on.

    A   B   C
    B   C   E
    C   G
    D   A   F
    E   F
    F   H

The full set of dependencies is:

    A   B C E F G H
    B   C E F G H
    C   G
    D   A B C E F G H
    E   F H
    F   H

