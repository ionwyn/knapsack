# knapsack

Knapsack is a Pseudo-polynomial approach to Knapsack Problem. Knapsack problem is a problem, which I personally interest me. I decided to write an algorithm to solve the problem.

The knapsack problem has a fixed size knapsack. 
You have a fixed-size knapsack (meaning it will only hold at most weight of W, otherwise it will break.

In a set of items, where items can be anything, each item has an assigned value referring to the weight of the item.Each knapsack bag has a defined value, referring to the max weight it can carry. The goal is to determine the best possible combination of item, ensuring the item’s weight value is maximised and the knapsack bag does not overload. 

Similar, issues arise in real-life business. The problem is to find the best possible way to allocate the maximum resources without overloading the maximum capacity. 

The problem has also been studied in depth under Complexity Theory, Cryptography, and Combinatorics.  This is the very problem we solve before leaving our house: should I take my laptop?  Do I also take my textbook?  Nah, maybe I’m just gonna drop the knapsack and leave the house with nothing. 

A simple but less efficient solution is to adding and checking all the 2^n subsets of the n items, for the combination providing the maximum output value. An efficient solution is generated using the concept of dynamic programming. The algorithm finds an optimal sub-solution to tackle the bigger problem. We implement a solution to Knapsack problem with the complexity of the algorithm O(nW) (pseudopolynomial of course, as the problem is NP-Hard)
