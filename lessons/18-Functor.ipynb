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
    "# Functor"
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
    "Welcome to a new lesson of the Haskell curse. This one is all about the `Functor` type class."
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
    "### Functors are 🌏 EVERYWHERE!! 🌎\n",
    "\n",
    "In this lesson:\n",
    "- You'll understand the concept of `Functor`\n",
    "- You'll learn everything you need to know to use them in practice."
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
    "We have Functors in mathematics, programming languages, linguistics, under your bed waiting for you to go to sleep... Functors are everywhere!! You might have worked with functors without even knowing.\n",
    "\n",
    "After this lesson, you will not only understand the concept of `Functor` in Haskell, but we'll also go the extra mile so you can learn everything you need to know to actually use it in practice.\n",
    "\n",
    "And how are we going to do that? This is how:"
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
    "* Abstracting the `map` function\n",
    "* The `Functor` type class\n",
    "* Defining `Functor` instances\n",
    "* Seemingly unintuitive `Functor` instances\n",
    "    * The `Either a` functor 🤔\n",
    "    * The `(,) a` functor 🤨\n",
    "    * The `(->) r` functor 🤯\n",
    "* Defining `<$>` and Lifting 🏋️ a function\n",
    "* `Functor` nesting dolls 🪆\n",
    "* Extra functions and `Functor` as defined in `base`"
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
    "## Abstracting the `map` function"
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
    "This chapter will be super easy since you already know about `map`. Let's implement a function that returns the lower-case version of a String:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"hi, how's it going?\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import Data.Char (toLower)\n",
    "\n",
    "lowerString :: [Char] -> [Char]\n",
    "lowerString []     = []\n",
    "lowerString (x:xs) = toLower x : lowerString xs\n",
    "\n",
    "lowerString \"Hi, How's it Going?\""
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
    "Now, let's implement a function that adds one to a list of numbers:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2,2,3,4]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "addOne :: Num a => [a] -> [a]\n",
    "addOne []     = []\n",
    "addOne (x:xs) = (x + 1) : addOne xs\n",
    "\n",
    "addOne [1,1,2,3]"
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
    "And now, let's implement a function that transforms a list of boolean values to a list of characters representing bits:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"101\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "boolToBit :: [Bool] -> [Char]\n",
    "boolToBit []     = []\n",
    "boolToBit (x:xs) = (if x then '1' else '0') : boolToBit xs\n",
    "\n",
    "boolToBit [True,False,True]"
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
    "Ok. So, I'm sure you see where I'm going with this. There's a repeating pattern, so we'll extract it into its own function.\n",
    "\n",
    "Let's start with the type. As input, we have a list of characters, a list of types that are instances of the `Num` type class, and a list of booleans. So, the most general type would be `[a]` (a list of `a`) for the input list. \n",
    "\n",
    "As output type, at first glance, we could use the same `[a]`, but as we see in the `boolToBit` function, there are cases when you return a list with values of different types. So, there's no need to add an extra restriction to have the same type for the list that goes in and the one that goes out. So, let's use a different variable, like `[b]`:"
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
    "map :: [a] -> [b]\n",
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
    "Now, let's extract the pattern:"
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
    "map []     = []\n",
    "map (x:xs) = f x : map xs\n",
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
    "This looks mostly ok. But we have to get the function `f` from somewhere, so we add it as a parameter. And, because the function `f` takes a value of type `a` from the input list and generates a value of type `b` from the output list, it follows that the function's type is `a -> b`. So, the final expression of our abstraction looks like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"hi, how's it going?\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "[2,2,3,4]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "\"101\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "map :: (a -> b) -> [a] -> [b]\n",
    "map _ []     = []\n",
    "map f (x:xs) = f x : map f xs\n",
    "\n",
    "\n",
    "map toLower \"Hi, How's it Going?\"\n",
    "\n",
    "map (+1) [1,1,2,3]\n",
    "\n",
    "map (\\x -> if x then '1' else '0') [True,False,True]"
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
    "Awesome! We abstracted away the concept of applying an arbitrary function to every value of a list, and we called this abstraction a \"map.\" Then, we used this function to avoid repeating ourselves and simplify our code. This is cool, but we can do better. Let's go one level higher with the `Functor` type class:"
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
    "## Abstracting the `Functor` Type Class"
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
    "In Haskell, we have lots of types. So, let's say we're working with optional values using the `Maybe` type. Same as with lists, we also need a way to conveniently modify values inside `Maybe` types. No biggy, we know the drill. We can define the `maybeMap` function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Just 'a'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Just 4"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Just '1'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Nothing"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Nothing"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Nothing"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "maybeMap :: (a -> b) -> Maybe a -> Maybe b\n",
    "maybeMap _ Nothing  = Nothing\n",
    "maybeMap f (Just x) = Just (f x)\n",
    "\n",
    "\n",
    "maybeMap toLower (Just 'A')\n",
    "\n",
    "maybeMap (+1) (Just 3)\n",
    "\n",
    "maybeMap (\\x -> if x then '1' else '0') (Just True)\n",
    "\n",
    "\n",
    "maybeMap toLower Nothing\n",
    "\n",
    "maybeMap (+1) Nothing\n",
    "\n",
    "maybeMap (\\x -> if x then '1' else '0') Nothing"
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
    "As you can see, the `maybeMap` function can't do anything when the `Maybe` value is `Nothing`. This makes sense: Something went wrong before the value arrived at this function, so we should propagate the error. But, when we have a value, we apply the function to the value and wrap it again in a `Just` constructor."
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
    "Notice how the function we apply as the first parameter in both `map` and `maybeMap` is oblivious to the structure that contains the value it modifies. This is important because it means we could use the same functions in both cases and let `map` and `maybeMap` handle the details."
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {
    "slideshow": {
     "slide_type": "skip"
    }
   },
   "source": [
    "OK. Let's do a harder one. Let's say we want to work with binary trees:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Node (Leaf 2) 1 (Node (Leaf 4) 3 (Leaf 5))"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "data Tree a = Leaf a | Node (Tree a) a (Tree a) deriving (Show, Eq)\n",
    "\n",
    "\n",
    "exampleTree = Node (Leaf 2) 1 (Node (Leaf 4) 3 (Leaf 5))\n",
    "exampleTree\n",
    "\n",
    "\n",
    "--   1\n",
    "--  / \\\n",
    "-- 2   3\n",
    "--    / \\\n",
    "--   4   5"
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
    "Now, I can think of many scenarios that involve modifying the values of each node and leaf without changing the structure of the tree. Maybe the tree represents a family tree, and each number is the age of a family member. After one year passes, we have to update the ages of everyone by one. Or maybe it represents the hierarchical structure of positions in a company, and we have to update the salaries by some percentage to account for inflation.\n",
    "\n",
    "Either way, we need to apply a function to the values without losing the structure. Same as we did for lists and `Maybe` values. So, we create `treeMap`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Node (Leaf 'b') 'a' (Node (Leaf 'd') 'c' (Leaf 'e'))"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Node (Leaf 3) 2 (Node (Leaf 5) 4 (Leaf 6))"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Node (Leaf '0') '1' (Node (Leaf '0') '1' (Leaf '1'))"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "treeMap :: (a -> b) -> Tree a -> Tree b\n",
    "treeMap f (Leaf x)       = Leaf (f x)\n",
    "treeMap f (Node lt x rt) = Node (treeMap f lt) (f x) (treeMap f rt)\n",
    "\n",
    "\n",
    "treeMap toLower (Node (Leaf 'B') 'A' (Node (Leaf 'D') 'C'(Leaf 'E')))\n",
    "\n",
    "treeMap (+1) (Node (Leaf 2) 1 (Node (Leaf 4) 3 (Leaf 5)))\n",
    "\n",
    "treeMap (\\x -> if x then '1' else '0') (Node (Leaf False) True (Node (Leaf False) True (Leaf True)))"
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
    "If it's a `Leaf`, `treeMap` applies the function to the current value. And if it's a `Node`, `treeMap` also applies the function to the current value and recursively calls `treeMap` on both branches."
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
    "As you can see, a new pattern is emerging:"
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
    "map :: (a -> b) -> [a] -> [b]\n",
    "map _ []     = []\n",
    "map f (x:xs) = f x : map f xs\n",
    "\n",
    "\n",
    "\n",
    "maybeMap :: (a -> b) -> Maybe a -> Maybe b\n",
    "maybeMap _ Nothing  = Nothing\n",
    "maybeMap f (Just x) = Just (f x)\n",
    "\n",
    "\n",
    "\n",
    "treeMap :: (a -> b) -> Tree a -> Tree b\n",
    "treeMap f (Leaf x)       = Leaf (f x)\n",
    "treeMap f (Node lt x rt) = Node (treeMap f lt) (f x) (treeMap f rt)\n",
    "\n",
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
    "- The `map` function modifies the elements of a list without changing its length or order.\n",
    "- The `maybeMap` modifies the elements of an optional value without changing its nature. It returns `Nothing` if the original value is `Nothing` and `Just` if it's `Just`.\n",
    "- The `treeMap` function modifies the elements of a tree without changing the amount and arrangement of nodes and leaves.\n",
    "\n",
    "In all cases we apply a function to a value or values inside a structure without modifying the structure itself."
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
    "This seems like an extremely valuable abstraction, so let's extract it.\n",
    "\n",
    "To extract `map`, we had to generalize the types of values inside the lists and the function we applied. Because that was what changed between examples.\n",
    "\n",
    "Now, the thing that changes is the structure that holds these values, which, here, is represented by the list, `Maybe`, and `Tree` types. So, we have to provide this abstraction as a type class that types could implement. We'll call this type class `Functor` because of math terminology, but that doesn't change what the abstraction means to us.\n",
    "\n",
    "So, what is a `Functor` in Haskell?"
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
    "A `Functor` is a type that can apply a function to the values of a structure without modifying the structure itself."
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
    "We need only one behavior, the function that does the mapping. If we look at the `map`, `maybeMap`, and `treeMap` functions, we see that the first parameter, the function, is always the same. This makes sense since we said before that we wanted the functions to be independent of the structure. Then, the second and third parameters are always structures of `a`s that become structures of `b`s. So, the type is almost there, we just need to generalize the structure itself. And that's how we obtain the type class definition:"
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
    "class Functor f where\n",
    "  fmap :: (a -> b) -> f a -> f b\n",
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
    "The `fmap` (or \"functor map\") function takes a function that goes from `a` to `b` and a structure `f` containing elements of type `a`, and applies the function to the elements to return the same structure `f` but with elements of type `b`."
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
    "If, for some reason, having polymorphic type constructors such as `f` doesn't feel intuitive, we'll talk more about it when creating instances. But I'd still recommend you revisit lesson 10 (\"Creating Type Classes and Instances\"), where we discuss this subject in depth and define several type classes with increasing levels of complexity.\n",
    "\n",
    "Ok. So, we have our `Functor` type class. But this is not over. We also have the requirement to avoid `fmap` changing the structure. What would that look like, though? Well, let's implement `fmap` for lists the wrong way:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2,3,4]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "[2,2,3,3,4,4]"
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
       "[1,1,1,1,2,2,2,2,3,3,3,3]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "-- map :: (a -> b) -> [a] -> [b]\n",
    "-- map _ []     = []\n",
    "-- map f (x:xs) = f x : map f xs\n",
    "\n",
    "wrongFmap :: (a -> b) -> [a] -> [b]\n",
    "wrongFmap _ []     = []\n",
    "wrongFmap f (x:xs) = f x : f x : wrongFmap f xs\n",
    "\n",
    "map (+1) [1,2,3]\n",
    "wrongFmap (+1) [1,2,3]\n",
    "\n",
    "(map (\\x -> x - 1)) . (map (+1)) $ [1,2,3]\n",
    "(wrongFmap (\\x -> x - 1)) . (wrongFmap (+1)) $ [1,2,3]"
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
    "If the structure doesn't change, we should get the original value if we apply a function and then apply the inverse. In this example, we first add one and then subtract one. In both cases, the types are correct. And we do get the original list using `map`. But because the `wrongMap` implementation concatenates each value twice, we get a completely new list instead of the original one!\n",
    "\n",
    "An easier way to test this, however, would be with a function that doesn't do anything. That way, if we apply `fmap` to that function, we know we should get the same result as if we didn't do anything. Haskell has that function, and it's called `id` for identity:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
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
       "True"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "\"HHeelllloo!!\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "-- id x = x\n",
    "\n",
    "id 3 == 3\n",
    "\n",
    "id [1,2,3] == [1,2,3] -- Apply id to the whole list\n",
    "\n",
    "map id \"Hello!\" == \"Hello!\" -- Apply id to every element of the list\n",
    "\n",
    "wrongFmap id \"Hello!\" == \"Hello!\"\n",
    "\n",
    "wrongFmap id \"Hello!\""
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
    "Same as with `Semigroup` and `Monoid`, since we can't enforce this property through the type system, we'll define a law using this `id` function and ask developers to pretty-please follow it:"
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
    "**Identity law**\n",
    "```haskell\n",
    "fmap id == id\n",
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
    "This basically means: \"If you apply the identity function to every element of a structure using `fmap`, it should be the same as applying the identity function to the whole structure.\"\n",
    "\n",
    "Because you have to return the same value and the `id` function is only concerned about the values inside your structure, you're forced to implement `fmap` in a way that maintains the structure.\n",
    "\n",
    "This is it for this law. One itsy bitsy thing I didn't tell you, though, is that we have a second law. But before you feel betrayed, let me say you don't need to worry about this law! And I'll tell you why. Here's the composition law:"
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
    "**Composition law**\n",
    "```haskell\n",
    "fmap (f . g) == fmap f . fmap g\n",
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
    "This law states that if you apply the composition of two functions to the elements of a structure using `fmap`, you have to get the same result as if you `fmap` one function and then `fmap` the other.\n",
    "\n",
    "This is obviously an important property since we use function composition everywhere. But the cool thing is that you don't have to check for this law when defining your instance! Thanks to Haskell's type system, if you follow the identity law, you also implicitly follow the composition law!! We could prove that using equational reasoning, but it falls out of the scope of the course, so I'll leave a link in the description for the curious ones."
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
    "Ok. So, our final type class looks like this:"
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
    "class Functor f where\n",
    "  fmap :: (a -> b) -> f a -> f b\n",
    "\n",
    "\n",
    "```\n",
    "**Identity law**\n",
    "```haskell\n",
    "fmap id == id\n",
    "```\n",
    "**Composition law**\n",
    "```haskell\n",
    "fmap (f . g) == fmap f . fmap g\n",
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
    "And that's it! This is what `Functor` is about. \n",
    "\n",
    "Some explanations present functors as containers of values. Others, as values that have context. You can think of it however you want. The bottom line is that any type that is an instance of the Functor type class and follows the Functor's laws is a `Functor`.\n",
    "\n",
    "And since we already have our type class, let's define some instances!"
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
    "## Defining `Functor` instances "
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
    "First, let's review the type class kind:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
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
       "</style><span class='get-type'>Eq :: * -> Constraint</span>"
      ],
      "text/plain": [
       "Eq :: * -> Constraint"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
       "</style><span class='get-type'>Ord :: * -> Constraint</span>"
      ],
      "text/plain": [
       "Ord :: * -> Constraint"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
       "</style><span class='get-type'>Functor :: (* -> *) -> Constraint</span>"
      ],
      "text/plain": [
       "Functor :: (* -> *) -> Constraint"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    ":k Eq\n",
    ":k Ord\n",
    ":k Functor"
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
    "Unlike `Eq`, `Ord`, and most other type classes we worked with before, `Functor` takes a type constructor of a kind star to star instead of a concrete type. \n",
    "\n",
    "This means that you can create instances of `Functor` only for type constructors that take one concrete type. Let's see how that looks in practice for the `Maybe` type:"
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
    "Maybe     -- * -> *\n",
    "Maybe a   -- * \n",
    "\n",
    "instance Eq a => Eq (Maybe a) where -- ✅\n",
    "\n",
    "instance Ord a => Ord (Maybe a) where -- ✅\n",
    "\n",
    "instance Functor a => Functor (Maybe a) where -- ❌\n",
    "\n",
    "instance Functor Maybe where -- ✅\n",
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
    "As you can see, for `Eq` and `Ord`, we need to apply `Maybe` to the type variable `a` to get the correct kind. But it is not necessary for `Functor`.\n",
    "\n",
    "Same with lists:"
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
    "[]     -- * -> *\n",
    "[a]    -- * \n",
    "\n",
    "instance Eq a => Eq [a] where -- ✅\n",
    "  ...\n",
    "\n",
    "instance Ord a => Ord [a] where -- ✅\n",
    "  ...\n",
    "\n",
    "instance Functor a => Functor [a] where -- ❌\n",
    "  ...\n",
    "  \n",
    "instance Functor [] where -- ✅\n",
    "  ...\n",
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
    "And, as we saw on lesson 10, if you have a constructor that requires more than one concrete type, you can partially apply it:"
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
    "data Present t a = Empty t | PresentFor t a\n",
    "\n",
    "Present     -- * -> * -> *\n",
    "Present t   -- * -> *\n",
    "Present t a -- *\n",
    "\n",
    "-----------------------------------------------------------------------\n",
    "\n",
    "instance (Eq t, Eq a) => Eq (Present t a) where -- ✅\n",
    "  ...\n",
    "\n",
    "instance (Ord t, Ord a) => Ord (Present t a) where -- ✅\n",
    "  ...\n",
    "\n",
    "instance (Functor t, Functor a) => Functor (Present t a) where -- ❌\n",
    "  ...\n",
    "\n",
    "instance Functor (Present t) where -- ✅\n",
    "  ...\n",
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
    "If you're not 100% clear on this, revisit lesson 10. If you are, let's define some instances!:"
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
    "-- class Functor f where\n",
    "--   fmap :: (a -> b) -> f a -> f b\n",
    "  \n",
    "  \n",
    "instance Functor [] where\n",
    "  -- fmap :: (a -> b) -> [a] -> [b]\n",
    "  fmap _ []     = []\n",
    "  fmap f (x:xs) = f x : fmap f xs\n",
    "\n",
    "\n",
    "instance Functor Maybe where\n",
    "  -- fmap :: (a -> b) -> Maybe a -> Maybe b\n",
    "  fmap _ Nothing  = Nothing\n",
    "  fmap f (Just x) = Just (f x)\n",
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
    "These are the `Functor` instances for lists and `Maybe` types. I added the specialized type as a comment to help you visualize what's going on.\n",
    "\n",
    "We don't run this cell because these instances are already present in the Prelude. But we can create one that it isn't:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "instance Functor Tree where\n",
    "  -- fmap :: (a -> b) -> Tree a -> Tree b\n",
    "  fmap f (Leaf x)       = Leaf (f x)\n",
    "  fmap f (Node lt x rt) = Node (fmap f lt) (f x) (fmap f rt)"
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
    "As you can see, the implementations are the same functions we previously had implemented as separate versions of `map`. So, no surprise there.\n",
    "\n",
    "We, however, now want to check if they work as expected and follow the identity law, so let's do that:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
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
       "\"010\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Just '1'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Node (Leaf '0') '1' (Node (Leaf '0') '1' (Leaf '1'))"
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
    "boolToBit :: Bool -> Char\n",
    "boolToBit x = if x then '1' else '0'\n",
    "\n",
    "exampleTree = Node (Leaf False) True (Node (Leaf False) True (Leaf True))\n",
    "\n",
    "fmap boolToBit [False,True,False]\n",
    "\n",
    "fmap boolToBit (Just True)\n",
    "\n",
    "fmap boolToBit exampleTree\n",
    "\n",
    "fmap id [1,2,3] == id [1,2,3]\n",
    "\n",
    "fmap id (Just 'c') == id (Just 'c')\n",
    "\n",
    "fmap id exampleTree == id exampleTree"
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
    "And those were our first three Functors in action. If you made it up until here, you learned what Functors are. But stay with me because there are a few practical aspects that you should really know about."
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
    "## Seemingly unintuitive `Functor` instances"
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
    "A few `Functor` instances seem unintuitive at first, and many new Haskell developers struggle to make sense of them. As part of my effort to give you the whole picture, let's explore them."
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
    "### The `Either a` functor 🤔"
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
    "The `Either` type constructor that takes two concrete types:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
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
       "</style><span class='get-type'>Either :: * -> * -> *</span>"
      ],
      "text/plain": [
       "Either :: * -> * -> *"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
       "</style><span class='get-type'>Either String :: * -> *</span>"
      ],
      "text/plain": [
       "Either String :: * -> *"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    ":k Either\n",
    ":k Either String"
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
    "So, to create a `Functor` instance, we have to partially apply one type variable:"
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
    "instance Functor (Either a) where\n",
    "  ...\n",
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
    "We could interpret this as the error value of type `a` being (quote and quote) \"part of the structure\" of the functor. This means that values of type `a` should be kept untouched since `fmap` has to preserve the structure.\n",
    "\n",
    "So, the instance of `Functor` for `Either a` is:"
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
    "instance Functor (Either a) where\n",
    "    fmap _ (Left x) = Left x\n",
    "    fmap f (Right y) = Right (f y)\n",
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
    "Which is virtually the same instance as `Maybe`. We ignore the failure case and only apply the function in the success scenario.\n",
    "\n",
    "Here are some examples:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Left 1"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Right 2"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Left 'A'"
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
    "fmap (+1) (Left 1)\n",
    "\n",
    "fmap (+1) (Right 1)\n",
    "\n",
    "fmap toLower (Left 'A')\n",
    "\n",
    "fmap id (Left 'A') == id (Left 'A')\n",
    "\n",
    "fmap id (Right 'A') == id (Right 'A')"
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
    "Wasn't that hard, right? Let's keep going."
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
    "### The `(,) a` functor 🤨"
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
    "These are tuples:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
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
       "</style><span class='get-type'>('c', True) :: (Char, Bool)</span>"
      ],
      "text/plain": [
       "('c', True) :: (Char, Bool)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
       "</style><span class='get-type'>(True, 'c') :: (Bool, Char)</span>"
      ],
      "text/plain": [
       "(True, 'c') :: (Bool, Char)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
       "</style><span class='get-type'>('c', True, 1 :: Int) :: (Char, Bool, Int)</span>"
      ],
      "text/plain": [
       "('c', True, 1 :: Int) :: (Char, Bool, Int)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    ":t ('c', True)\n",
    "\n",
    ":t (True, 'c')\n",
    "\n",
    ":t ('c', True, 1 :: Int)"
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
    "We already discussed in a previous lesson that the type of the tuple, unlike lists, depends on the amount and order of its values. If we ask the kind of all those tuples, of course, we get concrete types:"
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
       "</style><span class='get-type'>(Char, Bool) :: *</span>"
      ],
      "text/plain": [
       "(Char, Bool) :: *"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
       "</style><span class='get-type'>(Bool, Char) :: *</span>"
      ],
      "text/plain": [
       "(Bool, Char) :: *"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
       "</style><span class='get-type'>(Char, Bool, Int) :: *</span>"
      ],
      "text/plain": [
       "(Char, Bool, Int) :: *"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
       "</style><span class='get-type'>[Int] :: *</span>"
      ],
      "text/plain": [
       "[Int] :: *"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
       "</style><span class='get-type'>[] :: * -> *</span>"
      ],
      "text/plain": [
       "[] :: * -> *"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    ":k (Char, Bool)\n",
    ":k (Bool, Char)\n",
    ":k (Char, Bool, Int)\n",
    "\n",
    ":k [Int]\n",
    ":k []"
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
    "But these types are just parentheses with commas that surround other types. So, could we remove the types to get a type constructor like we do with lists? Yes, we can! Because parentheses with commas are value constructors at the value level and type constructors at the type level."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "scrolled": true,
    "slideshow": {
     "slide_type": "slide"
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
       "</style><span class='get-type'>(,) :: * -> * -> *</span>"
      ],
      "text/plain": [
       "(,) :: * -> * -> *"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
       "</style><span class='get-type'>(,,) :: * -> * -> * -> *</span>"
      ],
      "text/plain": [
       "(,,) :: * -> * -> * -> *"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
       "</style><span class='get-type'>(,) Int :: * -> *</span>"
      ],
      "text/plain": [
       "(,) Int :: * -> *"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
       "</style><span class='get-type'>(,,) String Bool :: * -> *</span>"
      ],
      "text/plain": [
       "(,,) String Bool :: * -> *"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    ":k (,)\n",
    ":k (,,)\n",
    "\n",
    "\n",
    ":k (,) Int  -- :k (a,) doesn't work. No sugar for tuples.\n",
    ":k (,,) String Bool "
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
    "These are just type constructors that take other types to create a concrete type. Tuples don't have the nice syntactic sugar that lists have, so we have to write first the constructor and then the type variables instead of having the type variables inside.\n",
    " \n",
    "Based on this, we can create `Functor` instances for tuples as long as we partially apply type variables to get a kind star to star:"
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
    "\n",
    "instance Functor ((,) a) where\n",
    "  ...\n",
    "\n",
    "instance Functor ((,,) a b) where\n",
    "  ...\n",
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
    "So, we have our types. How should we implement these instances? Well, we don't have much of a choice. For the pair, the first value of type `a` is part of the structure we can't touch, and for the tuple of three values, the first two values of type `a` and `b` are part of the structure. So, we can't touch either of those.\n",
    "\n",
    "At the end of the day, the most obvious and straightforward definitions would be these ones:"
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
    "instance Functor ((,) a) where\n",
    "  fmap f (x,y) = (x, f y)\n",
    "\n",
    "\n",
    "instance Functor ((,,) a b) where\n",
    "  fmap f (x,y,z) = (x, y, f z)\n",
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
    "This is sometimes unintuitive because you would assume that we should apply the function to all values, the same as lists. But the key here is to think in terms of value and structure.\n",
    "\n",
    "The values of the lists are all the elements it contains, and the structure is the order and number of elements.\n",
    "\n",
    "The case of tuples is different. For tuples, all the values except for the last one are part of the structure, as evidenced by the type we create the instance for. So, the only thing we can modify is the one value we don't provide a type variable for.\n",
    "\n",
    "Let's test our instances:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1,2)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "('a',2)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "(True,'a',4)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "('A','b')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "(1,'b')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "(2,True,'a')"
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
    "fmap (+1) (1,1)\n",
    "\n",
    "fmap (+1) ('a',1)\n",
    "\n",
    "fmap (*2) (True,'a',2)\n",
    "\n",
    "fmap toLower ('A','B')\n",
    "\n",
    "fmap toLower (1,'B')\n",
    "\n",
    "fmap toLower (2, True, 'A')\n",
    "\n",
    "fmap id ('a',1 ) == id ('a',1 )\n",
    "\n",
    "fmap id (2, True, 'A') == id (2, True, 'A')"
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
    "### The `(->) r` functor 🤯"
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
    "This might blow your mind, but I have to say it... functions are functors! Hear me out. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
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
       "</style><span class='get-type'>(Char, Bool) :: *</span>"
      ],
      "text/plain": [
       "(Char, Bool) :: *"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
       "</style><span class='get-type'>(,) :: * -> * -> *</span>"
      ],
      "text/plain": [
       "(,) :: * -> * -> *"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
       "</style><span class='get-type'>biggerThan3 :: Int -> Bool</span>"
      ],
      "text/plain": [
       "biggerThan3 :: Int -> Bool"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
       "</style><span class='get-type'>(Int -> Bool) :: *</span>"
      ],
      "text/plain": [
       "(Int -> Bool) :: *"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
       "</style><span class='get-type'>(->) :: * -> * -> *</span>"
      ],
      "text/plain": [
       "(->) :: * -> * -> *"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    ":k (Char, Bool)\n",
    ":k (,)\n",
    "\n",
    "biggerThan3 :: Int -> Bool\n",
    "biggerThan3 = (>3)\n",
    "\n",
    ":t biggerThan3\n",
    ":k (Int -> Bool)\n",
    "\n",
    ":k (->)"
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
    "The arrow we use to define the type signatures of functions is a type constructor. This type constructor takes two concrete types and returns a concrete type. \n",
    "\n",
    "Same as when we give two types like `Char` and `Bool` to the pair type constructor to get the type of a pair containing a character and a boolean if we give two types like `Int` and `Bool` to the arrow type constructor, we get the type of a function that takes an `Int` and returns a `Bool`. "
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
    "So, guess what. We can do with the arrow constructor the same we did for pairs to create the `Functor` instance. We'll partially apply a type variable:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "scrolled": false,
    "slideshow": {
     "slide_type": "slide"
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
       "</style><span class='get-type'>(,) :: * -> * -> *</span>"
      ],
      "text/plain": [
       "(,) :: * -> * -> *"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
       "</style><span class='get-type'>(,) Int :: * -> *</span>"
      ],
      "text/plain": [
       "(,) Int :: * -> *"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
       "</style><span class='get-type'>(->) :: * -> * -> *</span>"
      ],
      "text/plain": [
       "(->) :: * -> * -> *"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
       "</style><span class='get-type'>(->) Int :: * -> *</span>"
      ],
      "text/plain": [
       "(->) Int :: * -> *"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    ":k (,)      -- ❌\n",
    ":k (,) Int  -- Functastic! ✅\n",
    "\n",
    ":k (->)     -- ❌\n",
    ":k (->) Int -- Functastic! ✅"
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
    "We also don't have syntactic sugar in this case. So, our `Functor` instance would start like this:"
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
    "instance Functor ((->) r) where\n",
    "  ...\n",
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
    "Remember that the `r` is the first type we apply the constructor to. So, it's the input type of the function.\n",
    "\n",
    "Now, I'm aware this type is a bit overwhelming the first time you encounter it, so let's work our way through it. This is the type of `fmap`:"
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
    "fmap :: (a -> b) ->      f a  ->      f b\n",
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
    "In this particular instance of `fmap`, the Functor `f` is the arrow applied to a type variable:"
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
    "fmap :: (a -> b) -> (->) r a  -> (->) r b -- Specialize f to (->) r\n",
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
    "Haskell has syntactic sugar to show the arrow type in between the types as an infix function. That's how we've always used it. So let's change that:"
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
    "fmap :: (a -> b) -> (r -> a)  -> (r -> b) -- (->) r a = (r -> a) \n",
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
    "And that's the type of `fmap` for this particular instance. \n",
    "\n",
    "Now, we have to figure out the actual implementation. Both arguments are functions, so let's name them `f` and `g`:"
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
    "instance Functor ((->) r) where\n",
    "  -- fmap :: (a -> b) -> (r -> a) -> (r -> b)\n",
    "  fmap          f           g     =    ...\n",
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
    "Ok. So, as always, we need to apply the function `f` to `g` without changing the functor's structure.\n",
    "\n",
    "In this case, the structure is arrow `r` (`(->) r`), which means that before applying `fmap`, the function takes a value of type `r`, so, after `fmap`, the function has to still take a value of type `r`, as shown in the resulting value. So, the only thing that changes is the value returned by the function. Before `fmap` is a value of type `a`, and after is a value of type `b`.\n",
    "\n",
    "I'm pretty sure you could guess only by looking at the types. We need a function that takes `r` and returns `b`. And we have to obtain it using a function that takes `r` and returns `a` and a function that takes an `a` and returns a `b`. So, we compose them:"
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
    "instance Functor ((->) r) where\n",
    "  -- fmap :: (a -> b) -> (r -> a) -> (r -> b)\n",
    "  fmap          f           g     =    f . g\n",
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
    "And that's it. That's the instance. We can write it more succinctly, though. If we follow this series of simple transformations:"
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
    "fmap :: (a -> b) -> (r -> a) -> (r -> b)\n",
    "fmap       f           g     =   f . g\n",
    "fmap       f           g     = (.) f g   -- Move `.` as prefix\n",
    "fmap       f                 = (.) f     -- Rmv `g` from both sides\n",
    "fmap                         = (.)       -- Rmv `f` from both sides\n",
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
    "We get that the `Functor` instance for functions is actually just function composition:"
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
    "instance Functor ((->) r) where\n",
    "  -- fmap :: (a -> b) -> (r -> a) -> (r -> b)\n",
    "  fmap = (.)\n",
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
    "And now, let's try it out and test for the laws. Take into account that because we can not print functions to the console, I'll have to apply the function to some random value:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "scrolled": true,
    "slideshow": {
     "slide_type": "slide"
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
       "</style><span class='get-type'>value1 :: Int -> Int</span>"
      ],
      "text/plain": [
       "value1 :: Int -> Int"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
       "</style><span class='get-type'>(fmap (>4) value1) :: Int -> Bool</span>"
      ],
      "text/plain": [
       "(fmap (>4) value1) :: Int -> Bool"
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
    "value1 :: Int -> Int\n",
    "value1 = (*2)\n",
    "\n",
    ":t value1\n",
    "value1 3\n",
    "\n",
    ":t (fmap (>4) value1)\n",
    "(fmap (>4) value1) 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "scrolled": true,
    "slideshow": {
     "slide_type": "slide"
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
       "</style><span class='get-type'>value2 :: Bool -> Char</span>"
      ],
      "text/plain": [
       "value2 :: Bool -> Char"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'1'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
       "</style><span class='get-type'>(fmap succ value2) :: Bool -> Char</span>"
      ],
      "text/plain": [
       "(fmap succ value2) :: Bool -> Char"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'2'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "value2 :: Bool -> Char -- boolToBit function\n",
    "value2 x = if x then '1' else '0'\n",
    "\n",
    ":t value2\n",
    "value2 True\n",
    "\n",
    ":t (fmap succ value2)\n",
    "(fmap succ value2) True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
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
    }
   ],
   "source": [
    "(fmap id value1) 5 == (id value1) 5\n",
    "\n",
    "(fmap id value2) False == (id value2) False"
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
    "It works!! \n",
    "\n",
    "It's ok if you don't fully understand. This is one of the more abstract `Functor` instances you'll encounter. And, at the end of the day, if you remember that `fmap` for functions is function composition, you'll be fine.\n",
    "\n",
    "Ok! That was the last instance we'll create today. But there are still a few other things about using `Functors` that we have to take a look at."
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
    "## Defining `<$>` and *lifting* 🏋️ a function"
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
    "`fmap` takes only two arguments, so we can easily use it as an infix function:"
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
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Node (Leaf 'b') 'a' (Node (Leaf 'd') 'c' (Leaf 'e'))"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Node (Leaf 'b') 'a' (Node (Leaf 'd') 'c' (Leaf 'e'))"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Just 4"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Just 4"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "\"1010\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "\"1010\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "[2,4,6]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "[2,4,6]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fmap toLower (Node (Leaf 'B') 'A' (Node (Leaf 'D') 'C'(Leaf 'E')))\n",
    "toLower `fmap` (Node (Leaf 'B') 'A' (Node (Leaf 'D') 'C'(Leaf 'E')))\n",
    "\n",
    "\n",
    "fmap (+1) (Just 3)\n",
    "(+1) `fmap` (Just 3)\n",
    "\n",
    "\n",
    "fmap (\\x -> if x then '1' else '0') [True,False,True,False]\n",
    "(\\x -> if x then '1' else '0') `fmap` [True,False,True,False]\n",
    "\n",
    "\n",
    "fmap (*2) [1,2,3]\n",
    "(*2) `fmap` [1,2,3]"
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
    "And, it turns out, it's usually more convenient to apply `fmap` as an infix function. Luckily, the `base` library has us covered, and we have this beauty:"
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
    "(<$>) :: Functor f => (a -> b) -> f a -> f b\n",
    "(<$>) = fmap\n",
    "\n",
    "infixl 1 <&>\n",
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
    "Notice that we have to constrain the `f` type constructor as an instance of the `Functor` type class because we're using `fmap` in the definition.\n",
    "\n",
    "Using this infix synonym for `fmap`, we can write the previous code like this:"
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
       "Node (Leaf 'b') 'a' (Node (Leaf 'd') 'c' (Leaf 'e'))"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Node (Leaf 'b') 'a' (Node (Leaf 'd') 'c' (Leaf 'e'))"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Just 4"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Just 4"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "\"1010\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "\"1010\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "[2,4,6]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "[2,4,6]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "toLower `fmap` (Node (Leaf 'B') 'A' (Node (Leaf 'D') 'C'(Leaf 'E')))\n",
    "toLower <$> (Node (Leaf 'B') 'A' (Node (Leaf 'D') 'C'(Leaf 'E')))\n",
    "\n",
    "\n",
    "(+1) `fmap` (Just 3)\n",
    "(+1) <$> (Just 3)\n",
    "\n",
    "\n",
    "(\\x -> if x then '1' else '0') `fmap` [True,False,True,False]\n",
    "(\\x -> if x then '1' else '0') <$> [True,False,True,False]\n",
    "\n",
    "\n",
    "(*2) `fmap` [1,2,3]\n",
    "(*2) <$> [1,2,3]"
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
    "And that's how you use it.\n",
    "\n",
    "Now, there's a reason as to why this operator has a dollar sign in the middle. This is an allusion to function application. If we look at the types:"
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
    " ($)  ::              (a -> b) ->   a ->   b\n",
    "(<$>) :: Functor f => (a -> b) -> f a -> f b\n",
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
    "We see that it looks quite familiar. Not only type-wise but conceptually as well. We know from lesson 5 that functions are right-associative, so we can surround the two types to the right, and it would be the same as not having them:"
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
    " ($)  ::              (a -> b) -> (  a ->   b)\n",
    "(<$>) :: Functor f => (a -> b) -> (f a -> f b)\n",
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
    "Looking at this, we see that the function application operator takes a function `(a -> b)` and returns the same function `(a -> b)` with no change. Which we already knew. We use this operator only because it's right-associative. Allowing us to remove the parenthesis.\n",
    "\n",
    "But, if we look at the fmap operator (`<$>`), we see that it takes a function `(a -> b)` and returns the same function, but that now works for the functor version of `a` and `b`. This is what we call \"lifting\" a function. We say that the fmap operator (`<$>`) lifts the function `(a -> b)` to be able to work at the `f` level.\n",
    "\n",
    "Just in case it didn't click, let's see two examples:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "scrolled": true,
    "slideshow": {
     "slide_type": "slide"
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
       "</style><span class='get-type'>toLower :: Char -> Char</span>"
      ],
      "text/plain": [
       "toLower :: Char -> Char"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'a'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
       "</style><span class='get-type'>(toLower <$>) :: forall (f :: * -> *). Functor f => f Char -> f Char</span>"
      ],
      "text/plain": [
       "(toLower <$>) :: forall (f :: * -> *). Functor f => f Char -> f Char"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Just 'a'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
       "</style><span class='get-type'>boolToBit :: Bool -> Char</span>"
      ],
      "text/plain": [
       "boolToBit :: Bool -> Char"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "'0'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
       "</style><span class='get-type'>(boolToBit <$>) :: forall (f :: * -> *). Functor f => f Bool -> f Char</span>"
      ],
      "text/plain": [
       "(boolToBit <$>) :: forall (f :: * -> *). Functor f => f Bool -> f Char"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "\"0\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    ":t toLower             -- Type of original function\n",
    "toLower 'A'\n",
    "\n",
    ":t (toLower <$>)       -- Type of lifted function\n",
    "toLower <$> Just 'A'\n",
    "\n",
    "\n",
    "boolToBit :: Bool -> Char\n",
    "boolToBit x = if x then '1' else '0'\n",
    "\n",
    ":t boolToBit            -- Type of original function\n",
    "boolToBit False\n",
    "\n",
    ":t (boolToBit <$>)      -- Type of lifted function\n",
    "boolToBit <$>  [False]"
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
    "And now that we have this new frame of looking at `fmap` and its infix synonym, we can easily understand how to deal with nested functors."
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
    "## `Functor` nesting dolls 🪆"
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
    "Nested functors are pretty common in Haskell because we combine types a lot. For example:"
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
    "value1 :: Either String Bool\n",
    "value1 = Right False\n",
    "\n",
    "value2 :: [Either String Bool]\n",
    "value2 = [Left \"error\", Right True, Right False]\n",
    "\n",
    "value3 :: Maybe [Either String Bool]\n",
    "value3 = Just [Left \"error\", Right True, Right False]\n",
    "\n",
    "value4 :: Tree (Maybe [Either String Bool])\n",
    "value4 = Leaf $ Just [Left \"error\", Right True, Right False]"
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
    "All these values are nested functors. The number at the end of the name indicates the levels of nesting. `value4`, for example, has 4 levels of nesting: The `Either a` functor is inside the list functor, which is inside the `Mabye` functor, which is inside the `Tree` functor.\n",
    "\n",
    "If you notice, all `values` have booleans at their core. So, if we want to modify them, we need to map a function that takes booleans as inputs. We already have `boolToBit`, so let's use that one:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Right '0'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "boolToBit :: Bool -> Char\n",
    "boolToBit x = if x then '1' else '0'\n",
    "\n",
    "fmap boolToBit value1 -- value1 :: Either String Bool"
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
    "So far, so good. Now, if we try to do the same with `value2`: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "<interactive>:1:16: error:\n    • Couldn't match type ‘Either String Bool’ with ‘Bool’\n      Expected type: [Bool]\n        Actual type: [Either String Bool]\n    • In the second argument of ‘fmap’, namely ‘value2’\n      In the expression: fmap boolToBit value2\n      In an equation for ‘it’: it = fmap boolToBit value2"
     ]
    }
   ],
   "source": [
    "fmap boolToBit value2  -- value2 :: [Either String Bool]"
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
    "Of course, we'll get an error because we're trying to apply a function that takes a boolean to an `Either String Bool`. The solution is deceptively simple. If you have two functor levels, you have to lift your function twice. Once to reach the list level and another one to reach the `Either` level:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "scrolled": false,
    "slideshow": {
     "slide_type": "slide"
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
       "</style><span class='get-type'>boolToBit :: Bool -> Char</span>"
      ],
      "text/plain": [
       "boolToBit :: Bool -> Char"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
       "</style><span class='get-type'>(fmap boolToBit) :: forall (f :: * -> *). Functor f => f Bool -> f Char</span>"
      ],
      "text/plain": [
       "(fmap boolToBit) :: forall (f :: * -> *). Functor f => f Bool -> f Char"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
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
       "</style><span class='get-type'>((fmap . fmap) boolToBit) :: forall (f1 :: * -> *) (f2 :: * -> *). (Functor f1, Functor f2) => f1 (f2 Bool) -> f1 (f2 Char)</span>"
      ],
      "text/plain": [
       "((fmap . fmap) boolToBit) :: forall (f1 :: * -> *) (f2 :: * -> *). (Functor f1, Functor f2) => f1 (f2 Bool) -> f1 (f2 Char)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "[Left \"error\",Right '1',Right '0']"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    ":t boolToBit\n",
    ":t (fmap boolToBit)\n",
    ":t ((fmap . fmap) boolToBit)\n",
    "\n",
    "(fmap . fmap) boolToBit value2 -- value2 :: [Either String Bool]"
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
    "And you can do it as many times as needed:"
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
       "Just [Left \"error\",Right '1',Right '0']"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Leaf (Just [Left \"error\",Right '1',Right '0'])"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "(fmap . fmap . fmap) boolToBit value3 -- value3 :: Maybe [Either String Bool]\n",
    "\n",
    "(fmap . fmap . fmap . fmap) boolToBit value4 -- value4 :: Tree (Maybe [Either String Bool])"
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
    "I hope that makes it easier to understand the concept of lifting. If you're still fuzzy about it, work through the types, and it'll make sense.\n",
    "\n",
    "Now, as a final chapter, we'll see what other functions we get for free when we create an instance of functor."
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
    "## Extra functions and `Functor` as defined in `base`"
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
    "Now that we have the `Functor` type class, if we create functions that depend solely on `fmap`, we'll get functions that work for every `Functor`. For example, take a look at this unzip function:"
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
       "(\"abcd\",[2,4,6,8])"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "unzip' :: [(a, b)] -> ([a], [b])\n",
    "unzip' l = (map fst l, map snd l)\n",
    "\n",
    "\n",
    "unzip' [('a', 2), ('b', 4), ('c', 6), ('d', 8)]"
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
    "The `unzip` function takes a list of tuples and returns a tuple containing one list with all the first elements and another with all the second elements. This function can be used (for example) to separate keys and values from key-value pairs.\n",
    "\n",
    "Now, if we look at the definition, we use three functions. The `fst` and `snd` functions work on pairs. And `map` also works only on lists. But we have `fmap` now, a more general version of `map`. So, we can change the type from lists to `Functors` and use `fmap` instead:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "scrolled": true,
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(\"abcd\",[2,4,6,8])"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "(Just 'a',Just 2)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "(Node (Leaf 'a') 'b' (Leaf 'c'),Node (Leaf 2) 4 (Leaf 6))"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "unzipf :: Functor f => f (a, b) -> (f a, f b)\n",
    "unzipf xs = (fst <$> xs, snd <$> xs)\n",
    "\n",
    "\n",
    "unzipf [('a', 2), ('b', 4), ('c', 6), ('d', 8)]\n",
    "\n",
    "unzipf (Just ('a', 2))\n",
    "\n",
    "unzipf $ Node (Leaf ('a', 2)) ('b', 4) (Leaf ('c', 6))"
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
    "Now we have an `unzip` function that works for every `Functor`.\n",
    "\n",
    "That was one example, but we have a few more. Here are all the functions that come for free in the `base` library after you create an instance of `Functor`. Starting with the flipped `fmap` operator:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
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
       "[2,3,4]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Right 4"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "(<&>) :: Functor f => f a -> (a -> b) -> f b \n",
    "as <&> f = f <$> as  -- Flipped version of '<$>'.\n",
    "\n",
    "\n",
    "((+1) <$> (Just 2)) == (Just 2) <&> (+1)\n",
    "\n",
    "\n",
    "[1,2,3] <&> (+1)\n",
    "\n",
    "\n",
    "Right 3 <&> (+1)"
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
    "We have a version of the map infix operator that takes the arguments flipped. First, the functor, and second, the function. This could be useful (for example) when you define a long inline function. If your function is several lines long, having the functor at the end makes it more difficult to spot it. So you can use this instead and provide the functor first.\n",
    "\n",
    "Another one that comes for free is the \"const fmap\" operator :"
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
    "(<$) :: a -> f b -> f a\n",
    "(<$) =  fmap . const -- Replace all locations with the same value\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Just 'a'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Nothing"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "\"aaaaaa\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Node (Leaf 3) 3 (Node (Leaf 3) 3 (Leaf 3))"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "'a' <$ Just 2\n",
    "\n",
    "'a' <$ Nothing\n",
    "\n",
    "'a' <$ [1,2,3,4,5,6]\n",
    "\n",
    "3 <$ (Node (Leaf 'B') 'A' (Node (Leaf 'D') 'C'(Leaf 'E')))"
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
    "As you can see, we completely ignore the value already present in the functor and replace it with the value we provide as the first argument.\n",
    "\n",
    "We also have a flipped version of this one:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Just 'a'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Just 'a'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "\"aaaaaa\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "\"aaaaaa\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "($>) :: Functor f => f a -> b -> f b\n",
    "($>) = flip (<$)  -- Flipped version of '<$'.\n",
    "\n",
    "'a' <$ Just 2\n",
    "\n",
    "Just 2 $> 'a'\n",
    "\n",
    "\n",
    "'a' <$ [1,2,3,4,5,6]\n",
    "\n",
    "[1,2,3,4,5,6] $> 'a'"
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
    "As you can see, they are like arrows pointing to the value you'll get. This makes it easy to know the direction of the operator.\n",
    "\n",
    "And finally, we have the `void` function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Just ()"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "[(),(),(),(),(),()]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Node (Leaf ()) () (Node (Leaf ()) () (Leaf ()))"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "void :: Functor f => f a -> f ()\n",
    "void x = () <$ x  -- Discard or ignore the result of evaluation\n",
    "\n",
    "\n",
    "void (Just 2)\n",
    "\n",
    "void [1,2,3,4,5,6]\n",
    "\n",
    "void (Node (Leaf 'B') 'A' (Node (Leaf 'D') 'C'(Leaf 'E')))"
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
    "This one becomes handy when dealing with side effects. If the functor has side effects, you can map through it to trigger them. And if you only care about those side effects but not the result, you can use `void` to ignore them. We'll talk more about this in the future. Don't worry too much about it for now.\n",
    "\n",
    "So, after all this work, these are all the behaviors we get when defining an instance of `Functor`:"
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
    "class Functor f where\n",
    "    fmap :: (a -> b) -> f a -> f b\n",
    "    \n",
    "    (<$) ::     a    -> f b -> f a\n",
    "    (<$) =  fmap . const  --  Replace with constant value.\n",
    "    {-# MINIMAL fmap #-}\n",
    "    \n",
    "\n",
    "(<$>) :: Functor f => (a -> b) -> f a -> f b\n",
    "(<$>) = fmap         -- An infix synonym for 'fmap'.\n",
    "\n",
    "(<&>) :: Functor f => f a -> (a -> b) -> f b \n",
    "as <&> f = f <$> as  -- Flipped version of '<$>'.\n",
    "\n",
    "($>) :: Functor f => f a -> b -> f b\n",
    "($>) = flip (<$)     -- Flipped version of '<$'.\n",
    "\n",
    "unzip :: Functor f => f (a, b) -> (f a, f b)\n",
    "unzip xs = (fst <$> xs, snd <$> xs) -- Generalization of List's unzip\n",
    "\n",
    "void :: Functor f => f a -> f ()\n",
    "void x = () <$ x     -- Discard or ignore the result of evaluation\n",
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
    "If we look at how `Functor` is defined in the `base` library, we'll see that one of the functions we just talked about is part of the type class, and the rest is not. We don't really care about that. They are all derived from `fmap`, so we still get all of them for free when defining the instance. The only real difference in your day-to-day is that you'll have to import `Data.Functor` to get the ones that are not part of the type class."
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
    "# That's it for today! 😃"
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
    "And that's it for today! I know it's a lot to take in, so feel free to revisit the lesson as many times as needed. Crucially, to genuinely understand it, you'll have to code it yourself. So, make sure to do your homework, and I'll see you in the next one!!"
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
