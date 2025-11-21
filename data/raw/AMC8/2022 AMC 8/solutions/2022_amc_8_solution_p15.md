# 2022 AMC 8 Problem 15

## Problem

Laszlo went online to shop for black pepper and found thirty different black pepper options varying in weight and price, shown in the scatter plot below. In ounces, what is the weight of the pepper that offers the lowest price per ounce?

[asy] //diagram by pog size(5.5cm); usepackage("mathptmx"); defaultpen(mediumgray*0.5+gray*0.5+linewidth(0.63)); add(grid(6,6)); label(scale(0.7)*"$1$", (1,-0.3), black); label(scale(0.7)*"$2$", (2,-0.3), black); label(scale(0.7)*"$3$", (3,-0.3), black); label(scale(0.7)*"$4$", (4,-0.3), black); label(scale(0.7)*"$5$", (5,-0.3), black); label(scale(0.7)*"$1$", (-0.3,1), black); label(scale(0.7)*"$2$", (-0.3,2), black); label(scale(0.7)*"$3$", (-0.3,3), black); label(scale(0.7)*"$4$", (-0.3,4), black); label(scale(0.7)*"$5$", (-0.3,5), black); label(scale(0.8)*rotate(90)*"Price (dollars)", (-1,3.2), black); label(scale(0.8)*"Weight (ounces)", (3.2,-1), black); dot((1,1.2),black); dot((1,1.7),black); dot((1,2),black); dot((1,2.8),black); dot((1.5,2.1),black); dot((1.5,3),black); dot((1.5,3.3),black); dot((1.5,3.75),black); dot((2,2),black); dot((2,2.9),black); dot((2,3),black); dot((2,4),black); dot((2,4.35),black); dot((2,4.8),black); dot((2.5,2.7),black); dot((2.5,3.7),black); dot((2.5,4.2),black); dot((2.5,4.4),black); dot((3,2.5),black); dot((3,3.4),black); dot((3,4.2),black); dot((3.5,3.8),black); dot((3.5,4.5),black); dot((3.5,4.8),black); dot((4,3.9),black); dot((4,5.1),black); dot((4.5,4.75),black); dot((4.5,5),black); dot((5,4.5),black); dot((5,5),black); [/asy]

$\textbf{(A) }1\qquad\textbf{(B) }2\qquad\textbf{(C) }3\qquad\textbf{(D) }4\qquad\textbf{(E) }5$

## Solution
[asy] //diagram by pog size(5.5cm); usepackage("mathptmx"); defaultpen(mediumgray*0.5+gray*0.5+linewidth(0.63)); add(grid(6,6)); label(scale(0.7)*"$1$", (1,-0.3), black); label(scale(0.7)*"$2$", (2,-0.3), black); label(scale(0.7)*"$3$", (3,-0.3), black); label(scale(0.7)*"$4$", (4,-0.3), black); label(scale(0.7)*"$5$", (5,-0.3), black); label(scale(0.7)*"$1$", (-0.3,1), black); label(scale(0.7)*"$2$", (-0.3,2), black); label(scale(0.7)*"$3$", (-0.3,3), black); label(scale(0.7)*"$4$", (-0.3,4), black); label(scale(0.7)*"$5$", (-0.3,5), black); label(scale(0.8)*rotate(90)*"Price (dollars)", (-1,3.2), black); label(scale(0.8)*"Weight (ounces)", (3.2,-1), black); draw((0,0)--(6,5),red); dot((1,1.2),black); dot((1,1.7),black); dot((1,2),black); dot((1,2.8),black); dot((1.5,2.1),black); dot((1.5,3),black); dot((1.5,3.3),black); dot((1.5,3.75),black); dot((2,2),black); dot((2,2.9),black); dot((2,3),black); dot((2,4),black); dot((2,4.35),black); dot((2,4.8),black); dot((2.5,2.7),black); dot((2.5,3.7),black); dot((2.5,4.2),black); dot((2.5,4.4),black); dot((3,2.5),blue); dot((3,3.4),black); dot((3,4.2),black); dot((3.5,3.8),black); dot((3.5,4.5),black); dot((3.5,4.8),black); dot((4,3.9),black); dot((4,5.1),black); dot((4.5,4.75),black); dot((4.5,5),black); dot((5,4.5),black); dot((5,5),black); [/asy]
We are looking for a black point, that when connected to the origin, yields the lowest slope. The slope represents the price per ounce. We can visually find that the point with the lowest slope is the blue point. Furthermore, it is the only one with a price per ounce significantly less than $1$ . Finally, we see that the blue point is in the category with a weight of $\boxed{\textbf{(C) } 3}$ ounces.
~MathFun1000

## Solution 2 (Elimination)
By the answer choices, we can disregard the points that do not have integer weights. As a result, we obtain the following diagram:
[asy] //diagram by pog size(5.5cm); usepackage("mathptmx"); defaultpen(mediumgray*0.5+gray*0.5+linewidth(0.63)); add(grid(6,6)); label(scale(0.7)*"$1$", (1,-0.3), black); label(scale(0.7)*"$2$", (2,-0.3), black); label(scale(0.7)*"$3$", (3,-0.3), black); label(scale(0.7)*"$4$", (4,-0.3), black); label(scale(0.7)*"$5$", (5,-0.3), black); label(scale(0.7)*"$1$", (-0.3,1), black); label(scale(0.7)*"$2$", (-0.3,2), black); label(scale(0.7)*"$3$", (-0.3,3), black); label(scale(0.7)*"$4$", (-0.3,4), black); label(scale(0.7)*"$5$", (-0.3,5), black); label(scale(0.8)*rotate(90)*"Price (dollars)", (-1,3.2), black); label(scale(0.8)*"Weight (ounces)", (3.2,-1), black); dot((1,1.2),black); dot((1,1.7),black); dot((1,2),black); dot((1,2.8),black); dot((2,2),black); dot((2,2.9),black); dot((2,3),black); dot((2,4),black); dot((2,4.35),black); dot((2,4.8),black); dot((3,2.5),blue); dot((3,3.4),black); dot((3,4.2),black); dot((4,3.9),black); dot((4,5.1),black); dot((5,4.5),black); dot((5,5),black); [/asy]
We then proceed in the same way that we had done in Solution 1. Following the steps, we figure out the blue dot that yields the lowest slope, along with passing the origin. We then can look at the x-axis(in this situation, the weight) and figure out it has $\boxed{\textbf{(C) } 3}$ ounces.
~DairyQueenXD (edited by HW73)

## Solution 3 (Elimination)
We can find the lowest point in each line ( $1$ , $2$ , $3$ , $4$ , or $5$ ) and find the price per pound. (Note that we don't need to find the points higher than the points below since we are finding the lowest price per pound.)
[asy] //diagram by pog size(5.5cm); usepackage("mathptmx"); defaultpen(mediumgray*0.5+gray*0.5+linewidth(0.63)); add(grid(6,6)); label(scale(0.7)*"$1$", (1,-0.3), black); label(scale(0.7)*"$2$", (2,-0.3), black); label(scale(0.7)*"$3$", (3,-0.3), black); label(scale(0.7)*"$4$", (4,-0.3), black); label(scale(0.7)*"$5$", (5,-0.3), black); label(scale(0.7)*"$1$", (-0.3,1), black); label(scale(0.7)*"$2$", (-0.3,2), black); label(scale(0.7)*"$3$", (-0.3,3), black); label(scale(0.7)*"$4$", (-0.3,4), black); label(scale(0.7)*"$5$", (-0.3,5), black); label(scale(0.8)*rotate(90)*"Price (dollars)", (-1,3.2), black); label(scale(0.8)*"Weight (ounces)", (3.2,-1), black); dot((1,1.2),red); dot((1,1.7),black); dot((1,2),black); dot((1,2.8),black); dot((2,2),green); dot((2,2.9),black); dot((2,3),black); dot((2,4),black); dot((2,4.35),black); dot((2,4.8),black); dot((3,2.5),blue); dot((3,3.4),black); dot((3,4.2),black); dot((4,3.9),orange); dot((4,5.1),black); dot((5,4.5),purple); dot((5,5),black); [/asy]
The red dot has a price per pound of something that is larger than $1$ . The green dot has a price per pound of $1$ . The blue dot has a price per pound of something like $\frac{2.5}{3}$ . The orange dot has a price per pound that is less than $1$ , but is very close to it. The purple dot has a price per pound of something like $\frac{4.5}{5}$ . We see that choices $\textbf{(A)}$ , $\textbf{(B)}$ ,and $\textbf{(D)}$ are eliminated. Also, $\frac{4.5}{5} > \frac{2.5}{3}$ thus the answer is $\boxed{\textbf{(C) } 3}$ .

## Video Solution (A Clever Explanation You’ll Get Instantly)
https://youtu.be/tYWp6fcUAik?si=V8hv_zOn_zYOi9E5&t=1847 ~hsnacademy

## Video Solution by Math-X (First understand the problem!!!)
https://youtu.be/oUEa7AjMF2A?si=ZY5Ty2OgPWUtsxgb&t=2374
~Math-X

## Video Solution (CREATIVE THINKING!!!)
https://youtu.be/rKxwNlKlAW4
~Education, the Study of Everything

## Video Solution
https://youtu.be/Ij9pAy6tQSg?t=1305
~Interstigation

## Video Solution
https://youtu.be/p29Fe2dLGs8?t=270
~STEMbreezy

## Video Solution
https://youtu.be/bNc5j2feJKo
~savannahsolver

## Video Solution by Dr. David
https://youtu.be/PCEz7P5f56Q
### See Also