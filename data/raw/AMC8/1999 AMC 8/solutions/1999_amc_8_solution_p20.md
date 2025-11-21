# 1999 AMC 8 Problem 20

## Problem

Figure 1 is called a "stack map." The numbers tell how many cubes are stacked in each position. Fig. 2 shows these cubes, and Fig. 3 shows the view of the stacked cubes as seen from the front.

Which of the following is the front view for the stack map in Fig. 4?

[asy] unitsize(24); draw((0,0)--(2,0)--(2,2)--(0,2)--cycle); draw((1,0)--(1,2)); draw((0,1)--(2,1)); draw((5,0)--(7,0)--(7,1)--(20/3,4/3)--(20/3,13/3)--(19/3,14/3)--(16/3,14/3)--(16/3,11/3)--(13/3,11/3)--(13/3,2/3)--cycle); draw((20/3,13/3)--(17/3,13/3)--(17/3,10/3)--(14/3,10/3)--(14/3,1/3)); draw((20/3,10/3)--(17/3,10/3)--(17/3,7/3)--(20/3,7/3)); draw((17/3,7/3)--(14/3,7/3)); draw((7,1)--(6,1)--(6,2)--(5,2)--(5,0)); draw((5,1)--(6,1)--(6,0)); draw((20/3,4/3)--(6,4/3)); draw((17/3,13/3)--(16/3,14/3)); draw((17/3,10/3)--(16/3,11/3)); draw((14/3,10/3)--(13/3,11/3)); draw((5,2)--(13/3,8/3)); draw((5,1)--(13/3,5/3)); draw((6,2)--(17/3,7/3)); draw((9,0)--(11,0)--(11,4)--(10,4)--(10,3)--(9,3)--cycle); draw((11,3)--(10,3)--(10,0)); draw((11,2)--(9,2)); draw((11,1)--(9,1)); draw((13,0)--(16,0)--(16,2)--(13,2)--cycle); draw((13,1)--(16,1)); draw((14,0)--(14,2)); draw((15,0)--(15,2)); label("Figure 1",(1,0),S); label("Figure 2",(17/3,0),S); label("Figure 3",(10,0),S); label("Figure 4",(14.5,0),S); label("$1$",(1.5,.2),N); label("$2$",(.5,.2),N); label("$3$",(.5,1.2),N); label("$4$",(1.5,1.2),N); label("$1$",(13.5,.2),N); label("$3$",(14.5,.2),N); label("$1$",(15.5,.2),N); label("$2$",(13.5,1.2),N); label("$2$",(14.5,1.2),N); label("$4$",(15.5,1.2),N); [/asy]

[asy] unitsize(18); draw((0,0)--(3,0)--(3,2)--(1,2)--(1,4)--(0,4)--cycle); draw((0,3)--(1,3)); draw((0,2)--(1,2)--(1,0)); draw((0,1)--(3,1)); draw((2,0)--(2,2)); draw((5,0)--(8,0)--(8,4)--(7,4)--(7,3)--(6,3)--(6,2)--(5,2)--cycle); draw((8,3)--(7,3)--(7,0)); draw((8,2)--(6,2)--(6,0)); draw((8,1)--(5,1)); draw((10,0)--(12,0)--(12,4)--(11,4)--(11,3)--(10,3)--cycle); draw((12,3)--(11,3)--(11,0)); draw((12,2)--(10,2)); draw((12,1)--(10,1)); draw((14,0)--(17,0)--(17,4)--(16,4)--(16,2)--(14,2)--cycle); draw((17,3)--(16,3)); draw((17,2)--(16,2)--(16,0)); draw((17,1)--(14,1)); draw((15,0)--(15,2)); draw((19,0)--(22,0)--(22,4)--(20,4)--(20,1)--(19,1)--cycle); draw((22,3)--(20,3)); draw((22,2)--(20,2)); draw((22,1)--(20,1)--(20,0)); draw((21,0)--(21,4)); label("(A)",(1.5,0),S); label("(B)",(6.5,0),S); label("(C)",(11,0),S); label("(D)",(15.5,0),S); label("(E)",(20.5,0),S); [/asy]

## Solution
The third view is a direct, head-on view of the cubes. Thus, you will only see the highest (or, in these cases, higher) tower in each up-down column. For figure $4$ :
The highest tower in the first up-down column is $2$ in the upper-left box.
The highest tower in the second up-down column is the $3$ in the lower-middle box.
The highest tower in the third up-down column is the $4$ in the upper-right box.
Thus, the head-on view of this tower should have $2$ boxes on the left, $3$ in the middle, and $4$ on the right.
Diagram $\boxed{B}$ shows this description.
As trivia, option C shows the stack from the point of view of an observer on the right, facing towards the left.

## Video Solution by CosineMethod [🔥Fast and Easy🔥]
https://www.youtube.com/watch?v=S4KVSEsQWeY
### See Also