# 2003 AIME II Problem 3

## Problem

Define a $\text{good~word}$ as a sequence of letters that consists only of the letters $A$ , $B$ , and $C$ - some of these letters may not appear in the sequence - and in which $A$ is never immediately followed by $B$ , $B$ is never immediately followed by $C$ , and $C$ is never immediately followed by $A$ . How many seven-letter good words are there?

## Solution 1
There are three letters to make the first letter in the sequence. However, after the first letter (whatever it is), only two letters can follow it, since one of the letters is restricted. Therefore, the number of seven-letter good words is $3*2^6=192$
Therefore, there are $\boxed{192}$ seven-letter good words.

## Solution 2 (Recursion)
We solve this problem using recursion. Let $f(x)$ be the number of $x$ -letter good words. Thus $f(1) = 3$ (A, B or C) and the answer is just $f(7)$ . The recurrence relation can be found by considering the last letter of one of the valid strings of length $x - 1$ . There are $2$ possibilities for the next letter and thus $f(x) = 2 \cdot f(x-1)$ . Now we can find a closed form as $f(x) = 3 \cdot 2 ^{x-1}$ (easy to prove by induction) and thus $f(7) = 64 * 3 = \boxed{192}$ seven-letter good words. ~AK2006

## Solution 3
This restriction forces the letters to appear in $\emph{blocks}$ in a fixed cyclic order: \[A \;\to\; C \;\to\; B \;\to\; A \;\to\; C \;\to\; B \;\to \dots\] For example, if a word starts with $A$ , $\text{ it must look like: }$ $\underbrace{AAA\cdots}_{\text{A-block}} \; \underbrace{CCC\cdots}_{\text{C-block}} \; \underbrace{BBB\cdots}_{\text{B-block}} \; \underbrace{AAA\cdots}_{\text{A-block}} \; \dots$
The word's structure is therefore determined by the starting letter and where the block transitions occur. In a $7$ letter word, there are $6$ gaps between the letters. At each gap, we can either stay in the block or move on to the next. This gives $2$ choices for each gap, or $2^6$ possibilities. Multiply this by the $3$ possible starting letters to get $3*2^6 = \boxed{192}$ .
~lprado

## Video Solution by Sal Khan
https://www.youtube.com/watch?v=JU67TL2L1CA&list=PLSQl0a2vh4HCtW1EiNlfW_YoNAA38D0l4&index=9 - AMBRIGGS
These problems are copyrighted © by the Mathematical Association of America.