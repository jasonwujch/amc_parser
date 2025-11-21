# 2018 AIME II Problem 1

## Problem

Points $A$ , $B$ , and $C$ lie in that order along a straight path where the distance from $A$ to $C$ is $1800$ meters. Ina runs twice as fast as Eve, and Paul runs twice as fast as Ina. The three runners start running at the same time with Ina starting at $A$ and running toward $C$ , Paul starting at $B$ and running toward $C$ , and Eve starting at $C$ and running toward $A$ . When Paul meets Eve, he turns around and runs toward $A$ . Paul and Ina both arrive at $B$ at the same time. Find the number of meters from $A$ to $B$ .

## Solution 1
We know that in the same amount of time given, Ina will run twice the distance of Eve, and Paul would run quadruple the distance of Eve. Let's consider the time it takes for Paul to meet Eve: Paul would've run 4 times the distance of Eve, which we can denote as $d$ . Thus, the distance between $B$ and $C$ is $4d+d=5d$ . In that given time, Ina would've run twice the distance $d$ , or $2d$ units.
Now, when Paul starts running back towards $A$ , the same amount of time would pass since he will meet Ina at his starting point. Thus, we know that he travels another $4d$ units and Ina travels another $2d$ units.
Therefore, drawing out the diagram, we find that $2d+2d+4d+d=9d=1800 \implies d=200$ , and distance between $A$ and $B$ is the distance Ina traveled, or $4d=4(200)=\boxed{800}$

## Solution 2
Let $x$ be the distance from $A$ to $B$ . Then the distance from $B$ to $C$ is $1800-x$ . Since Eve is the slowest, we can call her speed $v$ , so that Ina's speed is $2v$ and Paul's speed is $4v$ .
For Paul and Eve to meet, they must cover a total distance of $1800-x$ which takes them a time of $\frac{1800-x}{4v+v}$ . Paul must run the same distance back to $B$ , so his total time is $\frac{2(1800-x)}{5v}$ .
For Ina to reach $B$ , she must run a distance of $x$ at a speed of $2v$ , taking her a time of $\frac{x}{2v}$ .
Since Paul and Ina reach $B$ at the same time, we know that $\frac{2(1800-x)}{5v} = \frac{x}{2v}$ (notice that $v$ cancels out on both sides). Solving the equation gives $x = \boxed{800}$ .

## Video Solution by OmegaLearn
https://youtu.be/XixU0JZ5FLk?t=1355
~ pi_is_3.14
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .