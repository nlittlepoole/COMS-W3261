# COMS W3261

  Computer Science Theory

  Lecture 1: September 3, 2014

  Introduction to Computer Science Theory

## 1. Teaching Staff

## 2. Schedule

- Lectures: Mondays and Wednesdays, 1:10-2:25pm, 833 Mudd.
- Office Hours: Mondays and Wednesdays, after class.

## 3. Course Objectives

- Learning computational thinking
- Understanding the fundamental models of computation that
  underlie modern computer hardware, software, and programming 
  languages.
- Discovering that there are problems no computer can solve.
- Discovering that there are limits on how fast a computer can solve a
  problem.
- Mastering the foundations of automata theory, computability theory,  
  and complexity theory.
- Learning about applications of computer science theory to    
  algorithms, programming languages, compilers, natural language 
  translation, operating systems, and software verification.

## 4. Course Syllabus

- Languages and decision problems
- Finite automata
- Regular expressions
- Properties of regular languages
- Context-free grammars
- Pushdown automata
- Properties of context-free languages
- Algorithms and Turing machines
- Lambda calculus
  - The computational model for functional languages. Java 8 now has lambdas.
- Undecidability
- Complexity theory

## 5. Textbooks and References

- The course text is

   <dd>John E. Hopcroft, Rajeev Motwani, and Jeffrey D. Ullman</dd>
   <dd>_Introduction to Automata Theory, Languages, and Computation_, 
   Third Edition</dd>
   <dd>Pearson/Addison-Wesley, 2007, ISBN-10: 0321462254 | ISBN-13: 
   9780321462251</dd>

## 6. Course Requirements

- Homeworks (best four out of five homeworks will constitute 20% of 
  final grade)
- Midterm (40% of final grade)
- Final (40% of final grade)

## 7. Languages

- An _alphabet_ &#931; is a finite, nonempty set of symbols.
  - A function maps an element to a range.
- Examples: {0,1}, ASCII, Unicode. A _string_ is a finite sequence of 
  symbols chosen from some alphabet.

- Examples: &#949; (the empty string), 0, 01, 011
  - Don't forget about the empty string. It's important.

##### Terms associated with strings
**Prefix**: Any sequence of characters at the beginning of a string.
  - The first prefix for any string is the empty string, &#949;.
  - Example: "dog" has 4 prefixes. &#949;, d, do, dog.
  - All strings have n + 1 prefixes.

**Suffixes**: Any sequence of characters at the end of a string.
  - Example: "dog" has 4 prefixes. &#949;, g, go, dod.
  - All strings have n + 1 prefixes.

**Substrings**: Obtained by maintaining the sequence of characters while reducing the size of the string.
  - Example: dog.  
  - Shortest string: &#949;
  - Substring of length 1: d, o, g
  - Substring of length 2: do, og
  - Substring of length 3: dog
  - All substrings are of length n! + 1

**Subsequences**: Obtained by deleteing zero or more characters in a string.
  - Example: dog
  - &#949; , d, o, g, do, dg, og, dog
  - 2^n subsequences in any given character x.

- A string is ordered, strings are sequences and sequences have orders.
- Common operations on strings: concatenation, reversal
- Terms associated with strings: prefix, suffix, substring, 
  subsequence*   A _language_ over &#931; is a set of strings whose 
  symbols are chosen from &#931;. Examples:

- the empty set, &#8709;
- {0,1}, {0}, {1}, {01}
- _P_ = {10, 11, 101, 111, 1011, 1101, ... } (the binary 
  representations of the prime numbers)
- Distinction between finite and infinite languages:
  - There are a finite number of objects in the set.
  - Two types of infinite:
    - Countably: 1-to-1 mapping between the numbers in the set against the natural integers.
    - Uncountably: Do not have a 1-to-1 mapping between the natural integers and the given set.

- The set of all syntactically valid Java programs.
  - Ordering programs by the number of length shows that they are countably infinite.

- The set of all valid English sentences?*   Operations on languages: 
  union, concatenation, Kleene closure

  L \union M
  L \intersection M
  LM = {xy| x in the set L and y in the set M}
  L^0 = {empty set}
  L^i = L^i-1(L) i >= 1

- Example of Kleene closure: {0,1}* = { &#949;, 0, 1, 00, 01, 10, 11, 
  000, ... } (all strings of 0s and 1s)*   A _problem_ is the 
  question of deciding whether a given string is a member of some 
  particular language.
    L^* = U^infinite_L=0 L^i = L^0 Union L^1 Union L^2 Union ...
  EmptySet^* = {emptystring}, L^1 = LL^0
  {0, 1}^* = set of all strings of 0s and 1s
           = {empty, 0, 1, 00, 01, 10, 11, ...} all binary numbers

- Example: Given a binary number _x_, is _x_ in _P_?   Question: How 
  many languages over {0,1} are there?

- Given a language L and a string x is x in L?
- Give two sets A and B, determine whether A = B.
  - Is A a subset of B and is B a subset of A?

## 8. Proofs

-   What is a theorem?

-   A theorem is a statement that has been proven true by a
       convincing logical argument.*   What is a proof?

-   A (deductive) proof is a sequence of statements each one of
    which is a given fact or follows by a logical rule from some
    previous statements in the proof.*   Types of proof

## 9. Practice Problems

1.  How many (a) prefixes, (b) suffixes, (c) substrings, (d) 
      subsequences are there in a string of length _n_?
2.  What does it mean for a string to have balanced parentheses?
3.  Prove that the following recursive definition generates all and only
      all strings of balanced parentheses.

-   Rule 1 (basis): The empty string is a balanced string.
-   Rule 2 (induction): If _x_ and _y_ are balanced strings,
    then (_x_)_y_ is a balanced string.4.  Research problem: If _x_ is 
    a string of length _m_ and _y_ is a string of length _n_, then what 
    is the maximum possible number of longest common subsequences 
    between _x_ and _y_ as a function of _m_ and _n_?

## 10. Reading Assignment

-   HMU: Ch. 1


## 11. Side Notes

- Are all human beings biological computers?
- What makes a discussion of consciouness somewhat meaningless?
- Can we tell apart a human from a computer?
- What is computation?
- What are the limits of computation?
- What problems can be solved and which problems cannot be solved?
- Speed limits in computing.
- P = NP
- Must all algorithms halt on every input?
  - An algorithm has to halt on all inputs, according to Aho.

## 12. Computational Thinking

A natural way to look at life. **A two step process**
- First step: A mathematical abstraction for thinking about said problem. It should be such that it leads to solutions that can be executed using computational steps, algorithms.  
- Second step: Apply that abstraction.  
  **Examples:** 
  - Boolean Algebra for logic circuits
  - Quantum Computing

- - -