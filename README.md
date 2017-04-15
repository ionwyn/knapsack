# knapsack
Pseudo-polynomial approach to Knapsack Problem

I thought I might write one algorithm that I find really interesting: Knapsack problem.

Its problem statement is simple:

You have a fixed-size knapsack (meaning it will only hold at most weight of W, otherwise it will break.
You have a set of items, whatever it may be, and each item has its weight and its value.
You have to determine the best combination of items so that the value is maximized without overloading your bag.
A problem so simple, yet difficult.  We see it practically everywhere.  Resource allocation is a problem that arises in Business, too.  The problem has also been studied in depth under Complexity Theory, Cryptography, and Combinatorics.  This is the very problem we solve before leaving our house: should I take my laptop?  Do I also take my textbook?  Nah, maybe I’m just gonna drop the knapsack and leave the house with nothing.

A naive way to solve this problem is to go through all the 2^n subsets of the n items that we could possibly add and check whichever gives the maximum output.  We can come up with a usually better solution using dynamic programming.  Just like any other dynamic programming approach, we aim to find an optimal sub-solution to tackle the bigger problem.  We implement a solution to Knapsack problem with the complexity of the algorithm O(nW) (pseudopolynomial of course, as the problem is NP-Hard)
