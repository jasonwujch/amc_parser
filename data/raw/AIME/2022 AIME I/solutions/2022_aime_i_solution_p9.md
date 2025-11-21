# 2022 AIME I Problem 9

## Problem

Ellina has twelve blocks, two each of red ( $\textbf{R}$ ), blue ( $\textbf{B}$ ), yellow ( $\textbf{Y}$ ), green ( $\textbf{G}$ ), orange ( $\textbf{O}$ ), and purple ( $\textbf{P}$ ). Call an arrangement of blocks $\textit{even}$ if there is an even number of blocks between each pair of blocks of the same color. For example, the arrangement \[\textbf{R B B Y G G Y R O P P O}\] is even. Ellina arranges her blocks in a row in random order. The probability that her arrangement is even is $\frac{m}{n},$ where $m$ and $n$ are relatively prime positive integers. Find $m+n.$

## Solution 1
Consider this position chart: \[\textbf{1 2 3 4 5 6 7 8 9 10 11 12}\] Since there has to be an even number of spaces between each pair of the same color, spots $1$ , $3$ , $5$ , $7$ , $9$ , and $11$ contain some permutation of all $6$ colored balls. Likewise, so do the even spots, so the number of even configurations is $6! \cdot 6!$ (after putting every pair of colored balls in opposite parity positions, the configuration can be shown to be even). This is out of $\frac{12!}{(2!)^6}$ possible arrangements, so the probability is: \[\frac{6!\cdot6!}{\frac{12!}{(2!)^6}} = \frac{6!\cdot2^6}{7\cdot8\cdot9\cdot10\cdot11\cdot12} = \frac{2^4}{7\cdot11\cdot3} = \frac{16}{231},\] which is in simplest form. So, $m + n = 16 + 231 = \boxed{247}$ .
~Oxymoronic15

## Solution 2
We can simply use constructive counting. First, let us place the red blocks; choose the first slot in $12$ ways, and the second in $6$ ways, because the number is cut in half due to the condition in the problem. This gives $12 \cdot 6$ ways to place the red blocks. Similarly, there are $10 \cdot 5$ ways to place the blue blocks, and so on, until there are $2 \cdot 1$ ways to place the purple blocks. Thus, the probability is \[\frac{12 \cdot 6 \cdot 10 \cdot 5 \cdot 8 \cdot 4 \cdot 6 \cdot 3 \cdot 4 \cdot 2 \cdot 2 \cdot 1}{12!}=\frac{16}{231},\] and the desired answer is $16+231=\boxed{247}$ .
~A1001

## Solution 3
Use constructive counting, as per above. WLOG, place the red blocks first. There are 11 ways to place them with distance 0, 9 ways them to place with distance 2, so on, so the way to place red blocks is $11+9+7+5+3+1=36$ . Then place any other block similarly, with $25$ ways (basic counting). You get then $6!^2$ ways to place the blocks evenly, and $12!/64$ ways to place the blocks in any way, so you get $\frac{16}{231}=247$ by simplifying.
-drag00n

## Solution 4
We can divide the $12$ positions into odd and even positions. Each color needs one block in an odd position and one block in an even position.
WLOG, we place the first block of the first pair into an odd position. This leaves $6$ even positions out of the $11$ remaining positions for the second block of the first pair. This results in a probability of $\frac{6}{11}$ for the second block to fall into an even position.
We can now place the first block of the second pair into another odd position, leaving $5$ even positions out of the $9$ remaining positions for the second block of the second pair.
Continuing this pattern for the other $4$ pairs results in the product $\frac{6\cdot5\cdot4\cdot3\cdot2\cdot1}{11\cdot9\cdot7\cdot5\cdot3\cdot1}=\frac{16}{231}$ . Thus, our answer is $16+231=\boxed{247}$ .
~Zhixing

## Solution 5
There are a total of $\frac{12!}{(2!)^{6}}$ ways to arrange the blocks because there are $12!$ total ways to arrange the blocks but we're overcounting $2!$ ways for each of the $6$ blocks. Now, to better visualize how we can arrange these blocks, consider the first slot. There are $6$ colors to choose from. WLOG, say it's red. Now, we can easily see that the next and last red block can be put into a total of 6 slots to make sure that the number of slots between the first slot and the next slot is even. To better visualize this, I have drawn a chart type figure:
RR_ _ _ _ _ _ _ _ _ _ R _ _ R _ _ _ _ _ _ _ _ . . . From this, you can get the idea. Counting up all these cases, it is obvious that there are $6$ ways to put the next and last red block. We continue by placing the next block into the next open slot. There are $5$ ways to choose the next color and similarly, only $5$ ways to put the next and last colored block to maintain an even number of slots. We get the idea. It seems that there are $(6!)^{2}$ ways to put the blocks. We compute $\frac{(6!)^{2} \cdot (2!)^{6}}{12!} = \frac{16}{231}$ . This yields an answer of $16 + 231 = \boxed{247}$ .
~ilikemath247365

## Video Solution (Mathematical Dexterity)
https://www.youtube.com/watch?v=dkoF7StwtrM

## Video Solution (Power of Logic)
https://youtu.be/AF6TOG7MSwA
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .