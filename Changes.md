# Proposed changes for next iteration/version

The idea of this file is to have a single source of truth as to which changes we want to do when we update the course.
Feel free to provide a PR with more proposed changes!

## In general


## Lesson 1

### Lecture
- Rewrite "Each Jupyter notebook is a series of cells." to "Each Jupyter notebook is a series of text and code cells."
  and then "To execute a cell, click ..." to "To execute a cell that contains Haskell code, click ...".
- I did not understood the expression "... function definitions are trees of expressions" but when I watched the lecture 
  it is explained very nicely. Can we add a statement like "For further explanation what are trees of expressions watch
  the video lecture."?
- I'm not sure if the title "What are functional programming languages" is a good choice. The definition we have is the 
  same as on wikipedia for what is "functional programming". But on the web when you goole for "functional programming 
  languages" it says that functional PLs offer the user the features of purely functional PLs, but do not enforce them. 
  Also functional PLs do not implement lambda calculus under the hood as haskell does, where everthing is combinations  
  of functions. My suggestion is to change the title from "Functional programming languages" to "Functional programming" 
  and then possibly add a comment where we explain what is considered a functional programming language. 
### Homework
- 

## Lesson 2

### Lecture
- Add short explanation about type classes after polymorphysm. Just enough so the students don't struggle until we cover them properly on the type classes lesson.
- 
### Homework
- 

## Lesson 3

### Lecture
- Some code when executed returns comments in the form of "Found: ... Why not: ...". Can we disable that?
- Some cell results are not cleared. Thomas suggested that we should upload jupyter files such that we clear all previous
  output from cells. Then also the comments from point 1 will not be seen when looking at the lesson only on github.
- In the guards chapter add an example where you show it is possible to use more then one condition in a single guard line.
  If you split them with a comma they are combined with a logical AND. But you can also combine them with a logical OR:
### Homework
- 

## Lesson 4

### Lecture
- 
### Homework
- 

## Lesson 5

### Lecture
- Noticed that the command ":t filter" gives "filter :: forall a. (a -> Bool) -> [a] -> [a]". If the student sees the forall 
  statement we should explain what it is.
- We can add an explanation how variable lookup works in Haskell and explain lexical scope. This could be in the lambda function
  chapter, since you also use a lambda function to demonstrate this. 
### Homework
- 

## Lesson 6

### Lecture
- 
### Homework
- 

## Lesson 7

### Lecture
- 
### Homework
- 

## Lesson 8

### Lecture
- In the comments where we write "-- Real definition" I would rather write "-- Actual Haskell definition" because the workd Real
  can be dubious because up to this lesson the students did not looked at any Haskell source code. 
- It would be nice to explain the phrases "sum types" and "record types" when explaning algebraic data types. They are often used
  among programming language jargon.
- Also we can explain the advantages of sum types over product types used in hierarchical design by imperative languages. We can 
  show a code example thatneeds to be refactored by adding a type and how dificult it is when using product types in e.g. Java. 
### Homework
- Why not include an example (the one that was scratched) where you show different ways how to present your data with sum types? 