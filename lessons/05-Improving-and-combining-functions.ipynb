{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "slideshow": {
     "slide_type": "skip"
    }
   },
   "outputs": [],
   "source": [
    ":opt no-lint"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "# Improving and combining functions"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Outline\n",
    "\n",
    "- Higher-order functions\n",
    "\t- `filter`\n",
    "\t- `any`\n",
    "- Lambda functions\n",
    "- Precedence and associativity\n",
    "- Curried functions\n",
    "    - Partial application\n",
    "- Applying and composing functions \n",
    "\t- The `$` operator\n",
    "\t- The `.` operator\n",
    "- Point-free style"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Higher-order functions"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "A **higher-order function** is a function that takes other functions as arguments or returns a function as a result. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Because we can pass functions as an input, return them as a result, and assign them to variables, they are like any other value. So we say that functions are **first-class citizens**.\n",
    "\n",
    "Let's start with a classic example. Imagine that you have a function you usually apply twice (for some reason). Like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "complexFunc1 :: Int -> Int\n",
    "complexFunc1 x = x + 1\n",
    "\n",
    "func1 :: Int -> Int\n",
    "func1 x = complexFunc1 (complexFunc1 x)\n",
    "\n",
    "complexFunc2 :: Int -> Int\n",
    "complexFunc2 x = x + 2\n",
    "\n",
    "func2 :: Int -> Int\n",
    "func2 x = (complexFunc2 (complexFunc2 x)) + (complexFunc2 (complexFunc2 x))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "This is an exaggerated example, but you can see how a pattern starts to emerge. You always use the `complexFunc1` and `complexFunc2` twice! As soon as we saw this pattern, we realized we could do better. What if we create a function that takes two parameters–a function and a value–and applies the function to the value twice!\n",
    "\n",
    "We can do that by simply writing:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "applyTwice :: (a -> a) -> a -> a\n",
    "applyTwice f x = f (f x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Here, the type signature is different from previous ones. The `(a -> a)` part indicates that the first parameter is a function that takes a value of type `a` and returns a value of the same type. The second parameter is just a value of type `a`, and the whole `applyTwice` function returns a value of type `a`."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "And in the body of the function, you can see that it takes the first parameter (the function `f`), applies it to `x`, and then applies `f` again to the result. So we're applying the function `f` twice.\n",
    "\n",
    "And that's it! We created a higher-order function!\n",
    "\n",
    "We can use the `applyTwice` function to simplify the previous code like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "func1' :: Int -> Int\n",
    "func1' x = applyTwice complexFunc1 x\n",
    "\n",
    "func2' :: Int -> Int\n",
    "func2' x = (applyTwice complexFunc2 x) + (applyTwice complexFunc2 x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "This is a simple example, but higher-order functions are an extremely powerful feature. So much so that they are everywhere! In fact, you could create your own Domain Specific Language using higher-order functions! But let's take it step-by-step. Let's start by using two higher-order functions that come with Haskell."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "### `filter` function"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Let's start with the `filter` function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>/* Styles used for the Hoogle display in the pager */\n",
       ".hoogle-doc {\n",
       "display: block;\n",
       "padding-bottom: 1.3em;\n",
       "padding-left: 0.4em;\n",
       "}\n",
       ".hoogle-code {\n",
       "display: block;\n",
       "font-family: monospace;\n",
       "white-space: pre;\n",
       "}\n",
       ".hoogle-text {\n",
       "display: block;\n",
       "}\n",
       ".hoogle-name {\n",
       "color: green;\n",
       "font-weight: bold;\n",
       "}\n",
       ".hoogle-head {\n",
       "font-weight: bold;\n",
       "}\n",
       ".hoogle-sub {\n",
       "display: block;\n",
       "margin-left: 0.4em;\n",
       "}\n",
       ".hoogle-package {\n",
       "font-weight: bold;\n",
       "font-style: italic;\n",
       "}\n",
       ".hoogle-module {\n",
       "font-weight: bold;\n",
       "}\n",
       ".hoogle-class {\n",
       "font-weight: bold;\n",
       "}\n",
       ".get-type {\n",
       "color: green;\n",
       "font-weight: bold;\n",
       "font-family: monospace;\n",
       "display: block;\n",
       "white-space: pre-wrap;\n",
       "}\n",
       ".show-type {\n",
       "color: green;\n",
       "font-weight: bold;\n",
       "font-family: monospace;\n",
       "margin-left: 1em;\n",
       "}\n",
       ".mono {\n",
       "font-family: monospace;\n",
       "display: block;\n",
       "}\n",
       ".err-msg {\n",
       "color: red;\n",
       "font-style: italic;\n",
       "font-family: monospace;\n",
       "white-space: pre;\n",
       "display: block;\n",
       "}\n",
       "#unshowable {\n",
       "color: red;\n",
       "font-weight: bold;\n",
       "}\n",
       ".err-msg.in.collapse {\n",
       "padding-top: 0.7em;\n",
       "}\n",
       ".highlight-code {\n",
       "white-space: pre;\n",
       "font-family: monospace;\n",
       "}\n",
       ".suggestion-warning { \n",
       "font-weight: bold;\n",
       "color: rgb(200, 130, 0);\n",
       "}\n",
       ".suggestion-error { \n",
       "font-weight: bold;\n",
       "color: red;\n",
       "}\n",
       ".suggestion-name {\n",
       "font-weight: bold;\n",
       "}\n",
       "</style><span class='get-type'>filter :: forall a. (a -> Bool) -> [a] -> [a]</span>"
      ],
      "text/plain": [
       "filter :: forall a. (a -> Bool) -> [a] -> [a]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    ":t filter "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "This function takes a predicate (a function that returns a boolean) `a -> Bool` and a list of elements of type `a` and filters the elements of the list given the predicate.\n",
    "\n",
    "For example, if we want to filter only the even numbers from a list of 1 to 20, we could do something like:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2,4,6,8,10,12,14,16,18,20]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "filter even [1..20]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Or, for a more involved condition, we could filter from a list of fruits only the ones that contain the letter `'a'`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[\"Banana\",\"Pear\",\"Grape\"]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fruitWithA = filter tempFunct [\"Apple\", \"Banana\", \"Pear\", \"Grape\", \"Wood\"]\n",
    "                where tempFunct x = 'a' `elem` x\n",
    "fruitWithA"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "As you can see, you can also define a function in a `where` clause to pass it as the predicate of the `filter` function."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "### `any` function"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "We also have the `any` function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "-- Only for lists:  any :: (a -> Bool) -> [a] -> Bool"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "This function also takes a predicate and a list of elements. But this one checks if there exists **any** element in the list for which the predicate holds.\n",
    "\n",
    "For example, here we're checking if any of the elements of the list is greater than 4. If only one is, `any` returns `True`, else, it returns `False`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "biggerThan4 x = x > 4\n",
    "\n",
    "any biggerThan4 [1,2,3,4] "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "A more realistic way to use `any` would be to check if we have any cars left on our car-selling website:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "cars = [(\"Toyota\",0), (\"Nissan\",3), (\"Ford\",1)]\n",
    "\n",
    "biggerThan0 (_,x) = x > 0\n",
    "\n",
    "any biggerThan0 cars"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "In `biggerThan0`, we're pattern matching on the tuple to extract the number of cars and check if it's greater than zero. Then, we're using `any` to check if any of all the pairs in the list has at least one car left."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Ok, we saw plenty of examples of functions that take other functions as parameters. But what about functions that return functions as results? We'll get there. First we'll learn about lambda abstractions and curried functions."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Lambda functions"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "The term lambda function comes from the mathematical system called **lambda calculus**. It's an intriguing and powerful subject by itself, but today, we're going to look at it from the practical-programmer point of view."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "A lambda function (also called anonymous function) is a function definition that doesn't have a name."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "For example, here's how a lambda function that takes two arguments and multiplies them ( $f(x,y)=x*y$ ) looks in Haskell:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "\\x y -> x * y\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "A lambda function consists of four things:\n",
    "\n",
    " 1. The backslash `\\` at the beginning tells us that this is a lambda function.\n",
    " 2. The parameter names (in this case `x y`) that the function takes as inputs.\n",
    " 3. The arrow (`->`) that **separates** the inputs from the body.\n",
    " 4. And everything after the arrow that is the **body** of the function."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "<div class=\"alert alert-block alert-info\">\n",
    "Most modern programming languages also have anonymous functions. But not all of them work the same way.\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "### Why should you care?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "It sounds useless because how can you use a name-less function? You have no way of calling it later!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Actually, it's a powerful component of the language! Through this course, we'll encounter many situations where lambda expressions are practical. For starters, you can use lambda expressions to avoid naming functions that you'll only use once!\n",
    "\n",
    "This is useful in and of itself, but it really shines when working with higher-order functions! For example, take a look at the previous example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "biggerThan4 x = x > 4\n",
    "\n",
    "any biggerThan4 [1,2,3,4] "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "That `biggerThan4` function won't be used anywhere else, but it will linger in our environment forever. Also, it's an awfully simple function! The name is longer than the body!\n",
    "\n",
    "By using lambda expressions, we can create and use `biggerThan4` as a parameter for `any` all at the same time like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "any (\\x -> x > 4) [1,2,3,4]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "We can also use lambda expressions to simplify other functions. Let's review the `fruitWithA` function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[\"Banana\",\"Pear\",\"Grape\"]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fruitWithA = filter tempFunct [\"Apple\", \"Banana\", \"Pear\", \"Grape\", \"Wood\"]\n",
    "                where tempFunct x = 'a' `elem` x\n",
    "fruitWithA"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "We can simplify `fruitWithA` by removing the `tempFunct` and replacing it with a lambda function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[\"Banana\",\"Pear\",\"Grape\"]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "filter (\\x -> 'a' `elem` x) [\"Apple\", \"Banana\", \"Pear\", \"Grape\", \"Wood\"]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "And, of course, because lambda functions are just expressions, you could use them anywhere an expression can be used. Even by themselves:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "(\\x -> x*2 + 1) 3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "If you need more examples, keep watching/reading. Lambda functions will be a valuable tool to easily visualize currying.\n",
    "\n",
    "Right now, we'll take a few minutes to learn about precedence and associativity."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Precedence and associativity"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "### Precedence"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Precedence indicates the priority of an operator (denoted by a number from 0 to 9). If we use two operators with different precedence, the one with the higher precedence gets applied first. Meaning that higher precedence operators bind more tightly!\n",
    "\n",
    "We can get the precedence for an operator with the info command `:i`. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {},
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {},
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    ":i (+)  -- infixl 6 +\n",
    ":i (*)  -- infixl 7 *\n",
    "\n",
    "1 + 2 * 3  -- Same as 1 + (2 * 3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "<div class=\"alert alert-block alert-info\">\n",
    "    <code>infixl 6 +</code> and <code>infixl 7 *</code> are called <b>fixity declarations</b>.\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Because multiplication has precedence of 7, which is higher than the addition's precedence of 6, the result is 7 and not 9."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "And what happens when two operators have the same precedence? This is when associativity comes into play."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "### Associativity"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "When we used the `:i` command previously, it also returned the keyword `infixl`. This is the operator's associativity."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "When two operators have the same precedence, the associativity tells you which side (left with `infixl` or right with `infixr`) will be evaluated first.\n",
    "\n",
    "For example:\n",
    "- The operators `(+)` and `(*)` have left associativity, which means they evaluate the left side first.\n",
    "- The `(:)` operator has right associativity, which means it evaluates the right side first.\n",
    "- The `(==)` operator has no associativity (`infix`), which means that, if you use more than one, you need parenthesis to indicate the order."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "[1,2,3]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "1 + 2 + 3 + 4  -- infixl: Same as ((1 + 2) + 3) + 4\n",
    "\n",
    "1 : 2 : 3 : [] -- infixr: Same as 1 : (2 : (3 : []))\n",
    "\n",
    "True == (False == False) -- infix: If you remove parenthesis, you'll get an error."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "And, of course, you can change the evaluation order using parenthesis:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "outputs": [],
   "source": [
    ":i (**) -- infixr 8 **\n",
    "\n",
    "2**3**4  -- infixr: Same as 2 ** (3 ** 4)\n",
    "(2**3)**4"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Finally, we can define precedence and associativity when creating our own operator. Like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "x +++ y = x + y -- Creating +++ operator\n",
    "infixl 7 +++    -- Setting fixity of operator\n",
    "\n",
    "1 +++ 2 * 3  -- 9"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Now, the result is 9 because `+++` and `*` are both left-associative and have the same precedence."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "<div class=\"alert alert-block alert-info\">\n",
    "<b>Important note:</b> \n",
    "   <ul>\n",
    "       <li>Operators without an explicit fixity declaration are <code>infixl 9</code></li>\n",
    "       <li>Function application (the \"whitespace operator\") always has the highest precedence (imagine precedence 10).</li>\n",
    "   </ul>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Curried functions"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Currying is the process of changing a function so that rather than taking multiple inputs, it takes a single input and returns a function which accepts the second input, and so forth.\n",
    "\n",
    "And here's the kicker:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "**In Haskell, all functions are considered curried! That is, all functions in Haskell take just one argument!**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "To exemplify this, take a look at this function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "add3 :: Int -> Int -> Int -> Int\n",
    "add3 x y z = x + y + z"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "It seems like a multi-parameter function. But!, there are hidden associativities in play! We know that function application (the \"whitespace operator\") always has the highest precedence and associates to the left, so if we make that obvious, we get:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "add3 :: Int -> Int -> Int -> Int\n",
    "((add3 x) y) z = x + y + z"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "And if we check the fixture of the function arrow (`->`):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {},
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    ":i (->)  -- infixr -1 ->"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "We see that it associates to the right! So, a more explicit way of writing the signature of the `add3` function is:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "add3 :: Int -> (Int -> (Int -> Int))\n",
    "((add3 x) y) z = x + y + z\n",
    "\n",
    "add3 1 2 3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Which perfectly corresponds with the function's definition! But, just to make it painfully obvious, we'll make currying explicit using lambda functions.\n",
    "\n",
    "Starting with the previous definition:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "add3 :: Int -> (Int -> (Int -> Int)) -- Same as: add3 :: Int -> Int -> Int -> Int\n",
    "((add3 x) y) z = x + y + z           -- Same as: add3 x y z = x + y + z"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "We'll move each parameter from the left side of the `=` sign to the right side. Creating the same function several times but written differently. So, starting with `z` (the outermost parameter), an equivalent `add3` function that does exactly the same as the original can be written like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "add3 :: Int -> (Int -> (Int -> Int))\n",
    "(add3 x) y = \\z -> x + y + z"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Now, `add3` is a function that takes two numbers (`x y`) and returns a function that takes another number (`z`) and adds the three together.\n",
    "\n",
    "If we do it again for the second value:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "add3 :: Int -> (Int -> (Int -> Int))\n",
    "add3 x = \\y -> (\\z -> x + y + z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Now, `add3` is a function that takes one number (`x`) and returns a function that takes one number (`y`) that returns a function that takes one number (`z`) and adds the three together.\n",
    "\n",
    "And if we do it one more time:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "add3 :: Int -> (Int -> (Int -> Int))\n",
    "add3 = \\x -> (\\y -> (\\z -> x + y + z))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "We get that `add3` is a name that returns a function that takes one number (`x`) and returns a function that takes one number (`y`) that returns a function that takes one number (`z`) that adds the three numbers together."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "That was quite a journey, but we managed to make currying explicit!\n",
    "\n",
    "And now, the way signatures are written makes way more sense! Each time you replace one parameter, it returns a new function as a result. That is until you replace the final one that gives you the final result.\n",
    "\n",
    "And because `->` is right-associative, we can remove the use-less parentheses of both the signature and definition to get a cleaner code:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "add3 :: Int -> Int -> Int -> Int\n",
    "add3 = \\x -> \\y -> \\z -> x + y + z"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "And now, for example, if we apply the function to 3 parameters like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "add3 1 2 3 "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "skip"
    }
   },
   "source": [
    "This is what happens step by step (I added the parentheses for visual aid):"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "add3 :: Int -> (Int -> (Int -> Int))\n",
    "add3 = \\x -> (\\y -> (\\z -> x + y + z)) \n",
    "\n",
    "---\n",
    "\n",
    "add3 1 = \\y -> (\\z -> 1 + y + z)       :: Int -> (Int -> Int)\n",
    "\n",
    "add3 1 2 = \\z -> 1 + 2 + z             :: Int -> Int\n",
    "\n",
    "add3 1 2 3 = 1 + 2 + 3                 :: Int\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "So, besides being a cool conversation starter at the club, how is this useful to you? Well... with uncurried functions, if you provide fewer parameters than the ones required, you get an error. But because, in Haskell, all functions are curried, you can take advantage of it to use partial application!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "### Partial application"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Partial application in Haskell means that you provide fewer arguments than the maximum amount the function accepts."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "The result (like we saw earlier) is a new function that takes in the rest of the parameters you did not provide to the original function. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "As a practical example of how this is useful, let's say you have a function used to create an email in the format `name.lastName@domain`. The parameters you provide are the domain, the name, and the last name:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "createEmail :: String -> String -> String -> String\n",
    "createEmail domain name lastName = name ++ \".\" ++ lastName ++ \"@\" ++ domain"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Now, your company has two communities as clients, which have two different domain names. You don't want your users to write out the domain name every time, so you create 2 functions where you partially apply their domain names:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"Robertino.Martinez@teckel-owners.com\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "\"Vitalik.Buterin@secret-cardano-lovers.com\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "createEmailTeckel :: String -> String -> String\n",
    "createEmailTeckel = createEmail \"teckel-owners.com\"\n",
    "\n",
    "createEmailSCL :: String -> String -> String\n",
    "createEmailSCL = createEmail \"secret-cardano-lovers.com\"\n",
    "\n",
    "createEmailTeckel \"Robertino\" \"Martinez\"\n",
    "createEmailSCL \"Vitalik\" \"Buterin\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Notice that this is possible because the domain is the first parameter in the function `createEmail`. So the order of the arguments matters."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "If, for some reason, the parameter you want to apply is not the first one and you are not allowed to rewrite the existing function, you can create a helper function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "-- With partial application:\n",
    "\n",
    "createEmailJohn :: String -> String -> String\n",
    "createEmailJohn lastName domain = createEmail domain \"John\" lastName\n",
    "\n",
    "-- Without partial application:\n",
    "\n",
    "createEmail' :: String -> String -> String -> String\n",
    "createEmail' name lastName domain = createEmail domain name lastName"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "And because operators are just infix functions, we can also partially apply them!\n",
    "\n",
    "For example, recalling the previous example of a higher-order function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "any (\\x -> x > 4) [1,2,3,4]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "In the function we pass as a parameter, we need to compare if the input is larger than `4`. And the `>` operator is already a function that takes two parameters and compares if the first is larger than the second. So we can partially apply the parameter on the right to get the same result:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "any (>4) [1,2,3,4]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "The partial application of an infix operator is called a *section*."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "And I'm not sure if you noticed, but we just replaced the second parameter (the one on the right). The cool thing about sections is that you can partially apply the more convenient side:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"Thinking\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "\"Antilibrary\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "(++ \"ing\") \"Think\"     -- Same as \\x -> x ++ \"ing\"\n",
    "\n",
    "(\"Anti\" ++) \"library\"  -- Same as \\x -> \"Anti\" ++ x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "<div class=\"alert alert-block alert-warning\">\n",
    "<b>Warning:</b> The <code>-</code> operator is special because you can't partially apply it. <code>-1</code> is parsed as the literal <code>-1</code> rather than the sectioned operator <code>-</code> applied to <code>1</code>. The <code>subtract</code> function exists to circumvent this issue.\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Applying and composing functions "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "### The function application `$` operator"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "If we check how the function application operator is defined in Haskell, it seems a little... weird:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```\n",
    "($) :: (a -> b) -> a -> b\n",
    "f $ x =  f x\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "We see that it takes in a function `f` and a variable `x` and then applies the function to the variable (`f x`). So, it looks like this operator is redundant since it does the same as an ordinary function application (`f x`). \n",
    "\n",
    "And, you know what? It is! However, there's a small but significant difference between the two:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "- The \"white space\" operator has the highest left-associative precedence.\n",
    "- The function application operator (`$`) has the lowest right-associative precedence: `infixr 0 $`."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "You can see the difference if we make this evident using parenthesis:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "```\n",
    "f g h x      = ((f g) h) x\n",
    "\n",
    "f $ g $ h x  =  f (g (h x))\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "As an example of how this changes things, take a look at the following expressions:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "(2 *) 3 + 4    -- Same as: ((2 *) 3) + 4\n",
    "(2 *) $ 3 + 4  -- Same as: (2 *) (3 + 4)\n",
    "\n",
    "max 5 4 + 2    -- Same as: ((max 5) 4) + 2\n",
    "max 5 $ 4 + 2  -- Same as: (max 5) (4 + 2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "As you can see in the previous examples, when using `$`, the whole expression on its right is applied as the parameter to the function on its left. So you can see how using `$` is like surrounding everything to its right between parentheses.\n",
    "\n",
    "This brings us to the primary use of `$`: Omitting parentheses!\n",
    "\n",
    "In the following expression, there are 3 opportunities to remove parenthesis, so we remove them:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "-- All these expressions are equivalent:\n",
    "\n",
    "show ((2**) (max 3 (2 + 2)))\n",
    "\n",
    "show $ (2**) (max 3 (2 + 2))\n",
    "\n",
    "show $ (2**) $ max 3 (2 + 2)\n",
    "\n",
    "show $ (2**) $ max 3 $ 2 + 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "This makes your code more readable and easy to understand.\n",
    "\n",
    "Of course, you can do more than remove parenthesis, but that's what you'll do most of the time. So we'll leave it there and start learning about the function composition operator (`.`)!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "### Function composition"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "We already covered the concept of function composition in our first lesson. So if you're not sure about it, go check it out! But, just a refresher and in a few words: \n",
    "\n",
    "When we compose two functions, we produce a new function that is the equivalent of calling the two functions in sequence when the first one takes the output of the second one as input."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "We could do this with parenthesis. Here, the function `f` takes as input the result of applying the function `g` to `x`:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "```haskell\n",
    "f (g x)\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "As a probably overcomplicated example, we could do something like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "complicatedF :: [Int] -> Bool\n",
    "complicatedF x = any even (filter (>25) (tail ( take 10 x)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Here, we're composing quite a lot! 3 times to be exact! And as you can see, this is quite hard to read, so a diagram could help:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "$$\n",
    "    \\boxed{\\mathrm{[Int]}}\n",
    "        \\xrightarrow{\\mathrm{~~~~~~take~10~~~~~~}}\n",
    "    \\boxed{\\mathrm{[Int]}}\n",
    "        \\xrightarrow{\\mathrm{~~~~~~tail~~~~~~}}\n",
    "    \\boxed{\\mathrm{[Int]}}\n",
    "        \\xrightarrow{~~~~~~\\mathrm{filter~(>25)}~~~~~~}\n",
    "    \\boxed{\\mathrm{[Int]}}\n",
    "        \\xrightarrow{~~~~~~\\mathrm{any~even}~~~~~~}\n",
    "    \\boxed{\\mathrm{Bool}}\n",
    "    \\\\\n",
    "    \\\n",
    "    \\\\\n",
    "    \\\n",
    "    =\n",
    "    \\\n",
    "    \\\\\n",
    "    \\\n",
    "    \\\\\n",
    "    \\boxed{\\mathrm{[Int]}}\n",
    "        \\xrightarrow{\\mathrm{~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~complicatedF~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}}\n",
    "    \\boxed{\\mathrm{Bool}}\n",
    "$$"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "We take a list of `Int` as input, then use `take 10` to take the first 10 elements of the list, then use the result as an input for `tail` that returns the last 9 elements, then use the result of that as an input for `filter (>25)` to filter the values greater than 25, and finally, take the result of that as an input for `any even` to check if there are any even numbers left in the list."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "The diagram helped, but what if I tell you there's a way to have something as clean and easy to understand but in our code? \n",
    "\n",
    "This can be done by abstracting function composition to an operator. And because, in mathematics, the composition symbol is a ring that kind of resembles a dot, we'll use a dot:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "```haskell\n",
    "(.)  :: (b -> c) -> (a -> b) -> a -> c\n",
    "f . g = \\x -> f (g x)\n",
    "infixr 9 .\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Here, we see that the `.` operator takes two functions (`f :: b -> c` and `g :: a -> b`) and composes them using a lambda function to indicate that the whole `f . g` expression returns a function that takes the parameter `x :: a`, applies `g` to it to get a value of type `b`, and finally applies `f` to it to get a value of type `c`."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "It's important to notice that `f` takes as input a value that has the same type as the output of `g`. So the resulting function takes as input a value of the same type as `g`'s input (`a`) and returs as output a value of the same type as `f`'s output (`c`)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "So, now that we have this new operator, how does the `complicatedF` function look now? Like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "complicatedF :: [Int] -> Bool\n",
    "complicatedF x = any even . filter (>25) . tail . take 10 $ x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Waaay more readable! You can tell everything the function does with a quick glance!\n",
    "\n",
    "Also, notice that every function to both sides of the `.` operator takes a single argument or is partially applied until it takes a single argument."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "If we rewrite the example from the application operator chapter by using the dot operator, we get:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "show ((2**) (max 3 (2 + 2)))\n",
    "\n",
    "show . (2**) . max 3 $ 2 + 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "As you can see, `$` and `.` can make your code clear and concise. But be wary to not overuse them! You could end up having a worst result!\n",
    "\n",
    "And now, as a final way to make your functions more readable, ladies and gentlemen, we present the point-free style!! 👏👏👏"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "### Point-free style"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "In point-free style (also called tacit programming), function definitions don't declare the arguments.\n",
    "\n",
    "So, instead of doing this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "fourOrLarger :: Int -> Int\n",
    "fourOrLarger x = max 4 x\n",
    "\n",
    "add1 :: Int -> Int\n",
    "add1 x = 1 + x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "We can do this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "fourOrLarger :: Int -> Int\n",
    "fourOrLarger = max 4\n",
    "\n",
    "add1 :: Int -> Int\n",
    "add1 = (1+)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "The functions do the same, but now, we're not explicitly binding the argument and using it inside the body. That's implicit in the definition but still explicit in the signature.\n",
    "\n",
    "Pont-free functions have the advantages of:\n",
    "- Being more compact.\n",
    "- Easier to understand.\n",
    "- Cleaner, since they discard redundant information."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "So, we can use the point-free style to change this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "complicatedF :: [Int] -> Bool\n",
    "complicatedF x = any even . filter (>25) . tail . take 10 $ x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Into this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "complicatedF :: [Int] -> Bool\n",
    "complicatedF = any even . filter (>25) . tail . take 10"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "This gives us our final expression of `complicatedF`."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "This style is particularly useful when deriving efficient programs by calculation and, in general, constitutes good discipline. It helps the writer and reader think about composing functions at the high level instead of shuffling data at the low level."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "This concludes today's lesson. Today we learned plenty of new concepts and ways to improve and combine our functions. It may be a lot to take in at once, but all these concepts are important. So make sure you understand them well before advancing with the course."
   ]
  }
 ],
 "metadata": {
  "celltoolbar": "Slideshow",
  "kernelspec": {
   "display_name": "Haskell",
   "language": "haskell",
   "name": "haskell"
  },
  "language_info": {
   "codemirror_mode": "ihaskell",
   "file_extension": ".hs",
   "mimetype": "text/x-haskell",
   "name": "haskell",
   "pygments_lexer": "Haskell",
   "version": "8.10.7"
  },
  "rise": {
   "enable_chalkboard": true,
   "header": "<img style=\"position: relative; left: 1230px; width: 200px; top: 10px;\" src=\"https://raw.githubusercontent.com/rober-m/haskell-bootcamp/main/images/input-output.svg\"/>"
  },
  "vscode": {
   "interpreter": {
    "hash": "e7370f93d1d0cde622a1f8e1c04877d8463912d04d973331ad4851f04de6915a"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
