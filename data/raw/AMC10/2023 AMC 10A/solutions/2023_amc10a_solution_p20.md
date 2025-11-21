# 2023 AMC 10A Problem 20

## Problem

Each square in a $3\times3$ grid of squares is colored red, white, blue, or green so that every $2\times2$ square contains one square of each color. One such coloring is shown on the right below. How many different colorings are possible?

[asy] unitsize(0.5cm, 0.5cm); draw((0,0)--(9,0)--(9,9)--(0,9)--cycle); draw((0,3)--(9,3)); draw((0,6)--(9,6)); draw((3,0)--(3,9)); draw((6,0)--(6,9)); draw((18,0)--(27,0)--(27,9)--(18,9)--cycle); draw((18,3)--(27,3)); draw((18,6)--(27,6)); draw((21,0)--(21,9)); draw((24,0)--(24,9)); label("R", (19.5,1.5)); label("B", (22.5,1.5)); label("R", (25.5,1.5)); label("G", (19.5,4.5)); label("W", (22.5,4.5)); label("G", (25.5,4.5)); label("B", (19.5,7.5)); label("R", (22.5,7.5)); label("B", (25.5,7.5)); [/asy]

$\textbf{(A) }24\qquad\textbf{(B) }48\qquad\textbf{(C) }60\qquad\textbf{(D) }72\qquad\textbf{(E) }96$

## Solution 1
Let a "tile" denote a \(1 \times 1\) square, and a "square" refer to a \(2 \times 2\) square.
We have \(4! = 24\) possible ways to fill out the top-left square. Next, we fill out the bottom-right corner tile. In the bottom-right square, one corner is already filled (the central tile) from our initial coloring), so we have 3 color options remaining for this.
Now considering the remaining tiles, all of these only have one way to be filled (Try it yourself if you don’t believe).
For example, the right tile of the middle row is part of two squares: the top-right and the bottom-right. Among these squares, 3 colors have already been used, leaving us with only 1 remaining option. Similarly, every other remaining square has only one available option for coloring.
Thus, the total number of ways is \(3 \times 4! = \boxed{\textbf{(D) }72}\).
~ jlcong
~ stevehan
~ Technodoggo
A quick version of this method is used when you use for example B as the top left corner block. You can see that $B$ in the top left corner has $6$ possible ways. Now, see that there are $3$ possible corners for a center cell and there are $4$ possible center cells. We get $6$ times $4$ times $3 = D$ , the answer is \( \boxed{\textbf{(D) }72}\). (I'm not very good at using latex) ~breakingbread ~latex done by pungent_muskrat

## Solution 2 (Circular Counting)
Recall the circular gap theorem \[C_n(A) = \frac{n}{k} \binom{n-k-1}{k-1}.\] We have nine slots and a maximum of 4 colors cannot be next to one another (if you aren't convinced, try plugging in any number greater than 4 and see what happens to the formula; it becomes invalid, and is therefore 0). Therefore, we take the cases $n=9$ and $k \in \{1,2,3,4\}$ .
Case 1: $k \in \{1\}$
This is simply just $\frac{9}{1} \binom{9-1-1}{1-1} = 9$ ways.
Case 2: $k \in \{2\}$
This is just $\frac{9}{2} \binom{9-2-1}{2-1} = \frac{9}{2} \cdot 6 = 27$ ways.
Case 3: $k \in \{3\}$
This is $\frac{9}{3} \binom{9-3-1}{3-1} = 3 \cdot 10 = 30$ ways.
Case 4: $k \in \{4\}$
This is $\frac{9}{4} \binom{9-4-1}{4-1} = \frac{9}{4} \cdot 4 = 9$ ways.
The number of ways to arrange the colors such that no same color is next to each other at least once is $9+27+30+9 = 75$ .
However, it is clear that every color (excluding the center) is only used a maximum of three times, so we apply the formula for $k \in \{1,2,3\}$ and $n = 3$ (three total slots it can go to). Notice that $k \in \{2,3\}$ is just 0, so therefore we just consider $k \in \{1\}$ and get \[\frac{3}{1} \binom{3-1-1}{1-1} = 3\]
Our final answer is just $75 - 3 =$ $\boxed{\textbf{(D) }72}$
~Pinotation

## Solution 3
[asy] unitsize(0.5cm, 0.5cm); draw((0,0)--(9,0)--(9,9)--(0,9)--cycle); draw((0,3)--(9,3)); draw((0,6)--(9,6)); draw((3,0)--(3,9)); draw((6,0)--(6,9)); label("R", (1.5,1.5)); label("B", (4.5,1.5)); label("R", (7.5,1.5)); label("G", (1.5,4.5)); label("W", (4.5,4.5)); label("G", (7.5,4.5)); label("B", (1.5,7.5)); label("R", (4.5,7.5)); label("B", (7.5,7.5)); draw((18,0)--(27,0)--(27,9)--(18,9)--cycle); draw((18,3)--(27,3)); draw((18,6)--(27,6)); draw((21,0)--(21,9)); draw((24,0)--(24,9)); label("R", (19.5,1.5)); label("B", (22.5,1.5)); label("R", (25.5,1.5)); label("G", (19.5,4.5)); label("W", (22.5,4.5)); label("G", (25.5,4.5)); label("R", (19.5,7.5)); label("B", (22.5,7.5)); label("R", (25.5,7.5)); [/asy] We can split this problem into $2$ cases as shown in solution 1. We can swap a set of equal colors for another set of equal colors to create a new square.
Square 1: The first square can be rotated to create another square so we have to multiply the number of arrangements by $2$ . We have $4! = 24$ arrangements without rotating and $24\cdot 2 = 48$ arrangements in total for the first square.
Square 2: There are $4! = 24$ ways to arrange the colors.
In total, we have $48 + 24 = \boxed{\textbf{(D) }72}$ arrangements.
~ South (LaTeX and Solution) Edit by: Mismatchedcubing/Andrew_Lu

## Solution 4
Let’s call the top-right corner color A, the top-middle color B, the top-right color C, and so on, with color D being the middle row, and right corner square, and color G being the bottom-left square’s color.
WLOG A=Red, B=White, D=Blue, and E=Green. We will now consider squares C and F’s colors. Case 1 : C=Red and F=Blue
In this case, we get that G and H have to be Red and White in some order, and the same for H and I. We can color this in 2 ways. Case 2 : C=Blue and F=Red
In this case, one of G and H needs to be White and Red, and H and I needs to be White and Blue. There is 1 way to color this. In total, we get $24*(2+1)=72$ ways to color the grid. $\boxed{\textbf{(D) }72}$ .
-paixiao
-jkim0656 (minor formatting and latex)

## Solution 5
We will choose colors step-by-step:
1. There are $4$ ways to choose a color in the center.
2. Then we select any corner and there would be $3$ ways to choose a color as we can't use the same color as the one in the center.
3. Consider the $2\times 2$ square that contains the center and the corner we have selected. For the other $2$ squares, there are $2$ ways to choose colors.
4. Now, consider how many configurations it makes sense to construct the $2\times 2$ square opposite to the corner we have selected using the $2$ other $2\times 2$ squares, and we get $3$ configurations.
Finally, the answer is $4 \cdot 3 \cdot 2 \cdot 3 = \boxed{\textbf{(D) }72}$
~jjaamm

## Solution 6 (possibly bad)
[asy] unitsize(0.5cm, 0.5cm); draw((0,0)--(9,0)--(9,9)--(0,9)--cycle); draw((0,3)--(9,3)); draw((0,6)--(9,6)); draw((3,0)--(3,9)); draw((6,0)--(6,9)); label("2", (1.5,1.5)); label("1", (4.5,1.5)); label("1", (7.5,1.5)); label("2", (1.5,4.5)); label("3", (4.5,4.5)); label("1", (7.5,4.5)); label("3", (1.5,7.5)); label("1", (4.5,7.5)); label("2", (7.5,7.5)); [/asy]
Note that we could fill the 3 by 3 square with numbers of choices, rather than letters or color names. The top-left corner receives a 3 because there are 3 total choices to choose from: R, G and B. The squares bordering them has values of 2 and 1, regardless of order. 2 indicates that the small square can have any color excluding the one existing color, 1 indicates the remaining color of the 2 by 2 square. Finally, the middle square receives 3, since the first 2 by 2 square has RGB already, and it does not matter what color it has. Moving onto the next 2 by 2 square, we see that there are already 2 decided colors, so the other squares must be 2 and 1, again, regardless of the order. The same applys to the third 2 by 2 square, and finally the last square has the value of one, as it is the only square left. Multiplying the numbers, $2\times2\times2\times3\time3\times3$ = $\boxed{\textbf{(D) }72}$ (Similar to Solution 1)
-MEZE_RUN why are there only 3 choices for the top right corner? you havent placed any colors yet so there should be 4 choices which would make your answer incorrect

## Solution 7
[asy] unitsize(0.5cm, 0.5cm); draw((0,0)--(9,0)--(9,9)--(0,9)--cycle); draw((0,3)--(9,3)); draw((0,6)--(9,6)); draw((3,0)--(3,9)); draw((6,0)--(6,9)); label("G", (1.5,1.5)); label("H", (4.5,1.5)); label("I", (7.5,1.5)); label("D", (1.5,4.5)); label("E", (4.5,4.5)); label("F", (7.5,4.5)); label("A", (1.5,7.5)); label("B", (4.5,7.5)); label("C", (7.5,7.5)); [/asy]
Case 1. Cell $B$ and cell $H$ have the same color. The middle one cell $E$ has $4$ choices, cell $B$ has $3$ choices, then cell $E$ has $2$ choices and cell $F$ has $2$ choices, this gives $4\cdot 3\cdot 2\cdot 2=48$ ways.
Case 2. Cell $B$ and cell $H$ have different colors. The middle one cell $E$ has $4$ choices, cell $B$ has $3$ choices, cell $H$ has $2$ choices, then cell $D$ and $F$ each can only have one choice (different from $B,E,H).$ This gives $4\cdot 3\cdot 2=24$ ways.
The answer is thus $48+24=72,$ corresponding to answer choice $\boxed{D}$

## Solution 8
Consider Cases based on the color of the top left and bottom left square.
Case 1: The top left and bottom left squares are the same:
We have $4$ ways to assign the top and bottom squares, lets say it is red. Once that is done, we can assign the center square in 3 ways, since it can be anything except the color of the top and bottom squares (Lets say it is white). We can then assign the bottom middle square any color except the center and bottom left square, so there is two ways to do that (Lets say its blue). From there, you can assign the other squares in the first two columns in only one way (Top middle = Blue, Middle Left = Green). Then, the right column can go in one of two ways: Green, Red, Green, or Red, Green, Red, for a total of two ways. Taking this altogether gives $4 * 3 * 2 * 2 = 48$
Case 2: The top left and bottom left squares are different:
We have $4 * 3 = 12$ ways to assign the top and bottom squares, let them be Red and Green respectively. Then the square between them can be assigned in two ways. We realize how the middle square can only be filled in one way (White, because it can't be Blue, Green, or Red). From there, the entire second column can only be filled in one way (From top to bottom, it is Green, White, Red). The same story goes for the last column, it can only be filled in one way (From top to bottom it is Red, Blue, Green). That gives $4 * 3 * 2 = 24$ ways.
Thus, the answer is $48+24=72,$ which is answer choice $\boxed{\textbf{(D) }72}$ ~latex work done by pungent_muskrat$

## Solution 9
We can first choose the center square. There are $4$ possibilities: Red, Blue, Green, or White. WLOG, lets assume that the center is white. Next, there are $3$ possibilities for the top middle square: Red, Blue, or Green. WLOG, lets assume that it is Red. We now have two cases:
CASE $1$ : The first and last column are in the form BG... and BG... or GB... and GB...: We can see that there are two possibilities for this case: the bottom row is RBR or BRB. The total number of ways for this case is $4\cdot3\cdot2\cdot2$ . CASE $2$ : The first and last column are in the form BG... and GB... or GB... and BG... We can now see that the bottom middle cell HAS to be a red (if it isn't, either the bottom left or bottom right 2x2 squares will have duplicate colors). After we choose the bottom middle, the rest of the cells are automatically chosen. Thus, the total number of ways for this case is $4\cdot3\cdot2\cdot1$ . Thus, our final answer is the sum of case 1 and case 2, which is $48 + 24 = 72$ , or $\boxed{\textbf{(D) }72}$ . ~ Irfans123

## Video Solution by Little Fermat
https://youtu.be/h2Pf2hvF1wE?si=TCQJ2UEm-sB8rVjZ&t=4487 ~little-fermat

## Video Solution by Math-X (First fully understand the problem!!!)
https://youtu.be/GP-DYudh5qU?si=YXUPq1RZv92E0d8H&t=7113
~Math-X

## Video Solution by MegaMath
https://www.youtube.com/watch?v=AhqOj8502Dc&t=65s
~megahertz13

## Video Solution by Power Solve (easy to digest!)
https://youtu.be/0_eRTysDEsI

## Video Solution by OmegaLearn
https://youtu.be/Zrqy5yGYlvQ

## Video Solution by CosineMethod [🔥Fast and Easy🔥]
https://www.youtube.com/watch?v=vlaZ5P8UZls

## Video Solution by Solve It (Simple)
https://www.youtube.com/watch?v=ke4ZOV4KA6Y

## Video Solution
https://youtu.be/8ki0D3m_mEo
~Steven Chen (Professor Chen Education Palace, www.professorchenedu.com)

## Video Solution by TheBeautyofMath
https://youtu.be/BDNsMEIzHF0
~IceMatrix
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .