# 2025 AMC 12A Problem 2

## Problem

A box contains $10$ pounds of a nut mix that is $50$ percent peanuts, $20$ percent cashews, and $30$ percent almonds. A second nut mix containing $20$ percent peanuts, $40$ percent cashews, and $40$ percent almonds is added to the box resulting in a new nut mix that is $40$ percent peanuts. How many pounds of cashews are now in the box?

$\textbf{(A) } 3.5 \qquad\textbf{(B) } 4 \qquad\textbf{(C) } 4.5 \qquad\textbf{(D) } 5 \qquad\textbf{(E) } 6$

## Solution 1
We are given $0.2(10) = 2$ pounds of cashews in the first box.
Denote the pounds of nuts in the second nut mix as $x.$
\[5 + 0.2x = 0.4(10 + x)\] \[0.2x = 1\] \[x = 5\]
Thus, we have $5$ pounds of the second mix.
\[0.4(5) + 2 = 2 + 2 = \boxed{\text{(B) }4}\]
~pigwash
~yuvaG (Formatting)
~LucasW (Minor LaTeX)

## Solution 2
Let the number of pounds of nuts in the second nut mix be $x$ . Therefore, we get the equation $0.5 \cdot 10 + 0.2 \cdot x = 0.4(x+10)$ . Solving it, we get $x=5$ . Therefore the amount of cashews in the two bags is $0.2 \cdot 10 + 0.4 \cdot 5 = 4$ , so our answer choice is $\boxed{\textbf{(B)} 4}$ .
~iiiiiizh
~yuvaG - $\LaTeX$ Formatting ;)
~Amon26(really minor edits)

## Solution 3
The percent of peanuts in the first mix is $10\%$ away from the total percentage of peanuts, and the percent of peanuts in the second mix is $20\%$ away from the total percentage. This means the first mix has twice as many nuts as the second mix, so the second mix has $5$ pounds. $0.20 \cdot 10 + 0.40 \cdot 5 = 4$ pounds of cashews. So our answer is, $\boxed{\textbf{(B)}4}$ ~LUCKYOKXIAO
~LEONG2023-Latex

## Solution 4
Note that we can set the information given in the problem into a table shown below:
\[\renewcommand{\arraystretch}{1.5} \begin{centering} \begin{array}{| c | c | c |} \hline \text{Peanuts} & \text{Cashews} & \text{Almonds}\\ \hline 5 & 2 & 3\\ \hline \frac{2}{10}x & \frac{4}{10}x & \frac{4}{10}x\\ \hline \end{array} \end{centering}\]
We are given that the new nut mix will contain $40\%$ peanuts. Hence, $5 + \frac{2}{10}x$ is $40\%$ of the total mix which is $10 + x$ . Solving the equation $5 + \frac{2}{10}x = \frac{2}{5} \cdot (10 + x)$ yields $x=5.$ Therefore, the number of cashews in the new mix is equal to $2 + \frac{2}{5} \cdot 5 = \boxed{\textbf{(B)} 4}$ .
~Moonlight11
~TehSovietOnion (LaTeX)

## Solution 5(extremely long, overcomplicated, never use on the test)
Note: This got messed up when putting into the wiki and it has been re-interpreted by AI. Please review this solution carefully and correct any AI errors.
1️⃣ Measure-Theoretic Setup
Let (Ω, F, μ) be a finite measure space, where Ω = {peanuts, cashews, almonds}.
Define a density function f_i : Ω → [0,1] representing the probability distribution (composition) of each mix i:
- f₁(peanuts) = 0.5, f₁(cashews) = 0.2, f₁(almonds) = 0.3 - f₂(peanuts) = 0.2, f₂(cashews) = 0.4, f₂(almonds) = 0.4
Each mix corresponds to a measure ν_i = m_i f_i μ, where m_i is the total mass (10 lb for i=1, unknown x lb for i=2).
The combined measure is: ν = ν₁ + ν₂ = (m₁f₁ + m₂f₂)μ
The normalized mixture (probability measure for composition) is: f = (m₁f₁ + m₂f₂) / (m₁ + m₂)
We are told that f(peanuts) = 0.4.
2️⃣ Functional Equation in Measure Form
This is equivalent to: [m₁f₁(peanuts) + m₂f₂(peanuts)] / (m₁ + m₂) = 0.4
Substitute m₁ = 10: [10(0.5) + x(0.2)] / (10 + x) = 0.4
Same as before — but this time we view x as a scalar measure parameter in the space of signed measures.
Solving yields: x = 5
3️⃣ Abstract Affine Geometry View
Let Δ₂ = {(p,c,a) ∈ ℝ³ : p+c+a=1, p,c,a≥0}, the 2-simplex representing all possible nut compositions.
Each mix is a point in this simplex: - v₁ = (0.5, 0.2, 0.3) - v₂ = (0.2, 0.4, 0.4)
The combined mix lies on the affine line joining them: v = (10v₁ + 5v₂) / 15
The map Φ: (ℝ₊)² → Δ₂, (m₁,m₂) ↦ (m₁v₁ + m₂v₂)/(m₁ + m₂) is an affine morphism of positive cones that collapses scalar measures to compositions.
The constraint π_p(v) = 0.4 defines a hyperplane section of the simplex, and the intersection with the line segment joining v₁, v₂ defines a unique barycentric coordinate λ = 1/3.
This corresponds to an affine convex combination: v = (1-λ)v₁ + λv₂, λ = 1/3
4️⃣ Categorical Abstract Algebra Interpretation
We can view the mixing process as a functor: Mix: (FinMeas, +) → (Δ₂, convex combinations)
where each object is a measure with labeled components (mass and composition), and morphisms are scalar additions of measures.
The condition "final mix has 40% peanuts" is a natural transformation constraint between two functors: Φ, Ψ: FinMeas → ℝ
where: - Φ(ν) = total mass of peanuts - Ψ(ν) = total mass
We require Φ(ν)/Ψ(ν) = 0.4.
This induces a categorical equation that forces the unique morphism ratio ν₂:ν₁ = 1:2.
Hence x = 5 .
5️⃣ Differential-Geometric / Tangent-Space Insight
On the manifold M = Δ₂, the line of mixtures parameterized by x is a 1D affine submanifold: γ(x) = (10v₁ + xv₂)/(10 + x)
The constraint surface S = {v ∈ Δ₂ : p = 0.4} is a codimension-1 affine submanifold (a plane slice).
The intersection S ∩ Im(γ) is transversal because the derivative dπ_p(γ'(x)) ≠ 0.
Hence there exists a unique transverse intersection point x = 5 .
That transversality guarantees that the equilibrium composition is structurally stable under small perturbations of the parameters — i.e., you could wiggle the percentages slightly and the solution still exists and varies smoothly.
6️⃣ Return to measurable quantity
Total cashew mass: M_cashew = 10(0.20) + 5(0.40) = 2 + 2 = 4 pounds
Write composition vectors as column vectors (mass fractions multiplied by mass):
Initial mass vector (peanuts, cashews, almonds) for 10 lb: \[\mathbf{v}_0 = 10 \begin{pmatrix} 0.50 \\ 0.20 \\ 0.30 \end{pmatrix} = \begin{pmatrix} 5 \\ 2 \\ 3 \end{pmatrix}.\] Added mix per unit mass: \[\mathbf{u} = \begin{pmatrix} 0.20 \\ 0.40 \\ 0.40 \end{pmatrix}.\] After adding \( x \) lb, total mass vector is \[\mathbf{v}(x) = \mathbf{v}_0 + x \mathbf{u} = \begin{pmatrix} 5 \\ 2 \\ 3 \end{pmatrix} + x \begin{pmatrix} 0.2 \\ 0.4 \\ 0.4 \end{pmatrix}.\] Peanut fraction requirement: \[\frac{\mathbf{e}_1^\top \mathbf{v}(x)}{\mathbf{1}^\top \mathbf{v}(x)} = 0.4,\] where \( \mathbf{e}_1 = \begin{pmatrix} 1, 0, 0 \end{pmatrix}^\top \) and \( \mathbf{1} = \begin{pmatrix} 1, 1, 1 \end{pmatrix}^\top \). This is exactly the same scalar equation, \[\frac{5 + 0.2x}{10 + x} = 0.4,\] leading to \( x = 5 \) and hence \[\mathbf{v}(5) = \begin{pmatrix} 5 \\ 2 \\ 3 \end{pmatrix} + 5 \begin{pmatrix} 0.2 \\ 0.4 \\ 0.4 \end{pmatrix} = \begin{pmatrix} 6 \\ 4 \\ 5 \end{pmatrix}.\] Thus cashews \( = 4 \) lb.

## Video Solution by Power Solve
https://youtu.be/QBn439idcPo?si=jrzzKE72p29BIDQZ&t=102

## Chinese Video Solution
https://www.bilibili.com/video/BV1S52uBoE8d/
~metrixgo

## Video Solution (Intuitive, Quick Explanation!)
https://youtu.be/Qb-9KDYDDX8
~ Education, the Study of Everything

## Video Solution (Fast and Easy)
https://youtu.be/YpJ3QZTmDuw?si=ucvH15JKX2tw4SKZ ~ Pi Academy

## Video Solution by SpreadTheMathLove
https://www.youtube.com/watch?v=dAeyV60Hu5c

## Video Solution by Daily Dose of Math
https://youtu.be/LN5ofIcs1kY
~Thesmartgreekmathdude

## Video Solution
https://youtu.be/gWSZeCKrOfU
~MK

## Video Solution
https://youtu.be/l1RY_C20Q2M
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .