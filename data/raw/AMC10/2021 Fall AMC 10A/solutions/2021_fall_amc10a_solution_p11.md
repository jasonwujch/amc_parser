# 2021 Fall AMC 10A Problem 11

## Problem

Emily sees a ship traveling at a constant speed along a straight section of a river. She walks parallel to the riverbank at a uniform rate faster than the ship. She counts $210$ equal steps walking from the back of the ship to the front. Walking in the opposite direction, she counts $42$ steps of the same size from the front of the ship to the back. In terms of Emily's equal steps, what is the length of the ship?

$\textbf{(A) }70\qquad\textbf{(B) }84\qquad\textbf{(C) }98\qquad\textbf{(D) }105\qquad\textbf{(E) }126$

## Solution 1 (One Variable)
Let $x$ be the length of the ship. Then, in the time that Emily walks $210$ steps, the ship moves $210-x$ steps. Also, in the time that Emily walks $42$ steps, the ship moves $x-42$ steps. Since the ship and Emily have the same ratio of absolute speeds in either direction, $\frac{210}{210-x} = \frac{42}{x-42}$ . Dividing both sides by $42$ and cross multiplying, we get $5(x-42) = 210-x$ , so $6x = 420$ , and $x = \boxed{\textbf{(A) }70}$ .
~ihatemath123

## Solution 2 (Two Variables)
Let the speed at which Emily walks be $42$ steps per hour. Let the speed at which the ship is moving be $s$ . Walking in the direction of the ship, it takes her $210$ steps, or $\frac {210}{42} = 5$ hours, to travel. We can create an equation: \[d = 5(42-s),\] where $d$ is the length of the ship. Walking in the opposite direction of the ship, it takes her $42$ steps, or $42/42 = 1$ hour. We can create a similar equation: \[d = 1(42+s).\] Now we have two variables and two equations. We can equate the expressions for $d$ and solve for $s$ : \begin{align*} 210-5s &= 42 + s \\ s &= 28. \\ \end{align*} Therefore, we have $d + s = 42 + s = \boxed{\textbf{(A) }70}$ .
~LucaszDuzMatz (Solution)
~Minor edits by Yvz2900

## Solution 3 (Three Variables)
Suppose that Emily and the ship take steps simultaneously such that Emily's steps cover a greater length than the ship's steps.
Let $L$ be the length of the ship, $E$ be Emily's step length, and $S$ be the ship's step length. We wish to find $\frac LE.$
When Emily walks from the back of the ship to the front, she walks a distance of $210E$ and the front of the ship moves a distance of $210S.$ We have $210E=L+210S$ for this scenario, which rearranges to \[210E-210S=L. \hspace{15mm}(1)\] When Emily walks in the opposite direction, she walks a distance of $42E$ and the back of the ship moves a distance of $42S.$ We have $42E=L-42S$ for this scenario, which rearranges to \[42E+42S=L. \hspace{19.125mm}(2)\] We multiply $(2)$ by $5$ and then add $(1)$ to get $420E=6L,$ from which $\frac LE = \boxed{\textbf{(A) }70}.$
~Steven Chen (www.professorchenedu.com)
~MRENTHUSIASM

## Solution 4 (Using the Boat's "Step")
Every time Emily takes a step, the boat also "takes a step". Call the length of the boats step $s$ . Call the length of the boat $x$ .
When Emily is walking in the same direction as the boat, every time she takes a step the boat moves an additional distance of $s$ . This means that she travels a total distance of $x + 210 s$ to reach the other end of the boat.
When Emily is walking in the opposite direction of the boat, every time she takes a step the distance till the end of the boat reduces by $s$ (since the boat is coming towards her and moves a distance of $s$ ). This means that she travels a total distance of $x - 42 s$ to reach the other end of the boat.
Taking Emily's step as a unit of distance, we now have two equations \begin{align*} 210 &= x + 210 s, \\ 42 &= x - 42s. \end{align*} Solving for $x$ you get $\boxed{\textbf{(A) }70}$ .
~zeeshan12

## Solution 5 (Relative Speeds)
Call the speed of the boat $v_s$ and the speed of Emily $v_e$ .
Consider the scenario when Emily is walking along with the boat. Relative to an observer on the boat, her speed is $v_e-v_s$ .
Consider the scenario when Emily is walking in the opposite direction. Relative to an observer on the boat, her speed is $v_e+v_s$
Since Emily takes $210$ steps to walk along with the boat and $42$ steps to walk opposite the boat, that means it takes her $5$ times longer to walk the length of a stationary boat at $v_e-v_s$ compared to $v_e+v_s$ .
This means that $5(v_e-v_s)=v_e+v_s$ , so $v_s = \frac{2v_e}{3}$ .
As Emily takes $210$ steps to walk the length of the boat at a speed of $v_e- \frac{2v_e}{3}=\frac{v_e}{3}$ , she must take $\frac13$ of the time to walk the length of the boat at a speed of $v_e$ , so our answer is $\frac{210}{3} = \boxed{\textbf{(A) }70}$ .

## Video Solution by TheBeautyofMath
https://youtu.be/zq3UPu4nwsE
~IceMatrix

## Video Solution by WhyMath
https://youtu.be/0JOj_fbCB40
~savannahsolver
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .