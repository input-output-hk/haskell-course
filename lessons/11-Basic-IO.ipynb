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
    "# Basic I/O"
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
    "* Pure functions\n",
    "* Introduction to IO actions\n",
    "* IO actions under the hood\n",
    "* IO actions in practice\n",
    "  - The `()` type\n",
    "* Interacting with the user\n",
    "  - `getChar`, `getLine`, and `putStrLn`\n",
    "* Actions are first-class values\n",
    "* Composing IO actions (`>>` and `>>=` operators)\n",
    "* The do block\n",
    "  - Using `let`, nesting do-blocks, escaping `IO` and `return`\n",
    "* The `main` action\n",
    "* Recap"
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
    "## Pure functions"
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
    "So far, we've been working with pure functions. These functions have no side effects and take all their arguments as input and produce a value as an output that depends only on those arguments."
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
    "<img src=\"../images/diagram_purefunc_generic.png\"\n",
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
     "slide_type": "notes"
    }
   },
   "source": [
    "What we mean by input and output is crucial here. A function's input can be only the values we provide as arguments, and its output is the value it returns.\n",
    "\n",
    "For example:"
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
    "<img src=\"../images/diagram_purefunc_lame.png\"\n",
    "  style=\"\n",
    "  display:block;\n",
    "  margin-left: auto;\n",
    "  margin-right: auto;\n",
    "  width: 60%;\"/>"
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
    "The `lame` function takes a single numeric parameter and returns the value multiplied by three. The output of this function depends exclusively on the value we provide as input. So, every time we apply this `lame` function to four, we'll get twelve."
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
    "<img src=\"../images/diagram_purefunc_max6.png\"\n",
    "  style=\"\n",
    "  display:block;\n",
    "  margin-left: auto;\n",
    "  margin-right: auto;\n",
    "  width: 60%;\"/>"
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
    "Even if we don't explicitly show the input of `max6`, we know that because `filter` is partially applied, it takes a list of `Integers`. (I simplified the signature a bit.) Same as before, the output depends exclusively on the value we provide as input. So, every time we apply this `max6` function to the same list, we'll get the same result.\n",
    "\n",
    "And, of course, functions are curried. So if a function looks like it takes multiple arguments, it actually takes a single parameter and returns a function that takes another single parameter, and so on, until all parameters are applied, and we get the final value. If we use the same parameters, we get the same result. And in every intermediate step, we also get the same intermediate result."
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
    "All good so far. But what if we don't have the input yet?\n",
    "\n",
    "What if we want to make an interactive program? A website? Or a game? When we write our program, we have no idea what the user will do with it. We can't know in advance if a player in our game will move to the left or right. Or if a user on our website will click on a specific button or not. \n",
    "\n",
    "Those things happen while running the program, so there's no way for the programmer to pass them as inputs of a function.\n",
    "\n",
    "I mean, we could, but imagine if we chose them beforehand. A game that always does and finishes the same way. Without any way for the player to interact with it. That sounds more like a movie. Still not bad. Until you realize that you can't even show the image on the screen because that would entail sending and receiving information from your computer's screen while running the program. So, if you run this \"game,\" you're basically using your computer as a very expensive heater.\n",
    "\n",
    "The only way to provide our program with the information and capabilities it needs is to give it a method to interact with the real world.\n",
    "\n",
    "And for that, Haskell uses IO actions."
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
    "## Introduction to IO Actions "
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
    "Before starting with IO actions, I'll address the elephant in the room. I just told you that everything we coded so far was pure, and we couldn't interact with it. But we've been interacting with our functions and passing arguments since lesson one! That's because we've been cheating by using GHCi, which performs IO actions in the background without explicitly telling us. So, at the end of the day, if we want our program to interact with the real world, we still need IO actions."
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
    "***IO action* (or just *action*/*computation*)** can interact with and change the world outside our program. "
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
    "The name IO action gives room for misinterpretation. When we talk about IO actions, we're not talking about the input and output of the function. We talk about the input and output between our program and the real world. IO actions can interact with and change the world outside our program. They might or might not interact with the world, but they CAN. That's key. They are **allowed** to interact with the world.\n",
    "\n",
    "These IO actions are what we call a side effect."
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
    "**A side effect is any observable effect other than the effect of returning a value.**"
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
    "That's why all the functions we've written so far have been pure. The only thing they did was to return a value. It might sound a bit abstract, so let's see a few examples so we can build up our intuition:"
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
    "- Obtain the result of what a person typed on the keyboard."
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
    "<img src=\"../images/diagram_IO_keyboard.png\" style=\"\n",
    "  display:block;\n",
    "  margin-left: auto;\n",
    "  margin-right: auto;\n",
    "  width: 55%;\"/>"
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
    "Notice that IO actions are on top of the diagram. We represented functions with boxes that took their inputs from the left and returned the outputs on the right. But now that we're dealing with actions, we indicate side effects at the top of the diagram with arrows going both in and out because side effects can both send and receive information."
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
    "- Show some text, an image, or something on the screen."
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
    "<img src=\"../images/diagram_IO_screen.png\" style=\"\n",
    "  display:block;\n",
    "  margin-left: auto;\n",
    "  margin-right: auto;\n",
    "  width: 55%;\"/>"
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
    "- Call an API or a database (it doesn't really matter what you do)."
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
    "<img src=\"../images/diagram_IO_api.png\" style=\"\n",
    "  display:block;\n",
    "  margin-left: auto;\n",
    "  margin-right: auto;\n",
    "  width: 65%;\"/>"
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
    "Ok, so we are clear about the idea of IO actions. But how does Haskell handle those IO actions?"
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
    "## IO actions under the hood"
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
    "Now, I'm going to show you the definition of the type that alows us to safely interact with the real world using IO actions. A heads up! Don't try to understand the code. We'll only use it to create a mental model of what's happening under the hood.\n",
    "\n",
    "Without further ado, here's the `IO` type:"
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
    "newtype IO a = IO (State# RealWorld -> (# State# RealWorld, a #))\n",
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
    "The `IO` type constructor has a single `IO` value constructor.\n",
    "\n",
    "The interesting part is the function passed as a parameter of the value constructor. It takes the state of the real world, does something to it, and returns a tuple containing the new state of the real world and a value of type `a` that was generated while all that was happening."
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
    "Aren't the designers of Haskell a bunch of smarty-pants? If you give a function the state of the whole real world, that function can do anything! Talk to databases, access files on your computer, allow penguins to fly, anything!\n",
    "\n",
    "We'll use it to print stuff on the screen, though.\n",
    "\n",
    "Of course, this is not what is really happening under this seemingly magical type. But we can think of it this way. The IO type is actually an abstract type."
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
    "**An abstract data type is a type whose representation is hidden 🫣 but provides associated operations.**"
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
    "So, the inner workings of IO are hidden. And instead, we get a bunch of functions and actions that use this type. Which means:"
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
    "**We don't use the IO constructor directly. We use functions and actions that operate with IO values.**"
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
    "So there you go, that's as far as we're going to go about this. If you want to know more, there are tons of tutorials out there, or you could even explore the source code itself! But I'd recommend waiting until you're more fluent in Haskell to tackle that challenge."
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
    "Now, let's switch to the practical side. In practice, we don't care about the details of how the interaction with the real world is handled. We don't even care about how the `IO` type is defined! The only thing we care about is that, if we use it properly, the compiler will handle the details, and we won't get any surprises when running our code. So let's learn how to properly use the `IO` type."
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
    "## IO actions in practice"
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
    "<img src=\"../images/diagram_IO_something.png\"  style=\"\n",
    "  display:block;\n",
    "  margin-left: auto;\n",
    "  margin-right: auto;\n",
    "  width: 55%;\"/>"
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
    "The `IO a` type tells us that `something` is an IO action that first interacts with the real world and then returns a value of type `a`.\n",
    "\n",
    "For example:"
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
    "action1 :: IO Bool             -- Performs IO and returns a Bool\n",
    "\n",
    "action2 :: IO Int              -- Performs IO and returns an Int\n",
    "\n",
    "action3 :: IO (Double -> Char) -- Performs IO and returns a function\n",
    "\n",
    "action4 :: IO ()               -- Performs IO and returns ()\n",
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
    "There are three key things to note here:\n",
    "1. One is that, after performing the action, we get a VALUE of the specified type we can use in our code.\n",
    "2. The other is that the action returns a value AFTER performing the IO action. We CAN NOT get that value without interacting with the real world.\n",
    "3. And finally, we see a new type in the last action: The unit type."
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
    "### The unit type"
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
    "This is the unit type:"
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
    "data () = ()\n",
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
    "We see that it has only one value constructor that takes no parameters (also called a nullary constructor). So, it's a type that has only one possible value (`()`). Also, notice that the type and the value have the same name. \n",
    "\n",
    "But wait! Why do we learn about this just now? Well, because, until now, we've been working with pure functions. If the only thing a pure function does is to return `(),` why do you even bother to use that function? Just use the value directly! And if a function takes the unit value as a parameter, why do you even bother requiring it if it's always the same value? Just remove that parameter and use the unit inside the function directly! \n",
    "\n",
    "So, when you think about it, we could remove the unit type from any pure function and lose nothing. BUT! Now that we're dealing with actions and side effects, there are plenty of cases when we don't care about what the action returns as a value because we care only about the side effect it performs. Take printing something on the screen or deleting a file. We don't need something in return. We care only about the side effect.\n",
    "\n",
    "That's why, now, it makes sense to have this type. To represent a value that we don't care about.\n",
    "\n",
    "If it doesn't quite click, don't worry, we'll see a couple of real-life examples during this lesson. Let's start wit how to retrieve the input from a user."
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
    "## Interacting with the real world (`getChar`, `getLine`, and `putStrLn`)"
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
    "The most basic IO action I can think of is `getChar`:"
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
    "<img src=\"../images/diagram_IO_getChar.png\"  style=\"\n",
    "  display:block;\n",
    "  margin-left: auto;\n",
    "  margin-right: auto;\n",
    "  width: 55%;\"/>"
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
    "This function performs the IO action of asking the user to write a single character on the standard input. As soon as the user writes that character, it takes it and finishes the IO action. The value of type `Char` it returns is the character the user wrote. We can run the function here to see how that looks."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
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
      "<stdin>: hGetChar: end of file"
     ]
    }
   ],
   "source": [
    "-- getChar :: IO Char\n",
    "getChar"
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
    "As you can see, when we run this cell, a text area appears so we can input a character. There's still some magic going on because we're using these Jupyter cells that run GHCi under the hood as training wheels. But we'll get rid of them soon enough. \n",
    "\n",
    "Now, there are cases when a single character is enough, like when you need to confirm or deny an action in a CLI. But what about a whole phrase? For that, we can use another function called  `getLine`:"
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
    "<img src=\"../images/diagram_IO_getLine.png\"  style=\"\n",
    "  display:block;\n",
    "  margin-left: auto;\n",
    "  margin-right: auto;\n",
    "  width: 55%;\"/>"
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
    "This one performs the IO action of asking the user to write a line on the standard input. And the value of type `String` it returns is the text the user wrote until it pressed Enter."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "scrolled": true,
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
      "<stdin>: hGetLine: end of file"
     ]
    }
   ],
   "source": [
    "-- getLine :: IO String\n",
    "getLine"
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
    "The `getChar` and `getLine` functions are great and all. But, if we run a program with just these, it will prompt us for a character or string without any explanation. Like when your dog suddenly stands in front of you and silently but intensely stares at you with puppy eyes. You know it wants something, but what?\n",
    "\n",
    "Not only do we need a way to get but also to send messages to the outside world. And for that, we use `putStrLn`:"
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
    "<img src=\"../images/diagram_IO_putStrLn.png\"  style=\"\n",
    "  display:block;\n",
    "  margin-top:5%;\n",
    "  margin-left: auto;\n",
    "  margin-right: auto;\n",
    "  width: 70%;\"/>"
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
    "`putStrLn` is a function that takes a string as input and returns an IO action. And what does the action returned by `putStrLn` do?"
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
    "<hr/>\n",
    "<img src=\"../images/diagram_IO_putStrLn_Hi.png\"  style=\"\n",
    "  display:block;\n",
    "  margin-top:5%;\n",
    "  margin-left: auto;\n",
    "  margin-right: auto;\n",
    "  width: 55%;\"/>"
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
    "It prints the `String` we previously passed as a parameter to the standard output.\n",
    "\n",
    "As an example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
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
       "Hello World from inside the program!"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "putStrLn \"Hello World from inside the program!\""
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
    "In this case, `putStrLn` is applied to the `String` and returns an action of type `IO ()`. Then, because we're using a Jupyter notebook,  it automatically performs the action, and we get the `String` in our standard output below the cell."
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
    "But check this out:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "x = putStrLn \"Hello World from inside the program!\" "
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
    "If we run the last cell, we don't get the `String` in our standard output. That's because we didn't ask for the action to be performed. We just named it `x`, and that's it. We never actually need the action to be performed, so Haskell didn't perform it.\n",
    "\n",
    "And that's another property of actions. They are what in programming are called first-class values."
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
    "## Actions are first-class values"
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
    "It means that you can treat actions the same as any other value. For example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "-- putStrLn is an example of a function that returns an action\n",
    "\n",
    "\n",
    "-- Bind to names\n",
    "x = putStrLn \"Hello World from inside the program!\"\n",
    "\n",
    "\n",
    "-- Put them inside lists or other data structures\n",
    "listOfActions :: [IO ()]\n",
    "listOfActions = [putStrLn \"a\", putStrLn \"b\"]\n",
    "\n",
    "\n",
    "-- Pass them as function parameters\n",
    "fakeLength :: [IO ()] -> Int\n",
    "fakeLength list = 1 + length list"
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
    "And, if we run the `fakeLenghth` function passing the `listOfActions` as parameters..."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fakeLength listOfActions"
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
    "We don't get any of the messages in the standard output because none of the actions inside the list are performed! Why should they be performed? We just asked about the length of the list, not the values it contains. Remember that Haskell is lazier than a cat sunbathing. It won't do anything unless it has to.\n",
    "\n",
    "So, until they are performed, IO actions are just plans to do something, programs to be run, or actions to be performed. And because the side effects aren't performed while evaluating all those expressions, we can keep reasoning about our code like we're used to. And only care for the actual side effects when we ask Haskell to perform them.\n",
    "\n",
    "So, how can we ask Haskell to perform a few different actions? By composing them with special operators."
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
    "## Composing IO actions (`>>` and `>>=` operators)"
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
    "We'll create a few simple bots to learn how to compose IO actions"
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
    "### Rude bot"
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
    "The first one is a rude bot. As soon as you interact with it, it yells at you.\n",
    "\n",
    "It starts with a simple message:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Hey!"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "rudeBot :: IO ()\n",
    "rudeBot = putStrLn \"Hey!\"\n",
    "\n",
    "rudeBot"
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
    "The bot has to catch its breath before yelling at you again, so we'll add the next phrase in a second action. To do that, we'll introduce the \"then\" operator:"
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
    "(>>) :: IO a -> IO b -> IO b\n",
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
    "This is a specialized signature specifically for IO actions. And as you can see, the operator takes two actions as inputs: `IO a` and `IO b`. It first executes `IO a`, ignores the result (whatever this `a` is), and returns the `IO b` action.\n",
    "\n",
    "If this were a pure operator, the implementation would look like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
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
       "5"
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
    }
   ],
   "source": [
    "pureThen :: a -> b -> b\n",
    "x `pureThen` y = y\n",
    "\n",
    "\n",
    "3 `pureThen` 5\n",
    "\n",
    "3 `pureThen` 5 `pureThen` 6 `pureThen` 'a'"
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
    "We'd be just throwing away the first value and returning the second.\n",
    "\n",
    "But! Because we're dealing with IO actions, this operator has some secret sauce that allows it to perform the first IO action before returning the second one. More specifically:"
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
    "(>>) :: IO a -> IO b -> IO b\n",
    "\n",
    "```\n",
    "\n",
    "\n",
    "**The `>>` operator sequentially composes two actions, discarding any value produced by the first.**"
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
    "For example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "scrolled": false,
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "a\n",
       "b\n",
       "c"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "abc :: IO ()\n",
    "abc = putStrLn \"a\" >> putStrLn \"b\" >> putStrLn \"c\"\n",
    "\n",
    "abc"
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
    "`abc` is an action composed by multiple actions.\n",
    "\n",
    "When we ask Haskell to perform the `abc` action, it first performs the `putStrLn \"a\"` action and discards the result, then performs the `putStrLn \"b\"` action and discards the result, and finally, performs the `putStrLn \"c\"` action and returns whatever the last action returns. So, because `putStrLn \"c\"` returns the unit after the side effects, the `abc` action also returns the unit after the side effects."
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
    "The direction of the arrows indicates the direction of the sequence. We perform actions from left to right.\n",
    "\n",
    "Now, let's use this operator to finish the rude bot:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
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
       "Hey!\n",
       "Get out of my lawn!"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "rudeBot :: IO ()\n",
    "rudeBot = putStrLn \"Hey!\" >> putStrLn \"Get out of my lawn!\"\n",
    "\n",
    "rudeBot"
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
    "Exactly what we wanted!\n",
    "\n",
    "But maybe we could make it even ruder."
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
    "### An even ruder bot"
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
    "How could we make this bot more annoying? Hmm... I know! Let's make it seem interested in us and then yell at us! So it also wastes our time.\n",
    "\n",
    "So, we'll make the bot ask our name, completely ignore it, and then yell at us. All that with this simple code:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
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
      "<stdin>: hGetLine: end of file"
     ]
    }
   ],
   "source": [
    "evenRuderBot :: IO ()\n",
    "evenRuderBot =\n",
    "  putStrLn \"What's your name?\"            -- IO ()\n",
    "    >> getLine                            -- IO String\n",
    "    >> putStrLn \"like I care! Get lost!\"  -- IO ()\n",
    "    \n",
    "evenRuderBot"
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
    "It's getting a bit too long, so we'll split it into several lines.\n",
    "\n",
    "Besides that, not much has changed. The only real change is that we added a `getLine` function between the `putStrLn` ones. But if we run it now, we see that\n",
    "\n",
    "1. First, it performs the side effect of asking for our name in the standard output.\n",
    "2. Then, it performs the side effect of waiting for us to type it and returning that as a value. But because we're using the `>>` operator, we ignore it.\n",
    "3. And finally, it sends the last message."
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
    "It's definitely ruder than before, but maybe we took it too far. Let's learn how to use the value returned by `getLine` by taking our rude bot to therapy."
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
    "### Rude bot  after therapy"
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
    "After therapy, our bot feels way better and wants to be our friend. And for that, it has to use our name. We can't use the `>>` operator cause that ignores it. So, we need another operator that does the same but passes the result of the first action to the second one. And that's the \"bind\" operator."
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
    "(>>=) :: IO a -> (a -> IO b) -> IO b\n",
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
    "This is also a specialized signature for IO actions. It looks complicated, but it's not that different from the `>>` operator.\n",
    "\n",
    "This operator takes an `IO a` action and a function that takes a value of the same type `a` as the one produced by the first action and returns another action, `IO b`. \n",
    "\n",
    "What this operator does, is: It performs the IO action to get the value `a`, then passes that value to the function to get the `IO b` action, and returns that as a result. The operator does not perform the `IO b` action, just the `IO a` action.\n",
    "\n",
    "So:"
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
    "**The `>>=` operator sequentially composes two actions, passing any value produced by the first as an argument to the second.**"
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
    "For example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Hey!!!!!!"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "-- Remainders:\n",
    "-- (>>=) :: IO a  -> (a -> IO b)  -> IO b\n",
    "-- getLine :: IO String\n",
    "\n",
    "\n",
    "yellIt :: String -> IO ()\n",
    "yellIt str = putStrLn (str ++ \"!!!!!!\")\n",
    "\n",
    "yellItBack :: IO ()\n",
    "yellItBack = getLine >>= yellIt\n",
    "\n",
    "yellIt \"Hey\"\n",
    "--yellItBack"
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
    "As you can see, we have the `yellIt` function that takes a String and returns the action of printing that string with a bunch of exclamation marks. \n",
    "\n",
    "And in the `yellItBack` function, we perform the action of `getLine` that returns a String. But instead of throwing the string away, this time, we use the `>>=` operator to pass it as the parameter of `yellIt`. `yellIt` returns that action, and because it's the last one, it gets evaluated too. Sending the outside world the same message but with more emphasis."
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
    "Now, let's use this operator on the—now nicer—bot:"
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
    "response :: String -> IO ()\n",
    "response name = putStrLn $ \"Nice to meet you, \" ++ name ++ \"!\"\n",
    "\n",
    "rudeBotAfterTherapy :: IO ()\n",
    "rudeBotAfterTherapy =\n",
    "  putStrLn \"What's your name?\"\n",
    "    >> getLine\n",
    "    >>= response"
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
    "We create the `rudeBotAfterTherapy` function that first asks for your name. Then, it waits for you to provide it. And after you do, it passes that value to the `response` function that uses it to print a message.\n",
    "\n",
    "It works, but the `response` function is a simple function that we only use once. And we already know what to do in these cases. We use a lambda function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
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
      "<stdin>: hGetLine: end of file"
     ]
    }
   ],
   "source": [
    "rudeBotAfterTherapy :: IO ()\n",
    "rudeBotAfterTherapy =\n",
    "  putStrLn \"What's your name?\"\n",
    "    >> getLine\n",
    "    >>= (\\name -> putStrLn $ \"Nice to meet you, \" ++ name ++ \"!\")\n",
    "    \n",
    "\n",
    "rudeBotAfterTherapy"
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
    "There you go! A simple and compact function with just a little bit of noise."
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
    "### Now it's a chatty bot!"
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
    "Our bot is now completely rehabilitated, and it turns out it's a chatty bot! Let's add a few chatty features! \n",
    "\n",
    "For example, let's add another message that tells us the number of letters our name has:"
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
   "outputs": [],
   "source": [
    "lettersInName :: String -> String\n",
    "lettersInName name =\n",
    "  \"Your name has \"\n",
    "    ++ show (length name)\n",
    "    ++ \" letters, in case you where wandering...\""
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
    "The `lettersInName` function is a pure function that takes a name and returns a silly little comment on it. To add it to our chatty bot, we need to do it like this:"
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
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "<stdin>: hGetLine: end of file"
     ]
    }
   ],
   "source": [
    "chattyBot :: IO ()\n",
    "chattyBot =\n",
    "  putStrLn \"Hey! What's your name?\"\n",
    "    >> getLine\n",
    "    >>= ( \\name ->\n",
    "            putStrLn (\"Nice to meet you, \" ++ name ++ \"!\")\n",
    "              >> putStrLn (lettersInName name)\n",
    "        )\n",
    "\n",
    "\n",
    "chattyBot"
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
    "We need the value `name` (provided as the result of the second action), so we need to compose our action inside that lambda function."
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
    "And now it's more of the same. We can keep adding more and more actions in the same way. Here's something a bit more complicated:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "<stdin>: hGetLine: end of file"
     ]
    }
   ],
   "source": [
    "finalChattyBot :: IO ()\n",
    "finalChattyBot =\n",
    "  putStrLn \"Hey! What's your name?\"\n",
    "    >> getLine\n",
    "    >>= ( \\name ->\n",
    "            putStrLn (\"Nice to meet you, \" ++ name ++ \"!\")\n",
    "              >> putStrLn (lettersInName name)\n",
    "              >> putStrLn (\"So, \" ++ name ++ \", what do you do for fun?\")\n",
    "              >> getLine\n",
    "              >>= ( \\hobby ->\n",
    "                      putStrLn (\"Are you kidding, \" ++ name ++ \"! I love \" ++ hobby ++ \"!\")\n",
    "                  )\n",
    "        )\n",
    "    >> putStrLn \"OK, bye!\"\n",
    "\n",
    "\n",
    "finalChattyBot"
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
    "As you can see, if we keep increasing the interactions, we start to see a pattern. An ugly and hard-to-read pattern.\n",
    "\n",
    "Luckily, we have a sweeter alternative. Enter the \"Do Notation\":"
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
    "## The `do` notation"
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
    "The `do` notation is just syntactic sugar for expressions composed by `>>` an `>>=` operators.\n",
    "\n",
    "We're going to rewrite all the previous expressions with do notation so we can see the difference. Starting with the rude bot:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Hey!"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "rudeBot :: IO ()\n",
    "rudeBot = putStrLn \"Hey!\"\n",
    "\n",
    "rudeBotDo :: IO ()\n",
    "rudeBotDo = do\n",
    "    putStrLn \"Hey!\"\n",
    "\n",
    "\n",
    "rudeBotDo"
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
    "As you can see, we write the keyword `do` after the equal sign. And then,  we start a block with the actions. \n",
    "\n",
    "In this case, this syntax is not useful. It's more straightforward to write it without the `do` syntax!\n",
    "\n",
    "Let's see the second version of the rude bot:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
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
       "Hey!\n",
       "Get out of my lawn!"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "rudeBot :: IO ()\n",
    "rudeBot = putStrLn \"Hey!\" >> putStrLn \"Get out of my lawn!\"\n",
    "\n",
    "rudeBotDo :: IO ()\n",
    "rudeBotDo = do \n",
    "    putStrLn \"Hey!\"\n",
    "    putStrLn \"Get out of my lawn!\"\n",
    "\n",
    "\n",
    "rudeBotDo"
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
    "Now we start to see some slight improvement. It's not much, but we can see that each action is in a different line, making it easier to identify. \n",
    "\n",
    "Without the `do` notation, the actions go from left to right. With the `do` notation, they go from top to bottom. \n",
    "\n",
    "And what about the even ruder bot?"
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
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "<stdin>: hGetLine: end of file"
     ]
    }
   ],
   "source": [
    "evenRuderBot :: IO ()\n",
    "evenRuderBot =\n",
    "  putStrLn \"What's your name?\"  \n",
    "    >> getLine  \n",
    "    >> putStrLn \"like I care! Get lost!\"\n",
    "    \n",
    "    \n",
    "evenRuderBotDo :: IO ()\n",
    "evenRuderBotDo = do\n",
    "  putStrLn \"What's your name?\"  \n",
    "  getLine  \n",
    "  putStrLn \"like I care! Get lost!\"\n",
    "    \n",
    "evenRuderBotDo"
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
    "Same as before, add the `do` keyword, remove the `>>` operators, and you're ready to go. Notice that now we're aligning everything at the same indentation level.\n",
    "\n",
    "Now is when the cool stuff starts. Here we have the rude bot after therapy:"
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
    "rudeBotAfterTherapy :: IO ()\n",
    "rudeBotAfterTherapy =\n",
    "  putStrLn \"What's your name?\"\n",
    "    >> getLine\n",
    "    >>= (\\name -> putStrLn $ \"Nice to meet you, \" ++ name ++ \"!\")"
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
    "How do we handle the `name`? \tIn the previous bot, we ignored it, but now we need a way to bind the result of `getLine` to a name.  For that, we'll introduce the `<-` (left arrow or bind):"
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
    "rudeBotAfterTherapyDo :: IO ()\n",
    "rudeBotAfterTherapyDo = do\n",
    "  putStrLn \"What's your name?\"\n",
    "  name <- getLine -- (getline :: IO String) so (name :: Sring)\n",
    "  putStrLn $ \"Nice to meet you, \" ++ name\n",
    "\n",
    "\n",
    "rudeBotAfterTherapyDo"
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
    "This left arrow binds the result of running the `putStrLn` action to `name`. And once you have the `name` variable, you can use it anywhere after that action.\n",
    "\n",
    "Now let's see how we can use do notation for the chatty bot:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "<stdin>: hGetLine: end of file"
     ]
    }
   ],
   "source": [
    "chattyBot :: IO ()\n",
    "chattyBot =\n",
    "  putStrLn \"Hey! What's your name?\"\n",
    "    >> getLine\n",
    "    >>= ( \\name ->\n",
    "            putStrLn (\"Nice to meet you, \" ++ name ++ \"!\")\n",
    "              >> putStrLn (lettersInName name)\n",
    "        )\n",
    "\n",
    "\n",
    "chattyBotDo :: IO ()\n",
    "chattyBotDo = do\n",
    "  putStrLn \"Hey! What's your name?\"\n",
    "  name <- getLine\n",
    "  putStrLn (\"Nice to meet you, \" ++ name ++ \"!\")\n",
    "  putStrLn $ lettersInName name\n",
    "\n",
    "\n",
    "chattyBotDo"
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
    "Now the differences start to get big! You have to stop on `chattyBot` for a few seconds to grasp what it's doing, but `chattyBotDo` is really easy to follow! \n",
    "\n",
    "Finally, let's compare the most complicated one:"
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
    "finalChattyBot :: IO ()\n",
    "finalChattyBot =\n",
    "  putStrLn \"Hey! What's your name?\"\n",
    "    >> getLine\n",
    "    >>= ( \\name ->\n",
    "            putStrLn (\"Nice to meet you, \" ++ name ++ \"!\")\n",
    "              >> putStrLn (lettersInName name)\n",
    "              >> putStrLn (\"So, \" ++ name ++ \", what do you do for fun?\")\n",
    "              >> getLine\n",
    "              >>= ( \\hobby ->\n",
    "                      putStrLn (\"Are you kidding, \" ++ name ++ \"! I love \" ++ hobby ++ \"!\")\n",
    "                  )\n",
    "        )\n",
    "    >> putStrLn \"OK, bye!\"\n",
    "\n",
    "\n",
    "finalChattyBotDo :: IO ()\n",
    "finalChattyBotDo = do\n",
    "  putStrLn \"Hey! What's your name?\"\n",
    "  name <- getLine\n",
    "  putStrLn (\"Nice to meet you, \" ++ name ++ \"!\")\n",
    "  putStrLn (lettersInName name)\n",
    "  putStrLn (\"So, \" ++ name ++ \", what do you do for fun?\")\n",
    "  hobby <- getLine\n",
    "  putStrLn (\"Are you kidding, \" ++ name ++ \"! I love \" ++ hobby ++ \"!\")\n",
    "  putStrLn \"OK, bye!\""
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
    "Always keep all the statements aligned at the same indentation level to avoid confusing the compiler and having silly errors.\n",
    "\n",
    "As you can see, the `do` notation is nice to read and write! It allows for a more clean and concise code. But waaaaait a minute! This code looks oddly imperative! We're stating what to do step by step in sequence! Wasn't it that declarative code was so great? \n",
    "\n",
    "Until now, all the functions we wrote were pure, which means that, we'd always have the same result, no matter the order of evaluation. That's why we could write declarations and let the compiler handle the details.\n",
    "\n",
    "Now that we have side effects, the order in which things happen matters! We don't want to run the side effect of getting the name before the one that prints the \"What's your name?\" question. That's why we adopt a more imperative style with the do notation."
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
    "That's the do notation, in essence. But there are a few other things regarding the practical aspect of using the `do` notation. It gets a bit more complicated, but not much.\n",
    "\n",
    "Let's start with how to use `let` inside the `do` notation:"
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
    "### Using `let` inside the `do` notation"
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
    "We can use the `let` keyword inside a `do` block like this:"
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
    "unscramble :: IO ()\n",
    "unscramble = do\n",
    "  putStrLn \"Write a bunch of numbers and letters scrambled together:\"\n",
    "  arg <- getLine\n",
    "  let numbers = filter (`elem` \"1234567890\") arg\n",
    "      letters = filter (`notElem` numbers) arg\n",
    "  putStrLn $ \"Numbers: \" ++ numbers\n",
    "  putStrLn $ \"Letters: \" ++ letters\n",
    "\n",
    "\n",
    "unscramble"
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
    "There are a few details to keep in mind:\n",
    "- The constructs bounded with the `let` keyword are lazy. So, even though they occupy a line in the do block, they aren't evaluated unless needed somewhere else.\n",
    "- We don't need the `in` keyword like we do outside the `do` notation. Everything after the let binding can access it. Sames as the variables bounded using the left arrow.\n",
    "- If you have a couple of `let` bindings one after the other. The `let` keyword is needed only for the first one, and you have to maintain all on the same indentation level. It is not mandatory to use this feature (you can write `let` for every single one), but it's convenient."
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
    "This `let` binding syntax is pretty convenient. Same as the ability to nest `do` blocks."
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
    "### Nesting `do` blocks"
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
    "We can nest do blocks as much as we want. For example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "<stdin>: hGetLine: end of file"
     ]
    }
   ],
   "source": [
    "plusADecade :: IO ()\n",
    "plusADecade = do\n",
    "  putStrLn \"What is your age?:\"\n",
    "  ageString <- getLine\n",
    "  let validAge = all (`elem` \"1234567890\") ageString\n",
    "  if validAge\n",
    "    then do\n",
    "      let age = read ageString :: Int\n",
    "      putStrLn $ \"Int 10 years you will be \" ++ show (age + 10) ++ \" years old.\"\n",
    "    else do\n",
    "      putStrLn \"Your age should contain only digits from 0-9. (Press CTRL+C to close)\"\n",
    "      plusADecade\n",
    "\n",
    "\n",
    "\n",
    "plusADecade"
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
    "The `plusADecade` function first asks for the age of the user. Then it checks that the String provided by the user contains only numbers. If it does, we use the `read` function to get the numeric representation, add 10 to it, and print a message about how old the user will be in 10 years.\n",
    "\n",
    "If it doesn't contain only numbers, we print a message letting the user know that only numbers are allowed and recursively call the `plusADecade` function to restart the program."
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
    "Important detail!: The last statement in a do block has to be an expression that returns an IO action of the correct type."
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
    "If we look at how the `plusADecade` function ends, we have two possible cases depending if `validAge` is `True` or `False`.\n",
    "\n",
    "Inside the `then`, we see a do block that ends with a `putStrLn` applied to a string, so the expression is of type `IO ()` like we indicated at the `plusADecade` signature. All good.\n",
    "\n",
    "Inside the `else`, we see  a do block that ends with a recursive call of the `plusADecade` function, so it's of type `IO ()`. All good.\n",
    "\n",
    "Of course, we couldn't have ended with something that returns a value of type `IO Int` or `IO Bool`. But there's more! We can not do something like this:"
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
    "twice :: IO String\n",
    "twice = do\n",
    "  str <- getLine\n",
    "  let tw = str ++ str -- Error"
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
    "Why? Well, let's take a look at this code without all the sugary syntax:"
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
    "twice :: IO String\n",
    "twice =\n",
    "  getLine >>= \\str ->  \n",
    "    let tw = str ++ str in -- Error"
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
    "That's right! If we take a peek under the hood, we see that the `let` binding expands to a complete `let` expression. And the problem is evident: It's an incomplete expression! Let `tw` in what?\n",
    "\n",
    "And that's when the brilliant idea that we all have when first learning Haskell comes to mind. What if I return the `String` like this?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "twice :: IO String\n",
    "twice =\n",
    "  getLine >>= \\str -> \n",
    "    let tw = str ++ str in tw -- Error: Couldn't match type!"
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
    "The let expression is complete. But now we get a type error because we have to return an `IO String`, and we're returning a pure `String`. Easy fix! We can change the type of `twice` to `String` since that's what we're returning!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "twice :: String\n",
    "twice =\n",
    "  getLine >>= \\str -> \n",
    "    let tw = str ++ str in tw  -- Error: Couldn't match type!"
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
    "And, just for completeness, here's the equivalent code with do notation:"
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
    "twice :: String\n",
    "twice = do\n",
    "  str <- getLine\n",
    "  let tw = str ++ str -- tw :: String\n",
    "  tw -- Error: Couldn't match type!"
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
    "If we try to compile any of the last two versions of `twice`, we'll get a type error. But we said that the type is String, and we're returning a String. What's the problem? \n",
    "\n",
    "The problem is that we used the `getLine` impure action inside twice, and we're trying to return a pure value! In Haskell, once you go impure, you can't go back. You can not ask for forgiveness, and there's no redemption. In other words, you can't escape IO."
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
    "### Escaping `IO` and the `return` function"
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
    "Just to make sure there's no confusion:"
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
    "**`return` DOES NOT WORK LIKE IN OTHER PROGRAMMING LANGUAGES! IT'S A DIFFERENT THING!**"
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
    "If you don't know any other programming languages, don't worry about it. I wanted to open with that to avoid confusion or in case you were about to skip this section."
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
    "OK, so let's go back to the problem at hand: Why doesn't this code compile?:"
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
    "twice :: String\n",
    "twice = do\n",
    "  str <- getLine -- (str :: String) because (getLine :: IO String)\n",
    "  let tw = str ++ str -- tw :: String\n",
    "  tw -- Compiler error: Couldn't match type! "
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
    "Because if we allow that to compile, for the one that uses the `twice` function, it would look like it's using a pure function! Pure and impure code would be able to mix without any way of differentiating them! And if that's the case, we'd never be sure if our code is pure, which means that we'd never know if our functions behave like we think they do. We would have to treat everything as if it was impure, and we'd lose all the advantages of purity! No more referential transparency, no more code that's easy to reason about, no more certainty that modifying a function doesn't break anything without you knowing about it, etc.\n",
    "\n",
    "That's why we can not return a pure value if we perform an impure action inside the function. There has to be a way for both the compiler and developer to identify if we used an impure action.\n",
    "\n",
    "The solution is simple: **Once we use any side effect, we will never be able to escape impurity.**\n",
    "\n",
    "How does this work in practice? Well, we can perform IO actions to get the resulting value and work with it (like we did with `getLine` to obtain `str`) as long as we do it inside another IO context! The compiler enforces this by checking that: **A function performing an IO action inside has to return an IO action.**\n",
    "\n",
    "So:"
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
    "twice :: IO ... -- IO of something because we use getLine inside\n",
    "twice = do\n",
    "  str <- getLine -- getLine :: IO String\n",
    "  let tw = str ++ str\n",
    "  -- ... We have to do something else\n",
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
    "Because we performed the `getLine` action inside `twice`, now `twice` has to return an `IO` action."
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
    "Ok, so we want to return `tw`. But `tw` is of type `String`, and we need to return a value of type `IO String`. What can we do now? \n",
    "\n",
    "That's when the `return` function comes in handy:"
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
    "return :: a -> IO a\n",
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
    "The `return` function injects a value inside an `IO` action that does nothing. It takes a value of any type and returns an action that results in that value.\n",
    "\n",
    "Remember when we presented the idea of IO actions that we say they MAY interact with the real world? Well, in this case, it doesn't. The action returned by the `return` function is a dummy action that doesn't produce any side effects and returns the value.\n",
    "\n",
    "This is perfect for our use case. We need a value wrapped in an IO action, but we don't need to perform any more actions. \n",
    "\n",
    "So, using our new function, we obtain the final version of `twice`:"
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
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "<stdin>: hGetLine: end of file"
     ]
    }
   ],
   "source": [
    "twice :: IO String\n",
    "twice = do\n",
    "  str <- getLine\n",
    "  let tw = str ++ str\n",
    "  return tw\n",
    "  \n",
    "twice"
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
    "Which, without sugar, looks like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": false,
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
      "<stdin>: hGetLine: end of file"
     ]
    }
   ],
   "source": [
    "twice' :: IO String\n",
    "twice' =\n",
    "  getLine >>= \\str ->\n",
    "    let tw = str ++ str in return tw\n",
    "\n",
    "twice'"
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
    "Remember that `return` is just a function. It doesn't need to be used at the end, and you could use it multiple times like any other function.\n",
    "\n",
    "And that's how we work with side effects."
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
    "And you may be thinking: \"But, if, once we use an impure action, we have to carry that IO type forever, where does it end? And if we need to interact with the world at the beginning of our program, like when a user clicks the start button, doesn't that mean that the whole program would be impure?\"\n",
    "\n",
    "Those are valid questions. Let's answer them one at a time.\n",
    "\n",
    "Like many other programming languages, Haskell has what it's known as an \"entry point\"."
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
    "## The `main` action"
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
    "The entry point is the place in a program where its execution of it begins. The first thing that runs when you run the program."
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
    "Many programming languages have entry points. And in almost all cases, the entry point is named main. Sometimes it's a function, others a static method. Rust, Java, Dart, C, C++, and many more have it. And, of course, Haskell has it. In Haskell's case, its an IO action called `main`:"
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
    "main :: IO ()\n",
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
    "This action is the only one that gets executed when we run any program written in Haskell. And it always has the type `IO ()`. Actually, you could return a value different than `()`, but it would get ignored because there's nothing above this action. So there's no point. \n",
    "\n",
    "Now, when you interact with the outside world and have to carry out the `IO` type, that's where it ends. In the main action.\n",
    "\n",
    "An important thing to know is that if you want a function or action to be evaluated and performed when running your program, it has to be—directly or indirectly—inside `main`. When composing actions and functions, in the end, we're gluing everything together in a single `IO ()` action that, when run, performs everything as we specified."
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
    "Why do we hear about this just now? Because we've been using GHCi that handles this behind the scenes. But, next lesson, we'll start working with real compiled programs. So we better start practicing now.\n",
    "\n",
    "On that note, let me present to you one of the shortest programs you could write in Haskell:"
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
    "main :: IO ()\n",
    "main = putStrLn \"Hello World!\""
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
    "This is it! A complete Haskell program! You could put this in a Haskell file and compile it using `ghc fileName.hs`,  and you would get a program that prints `\"Hello World!\"` when executed!"
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
    "Ok, so if every time you perform an action, you have to carry the IO, and the first thing a Haskell program runs is an action that has all the code inside... At which moment do we write pure code?"
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
    "Haskell programs in the real world usually have a small `main` function with a couple of actions and pure functions. And inside those pure functions is where the bulk of the code lives. That way, you minimize the interaction with side effects, and most of your code is pure and easy to deal with.\n",
    "\n",
    "Sort of like this:"
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
    "main :: IO ()\n",
    "main = do\n",
    "  config <- getConfig              -- Custom IO action\n",
    "  let result = pureFunction config -- Huge pure function\n",
    "  putStrLn $ \"Done! The result is: \" ++ show result\n",
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
    "The bulk of the code is pure and inside the `pureFunction` that takes a pure `config` value. And a small part of the program interacts with the real world to get the configuration and show the final result."
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
    "And that's pretty much everything I wanted to cover for this lesson. It's a lot to take in, but with everything we covered today and a little practice, you'll have no issues writing interactive programs! \n",
    "\n",
    "And because  I know we covered a lot of new concepts and syntax, here's a recap to use as a refresher while working on the homework:"
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
    "## Pure VS Impure IO recap:"
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
    "| Pure | Impure |\n",
    "| --- | --- |\n",
    "| Always produces the same result when given the same parameters | May produce different results for the same parameters |\n",
    "| Never has side effects | May have side effects |\n",
    "| Never alters state | May alter the global state of the program, system, or world |\n",
    "| Doesn't have `IO` | Has `IO` |\n",
    "| Functions behave nicely | Be extra careful |"
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
    "## Syntax recap"
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
    "|  Symbol  | Meaning |\n",
    "| ---  | ---|\n",
    "| `>>` | Sequentially composes two actions, discarding any value produced by the first |\n",
    "|`>>=` | Sequentially composes two actions, forwarding the value produced by the first to the second |\n",
    "| `return` | Function to inject a value inside a context |\n",
    "| `do` | Start a `do` block |\n",
    "| `<-` | Inside the `do` block: Bind result of performing an action |\n",
    "| `let` | Inside the `do` block: Lazy binding of any expression (it doesn't perform actions) |\n",
    "| `main` | The entry point of a Haskell program. (All functions/actions end in `main`.) |"
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
     "slide_type": "notes"
    }
   },
   "source": [
    "And that's it for today! If you're curious about how to create your own programs, don't worry. Next lesson, we'll learn how to set up our own local development environment, how to use modules, and how to manage Haskell projects. We'll still provide everything in online Jupyter notebooks and online development environments, but we'll remove all training wheels so you can manage your projects by yourself if you want to.\n",
    "\n",
    "Make sure to complete your homework, and I'll see you on the next one! "
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
   "version": "9.0.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
