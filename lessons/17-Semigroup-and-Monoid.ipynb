{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "# Abstractions, Semigroup, and Monoid"
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
    "This is the first lesson of the \"Abstracting Patterns\" section of the course. In this lesson, we'll cover:"
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
    "- What does it mean to abstract a pattern?\n",
    "- Why abstracting patterns (in general)?\n",
    "- Teaser: Why abstracting `Semigroup` and `Monoid`?\n",
    "- The `Semigroup` type class\n",
    "- The `Monoid` type class\n",
    "- What can we do with `Semigroup` and `Monoid`?"
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
    "## What does it mean to abstract a pattern?"
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
    "We humans are very good at detecting patterns. For example, in the 6th lesson of this course, we wrote these functions:"
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
    "sum'     :: [Int]  -> Int\n",
    "sum'     []     = 0\n",
    "sum'     (x:xs) = x + sum' xs\n",
    "\n",
    "product' :: [Int]  -> Int\n",
    "product' []     = 1\n",
    "product' (x:xs) = x * product' xs\n",
    "\n",
    "and'     :: [Bool] -> Bool\n",
    "and'     []     = True\n",
    "and'     (x:xs) = x && and' xs\n",
    "```"
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
    "We figured out that there was a repeating pattern in all of those functions, so we created a single one that contains that pattern and takes whatever is different as arguments:"
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
    "--           +/*/&&    -> 0/1/True -> [Int]/[Bool] -> Int/Bool\n",
    "foldr :: (a -> b -> b) ->    b     ->     [a]      ->    b\n",
    "foldr _ v [] =  v\n",
    "foldr f v (x:xs) = f x (foldr f v xs)\n",
    "```"
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
    "And then, because we had a function that represented the abstract idea of:"
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
    "\"Applying a function to combine the first value of a list and the result of recursively applying the same function to the rest of the list\""
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
    "Or more sucinctly:"
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
    "\"Reducing a list using a binary operator\""
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
    "We replaced the implementation of the original functions with the abstraction like this:"
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
    "sum'     :: [Int]  -> Int\n",
    "sum'     = foldr (+) 0 -- We partially apply foldr\n",
    "\n",
    "product' :: [Int]  -> Int\n",
    "product' = foldr (*) 1\n",
    "\n",
    "and'     :: [Bool] -> Bool\n",
    "and'     = foldr (&&) True\n",
    "```"
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
    "That seires of steps:"
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
    "1. Write some code.\n",
    "2. Identifying a pattern.\n",
    "3. Create a structure* to contain that pattern (if useful).\n",
    "4. Use that structure instead of explicitly writting the pattern.\n",
    "\n",
    "<sub>*By \"structure,\" we mean types, functions, and type classes. Other programming languages may use different ones (like OOP classes).</sub>"
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
    "Ok, so this is what we mean when we talk about abstracting a pattern.\n",
    "\n",
    "As a small caveat, it's important to note that we shouldn't extract all patterns. As I said before, we humans are very good at detecting patterns, but not all of them are worthy of abstraction. But don't worry about that for now. You'll learn to tell the difference with practice."
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
    "## Why abstracting patterns (in general)?"
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
    "One somewhat reasonable question would be to ask: \"Why should I abstract patterns?\" And there are several reasons, the most important ones are:"
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
    "- To easily reuse code"
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
    "As we showed in the previous `foldr` example, now you have to implement the recursive pattern once, and you can use it anywhere."
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
    "- To hide the unimportant details"
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
    "Also, in the previous example, we hid the details of how exactly we implement the recursion inside `foldr`. Thanks to that, the code becomes a short one-liner that only shows what we care about: Which binary function we apply and what is the starting value."
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
    "- To have clear and concise code that you (and others) can quickly understand"
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
    "By using `foldr` instead of explicitly writing the pattern, the reader instantly understands what we're doing. We're folding a list. That's it. 1 second is enough to know what this line does and keep moving. "
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
    "These reasons apply for every correctly derived abstraction. But what about `Semigroup` and `Monoid` specifically?"
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
    "## Teaser: Why abstracting `Semigroup` and `Monoid`?"
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
    "To make sure I get your full attention throughout the rest of this lesson, I'll share a real-world problem that becomes significantly easier by abstracting `Semigroup` and `Monoid`, and that is:"
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
    "### Scalability"
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
    "More specifically:"
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
    "- **Scaling computations**\n",
    "- **Scaling result complexity without increasing code complexity**"
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
    "If you've worked with any programming language in production, you'll likely know this is a tough and complex problem. So, we developers need all the help we can get."
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
    "At the end of the lesson, after learning about `Semigroup` and `Monoid`, we'll see how these abstractions allow us to more easily scale."
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
    "## The `Semigroup` type class"
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
    "In the first example, we abstracted away a pattern into a function, and now we'll abstract away into a type class. This is not something new. If you think about it:"
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
    "``` haskell\n",
    "type Num :: * -> Constraint\n",
    "class Num a where\n",
    "  (+) :: a -> a -> a\n",
    "  (-) :: a -> a -> a\n",
    "  (*) :: a -> a -> a\n",
    "  negate :: a -> a\n",
    "  abs :: a -> a\n",
    "  signum :: a -> a\n",
    "  fromInteger :: Integer -> a\n",
    "```"
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
    "The `Num` type class is an abstraction of the properties and behaviors a number should have. All numbers should be able to be added, subtracted, multiplied, and so on. Some types we think of as numbers behave fundamentally differently in some ways. For example, we can get fractional numbers with `Float`, but we can not with `Integer`. So, the `Num` type class abstracts away only the behaviors every number-like type should have."
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
    "We are going to do the same someone else did for numbers, but for a different concept. Take a look at this code:"
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
    "(\"Abstract \" ++ \"me\") ++ \"!\"  -- \"Abstract me!\"\n",
    "\"Abstract \" ++ (\"me\" ++ \"!\")  -- \"Abstract me!\"\n",
    "\n",
    "(2 * 3) * 4  -- 24\n",
    "2 * (3 * 4)  -- 24\n",
    "\n",
    "(True && False) && True  -- False\n",
    "True && (False && True)  -- False\n",
    "```"
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
    "What do we have in common in all three cases? Well, in all three cases, there's a binary function (a function that takes two parameters) that somehow combines two values of one type to produce a new value of the same type:"
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
    "(++) :: [a] -> [a] -> [a]\n",
    "\n",
    "(*) :: Num a => a -> a -> a\n",
    " \n",
    "(&&) :: Bool -> Bool -> Bool\n",
    "```"
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
    "And, on top of that, the binary operation is associative! Meaning the order in which we apply the binary function doesn't matter. And that's it! That's the whole concept:"
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
    " A `Semigroup` is a type that has an associative binary operation."
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
    "It seems like an arbitrary choice. Like, why this abstraction instead of another? Well, it'll be clear why at the end of the lesson. However, as with all the abstractions we'll cover in this course, it boils down to this: We realized they are more useful than others.\n",
    "\n",
    "Ok. So, now that we have the concept we want to represent and know that we need it to be available for multiple types, we'll create a type class that represents it. \n",
    "\n",
    "Aaand... this is it:"
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
    "class Semigroup a where\n",
    "  (<>) :: a -> a -> a\n",
    "```"
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
    "I know, I know, a bit anti-climactic. All that hype for a two-line type class."
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
    "We chose to use an operator that looks like a diamond instead of a regular prefix function because the most common use case (as we saw in the examples we used to extract the pattern) is to apply the binary function as an infix function."
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
    "Now, wait a minute... what about the assosociativity? Where does that appear in the code? \n",
    "\n",
    "Well, the sad truth is that not even Haskell's type system, the most powerful of all general-purpose mainstream languages, can restrict this property. And, because we can not use code to transmit these requirements, we use laws written in plain text and kindly ask developers to follow them. Of course, developers follow them because these laws bring a lot of value.\n",
    "\n",
    "In this case, every time you create an instance of `Semigroup`, you have to make sure to satisfy the associativity law:"
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
    "**Associativity law:**\n",
    "```haskell\n",
    "x <> (y <> z) = (x <> y) <> z\n",
    "```"
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
    "Ok, we have our abstraction ready. Let's implement an instance to see how that would look, starting with the list instance. \n",
    "\n",
    "We have to choose a binary operation. This is really easy for lists. If you explore the `Prelude` and the `Data.List` modules, or even easier, if you look up the type using Hoogle, you'll find out that there's only one operator that takes two lists to generate another list, and on top of that, it's associative! And that's the `++` operator that appends two lists:"
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
    "(\"Abstract \" ++ \"me\") ++ \"!\"  -- \"Abstract me!\"\n",
    "\"Abstract \" ++ (\"me\" ++ \"!\")  -- \"Abstract me!\"\n",
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
    "Awesome! We have our operator. And now, we can implement our instance. Just this time, I'll show all possible ways to do it. But, I trust that, by now, you could figure this out by yourself:"
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
    "instance Semigroup [a] where\n",
    "  (<>) = (++)\n",
    "\n",
    "-- same as doing:\n",
    "\n",
    "instance Semigroup [a] where\n",
    "  (<>) []     ys = ys\n",
    "  (<>) (x:xs) ys = x : xs <> ys\n",
    "  \n",
    "-- same as doing:\n",
    "\n",
    "instance Semigroup [a] where\n",
    "  []     <> ys = ys\n",
    "  (x:xs) <> ys = x : xs <> ys\n",
    "  \n",
    "```"
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
    "All three implementations are the same thing written differently, so you could choose whichever you want. In this case, because the operator is already defined, the best would be to just use it, as shown in the first implementation. And, if you're curious, that's how it's actually defined in the `base` library."
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
    "To do a rough check that the associativity law holds, we could do a few tests by hand:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
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
    },
    {
     "data": {
      "text/plain": [
       "True"
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
    "(\"is \" <> \"this \") <> \"True?\" == \"is \" <> (\"this \" <> \"True?\")\n",
    "\n",
    "(([1] <> [2]) <> []) <> [3,4] == [1] <> ([2] <> ([] <> [3,4]))\n",
    "\n",
    "([True] <> ([True] <> [False])) == [True] <> [True] <> [False]"
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
    "Of course, this is not proof that the law holds. It's just a suggestion that it seems to work, which is more than enough for us. However, thanks to Haskell's purity, we could prove this law by induction or property testing. That's out of the scope of this course, but I'll link an explanation in the video description. Just in case you're curious."
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
    "Ok, done! We have our first instance of `Semigroup`. It seems we're done with Semigroup, but there's one more thing to take into account: What if there's no clear answer as to which operation we should use? For example, if we're using numbers, a quick search would give us four binary operations:"
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
    "(+)       :: Num a => a -> a -> a\n",
    "(*)       :: Num a => a -> a -> a\n",
    "(-)       :: Num a => a -> a -> a\n",
    "substract :: Num a => a -> a -> a\n",
    "```"
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
    "But wait, if we quickly check of associativity:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
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
    },
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "24"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "24"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "-5"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "(2 + 3) + 4 -- 9\n",
    "2 + (3 + 4) -- 9 ✅\n",
    "\n",
    "(2 * 3) * 4 -- 24\n",
    "2 * (3 * 4) -- 24 ✅\n",
    "\n",
    "(2 - 3) - 4 -- -5\n",
    "2 - (3 - 4) -- 3 ❌\n",
    "\n",
    "(2 `subtract` 3) `subtract` 4 -- 3\n",
    "2 `subtract` (3 `subtract` 4) -- -1 ❌"
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
    "We see that the `(-)` (minus) and `subtract` functions aren't associative. This makes sense because subtraction isn't associative in maths, either.\n",
    "\n",
    "So, we're left with just two functions:"
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
    "(+) :: Num a => a -> a -> a\n",
    "\n",
    "(*) :: Num a => a -> a -> a\n",
    "```"
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
    "Which one should we use? Both functions satisfy the `Semigroup` requirements of being an associative binary function. But we can not choose more than one... or can we? "
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
    "It turns out that some types, in this case, all numeric types, have more than one valid `Semigroup` instance. To resolve this, we create one `newtype` per valid and useful operation that wraps the original type. That way, we can implement as many instances as we need because they are different types!\n",
    "\n",
    "In the current case, because both the sum and product operations are valuable, we'll wrap a type in the `Sum` and `Product` `newtypes`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "newtype Sum a = Sum { getSum :: a }\n",
    "  deriving (Show, Eq)\n",
    "\n",
    "newtype Product a = Product { getProduct :: a }\n",
    "  deriving (Show, Eq)"
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
    "As you can see, we just wrapped the `a` type with a `Sum` and `Product` constructors to get the new `Sum` and `Product` types. On top of that, we used record syntax to easily extract the wrapped value without the need for pattern-matching in case we want to.\n",
    "\n",
    "And now comes the magic. We'll implement their `Semigroup` instances using their corresponding binary operation:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "instance Num a => Semigroup (Sum a) where\n",
    "  (Sum a) <> (Sum b) = Sum (a + b)\n",
    "\n",
    "instance Num a => Semigroup (Product a) where\n",
    "  (Product a) <> (Product b) = Product (a * b)"
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
    "As you can see, the only thing that changes is that we have to make sure the type inside `Sum` and `Product` are also instances of `Num` in order to have the `+` and `*` operators available to us.\n",
    "\n",
    "Other than that, it's just pattern-matching to unwrap the numbers from the parameters, applying the binary operation to the numbers, and wrapping the result.\n",
    "\n",
    "Let's try them!:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "scrolled": true,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Sum {getSum = 5}"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Product {getProduct = 45}"
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
    },
    {
     "data": {
      "text/plain": [
       "30"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "Sum 3 <> Sum 2\n",
    "\n",
    "Product 5 <> Product 9\n",
    "\n",
    "(Sum 4 <> Sum 5) <> Sum 1 == Sum 4 <> (Sum 5 <> Sum 1)\n",
    "\n",
    "getProduct $ Product 3 <> Product 5 <> Product 2\n",
    "\n",
    "-- Sum 9 <> Product 10 -- ❌ Won't compile! Different types!!"
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
    "It works! This is not the only case. We also have two options between all the orderable types:"
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
    "max :: Ord a => a -> a -> a\n",
    "\n",
    "min :: Ord a => a -> a -> a\n",
    "```"
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
    "Both `max` and `min` functions are associative binary operations, and both make sense to use, so we do the same. We create `newtype` wrappers:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "newtype Max a = Max { getMax :: a }\n",
    "  deriving (Show, Eq)\n",
    "\n",
    "newtype Min a = Min { getMin :: a }\n",
    "  deriving (Show, Eq)"
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
    "And then, we create the `Semigroup` instances with the corresponding associative binary operations:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "instance Ord a => Semigroup (Max a) where\n",
    "  (Max a) <> (Max b) = Max (a `max` b)\n",
    "\n",
    "instance Ord a => Semigroup (Min a) where\n",
    "  (Min a) <> (Min b) = Min (a `min` b)"
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
    "Finally, we test it:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Min {getMin = 3}"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Max {getMax = 9}"
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
    },
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "Min 3 <> Min 6\n",
    "\n",
    "Max 9 <> Max 0\n",
    "\n",
    "(Min 4 <> Min 5) <> Min 1 == Min 4 <> (Min 5 <> Min 1)\n",
    "\n",
    "getMax $ Max 3 <> Max 5 <> Max 2"
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
    "The case for booleans is very similar; So similar that, in fact, you'll have to implement it as part of this lesson's homework.\n",
    "\n",
    "But before we move on, let's implement a `Semigroup` for a type we came up with ourselves. For example, the `Severity` type. A type that represents the severity of an emergency:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "data Severity = Low | Medium | High | Critical deriving (Show, Eq)"
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
    "We don't have any pre-existent associative binary operations, so we'll have to come up with one. What do you think would be a good associative binary operation for severity?: "
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
    "(<>) :: Severity -> Severity -> Severity\n",
    "```"
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
    "Pause the video if you want to think about it for a bit. Better yet, try to implement it yourself!\n",
    "\n",
    "Ok. So, we want to combine severity levels. It makes sense that if we have two emergencies of the same severity, we should return one with the same severity. And if they are of different severities, we should return the highest one. So, we could define `Severity`'s `Semigroup` instance like this: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "instance Semigroup Severity where\n",
    "  Critical <> _ = Critical\n",
    "  _ <> Critical = Critical\n",
    "  High <> _     = High\n",
    "  _ <> High     = High\n",
    "  Medium <> _   = Medium\n",
    "  _ <> Medium   = Medium\n",
    "  _ <> _        = Low"
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
    "I think this makes quite a lot of sense. Let's check if the binary operation is actually associative: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "scrolled": true,
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "High"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Medium"
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
    "High <> Medium\n",
    "\n",
    "Low <> Medium <> Low\n",
    "\n",
    "(High <> Low) <> Critical == High <> (Low <> Critical)"
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
    "And that's it! We created our fifth `Semigroup` instance. If you understand everything up until now, the next abstraction will be a piece of cake. So, let's talk about the `Monoid` type class:"
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
    "## The `Monoid` type class"
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
    "The `Monoid` type class builds on top of the `Semigroup` type class to add a small but significant extra behavior. Let's take a look at the same example we saw at the beginning, but with a slight tweak: "
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
    "(\"Abstract \" ++ \"me\") ++ \"!\"        -- \"Abstract me!\"\n",
    "\"Abstract \" ++ \"\" ++ (\"me\" ++ \"!\")  -- \"Abstract me!\"\n",
    "\n",
    "(2 * 3) * 4      -- 24\n",
    "2 * 1 * (3 * 4)  -- 24\n",
    "\n",
    "(True && False) && True          -- False\n",
    "True && True && (False && True)  -- False\n",
    "```"
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
    "Do you notice the changes I made in the code? And what about the changes in the result?\n",
    "\n",
    "As you can see, I added one more operation in the second line of each example, but it doesn't affect the end result because one of the values doesn't do anything. We call a value that doesn't modify the result: The \"Identity\" value. It's not the first time we encountered this concept. We first learned about identities when we learned about recursion and how vital identity values are in defining the base cases.\n",
    "\n",
    "And as you can see, the `1` is the identity for multiplication, the `True` is the identity for `&&`, and the empty string is the identity for concatenating `String`s, which, more generally speaking, means that the empty list is the identity of concatenating lists."
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
    "So, if we speel it out, the pattern we're seeing right here is:"
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
    "A `Monoid` is a type that has an associative binary operation with an identity."
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
    "But we already have a type class representing an associative binary operation. So, instead of repeating ourselves, we can make `Monoid` a subclass of `Semigroup` and add only the identity. Something like this:"
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
    "class Semigroup a => Monoid a where\n",
    "  mempty :: a\n",
    "```"
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
    "Here, the `mempty` value represents the identity. It's called like that due to convention. You can read it as `m` (from `Monoid`) `empty`. \n",
    "\n",
    "And this would be conceptually it. But, if we take a look at the actual `Monoid` type class in Haskell, it might look like this:"
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
    "class Semigroup a => Monoid a where\n",
    "  mempty  :: a             -- Identity element\n",
    "  mappend :: a -> a -> a   -- <>\n",
    "  mconcat :: [a] -> a      -- foldr <> mempty\n",
    "  {-# MINIMAL mempty | mconcat #-}\n",
    "```"
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
    "And why is that? Why the extra functions?\n",
    "\n",
    "Well, because in previous versions of Haskell, we didn't have the `Semigroup` type class. The `Monoid` type class was self-contained, and needed to define its own associative binary operator. The \"monoid append\" or `mappend` function was the associative binary operation we defined in `Semigroup`, and the \"monoid concat\" or `mconcat` function is a behavior that we get for free thanks to having the `mempty` and `mappend` functions. It's just `foldr` applied to the binary operator and `mempty`."
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
    "I say that it \"might look like this\" because, by the time you're watching this video, we might not have `mappend` in `Monoid` anymore since it's redundant now that we have `Semigroup`. \n",
    "\n",
    "We didn't remove `mappend` from `Monoid` when `Semigroup` was introduced because that would've broken virtually every program written in Haskell. So, to avoid receiving angry emails from every Haskell developer, the maintainers phased out the changes to give everyone the time to catch up before removing it."
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
    "Notice, however, that here it's happening the same as it happened with the associativity for `Semigroup`. The restriction that the `mempty` element has to be the identity of the operation is nowhere to be seen. We cannot enforce it with code, so we create laws that indicate to the developer that they have to adhere to some extra rules when implementing `Monoid` instances:"
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
    "**Right identity**\n",
    "```haskell\n",
    "    x <> mempty = x -- e.g.: Sum 4 <> Sum 0 == Sum 4\n",
    "```\n",
    "**Left identity**\n",
    "```haskell\n",
    "    mempty <> x = x -- e.g.: Sum 0 <> Sum 4 == Sum 4 \n",
    "```\n",
    "**Associativity**\n",
    "```haskell\n",
    "    x <> (y <> z) = (x <> y) <> z -- (Semigroup law)\n",
    "```\n",
    "**Concatenation**\n",
    "```haskell\n",
    "    mconcat = foldr (<>) mempty\n",
    "```"
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
    "Ok! Let's implement a few `Monoid` Instances.\n",
    "\n",
    "This is actually pretty easy because we did the hard part when implementing the `Semigroup` type class. These are the `Monoid` instances of all the types we worked with today:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "--instance Monoid [a] where\n",
    "--  mempty = []\n",
    "\n",
    "instance Num a => Monoid (Sum a) where\n",
    "  mempty = Sum 0\n",
    "\n",
    "instance Num a => Monoid (Product a) where\n",
    "  mempty = Product 1\n",
    "\n",
    "instance (Ord a, Bounded a) => Monoid (Max a) where\n",
    "  mempty = Max minBound\n",
    "\n",
    "instance (Ord a, Bounded a) => Monoid (Min a) where\n",
    "  mempty = Min maxBound\n",
    "\n",
    "instance Monoid Severity where\n",
    "  mempty = Low"
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
    "As you can see, all of the instances are pretty straightforward. You have to think of the value that doesn't change the result when applied to the `Semigroup`'s associative binary operation.\n",
    "\n",
    "- If you sum `0` to a value, you get the same initial value.\n",
    "- If you multiply a value by `1`, you get the same initial value.\n",
    "- If you compare if a value is greater than the smallest possible value, you get the same initial value.\n",
    "- If you compare if a value is smaller than the largest possible value, you get the same initial value.\n",
    "- If you combine any severity with the lowest one, you get the same initial severity.\n",
    "\n",
    "Here are a few examples:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "scrolled": true,
    "slideshow": {
     "slide_type": "slide"
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
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Max {getMax = -9223372036854775808}"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Max {getMax = 3}"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Min {getMin = 9223372036854775807}"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Min {getMin = 2}"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Medium"
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
    "Sum 2 <> mempty <> Sum 3 == Sum 2 <> Sum 3 -- True\n",
    "\n",
    "mconcat [Product 2, Product 3, mempty] == Product 2 <> Product 3 -- True\n",
    "\n",
    "(mempty) :: Max Int -- Max {getMax = -9223372036854775808}\n",
    "\n",
    "Max 2 <> mempty <> Max 3 :: Max Int -- Max {getMax = 3}\n",
    "\n",
    "(mempty) :: Min Int -- Min {getMin = 9223372036854775807}\n",
    "\n",
    "mempty <> Min 2 <> mempty :: Min Int -- Min {getMin = 2}\n",
    "\n",
    "mconcat [mempty, Medium, mempty, mempty] -- Medium\n",
    "\n",
    "Sum 9 <> Sum 11 == Sum 9 `mappend` Sum 11 -- True"
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
    "And that's it! We created our first 5 instances of `Monoid`.\n",
    "\n",
    "Now that we know about `Semigroup` and `Monoid`, let's answer the big question. Why are they useful?"
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
    "## What can I do with `Semigroup` and `Monoid`?"
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
    "We already established that by abstracting patterns, you can more easily reduce code, hide implementation details that aren't part of the core logic, and have clear and concise code that you (and others) can quickly understand. But that's for all abstractions in general. What do I gain with `Semigroup` and `Monoid` specifically?"
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
    "### Distributed computation"
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
    "Imagine you have a dataset of stars with various data points: Their size, mass, brightness, etc. And we want to know which one is the oldest.\n",
    "\n",
    "We cannot measure the age of a star, so we have to calculate it with a formula that takes all the data of a star and returns its approximate age.\n",
    "\n",
    "If that computation takes 1 second, and we have a dataset of 1000 stars, it would take around 17 minutes to complete. Not a big deal.\n",
    "\n",
    "But... that's not a realistic number of stars. Gaia, one of the European Space Agency's telescopes, is currently taking precise measurements of close to 1 billion of the brightest stars in the sky. That's too big of a number to wrap our heads around, so let's say we get our hands on a dataset of 1 million stars. If you want to run your function on that dataset, it will take 114 years to complete. You'll likely be dead before that finishes.\n",
    "\n",
    "If only there was a way to reduce the wait time..."
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
    "<img src=\"../images/distributed_computation.png\"\n",
    "  style=\"\n",
    "  display:block;\n",
    "  margin-left: 20%;\n",
    "  margin-right: auto;\n",
    "  width: 64%;\"/>"
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
    "Well, if the result of an `IO` computation is a `Monoid`, the `IO` computation is a `Monoid` too!! This means you could wrap the computation's result with the `Max` monoid, split the work into 200 servers that run in parallel, and merge the results as soon as two consecutive servers finish their computation.\n",
    "\n",
    "The end result? Instead of waiting 114 years, you have to wait only 6 months. 0.5% of the time it would take using a single server. And, of course, you could keep reducing the wait by spinning more servers."
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
    "Now, this feat could be accomplished without a `Semigroup` or `Monoid` instance. But having them made it waaaaay easier. So much easier, in fact, that we didn't have to change the computation!! We just wrapped the result with the `Max` constructor and called it a day. We changed 1 line of code to make our computation parallelizable."
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
    "## Scaling result complexity without increasing code complexity"
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
    "Let's say we have a social media app with a form that a user has to complete with their personal information to create their account:"
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
    "<img src=\"../images/monoid_form_1.png\"\n",
    "  style=\"\n",
    "  display:block;\n",
    "  margin-left: 20%;\n",
    "  margin-right: auto;\n",
    "  width: 64%;\"/>"
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
    "The user asks to be able to configure their experience, so we add a settings page tha its just a another form:"
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
    "<img src=\"../images/monoid_form_2.png\"\n",
    "  style=\"\n",
    "  display:block;\n",
    "  margin-left: 20%;\n",
    "  margin-right: auto;\n",
    "  width: 64%;\"/>"
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
    "After some time, we add a form to change their profile image. We need to add this to the settings. But also inside the one to create an account. So we created a reusable component and put it inside both:"
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
    "<img src=\"../images/monoid_form_3.png\"\n",
    "  style=\"\n",
    "  display:block;\n",
    "  margin-left: 20%;\n",
    "  margin-right: auto;\n",
    "  width: 64%;\"/>"
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
    "Companies also want to use our app, so we added a form for company settings that also has to be inside the one to open the account:"
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
    "<img src=\"../images/monoid_form_4.png\"\n",
    "  style=\"\n",
    "  display:block;\n",
    "  margin-left: 20%;\n",
    "  margin-right: auto;\n",
    "  width: 64%;\"/>"
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
    "Of course, people lose their passwords, so we'll create a reusable form to change our password that we'll put inside the regular user and company settings: "
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
    "<img src=\"../images/monoid_form_5.png\"\n",
    "  style=\"\n",
    "  display:block;\n",
    "  margin-left: 20%;\n",
    "  margin-right: auto;\n",
    "  width: 64%;\"/>"
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
    "Ok, I think that's enough, you get the idea. This is not only about forms. It's the conventional architecture most programs follow:"
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
    "Combine several components of type `A` to generate a \"network\" or \"structure\" of a different type `B`."
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
    "That means that every time we add something that generates a more complex end-user experience, the complexity of our code exponentially increases because we have to not only create the new component but also integrate it into the system. And with each addition, it gets harder and harder."
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
    "Now, what if the forms themselves where `Semigroup`s? In that case, we don't need to worry about integrating them since that's done by our associative binary operation:"
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
    "<img src=\"../images/monoid_form_6.png\"\n",
    "  style=\"\n",
    "  display:block;\n",
    "  margin-left: 15%;\n",
    "  margin-right: auto;\n",
    "  width: 68%;\"/>"
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
    "We combine several components of type `A` to generate a new one of the same type `A`."
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
    "So, if I want to add a new form now, it doesn't matter if we already have 1, 10, or 100 forms. The complexity is always the same. You still have to build the new form, but you get the integration for free."
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
    "Those are two fairly obvious ways that `Semigroup` and `Monoid` instances help. If you want more examples, you'll have to do the homework.\n",
    "\n",
    "And if you're thinking: \"Why did we need to separate `Semigroup` and `Monoid` again? Can't we just have `Monoid` and that's it?\"\n",
    "\n",
    "`Monoid` is more powerful than `Semigroup` because the identity element allows for an easy way to fold and concatenate the elements. So, based on what we know now, it would make sense to only have the `Monoid` type class. But here's the thing: Some types can be instances of `Semigroup` but not of `Monoid`, and it doesn't make sense we have to lose most of the power just because they don't have an identity element. \n",
    "\n",
    "For example, there's a type in Haskell that represents a list that can never be empty. And because of that, it doesn't have an identity element and can never be a `Monoid`! Curious about how that works? Well..."
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
    "# That's it for today!"
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
    "Do your homework to find out, and I'll see you in the next one!"
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
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
