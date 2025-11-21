# 2019 AIME II Problem 5

## Problem

Four ambassadors and one advisor for each of them are to be seated at a round table with $12$ chairs numbered in order $1$ to $12$ . Each ambassador must sit in an even-numbered chair. Each advisor must sit in a chair adjacent to his or her ambassador. There are $N$ ways for the $8$ people to be seated at the table under these conditions. Find the remainder when $N$ is divided by $1000$ .

## Solution 0
Suppose first that the chairs weren't numbered, and rotation doesn't matter. Then if we let the ambassador-advisor pairs act as a single person, we essentially want to pick $4$ seats out of $8$ seats, and fixing one pair gives $7 \cdot 6 \cdot 5$ ways. However, now we want to number the seats, in which there are $12$ possibilities (for some pair of people, we choose the order and then we choose which even spot the ambassador sits in, giving $2\cdot 6.$ ) However, the order of the other pairs is then uniquely determined, so this method works, giving us $7 \cdot 6 \cdot 5 \cdot 12 = 2520$ ways. We are asked to find the remainder when $\textit{N}$ is divided by $1000$ , which is $\boxed{520}$ . ~Maximilian113 ~Minor edits by Hiphopfrog1

## Solution 1
Let us first consider the $4$ ambassadors and the $6$ even-numbered chairs. If we consider only their relative positions, they can sit in one of $3$ distinct ways: Such that the $2$ empty even-numbered chairs are adjacent, such that they are separated by one occupied even-numbered chair, and such that they are opposite each other. For each way, there are $4!=24$ ways to assign the $4$ ambassadors to the $4$ selected seats.
In the first way, there are $6$ distinct orientations. The $4$ advisors can be placed in any of the $5$ odd-numbered chairs adjacent to the ambassadors, and for each placement, there is exactly one way to assign them to the ambassadors. This means that there are $24\cdot6\cdot\binom{5}{4}=720$ total seating arrangements for this way.
In the second way, there are $6$ distinct orientations. $3$ advisors can be placed in any of the $4$ chairs adjacent to the "chunk" of $3$ ambassadors, and $1$ advisor can be placed in either of the $2$ chairs adjacent to the "lonely" ambassador. Once again, for each placement, there is exactly one way to assign the advisors to the ambassadors. This means that there are $24\cdot6\cdot\binom{4}{3}\cdot\binom{2}{1}=1152$ total seating arrangements for this way.
In the third way, there are $3$ distinct orientations. For both "chunks" of $2$ ambassadors, $2$ advisors can be placed in any of the $3$ chairs adjacent to them, and once again, there is exactly one way to assign them for each placement. This means that there are $24\cdot3\cdot\binom{3}{2}\cdot\binom{3}{2}=648$ total seating arrangements for this way.
Totalling up the arrangements, there are $720+1152+648=2520$ total ways to seat the people, and the remainder when $2520$ is divided by $1000$ is $\boxed{520}$ . ~ emerald_block

## Solution 2
In the diagram, the seats are numbered 1...12. Rather than picking seats for each person, however, each ambassador/assistant team picks a gap between the seats (A...L) and the ambassador sits in the even seat while the assistant sits in the odd seat. For example, if team 1 picks gap C then Ambassador 1 will sit in seat 2 while assistant 1 will sit in seat 3. No two teams can pick adjacent gaps. For example, if team 1 chooses gap C then team 2 cannot pick gaps B,C or D. In the diagram, the teams have picked gaps C, F, H and J. Note that the gap-gaps - distances between the chosen gaps - (in the diagram, 2, 1, 1, 4) must sum to 8. So, to get the number of seatings, we:
1. Choose a gap for team 1 ( $12$ options)
1. Choose 3 other gaps around the table with positive gap-gaps. Note that because the sum of the distances between the gaps must be equal to $8,$ we create a bijection - to partition the 8 balls into 4 urns, with each urn having a positive number of balls. There is the same as partitioning 4 with 4 non-negative integers, and using stars-and-bars, this is $\dbinom{4+4-1}{4-1}=\dbinom{7}{3}=35$
1. Place the other 3 teams in the chosen gaps ( $6$ permutations)
So, the total is $12\cdot35\cdot6=2520$ .
Therefore, the remainder is $\boxed{520}$ .

## Solution 3 (PIE)
There are $6\cdot5\cdot4\cdot3\cdot2^4$ (placing the ambassadors and then choosing the locations of the advisors) total ways to let everyone sit. However, this may lead to advisors sitting in the same chair, leading to awkward situations. So we find how many ways this happens. There are $\dbinom{4}{2} = 6$ ways to choose which advisors end up sitting together, times $6\cdot2=12$ ways to find neighboring even seats (order matters), and for the other two ambassadors, there are $\dbinom{4}{2} \cdot 2 = 12$ ways to sit and 4 ways for their advisors to sit. This results in $6\cdot12\cdot12\cdot4=3456$ ways for this to happen. However, we overcounted the case when all four of the advisors run out of room to sit, where there are $\frac{6\cdot3}{2!}=9$ to choose the places the ambassadors sit and 4! ways to arrange the ambassadors. $9\cdot4!=216$ ways to happen. So the answer is $5760 - 3456 + 216 = 2520$ , which has a remainder of $\boxed{520}$ when divided by 1000.
~minor $LaTeX$ fixes by virjoy2001

## Solution 4
We see that for every 2 adjacent spots on the table, there is exactly one way for an ambassador and his or her partner to sit. There are 2 cases:
1. There is an ambassador at the 12th chair and his or her partner at the 1st chair
1. There is no pair that has their chairs numbered as 12 and 1
For the first case, there are 3 pairs and 4 empty spaces, which results in $\frac{7!}{3!4!} = 35$ ways to arrange the pairs.
For the second case, there are 4 pairs and 4 empty spaces, which results in $\frac{8!}{4!4!} = 70$ ways to arrange the pairs.
Finally, we have to assign ambassadors and their advisors to the pairs, which has $4!=24$ ways, so $N = (35+70)\cdot 24 = 2520$ , or $\boxed{520}$ ~PenguinMoosey

## Solution 5 (Lots of diagrams)
Let's begin with a simpler problem. We start with n ambassador chairs in a row and n+1 advisor chairs between them. As before, each advisor has to sit next to his/her ambassador. In the diagram, a black spot represents an ambassador, a blue ring represents an empty advisor seat, and a black dot on top of a blue dot represents an advisor. There are exactly (n+1)! solutions in this case as represented by the diagram. First, let's seat the ambassadors in their positions (n! ways). In the diagram, the first solution is that the advisors all sit an the left of their respective ambassadors. Then, we can slide the rightmost advisor over his/her ambassador to make a new solution. Then, we can do the same with the other advisor next to the empty seat. We can continue this process until all of the advisors sit an the right of their respective ambassadors. In total, there are n!(n+1) = (n+1)! ways.
Now, we are ready to tackle the original problem. If we forget about the numbers and the uniqueness of people, we will have the three configurations shown above. In the first configuration, there is a single red blob of four ambassadors. Let's stretch them out onto a line. Now, it's the same situation as the simpler problem and there are (4+1)! = 5! = 120 ways to seat the people. However, we need to multiply that by 6 because there are 6 orientations. Therefore, we have 720 outcomes for this case. In the second configuration, there is a orange blob and a green blob, each of the case n=2, resulting in (2+1)! * (2+1)! which equals 36. Multiplying the number of orientations, 3, we arrive at 108. Wait! We need to multiply by 6 to account for the many ways that we can choose 2 of the ambassadors to be in the orange blob. Therefore, we have 648 outcomes. Last but not least, we have the final configuration which is a blob of 1 and a blob of 3. Applying the formula results in (1+1)! * (3+1)! which evaluates to 48. Then, we multiply by 4, the number of ways to choose the blobs, and 6, the number of orientations. Our result is 1152. Finally, adding the numbers, we get 2520 and taking mod 1000, we get 520.
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .