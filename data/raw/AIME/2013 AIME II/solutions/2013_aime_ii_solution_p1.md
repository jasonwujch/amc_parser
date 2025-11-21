# 2013 AIME II Problem 1

## Problem

Suppose that the measurement of time during the day is converted to the metric system so that each day has $10$ metric hours, and each metric hour has $100$ metric minutes. Digital clocks would then be produced that would read $\text{9:99}$ just before midnight, $\text{0:00}$ at midnight, $\text{1:25}$ at the former $\text{3:00}$ AM, and $\text{7:50}$ at the former $\text{6:00}$ PM. After the conversion, a person who wanted to wake up at the equivalent of the former $\text{6:36}$ AM would set his new digital alarm clock for $\text{A:BC}$ , where $\text{A}$ , $\text{B}$ , and $\text{C}$ are digits. Find $100\text{A}+10\text{B}+\text{C}$ .

## Solution
There are $24 \cdot 60=1440$ normal minutes in a day , and $10 \cdot 100=1000$ metric minutes in a day. The ratio of normal to metric minutes in a day is $\frac{1440}{1000}$ , which simplifies to $\frac{36}{25}$ . This means that every time 36 normal minutes pass, 25 metric minutes pass. From midnight to $\text{6:36}$ AM, $6 \cdot 60+36=396$ normal minutes pass. This can be viewed as $\frac{396}{36}=11$ cycles of 36 normal minutes, so 11 cycles of 25 metric minutes pass. Adding $25 \cdot 11=275$ to $\text{0:00}$ gives $\text{2:75}$ , so the answer is $\boxed{275}$ .

## Solution 2
First we want to find out what fraction of a day has passed at 6:36 AM. One hour is $\frac{1}{24}$ of a day, and 36 minutes is $\frac{36}{60}=\frac{3}{5}$ of an hour, so at 6:36 AM, $6 \cdot \frac{1}{24} + \frac{1}{24} \cdot \frac{3}{5}=\frac{1}{4}+\frac{1}{40}=\frac{11}{40}$ of a day has passed. Now the metric timing equivalent of $\frac{11}{40}$ of a day is $\frac{11}{40}\cdot 1000=275$ metric minutes, which is equivalent to 2 metric hours and 75 metric minutes, so our answer is $\boxed{275}$ - mathleticguyyy
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America.
These problems are copyrighted © by the Mathematical Association of America .