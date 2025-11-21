# 2017 AIME II Problem 5

## Problem

A set contains four numbers. The six pairwise sums of distinct elements of the set, in no particular order, are $189$ , $320$ , $287$ , $234$ , $x$ , and $y$ . Find the greatest possible value of $x+y$ .

## Solution 1
Let these four numbers be $a$ , $b$ , $c$ , and $d$ , where $a>b>c>d$ . $x+y$ needs to be maximized, so let $x=a+b$ and $y=a+c$ because these are the two largest pairwise sums. Now $x+y=2a+b+c$ needs to be maximized. Notice that $2a+b+c=3(a+b+c+d)-(a+2b+2c+3d)=3((a+c)+(b+d))-((a+d)+(b+c)+(b+d)+(c+d))$ . No matter how the numbers $189$ , $320$ , $287$ , and $234$ are assigned to the values $a+d$ , $b+c$ , $b+d$ , and $c+d$ , the sum $(a+d)+(b+c)+(b+d)+(c+d)$ will always be $189+320+287+234$ . Therefore we need to maximize $3((a+c)+(b+d))-(189+320+287+234)$ . The maximum value of $(a+c)+(b+d)$ is achieved when we let $a+c$ and $b+d$ be $320$ and $287$ because these are the two largest pairwise sums besides $x$ and $y$ . Therefore, the maximum possible value of $x+y=3(320+287)-(189+320+287+234)=\boxed{791}$ .

## Solution 2
Let the four numbers be $a$ , $b$ , $c$ , and $d$ , in no particular order. Adding the pairwise sums, we have $3a+3b+3c+3d=1030+x+y$ , so $x+y=3(a+b+c+d)-1030$ . Since we want to maximize $x+y$ , we must maximize $a+b+c+d$ .
Of the four sums whose values we know, there must be two sums that add to $a+b+c+d$ . To maximize this value, we choose the highest pairwise sums, $320$ and $287$ . Therefore, $a+b+c+d=320+287=607$ .
We can substitute this value into the earlier equation to find that $x+y=3(607)-1030=1821-1030=\boxed{791}$ .

## Solution 3
Note that if $a>b>c>d$ are the elements of the set, then $a+b>a+c>b+c,a+d>b+d>c+d$ . Thus we can assign $a+b=x,a+c=y,b+c=320,a+d=287,b+d=234,c+d=189$ . Then $x+y=(a+b)+(a+c)=\left[(a+d)-(b+d)+(b+c)\right]+\left[(a+d)-(c+d)+(b+c)\right]=\boxed{791}$ .

## Solution 4 (Short Casework)
There are two cases we can consider. Let the elements of our set be denoted $a,b,c,d$ , and say that the largest sums $x$ and $y$ will be consisted of $b+d$ and $c+d$ . Thus, we want to maximize $b+c+2d$ , which means $d$ has to be as large as possible, and $a$ has to be as small as possible to maximize $b$ and $c$ . So, the two cases we look at are:
Case 1:
\[a+d = 287\] \[b+c = 320\] \[a+b = 234\] \[a+c = 189\]
Case 2:
\[a+d = 320\] \[b+c = 189\] \[a+b = 234\] \[a+c = 287\]
Note we have determined these cases by maximizing the value of $a+d$ determined by our previous conditions. So, the answers for each ( after some simple substitution ) will be:
Case 1:
\[(a,b,c,d) = (\frac{103}{2},\frac{365}{2},\frac{275}{2},\frac{471}{2})\]
Case 2:
\[(a,b,c,d) = (166,68,121,154)\]
See the first case has our largest $d$ , so our answer will be $471+\frac{640}{2} = \boxed{791}$
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .