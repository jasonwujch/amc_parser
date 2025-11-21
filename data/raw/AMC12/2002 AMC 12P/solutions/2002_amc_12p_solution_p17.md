# 2002 AMC 12P Problem 17

## Problem

Let $f(x) = \sqrt{\sin^4{x} + 4 \cos^2{x}} - \sqrt{\cos^4{x} + 4 \sin^2{x}}.$ An equivalent form of $f(x)$ is

$\text{(A) }1-\sqrt{2}\sin{x} \qquad \text{(B) }-1+\sqrt{2}\cos{x} \qquad \text{(C) }\cos{\frac{x}{2}} - \sin{\frac{x}{2}} \qquad \text{(D) }\cos{x} - \sin{x} \qquad \text{(E) }\cos{2x}$

Solution

## Solution 1
By the Pythagorean identity we can rewrite the given expression as follows. \[\sqrt{\sin^4{x} + 4 \cos^2{x}} - \sqrt{\cos^4{x} + 4 \sin^2{x}} = \sqrt{\sin^4{x} + 4(1 - \sin^2{x})} - \sqrt{\cos^4{x} + 4(1 - \cos^2{x})}\]
Expanding each bracket gives \[\sqrt{\sin^4{x} - 4\sin^2{x} + 4} - \sqrt{\cos^4{x} - 4\cos^2{x} + 4}\]
The expressions under the square roots can be factored to get \[\sqrt{(\sin^2{x} - 2)^2} - \sqrt{(\cos^2{x} - 2)^2}\]
Since $\sin^2{x} < 2$ and $\cos^2{x} < 2$ for all real $x$ , the expression must evaluate to $(2 - \sin^2{x}) - (2 - \cos^2{x})$ , which simplifies to $\cos^2{x} - \sin^2{x} = \boxed {\text{(E) }\cos{2x}}$ .

## Solution 2 (Cheese)
We don't actually have to solve the question. Just let $x$ equal some easy value to calculate $\cos {x}, \cos {2x}, \sin {x}, \sin {\frac{x}{2}},$ and $\cos {\frac{x}{2}}.$ For this solution, let $x=60^\circ.$ This means that the expression in the problem will give $\sqrt{\sin^4{60^\circ} + 4 \cos^2{60^\circ}} - \sqrt{\cos^4{60^\circ} + 4 \sin^2{60^\circ}}=\sqrt{(\frac{\sqrt{3}}{2})^4 + 4(\frac{1}{2})^2} - \sqrt{(\frac{1}{2})^4 + 4(\frac{\sqrt{3}}{2})^2}=\sqrt{\frac{9}{16} +1} - \sqrt{\frac{1}{16} + 3} = \frac{-1}{2}.$ Plugging in $x=60^\circ$ for the rest of the expressions, we get
$\text{(A) }1-\sqrt{2}\sin{60^\circ}=1-\frac{\sqrt{6}}{2} \neq \frac{-1}{2}.$
$\text{(B) }1+\sqrt{2}\cos{60^\circ}=1+\frac{\sqrt{2}}{2} \neq \frac{-1}{2}.$
$\text{(C) }\cos{\frac{60^\circ}{2}} - \sin{\frac{60^\circ}{2}}=\frac{\sqrt{3}}{2}-1 \neq \frac{-1}{2}.$
$\text{(D) }\cos{60^\circ} - \sin{60^\circ}=\frac{1-\sqrt{3}}{2} \neq \frac{-1}{2}.$
$\text{(E) }\cos {120^\circ}=\frac{-1}{2}.$
Therefore, our answer is $\boxed{\textbf{(E) } \cos {2x}}$ .
Comment: If you decide to cheese the problem, be very careful not to choose any $x$ where $x$ is a multiple of $\frac{\pi}{4}$ . It turns out that all of them except for $\frac{7\pi}{4} + 2\pi k$ result in equality between the correct answer and one or more wrong answers, which one could quickly verify by setting two choices equal and solving for $x$ .
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .