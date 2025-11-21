# 2005 AIME II Problem 6

## Problem

The cards in a stack of $2n$ cards are numbered consecutively from 1 through $2n$ from top to bottom. The top $n$ cards are removed, kept in order, and form pile $A.$ The remaining cards form pile $B.$ The cards are then restacked by taking cards alternately from the tops of pile $B$ and $A,$ respectively. In this process, card number $(n+1)$ becomes the bottom card of the new stack, card number 1 is on top of this card, and so on, until piles $A$ and $B$ are exhausted. If, after the restacking process, at least one card from each pile occupies the same position that it occupied in the original stack, the stack is named magical. For example, eight cards form a magical stack because cards number 3 and number 6 retain their original positions. Find the number of cards in the magical stack in which card number 131 retains its original position.

## Solution 1
Since a card from B is placed on the bottom of the new stack, notice that cards from pile B will be marked as an even number in the new pile, while cards from pile A will be marked as odd in the new pile. Since 131 is odd and retains its original position in the stack, it must be in pile A. Also to retain its original position, exactly $131 - 1 = 130$ numbers must be in front of it. There are $\frac{130}{2} = 65$ cards from each of piles A, B in front of card 131. This suggests that $n = 131 + 65 = 196$ ; the total number of cards is $196 \cdot 2 = \boxed{392}$ .

## Solution 2
If you index the final stack $1,2,\dots,2n$ , you notice that pile A resides only in the odd indices and has maintained its original order aside from flipping over. The same has happened to pile B except replace odd with even. Thus, if 131 is still at index 131, an odd number, then 131 must be from pile A. The numbers in pile A are the consecutive integers $1,2,\dots, n$ . This all leads us to the following equation. \[131=2n-2(131)+1\implies2n=\boxed{392}\]
These problems are copyrighted © by the Mathematical Association of America.