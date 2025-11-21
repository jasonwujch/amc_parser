# 2017 AMC 10B Problem 13

## Problem

There are $20$ students participating in an after-school program offering classes in yoga, bridge, and painting. Each student must take at least one of these three classes, but may take two or all three. There are $10$ students taking yoga, $13$ taking bridge, and $9$ taking painting. There are $9$ students taking at least two classes. How many students are taking all three classes?

$\textbf{(A)}\ 1\qquad\textbf{(B)}\ 2\qquad\textbf{(C)}\ 3\qquad\textbf{(D)}\ 4\qquad\textbf{(E)}\ 5$

## Solution 1 (PIE)
By PIE (Property of Inclusion/Exclusion), we have
$|A_1 \cup A_2 \cup A_3| = \sum |A_i| - \sum |A_i \cap A_j| + |A_1 \cap A_2 \cap A_3|.$ Number of people in at least two sets is $\sum |A_i \cap A_j| - 2|A_1 \cap A_2 \cap A_3| = 9.$ So, $20 = (10 + 13 + 9) - (9 + 2x) + x,$ which gives $x = \boxed{\textbf{(C) } 3}.$

## Solution 2 (Subtraction)
The total number of classes taken among the 20 students is $10 + 13 + 9 = 32$ . Each student is taking at least one class so let's subtract the $20$ classes ( $1$ per each of the $20$ students) from $32$ classes to get $12$ . $12$ classes is the total number of extra classes taken by the students who take $2$ or $3$ classes. Since we know that there are $9$ students taking at least $2$ classes, there must be $12 - 9 = \boxed{\textbf{(C) } 3}$ students that are taking all $3$ classes.

## Solution 3 (Algebra)
Total class count is 32. Assume there are $a$ students taking one class, $b$ students taking two classes, ad $c$ students taking three classes. Because there are $20$ students total, $a+b+c = 20$ . Because each student taking two classes is counted twice, and each student taking three classes is counted thrice in the total class count, $a+2b+3c = 10+13+9 = 32$ . There are $9$ students taking two or three classes, so $b+c = 9$ . Solving this system of equations gives us $c=\boxed{\textbf{(C) 3}}$ .

## Solution 4 (Venn Diagrams and Algebraic Substitution)
Let us assign the following variables and put them in our Venn Diagram [1] : $a$ which designates the number of people taking exactly Bridge and Yoga. $b$ which designates the number of people taking exactly Bridge and Painting. $c$ which designates the number of people that took all $3$ classes or what we want to find. $d$ which designates the number of people taking exactly Yoga and Painting.
Let's now recall what information we have given: There are exactly $9$ people that are taking at least $2$ classes meaning in other words, $9$ people total are taking strictly $2$ classes or strictly all the available classes meaning that $a+b+c+d=9$ .
Let's now start filling out the Venn Diagram: Strictly taking Bridge, no other classes: We know in total, the number is $13$ , however this includes the people taking other classes too meaning we'd need to do some subtraction. From our Venn Diagram we see that we'd need to subtract the following variables to get our wanted outcome here, $a, b, c$ . Giving our answer as $13-(a+b+c)$ .
However, this equation seems complicated as it has $3$ different variables, so to make this look a lot less complicated we can use our earlier equation: $a+b+c+d=9$ to see that $a+b+c=9-d$ . This means that this can also be written as $13-(9-d)=4+d$ .
Strictly taking Yoga Only: The total number of people is $10$ , but this would also count people taking other classes too along with it, so we need to subtract this overcount which is visible in the Venn Diagram giving us: $10-(a+c+d)$ .
Again, we can use substitution to see that $a+c+d=9-b$ . This simplifies our equation to $10-(9-b)=1+b$ .
Strictly taking Painting Only: We know again, in total this number is $9$ , which also accounts for the people taking other classes too. From our Venn Diagram it is visible that we need to subtract: $b, c, d$ giving $9-(b+c+d)$ .
Again, through substitution of our first equation we see that $b+c+d=9-a$ meaning we can simplify this equation to $9-(9-a)=a$
If we add these newly made equations of strictly taking one class, we get the total number of people taking exactly one class as these equations each were a subcase for it. We can also find the exact number for this because we are given that there are exactly $20$ students in total, and $9$ students are taking exactly $2$ or $3$ classes, meaning that if we do $20-9$ we get our answer for the number of students taking exactly $1$ class because those taking exactly one class have no overlap with those taking exactly $2$ or exactly $3$ classes as shown in our Venn Diagram and because $1$ , $2$ , and $3$ classes are subcases for finding the total number of students as we know that each student is in exactly $1, 2$ , or $3$ classes. This means that exactly $11$ students took strictly $1$ class.
We can add up our equations we found to equal $11$ because those equations were for subcases of having exactly $1$ class giving: $(4+d)+(1+b)+a=11$ . $=5+a+b+d=11$ .
From our equation $a+b+c+d=9$ , we can substitute $9-c$ for $a+b+d$ giving us: $5+9-c=11$ .
This gives $c=3$ . We assigned $c$ for the number of people taking exactly $3$ classes meaning that when we find $c$ , we find the answer. This means our answer is $\boxed{(C) 3}$ .
~Batmanstark

## Solution 5
We are told that there are $20$ students in all, and $10$ take yoga, $13$ take bridge, and $9$ take painting. Representing each student as a number from $1$ to $20$ , we can then make a list of which classes they are taking. Students 1-10 take yoga, and students $11$ to $20$ take bridge. However, this means that only $10$ students are taking bridge. To make up for it, we go back to the top of the list and start over from student $1$ . Students $1$ , $2$ , and $3$ will also take bridge giving the desired count of $13$ total bridge students.
Now, all that is left are the students who take painting. There are $9$ students who take painting, so students $4$ through students $9$ take painting. Note that because $9$ people take at least two classes, students $10$ through $20$ are unable to take more than one class. This means that we must once more start over from the top. Already $6$ painting slots have been filled, so students $1$ , $2$ , and $3$ will also take painting. This gives a total of $3$ students (students $1$ , $2$ , and $3$ ) who take all three classes. Therefore, our answer is $\boxed{\textbf{(C) } 3}$ .
~TheGoldenRetriever
### See Also
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .