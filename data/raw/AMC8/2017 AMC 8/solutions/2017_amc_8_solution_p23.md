# 2017 AMC 8 Problem 23

## Problem

Each day for four days, Linda traveled for one hour at a speed that resulted in her traveling one mile in an integer number of minutes. Each day after the first, her speed decreased so that the number of minutes to travel one mile increased by $5$ minutes over the preceding day. Each of the four days, her distance traveled was also an integer number of miles. What was the total number of miles for the four trips?

$\textbf{(A) }10\qquad\textbf{(B) }15\qquad\textbf{(C) }25\qquad\textbf{(D) }50\qquad\textbf{(E) }82$

## Solution
It is well known that $\text{Distance}=\text{Speed} \cdot \text{Time}$ . In the question, we want distance. From the question, we have that the time is $60$ minutes or $1$ hour. By the equation derived from $\text{Distance}=\text{Speed} \cdot \text{Time}$ , we have $\text{Speed}=\frac{\text{Distance}}{\text{Time}}$ , so the speed is $1$ mile per $x$ minutes. Because we want the distance, we multiply the time and speed together yielding $60\text{ mins}\cdot \frac{1\text{ mile}}{x\text{ mins}}$ . The minutes cancel out, so now we have $\dfrac{60}{x}$ as our distance for the first day. The distance for the following days are: \[\dfrac{60}{x},\dfrac{60}{x+5},\dfrac{60}{x+10},\dfrac{60}{x+15}.\] We know that $x,x+5,x+10,x+15$ are all factors of $60$ , therefore, $x=5$ because the factors have to be in an arithmetic sequence with the common difference being $5$ and $x=5$ is the only solution. \[\dfrac{60}{5}+\dfrac{60}{10}+\dfrac{60}{15}+\dfrac{60}{20}=12+6+4+3=\boxed{\textbf{(C)}\ 25}.\]

## Video Solution by OmegaLearn
https://youtu.be/XixU0JZ5FLk?t=39587687687687687686
~ pi_is_3.14
### See Also