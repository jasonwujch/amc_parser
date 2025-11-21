# 2017 AIME II Problem 9

## Problem

A special deck of cards contains $49$ cards, each labeled with a number from $1$ to $7$ and colored with one of seven colors. Each number-color combination appears on exactly one card. Sharon will select a set of eight cards from the deck at random. Given that she gets at least one card of each color and at least one card with each number, the probability that Sharon can discard one of her cards and $\textit{still}$ have at least one card of each color and at least one card with each number is $\frac{p}{q}$ , where $p$ and $q$ are relatively prime positive integers. Find $p+q$ .

## Solution 1
Without loss of generality, assume that the $8$ numbers on Sharon's cards are $1$ , $1$ , $2$ , $3$ , $4$ , $5$ , $6$ , and $7$ , in that order, and assume the $8$ colors are red, red, and six different arbitrary colors. There are ${8\choose2}-1$ ways of assigning the two red cards to the $8$ numbers; we subtract $1$ because we cannot assign the two reds to the two $1$ 's. In order for Sharon to be able to remove at least one card and still have at least one card of each color, one of the reds have to be assigned with one of the $1$ s. The number of ways for this to happen is $2 \cdot 6 = 12$ (the first card she draws has to be a $1$ (2 choices), while the second card can be any card but the remaining card with a $1$ (6 choices)). Each of these assignments is equally likely, so desired probability is $\frac{12}{{8\choose2}-1}=\frac{4}{9} \implies 4 + 9 = 13 = \boxed{013}$ .

## Solution 2
First note that out of the $8$ selected cards, one pair of cards have to share the same number and another pair of cards have to share the same color. Now, these $2$ pairs of cards can't be the same or else there will be $2$ cards which are completely same. Then, WLOG let the numbers be $1,1,2,3,4,5,6,$ and $7$ and the colors be $a,a,b,c,d,e,f,$ and $g$ . We therefore obtain only $2$ cases:
Case One: $1a,1b,2a,3c,4d,5e,6f,$ and $7g$ In this case, we can discard $1a$ . There are $2*6=12$ situations in this case.
Case Two: $1b,1c,2a,3a,4d,5e,6f,$ and $7g$ In this case, we can't discard. There are $\dbinom{6}{2}=15$ situations in this case.
So the probability is $\frac{12}{12+15}=\frac{4}{9}$ , giving us the answer of $4+9=\boxed{013}$ .

## Solution 3
There are $7!$ ways to choose a set of 7 cards that have all the numbers from 1-7 and all 7 colors. There are then $42$ cards remaining. Thus, there are $7!(42)$ desired sets.
Now, the next thing to find is the number of ways to choose 8 cards where there is not a set of 7 such cards. In this case, one color must have 2 cards and one number must have 2 cards, and they can't be the same number/color card. The number of ways to pick this is equal to a multiplication of $\binom{7}{2}$ ways to pick 2 numbers, $7$ colors to assign them to, $\binom{6}{2}$ ways to pick 2 nonchosen colors, $5$ ways to pick a number to assign them to, and $4!$ ways to assign the rest.
Thus, the answer is $\frac{7!(42)}{7!(42) + 21(15)(7)(5!)}$ . Dividing out $5!$ yields $\frac{42(42)}{42(42) + 21(15)(7)}$ which is equal to $\frac{2(42)}{2(42) + 15(7)}$ which is equal to $\frac{12}{12 + 15}$ which is equal to $\frac{4}{9}$ giving a final answer of $\boxed{013}$ .

## Solution 4
We can rewrite the problem as "What is the probability that, given 8 cards with numbers a, b, c, d, e, f, g, g and some assortment of seven colors A, B, C, D, E, F, G, G where G is repeated, one of the cards is Gg?" Note that this is a valid restatement because Sharon has to have two of one number and two of one color. She needs to be able to take away one of the cards with the duplicate number, but this also has to have the duplicate color. There are two cases.
Case I: One of the cards is Gg. This implies that the other card with color G can be placed in $6$ ways, and the rest of the colors can be paired with cards in $6!$ ways.
Case II: None of the cards are Gg. This implies that the cards with color G can be chosen in $\dbinom{6}{2}=15$ ways, and the rest of the colors can be paired with cards in $\frac{6!}{2}$ ways, with the divide by 2 because of the double-g.
Note that there is no case with Gg, Gg because all 49 cards are unique!
Therefore our answer is $\frac{6\times6!}{\frac{15}{2}\times6! + 6\times6!}=\frac{4}{9}$ , so $\boxed{013}$ .

## Solution 5
We count the two entities: The number of sets of eight cards that contain all seven numbers and all seven colors; and The number of sets of eight cards that contain all seven numbers and colors, and one card can be removed and the property still holds.
For the first: It is equivalent to counting: How many ways can (colors) $A, A, B, C, D, E, F, G$ be matched to (numbers) $1, 1, 2, 3, 4, 5, 6, 7$ such that the two $A's$ cannot both be matched to the two ones. (This would mean we've chosen two identical cards from the deck, both with color $A$ and number one.) We consider two cases:
1) Neither $A$ is matched with a one. Then there are $\binom{6}{2}$ ways to choose which two numbers are matched with the $A's,$ and $6! / 2!$ ways to order the remaining numbers. (There are two one's, so we divide by two.)
2) One of the $A$ 's is matched with a one. There are $6 \cdot 6!$ ways to arrange the remaining color
Since there are seven ways to choose the extra color and likewise for the extra number, we have in total $7 \cdot 7 \cdot \left( 6C2 \cdot \frac{6!}{2!} + 6 \cdot 6! \right)$ ways to choose eight cards satisfying the first condition.
For the second: View the cards as rooks on a seven by seven chess board. Seven cards that contain all colors and numbers is can be represented as placing seven rooks on the board so that no two rooks are attacking each other. There are $7!$ ways to do this. For each arrangement, we can choose any of the other 42 positions on the board (cards) to add an extra rook. Thus, there are $7! \cdot 42$ good sets of eight cards. Note that we are not overcounting.
Thus, the probability of getting a good set given the first condition is $\frac{ 7! \cdot 42 }{ 7 \cdot 7 \cdot \left( 6C2 \cdot \frac{6!}{2!} + 6 \cdot 6! \right) } = \frac{4}{9},$ and the answer is $\boxed{013}.$

## Solution 6
We recast this problem to coloring 8 cells in a 7x7 grid, such that each row and column has at least one colored cell. If a cell in row a and column b is colored, that means we drew a card with color a and number b.
By pigeonhole principle, there exists a row that has 2 colored cells, and intuitively, that row is unique. There also exists a column with 2 colored cells. Call the unique row, "Row A", and Call the unique column, "Column B".
If we are able to remove a card so that we still have a card of each color and number, that means, we can erase a cell, so each row still has at least one colored cell, and so does each column. If we erase a cell not in Row A, then the erased cell's row will be empty. If we erase a cell not in Column B, the erased cell's column will be empty. Thus the cell that we erase must be in both Row A and Column B. There is only one cell in both Row A and Column B, and thus that cell must be colored.
We first count the number of successful outcomes. We must chose which row to be "Row A", and which column to be "Column B". There are 7 ways to chose "Row A", and 7 ways to chose "Column B". Because of the logic used above, the intersection of Row A and Column B must be colored. However, Row A needs to have 2 colored cells. There are 6 other uncolored cells to chose from. Similarly, there are 6 uncolored cells in Column B.
Note that we can ignore all the rows and columns that contain colored cells. This is because Row A already contains 2 colored cells, and thus we can't color any more cells in Row A, similarly for Column B. The other row that contains a colored cell is not Row A, so it can only contain 1 colored cell, which it has, thus we can't color anymore cells in it. Similarly for the other column.
We can actually remove these rows/columns. This leaves a 5x5 grid, full of uncolored cells. Each row can have 1 cell, and so can each column. We count the # of colorings from the perspective of the rows. We look at the first row, it has 5 choices. We can look at the 2nd row, it has 4 choices, as it's selected cell can't occupy the same column. We continue down the line, and see there are $5! = 120$ ways to color.
Thus, the # of successful outcomes is $5! \cdot 6 \cdot 6 \cdot 7 \cdot 7$ .
We can then count the # of possible outcomes.
We can count the # of unsuccessful outcomes. We select "Row A" and "Column B" as usual, with $7 \cdot 7$ ways. We don't color the intersection, so we have to color 2 cells in each. There are 6 other cells that can be colored in each, so we have ${6 \choose 2} = 15$ ways to color each. Then, we can get rid of rows and columns using the method above and we are left with a 4x4 grid. There are $4! = 24$ ways to color.
Thus, the # of unsuccessful outcomes is $4! \cdot 15 \cdot 15 \cdot 7 \cdot 7$ .
After some calculation, we get $\frac{successful}{possible} = \frac{successful}{successful+unsuccessful} = \frac{5! \cdot 6^2 \cdot 7^2}{7^2 \cdot(5! \cdot 6^2 + 4! \cdot 15^2} = \frac{5! \cdot 6^2}{5! \cdot 6^2 +4! \cdot 15^2} = \frac{5 \cdot 6^2}{5 \cdot 6^2 + 15^2} = \frac{180}{180+225} = \frac{4}{9} \implies 4+9 = \boxed{13}$
-Alexlikemath

## Solution 7 (Official MAA)
In a set of eight cards that includes every color and every number, there will be exactly one repeated number and exactly one repeated color. If Sharon selects a set that includes the card with that number and color, Sharon can discard it. If the set does not include that card, Sharon cannot discard any card. In the former case, there are $7!$ ways to choose one card of each number and color, and then $42$ ways to choose the "extra" card. The total is $7!\cdot 42$ . In the latter case, there are $7$ ways to choose which number is repeated, and $\binom{7}{2} = 21$ ways to choose which two cards of that number are used. There are then $5$ ways to choose which color is repeated, and $\binom{6}{2} = 15$ ways to choose which cards of that color are used. There now remain four unused colors and four unused numbers, and there are $4! = 24$ ways to choose from those. The total is $7 \cdot 21 \cdot 5 \cdot 15 \cdot 24$ . The probability that a given set is of the first type is therefore $\frac{7! \cdot 42}{7! \cdot 42+7 \cdot 21 \cdot 5 \cdot 15 \cdot 24} = \frac{4}{9}.$ The requested sum is $4 + 9 = 13$ .

## Solution 8
WLOG let the colors be $R, R, O, Y, G, B, I, V$ and let the numbers be $1, 1, 2, 3, 4, 5, 6, 7$ . Now call a color or number $safe$ is there is at least two cards in that category. In this case, the color red is $safe$ and the number $1$ is safe because we have two of each.
Now notice that a card can be removed if and only if both its color AND number are $safe$ , since even if we remove it we will have one of each category. Therefore, we must have a $R1$ .
For this probability, we will first count the total ways to assign the cards. Treating each color and number as distinct, we have $8!$ ways. However, we cannot have two red ones, so we must subtract $2 * 6!$ cases from our total.
Meanwhile, to count the successful outcomes, one of the ones must be red. We have $2$ choices for the one, and $2$ choices for the red. Then, the other one has $6$ colors, and there are $6!$ ways to color the rest of the numbers.
Diving and simplifying, we have $\frac{2*2*6*6!}{8!-2*6!} = \frac{4}{9} \implies 4+9 = \boxed{13}$ .
~xHypotenuse
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .