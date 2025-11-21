# 2023 AIME I Problem 6

## Problem

Alice knows that $3$ red cards and $3$ black cards will be revealed to her one at a time in random order. Before each card is revealed, Alice must guess its color. If Alice plays optimally, the expected number of cards she will guess correctly is $\frac{m}{n},$ where $m$ and $n$ are relatively prime positive integers. Find $m+n.$

## Solution 1 (Casework)
We break the problem into stages, one for each card revealed, then further into cases based on the number of remaining unrevealed cards of each color. Since expected value is linear, the expected value of the total number of correct card color guesses across all stages is the sum of the expected values of the number of correct card color guesses at each stage; that is, we add the probabilities of correctly guessing the color at each stage to get the final answer (See https://brilliant.org/wiki/linearity-of-expectation/ )
At any stage, if there are $a$ unrevealed cards of one color and $b$ of the other color, and $a \geq b$ , then the optimal strategy is to guess the color with $a$ unrevealed cards, which succeeds with probability $\frac{a}{a+b}.$
Stage 1:
There are always $3$ unrevealed cards of each color, so the probability of guessing correctly is $\frac{1}{2}$ .
Stage 2:
There is always a $3$ - $2$ split ( $3$ unrevealed cards of one color and $2$ of the other color), so the probability of guessing correctly is $\frac{3}{5}$ .
Stage 3:
There are now $2$ cases:
- The guess from Stage 2 was correct, so there is now a $2$ - $2$ split of cards and a $\frac{1}{2}$ probability of guessing the color of the third card correctly.
- The guess from Stage 2 was incorrect, so the split is $3$ - $1$ and the probability of guessing correctly is $\frac{3}{4}$ .
Thus, the overall probability of guessing correctly is $\frac{3}{5} \cdot \frac{1}{2} + \frac{2}{5} \cdot \frac{3}{4} = \frac{3}{5}$ .
Stage 4:
This stage has $2$ cases as well:
- The guesses from both Stage 2 and Stage 3 were incorrect. This occurs with probability $\frac{2}{5} \cdot \frac{1}{4} = \frac{1}{10}$ and results in a $3$ - $0$ split and a certain correct guess at this stage.
- Otherwise, there must be a $2$ - $1$ split and a $\frac{2}{3}$ probability of guessing correctly.
The probability of guessing the fourth card correctly is therefore $\frac{1}{10} \cdot 1 + \frac{9}{10} \cdot \frac{2}{3} = \frac{7}{10}$ .
Stage 5:
Yet again, there are $2$ cases:
- In Stage 4, there was a $2$ - $1$ split and the guess was correct. This occurs with probability $\frac{9}{10} \cdot \frac{2}{3} = \frac{3}{5}$ and results in a $1$ - $1$ split with a $\frac{1}{2}$ chance of a correct guess here.
- Otherwise, there must be a $2$ - $0$ split, making a correct guess certain.
In total, the fifth card can be guessed correctly with probability $\frac{3}{5} \cdot \frac{1}{2} + \frac{2}{5} \cdot 1 = \frac{7}{10}$ .
Stage 6:
At this point, only $1$ card remains, so the probability of guessing its color correctly is $1$ .
In conclusion, the expected value of the number of cards guessed correctly is \[\frac{1}{2} + \frac{3}{5} + \frac{3}{5} + \frac{7}{10} + \frac{7}{10} + 1 = \frac{5+6+6+7+7+10}{10} = \frac{41}{10},\] so the answer is $41 + 10 = \boxed{051}.$
~OrangeQuail9

## Solution 2 (Casework)
At any point in the game, Alice should guess whichever color has come up less frequently thus far (although if both colors have come up equally often, she may guess whichever she likes); using this strategy, her probability of guessing correctly is at least $\frac{1}{2}$ on any given card, as desired.
There are ${6 \choose 3} = 20$ possible orderings of cards, all equally likely (since any of the $6! = 720$ permutations of the cards is equally likely, and each ordering covers $3!^2 = 6^2 = 36$ permutations).
Each of the $10$ orderings that start with red cards corresponds with one that starts with a black card; the problem is symmetrical with respect to red and black cards, so we can, without loss of generality, consider only the orderings that start with red cards.
We then generate a tally table showing whether Alice's guesses are correct for each ordering; for a given card, she guesses correctly if fewer than half the previously shown cards were the same color, guesses incorrectly if more than half were the same color, and guesses correctly with probability $\frac{1}{2}$ if exactly half were the same color.
In this table, $\mid$ denotes a correct guess, $\--$ denotes an incorrect guess, and $/$ denotes a guess with $\frac{1}{2}$ probability of being correct.
Now we sum the tallies across orderings, obtaining $41$ , and finally divide by the number of orderings ( $10$ ) to obtain the expected number of correct guesses, $\frac{41}{10}$ , which yields an answer of $41 + 10 = \boxed{051}.$
~IndigoEagle108

## Solution 3 (Dynamic Programming)
Denote by $N \left( a, b \right)$ the optimal expected number of cards that Alice guesses correctly, where the number of red and black cards are $a$ and $b$ , respectively.
Thus, for $a, b \geq 1$ , we have \begin{align*} N \left( a, b \right) & = \max \left\{ \frac{a}{a+b} \left( 1 + N \left( a - 1 , b \right) \right) + \frac{b}{a+b} N \left( a , b - 1 \right) , \right. \\ & \hspace{1cm} \left. \frac{a}{a+b} N \left( a - 1 , b \right) + \frac{b}{a+b} \left( 1 + N \left( a , b - 1 \right) \right) \right\} . \end{align*}
For $a = 0$ , Alice always guesses black. So $N \left( 0 , b \right) = b$ .
For $b = 0$ , Alice always guesses red. So $N \left( a , 0 \right) = a$ .
To solve this dynamic program, we can also exploit its symmetry that $N \left( a , b \right) = N \left( b , a \right)$ .
By solving this dynamic program, we get $N \left( 1, 1 \right) = \frac{3}{2}$ , $N \left( 1, 2 \right) = \frac{7}{3}$ , $N \left( 1 , 3 \right) = \frac{13}{4}$ , $N \left( 2 , 2 \right) = \frac{17}{6}$ , $N \left( 2 , 3 \right) = \frac{18}{5}$ , $N \left( 3, 3 \right) = \frac{41}{10}$ .
Therefore, the answer is $41 + 10 = \boxed{\textbf{(051) }}$ .
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Solution 4 (Simplification of Solution 3)
Denote by $N_{i,j}$ the optimal expected number of cards that Alice guesses correctly, where the number of cards are $i$ and $j \ge i.$
If $i = 0$ then Alice guesses correctly all cards, so $N_{0,j} = j.$
If $j = i$ then Alice guesses next card with probability $\frac {1}{2} \implies N_{i,i} = \frac {1}{2} + N_{i-1,i}.$
If $j = i+1$ then Alice guesses next card with probability $\frac {i+1}{2i+1} \implies N_{i,i+1} = \frac {i+1}{2i+1} (1+ N_{i,i}) + \frac{i}{2i+1} N_{i-1,i+1}.$
If $j = i+2$ then Alice guesses next card with probability $\frac {i+2}{2i+2} \implies N_{i,i+2} = \frac {i+2}{2i+2} (1+ N_{i,i+1}) + \frac{i}{2i+2} N_{i-1,i+2}.$
One can find consistently: $N_{1,1} = \frac {1}{2} + N_{0,1} = \frac {3}{2},$ \[N_{1,2} = \frac {2}{3} (1 + N_{1,1}) + \frac {1}{3} N_{0,2} = \frac {7}{3}.\] \[N_{2,2} = \frac {1}{2} + N_{1,2} = \frac {17}{6}.\] \[N_{1,3} = \frac {3}{4} (1 + N_{1,2}) + \frac {1}{4} N_{0,3} = \frac {13}{4}.\] \[N_{2,3} = \frac {3}{5} (1 + N_{2,2}) + \frac {2}{5} N_{1,3} = \frac {18}{5}.\] \[N_{3,3} = \frac {1}{2} + N_{2,3} = \frac {41}{10}.\] Therefore, the answer is $41 + 10 = \boxed{\textbf{(051) }}$ .
vladimir.shelomovskii@gmail.com, vvsss

## Solution 5 (Pseudo-recursion)
Denote $E_n$ the expected number of cards Alice guesses correctly given $n$ red cards and $n$ black cards. We want to find $E_3$ .
Alice has a $\frac{1}{2}$ chance of guessing the first card. WLOG assume the first card color is red. For the next card, Alice has a $\frac{3}{5}$ chance of guessing the card if she chooses black; if they guess right, there's one less red and black card, so the expected number of cards Alice guesses from here is $E_2$ . If Alice does not guess correctly (which occurs with probability $\frac{2}{5}$ ), this means that there's 3 black cards and 1 red card left, so Alice should guess black next with a $\frac{3}{4}$ chance of being right. If Alice is wrong (with probability $\frac{1}{4}$ ), there are only 3 black cards left, so Alice can guess these with certainty; if Alice is right, there are 2 blacks and 1 red left, so Alice should again guess black. If Alice is right (with probability $\frac{2}{3}$ ), there is now 1 black and red card each, so the expected number of cards guessed is $E_1$ ; if she is wrong (with probability $\frac{1}{3}$ ), there are 2 black cards left, so Alice can guess these with certainty.
Summing this up into a formula: \[E_3 = \frac{1}{2} + \frac{3}{5} \left(1 + E_2 \right) + \frac{2}{5} \left( \frac{1}{4}(3) + \frac{3}{4}\left(1 + \frac{2}{3}\left(1 + E_1 \right) + \frac{1}{3}(2)\right) \right)\]
We can apply similar logic to compute $E_2$ and get \[E_2 = \frac{1}{2} + \frac{2}{3}(1 + E_1) + \frac{1}{3}(2)\]
To compute $E_1$ , we know that Alice can guess the last card with certainty, and there's a $\frac{1}{2}$ chance they get the first card as well, so $E_1 = \frac{3}{2}$ .
Thus, $E_2 = \frac{17}{6}$ , and after long computation, we get $E_3 = \frac{41}{10}$ . The requested answer is $41 + 10 = \boxed{51}$ .
~ adam_zheng

## Solution 6 (non-recursive)
There's a beautiful observation that for any particular game path, the expected number of correct guesses is purely dependent on how often we are in a neutral state (i.e. there are the same number of red and black cards remaining in the deck). For example, given path $BRRBBR$ we are in a neutral state once in the beginning when no cards have been flipped, after the second card has been flipped, after the 4th card has been flipped, and finally a 4th time at the very end of the game. Call the number of times a given path is in the neutral state $n$ . Then the expected number of correct guesses equals:
\[E = 3 + \frac{n-1}{2}\]
Since this problem is small, we could just could just count them (noting that the problem is symmetric between reds and blacks):
\[ \begin{array}{|c|c|c|} \hline \textbf{Path} & \textbf{Neutral States} & \textbf{E}\\ \hline \text{RRRBBB} & 2 & 3.5\\ \text{RRBRBB} & 2 & 3.5 \\ \text{RRBRBB} & 3 & 4 \\ \text{RRBBBR} & 3 & 4 \\ \text{RBRRBB} & 3 & 4 \\ \text{RBRBRB} & 4 & 4.5 \\ \text{RBRBBR} & 4 & 4.5 \\ \text{RBBRRB} & 4 & 4.5 \\ \text{RBBRBR} & 4 & 4.5 \\ \text{RBBBRR} & 3 & 4 \\ \hline \end{array} \]
Using linearity of expectation, the expected number of correct guesses is:
\[E=\frac{3.5+3.5+4+4+4+4.5+4.5+4.5+4.5+4}{10}=\frac{41}{10}, \text{ thus } 41 + 10 = \boxed{51}\]
Note that if we call the total number of neutral states across all ${6 \choose 3}=20$ paths $N$ , this would be equivalent to:
\[E=3 + \frac{\frac{N}{20}-1}{2}\]
We can compute $N$ directly. Let the index $m$ be a point where we've seen $m$ red cards and $m$ black cards. There are $\binom{2m}{m}$ paths that lead up to that point. After which there are $6-2m$ cards remaining, $3-m$ of which are red and $3-m$ of which are black. Summing up over all possible values of $m$ gives us:
\[ \sum_{m=0}^{3} \binom{2m}{m} \cdot \binom{6-2m}{3-m} = \] \[ \binom{0}{0} \cdot \binom{6}{3} + \binom{2}{1} \cdot \binom{4}{2} + \binom{4}{2} \cdot \binom{2}{1} + \binom{6}{3} \cdot \binom{0}{0} \] \[ = 1 \cdot 20 + 2 \cdot 6 + 6 \cdot 2 + 20 \cdot 1 \] \[ = 20 + 12 + 12 + 20 = 64 \]
and as before:
\[E=3 + \frac{\frac{N}{20}-1}{2}=3 + \frac{\frac{64}{20}-1}{2}=3+\frac{11}{10}=\frac{41}{10}\]
~proloto

## Video Solution 1 by TheBeautyofMath
https://youtu.be/ITjbRKWbQeI
~IceMatrix
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .