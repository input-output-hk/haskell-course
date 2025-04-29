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
    "# Creating Type Classes and Instances"
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
    "* Overloading\n",
    "* Steps to create Type Classes and Instances\n",
    "* The `Eq` type class\n",
    "\t* Defining the Type Class\n",
    "    * Defining multiple instances\n",
    "\t* Improving our `Eq` type class with mutual recursion (and MCD)\n",
    "\t* Defining an instance for a parameterized type.\n",
    "* The `WeAccept` Type Class\n",
    "* The `Container` Type Class\n",
    "* Exploring `Ord` type class (Subclassing)\n",
    "* Deriving\n",
    "    * Deriving can go wrong\n"
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
    "## Overloading"
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
    "Before learning what Overloading is, let's learn what the word \"date\" means. "
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
    "DATE:"
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
    "What does \"date\" mean? If I'd say that you have only one chance to answer, and I'll give you $100 if you answer correctly, the intuitive answer is: \"It depends!\"\n",
    "\n",
    "If you're saying: \"What is your date of birth?,\" then it means:"
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
    "1. The time at which an event occurs."
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
    "If you're saying: \"Joe took Laura out on a date.\", then it means:"
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
    "2. A social engagement that often has a romantic character (unless Joe gets friend-zoned)."
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
    "If you're saying: \"I'll want to date a fossil,\" I want to believe you're not referring to a romantic social engagement but to:"
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
    "3. The act of estimating or computing a date or chronology."
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
    "And if you look up the word, \"date\" is also the name of a fruit and has even more definitions!\n",
    "\n",
    "In programming, we would say that the word \"date\" is overloaded. Because it has multiple definitions for the same name. \n",
    "\n",
    "The word \"overloading\" is overloaded itself."
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
    "OVERLOADING:"
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
    "In everyday context, it usually means:"
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
    "1. To put too large a load on or in (something)."
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
    "In a regular programming context, it means:"
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
    "2. Having multiple implementations of a function with the same name."
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
    "How this work in practice depends on the language. For example, some languages, like JavaScript, don't support overloading. So you can not do it. And in others, like C++, you can create multiple functions with the same name, and the compiler will choose which definition to use based on the types of the arguments.\n",
    "\n",
    "In Haskell, \"overloading\" means:"
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
    "3. Having multiple implementations of a function or value with the same name."
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
    "Of course, Haskell had to step up the game. In Haskell, overloading is not restricted to functions. Values can be overloaded too. For example:"
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
    "- The literals `1`, `2`, etc. are overloaded because they could be interpreted as any numeric type (`Int`, `Integer`, `Float`, etc.)\n",
    "\n",
    "- The value `minBound` is overloaded because, for example, when used as a `Char`, it will have value `'\\NUL'` while as an `Int`, it's `-2147483648`. \n",
    "\n",
    "- The equality operator (`==`) works with many types, each with its own implementation.\n",
    "\n",
    "- The function `max` also works with many types, each with its own implementation."
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
    "The first two are overloaded values, and the last are overloaded functions. So, we've been using overloaded functions and values all along. The question is: How do we get those in the first place? Well, the mechanism that allows overloading in Haskell is Type Classes."
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
    "## Steps to create Type Classes and Instances"
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
    "In the \"introduction to type classes\" lesson, we saw the utility of type classes. It basically boils down to having functions that can be used by many different types while having the safety that they only take the ones they can work with. So, if you create a function that takes two numbers and adds them together, that function works with all numeric types while also having the compiler stop you when trying to give it a non-numeric type.\n",
    "\n",
    "Type classes are a pretty unique feature–not many programming languages have them. But the good thing is that they're surprisingly easy to use!\n",
    "\n",
    "When creating our own type classes, we only need two things."
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
    "1. Create a Type Class stating some behaviors.\n",
    "\n",
    "\n",
    "2. Make a Type an instance of that Type Class with the implementation of those behaviors for that specific type."
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
    "That's it."
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
    "Practice makes perfect, so let's learn by doing. We'll start by redefining the `Eq` Type Class."
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
    "## The `Eq` type class"
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
    "The `Eq` type class comes with Haskell, so you don't have to define it. But let's say that we live in a world where the `Eq` type class doesn't exist, and every type has its own function to check for equality. Because of that, you have to learn a bunch of different functions that all do the same: Checking for equality.\n",
    "\n",
    "But, as Lennon said, imagine. While living in that horrible world, imagine all the types living in peace and using the same function. It's easy if you try. You may say I'm a dreamer, but let's do it anyway!"
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
    "We can define the `Eq` type class like this:"
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
    "class Eq a where\n",
    "  (==) :: a -> a -> Bool\n",
    "  (/=) :: a -> a -> Bool\n",
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
    "In the first line, we start with the `class` keyword to indicate we're creating a type class. Followed by how the type class will be called (`Eq`). Then, we write a type variable (`a`) that represents any type that will be made an instance of this type class in the future. So, it's like a placeholder. And finally, we use the `where` keyword to start the block where we define the behaviors of our newly created type class.\n",
    "\n",
    "And now comes the cool part. We have to define the behaviors. To do that,  we write the name and type of the functions or values we need. In this case, we define the behaviors to be the `==` function–to check if two values are equal and the `/=` function–to check if two values are different.\n",
    "\n",
    "We also indicate that both take two values of the type `a` we specified as the parameter of the type class and return a `Bool`. `True` if the condition passes, and `False` if it doesn't."
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
    "And done! We have our `Eq` type class ready to go! This means we have the name and types of the two functions that the `Eq` type class provides. We don't have the definitions here because each type will have its own definitions. And those definitions are provided when defining an instance for the type class."
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
    "### Defining an instance for the `Eq` type class"
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
    "First, we need a type, so let's define one for the payment methods a customer can use in our app:"
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
    "data PaymentMethod = Cash | Card | CC -- CC stands for Cryptocurrency\n",
    "\n",
    "type User = (String, PaymentMethod)"
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
    "And if we want, for example, to check if two users have the same payment method, we could write a function like this one:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
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
      "<interactive>:2:28: error:\n    • No instance for (Eq PaymentMethod) arising from a use of ‘==’\n    • In the expression: pm1 == pm2\n      In an equation for ‘samePM’: samePM (_, pm1) (_, pm2) = pm1 == pm2"
     ]
    }
   ],
   "source": [
    "samePM :: User -> User -> Bool\n",
    "samePM (_, pm1) (_, pm2) = pm1 == pm2  -- Won't work!"
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
    "But, the compiler won't let you use this code! And it tells us why:\n",
    "\n",
    "```\n",
    "No instance for (Eq PaymentMethod) arising from a use of ‘==’\n",
    "In the expression: pm1 == pm2\n",
    "```\n",
    "\n",
    "We're using `==` in the expression `pm1 == pm1`. But, because `==` is a behavior of the `Eq` type class, and our new `PaymentMethod` type is not an instance of the `Eq` type class! So it doesn't have the implementations of `==` and `/=` to use. To fix this, we'll make it an instance!"
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
    "-- class Eq a where\n",
    "--   ...\n",
    "\n",
    "instance Eq PaymentMethod where\n",
    "  -- Implementations for Eq behaviors specific to PaymentMethod\n",
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
    "To create an instance, we use the `instance` keyword followed by the name of the type class we want to make an instance for, the type that will be an instance of that type class, and the `where` keyword. Then, inside that block, we implement the functions defined in that type class."
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
    "As you can see, because now we're creating an instance for a type, we replace the type variable (`a`) we had in the type class definition with our specific type (`PaymentMethod`).\n",
    "\n",
    "And because we're creating an instance for the Eq type class, we need to implement the `==` and `/=` functions. So we'll do just that:"
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
   "outputs": [],
   "source": [
    "-- class Eq a where\n",
    "--   (==) :: a -> a -> Bool\n",
    "--   (/=) :: a -> a -> Bool\n",
    "\n",
    "-- data PaymentMethod = Cash | Card | CC\n",
    "\n",
    "instance Eq PaymentMethod where\n",
    "  -- Implementation of ==\n",
    "  Cash == Cash = True\n",
    "  Card == Card = True -- Same as: (==) Card Card = True\n",
    "  CC == CC = True\n",
    "  _ == _ = False\n",
    "  \n",
    "  -- Implementation of /=\n",
    "  Cash /= Cash = False\n",
    "  Card /= Card = False\n",
    "  CC /= CC = False\n",
    "  _ /= _ = True"
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
    "And that's it! That's how you define a type class and make a type an instance of it! Now, `PaymentMethod` can freely use the `Eq` behaviors (`==` and `/=`):"
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
       "False"
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
    "Card == Cash\n",
    "CC /= Card"
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
    "And the previous function will work now:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
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
    "samePM :: User -> User -> Bool\n",
    "samePM (_, pm1) (_, pm2) = pm1 == pm2  -- It's alive! \n",
    "\n",
    "samePM (\"Rick\", CC) (\"Marta\", CC)"
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
    "### Improving our `Eq` type class with Mutual Recursion"
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
    "Our work is technically done. We have our type class and our instance. But there's a property of the functions we just defined that we're not taking advantage of.\n",
    "\n",
    "If two values are equal, that means they are not different, and if they are different, that means they are not equal. So, we know that for each pair of values, `==` and `/=` will always give us the opposite `Bool` value.\n",
    "\n",
    "We're on our way to becoming epic Haskell developers, and epic Haskell developers can do better than that. So let's use this knowledge to improve our type class and instance! Starting by redefining the `Eq` type class like this:"
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
    "class Eq a where\n",
    "  (==), (/=)  :: a -> a -> Bool\n",
    "  x /= y      = not (x == y)\n",
    "  x == y      = not (x /= y)\n",
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
    "**Which is how `Eq` is actually defined in Haskell!**"
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
    "Let's analyze this code. Because both functions have the same type, we can specify them in a single line. And, yes, we're also writing function definitions inside the type class. We can do that as long as they are type-agnostic because they have to work with all types.\n",
    "\n",
    "Looking at the definitions in more detail, we see we're using the `not` function. The `not` function takes a boolean and returns its opposite.\n",
    "\n",
    "So, in the third line, we're saying that the result of applying `/=` to `x` and `y` is the oposite (`not`) of the result of applying `==` to the same `x` and `y`. And in the fourth line, we're saying that the result of applying `==` to `x` and `y` is the oposite (`not`) of the result of applying `/=` to the same `x` and `y`.\n",
    "\n",
    "This is called mutual recursion because both functions are defined in terms of each other. By defining `==` and `/=` as the opposite of each other, Haskell can infer the behavior of one from the other. \n",
    "\n",
    "And, of course, like any other recursion, it needs a base case to know when to stop the recursion! And that's what we provide when implementing an instance! For example, let's redefine the PaymentMethod instance for this new type class:"
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
    "instance Eq PaymentMethod where\n",
    "  Cash == Cash = True\n",
    "  Card == Card = True\n",
    "  CC == CC = True\n",
    "  _ == _ = False"
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
    "That's it! Because now the compiler can infer the value of one function with the other, we don't need to implement both `==` and `/=`. We can implement the more convenient one and call it a day!"
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
    "This is called **minimal complete definition**. Because it's the minimum you have to implement to get a fully functional instance. You can take advantage of this by checking the minimal complete definition of any type class using `:i <type class>` and implementing only those behaviors. For example, if you run `:i Eq` in GHCi, you'll get:"
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
    "type Eq :: * -> Constraint -- Eq takes a concrete type and returns a Constraint\n",
    "class Eq a where\n",
    "  (==) :: a -> a -> Bool\n",
    "  (/=) :: a -> a -> Bool\n",
    "  {-# MINIMAL (==) | (/=) #-}\n",
    "\n",
    "-- ... and a bunch of instances.\n",
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
    "In this line:\n",
    "\n",
    "```haskell\n",
    "{-# MINIMAL (==) | (/=) #-}\n",
    "```\n",
    "\n",
    "It says that to have the *minimal complete definition* of the type class, you have to implement either `==` OR `/=`."
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
    "In the real world, almost all types are instances of the `Eq` type class. But remember, we're in a parallel universe where you're a visionary creating the `Eq` type class to make the world a better place. So, if we stop here, the `==` and `/=` functions wouldn't be overloaded! Because they would have only the definition for `PaymentMethod`.\n",
    "\n",
    "But there's a reason you decided to create this `Eq` type class. And the reason is that you thought the behaviors it provides are useful for many types. For example, the Blockchain type:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "scrolled": false,
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
    "-- Create data type\n",
    "data Blockchain = Cardano | Ethereum | Bitcoin\n",
    "\n",
    "-- Create instance of Eq\n",
    "instance Eq Blockchain where\n",
    "    Cardano == Cardano = True\n",
    "    Ethereum == Ethereum = True\n",
    "    Bitcoin == Bitcoin = True\n",
    "    _ == _ = False\n",
    "\n",
    "\n",
    "-- Test\n",
    "Cardano /= Cardano"
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
    "Now, the `==` and `/=` are truly overloaded because they have more than one definition depending on the type of values they are applied to.\n",
    "\n",
    "We did it!! And we're on a roll, so let's keep going!\n",
    "\n",
    "So far, we've created two instances of the `Eq` type class. Both for non-parameterized types. Let's learn how we can define an instance for a parameterized type."
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
    "### Defining an instance for a parameterized type"
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
    "To create an instance for a parameterized type, first, we need the parameterized type:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "data Box a = Empty | Has a"
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
    "Now we can create our instance. But we can't do it like this:"
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
    "instance Eq Box where\n",
    "-- ...\n",
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
    "Why? Well, if we take a look at the type class using the `:i` command:"
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
    "type Eq :: * -> Constraint -- Eq takes a concrete type and returns a Constraint\n",
    "class Eq a where\n",
    "  (==) :: a -> a -> Bool\n",
    "  (/=) :: a -> a -> Bool\n",
    "  {-# MINIMAL (==) | (/=) #-}\n",
    "\n",
    "-- ... and a bunch of instances.\n",
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
    "We get remided that the type variable `a` is a concrete type. We can see this in two places:\n",
    "- If we check the types of the functions, we see that the type variable `a` is alone between arrows, so it represents a concrete type by itself.\n",
    "- And, because of that, the kind of `Eq` (`type Eq :: * -> Constraint`) clearly states that it takes a concrete type and produces a `Constraint`.\n",
    "\n",
    "Type classes always have a kind that returns a `Constraint` because type classes don't produce a type. They produce a constraint for polymorphic values. So, If we see a kind that ends in `Constraint`, we know it's a type class, and it goes to the left of the `=>` arrow to constraint polymorphic types. \n",
    "\n",
    "On top of that, we don't need to check the functions to know how the type class uses the type variable `a`. The kind already tells us if it needs a concrete type or a specific type constructor.\n",
    "\n",
    "So, because of `Eq :: * -> Constraint`, we know that the `a` in `Eq a` is a concrete type. But if we check the kind of `Box`:"
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
       "</style><span class='get-type'>Box :: * -> *</span>"
      ],
      "text/plain": [
       "Box :: * -> *"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    ":k Box"
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
    "We see that it's not a concrete type but a type constructor that takes one type as a parameter and returns a concrete type.\n",
    "\n",
    "So, what do we do? We could apply `Box` to another type to get a concrete type, like this:"
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
       "</style><span class='get-type'>Box Int :: *</span>"
      ],
      "text/plain": [
       "Box Int :: *"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    ":k Box Int"
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
    "That technically gives us a concrete type, so we could create the instances like this:"
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
    "instance Eq (Box Int) where\n",
    "-- ...\n",
    "\n",
    "instance Eq (Box String) where\n",
    "-- ...\n",
    "\n",
    "instance Eq (Box PaymentMethod) where\n",
    "-- ...\n",
    "\n",
    "--- etc\n",
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
    "And it would work perfectly. But, Hmm, this is a lot of work. And we already went through this when defining functions and solved it with type variables. This time is no different!:"
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
    "instance Eq (Box a) where\n",
    "-- ...\n",
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
    "By defining this instance, all the types created using the `Box` type constructor (like `Box String` or `Box Int`) will be an instance of `Eq`.\n",
    "\n",
    "Now, wait a second. How do we define the instance if we don't know the type of the value inside the box? Well, if we decide that:\n",
    "\n",
    "- Two boxes containing equal elements are equal.\n",
    "- Two empty boxes are equal.\n",
    "- And everything else is different.\n",
    "\n",
    "We can define the behaviors like this:"
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
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "<interactive>:2:20: error:\n    • No instance for (Eq a) arising from a use of ‘==’\n      Possible fix: add (Eq a) to the context of the instance declaration\n    • In the expression: x == y\n      In an equation for ‘==’: Has x == Has y = x == y\n      In the instance declaration for ‘Eq (Box a)’"
     ]
    }
   ],
   "source": [
    "instance Eq (Box a) where\n",
    "  Has x == Has y = x == y\n",
    "  Empty == Empty = True\n",
    "  _ == _ = False"
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
    "In the first formula, we define `==` for the `Box a` type by applying `==` to the `a` type it contains. Because `Has x` is of type `Box a`, `x` is of type `a`. Same for the rest of values. So, if both boxes contain the same element, the boxes themselves are the same. Else, they are different. So, were making the instance of `Box a` depend on the instance of `a`. \n",
    "\n",
    "In the second formula, we specify that if both boxes are empty, they are equal.\n",
    "\n",
    "For every other case, the boxes are different."
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
    "This makes sense, but there's a HUGE oversight on our part! Did you spot it? It's ok if you didn't. That's what the compiler is here for! If we run the cell, we'll get a compiler error:\n",
    "\n",
    "```\n",
    "No instance for (Eq a) arising from a use of ‘==’\n",
    "```\n",
    "\n",
    "Ok, so the compiler is telling us that we're applying the `==` function to a type that doesn't have an instance of `Eq`.\n",
    "\n",
    "Where are we doing that?\n",
    "\n",
    "```\n",
    "In the expression: x == y\n",
    "In an equation for ‘==’: Has x == Has y = x == y\n",
    "In the instance declaration for ‘Eq (Box a)’\n",
    "```\n",
    "The compiler is correct! We're using `==` between two values (`x` and `y`) of type `a` without making sure that the `a` type itself is an instance of `Eq`!\n",
    "\n",
    "So, what should we do? Well, the compiler also told us how to fix this:\n",
    "\n",
    "```\n",
    "Possible fix: add (Eq a) to the context of the instance declaration\n",
    "```\n",
    "\n",
    "Same as with functions, we can add the constraint that the type `a` in the instance of `Eq (Box a)` has to also be an instance of the `Eq` type class. Like this:"
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
   "outputs": [],
   "source": [
    "instance (Eq a) => Eq (Box a) where\n",
    "  Has x == Has y = x == y\n",
    "  Empty == Empty = True\n",
    "  _ == _ = False"
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
    "This way, the type `Box a` will be an instance of `Eq` for all the types `a` that are also an instance of `Eq`.\n",
    "\n",
    "Aaaaaaand we're done! We can use this new instance like this:"
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
       "False"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "<interactive>:1:1: error:\n    • No instance for (Eq Choice) arising from a use of ‘==’\n    • In the expression: Has Yes == Has No\n      In an equation for ‘it’: it = Has Yes == Has No"
     ]
    }
   ],
   "source": [
    "Has Cardano /= Has Ethereum -- True\n",
    "\n",
    "Has Card == Empty           -- False\n",
    "\n",
    "Has Bitcoin /= Has Bitcoin  -- False\n",
    "\n",
    "\n",
    "data Choice = Yes | No      -- We didn't create an Eq instance for Choice\n",
    "\n",
    "Has Yes == Has No           -- Angry compiler: There's no instance for (Eq Choice), you fool!"
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
    "So, even when wrapping the type inside another type, the compiler will still protect us of our human mistakes.\n",
    "\n",
    "Ok. Now that we did everything step-by-step with the `Eq` type class, let's do everything again, but quicker and with a new type class that it's not part of standard Haskell."
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
    "## The  `WeAccept` Type Class"
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
    "Imagine we're writing an app that accepts payments for a company, and this company doesn't accept all payment methods, blockchains, and countries. So, you have to create functions to check that:"
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
   "outputs": [],
   "source": [
    "-- Function to check if we accept that payment method\n",
    "weAcceptPayment :: PaymentMethod -> Bool\n",
    "weAcceptPayment p = case p of\n",
    "   Cash -> False\n",
    "   Card -> True\n",
    "   CC   -> True\n",
    "\n",
    "-- Function to check if we accept that blockchain\n",
    "weAcceptBlockchain :: Blockchain -> Bool\n",
    "weAcceptBlockchain b = case b of\n",
    "   Bitcoin  -> True\n",
    "   Ethereum -> False\n",
    "   Cardano  -> True\n",
    "\n",
    "-- Country type\n",
    "newtype Country = Country { countryName :: String }\n",
    "\n",
    "-- Function to check if we accept that country\n",
    "weAcceptCountry :: Country -> Bool\n",
    "weAcceptCountry c = case countryName c of\n",
    "   \"Mordor\"  -> False\n",
    "   _         -> True"
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
    "Seeing this code, we realize that this behavior of checking if the company accepts something could be used in many other aspects. Like providers, technologies, etc. There are a lot of things a company could decide to accept or not.\n",
    "\n",
    "To avoid having a bunch of different functions that do the same all over your code, we decide to create a type class that represents this behavior.\n",
    "\n",
    "And that type class looks like this:"
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
       "</style><span class='get-type'>WeAccept :: * -> Constraint</span>"
      ],
      "text/plain": [
       "WeAccept :: * -> Constraint"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "-- Creating WeAccept type class\n",
    "class WeAccept a where\n",
    "  weAccept :: a -> Bool\n",
    "\n",
    "-- Checking kind of WeAccept\n",
    ":k WeAccept"
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
    "Now that we have our type class, we can create the instances for `PaymentMethod`, `Blockchain`, `Country`, and even `Box` like this:"
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
    "instance WeAccept PaymentMethod where\n",
    "  weAccept x = case x of\n",
    "   Cash -> False\n",
    "   Card -> True\n",
    "   CC   -> True\n",
    "\n",
    "instance WeAccept Blockchain where\n",
    "  weAccept x = case x of\n",
    "   Bitcoin  -> True\n",
    "   Ethereum -> False\n",
    "   Cardano  -> True\n",
    "\n",
    "instance WeAccept Country where\n",
    "  weAccept x = case countryName x of\n",
    "    \"Mordor\" -> False\n",
    "    _        -> True\n",
    "\n",
    "instance (WeAccept a) => WeAccept (Box a) where\n",
    "  weAccept (Has x) = weAccept x\n",
    "  weAccept Empty   = False"
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
    "And done! This gives us the ability to apply the overloaded `weAccept` function to three different types:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
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
       "False"
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
       "True"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "weAccept Cardano\n",
    "weAccept Cash\n",
    "weAccept (Country \"Mordor\")\n",
    "weAccept (Has Bitcoin)"
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
    "We can also create functions that can be applied to all the types that are instances of `WeAccept`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"Do something fancy\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "\"Do something fancy\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "\"Don't do it!\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "\"Do something fancy\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "-- Creating fancyFunction\n",
    "fancyFunction :: (WeAccept a) => a -> String\n",
    "fancyFunction x =\n",
    "  if weAccept x\n",
    "    then \"Do something fancy\"\n",
    "    else \"Don't do it!\"\n",
    "    \n",
    "-- Using fancyFunction\n",
    "fancyFunction Cardano\n",
    "fancyFunction Card\n",
    "fancyFunction (Country \"Mordor\")\n",
    "fancyFunction (Has Bitcoin)"
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
    "Another type class under our belt! It's getting easier by the minute! \n",
    "\n",
    "We'll do one more example before continuning to the next section. This one is a bit more difficult, but if you understand it, you'll be able to understand any type class! No matter how complicated it gets!"
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
    "## The `Container` Type Class"
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
    "This is the scenario: We're working on a logistics software that has two different types of packages. A regular box that may or may not contain something, and a present, that may or may not contain something, but that it always has a name tag of who's the present for. So, we have these two types:"
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
       "</style><span class='get-type'>Box :: * -> *</span>"
      ],
      "text/plain": [
       "Box :: * -> *"
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
       "</style><span class='get-type'>Present :: * -> * -> *</span>"
      ],
      "text/plain": [
       "Present :: * -> * -> *"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "data Box a       = Empty          | Has a            deriving (Show)\n",
    "data Present t a = EmptyPresent t | PresentFor t a   deriving (Show)\n",
    "\n",
    ":k Box\n",
    ":k Present"
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
    "Because we decided that the tag of the present (`t`) can be a number, a name, or anything else that could identify a customer, we'll also parameterize its type.\n",
    "\n",
    "Now, a few parts of the process require functions common to both types. We need:\n",
    "- One to check if a box or present is empty.\n",
    "- One to check if a specific value is contained inside the box or present.\n",
    "- And one to replace the contents of the box or present.\n",
    "\n",
    "Instead of writing the functions by themselves and then transforming them to a type class and instances as we did in the two previous examples, let's go straight to the type class."
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
    "class Container c where\n",
    "    isEmpty  ::  -- ...\n",
    "    contains ::  -- ...\n",
    "    replace  ::  -- ...\n",
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
    "The type class will be called `Container` because it provides behaviors related to containers. The type variable is called `c` because it's a container.\n",
    "\n",
    "Now, let's write down the type signatures. We'll start with the `replace` function. Cause why not?"
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
    "class Container c where\n",
    "    isEmpty  ::  -- ...\n",
    "    contains ::  -- ...\n",
    "    replace  ::  c a -> b -> c b\n",
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
    "`replace` takes two inputs:\n",
    "- A container `c` that has some value of type—let's say `a`—inside.\n",
    "- And another value that can be of the same or different type than the one inside the container. Let's call it `b`. \n",
    "\n",
    "The function replaces the value of type `a` inside the container with the one of type `b`. So, in the end, we get a value of type `c b` because the value it contains is now of type `b`.\n",
    "\n",
    "Now, let's do the `contains` function:"
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
    "class Container c where\n",
    "    isEmpty  ::  -- ...\n",
    "    contains ::  (Eq a) => c a -> a -> Bool\n",
    "    replace  ::  c a -> b -> c b\n",
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
    "`contains` takes two inputs:\n",
    "- A container `c` that has some value of type `a` inside.\n",
    "- And another value that will be compared to the one inside the container. So it needs to be of the same type `a`, and an instance of `Eq` because we'll need to use `==` to check if it's the same value.\n",
    "\n",
    "The function takes the value, checks if it's the same as the one inside the container, and returns `True` if it is and `False` if it isn't. So, we return a boolean.\n",
    "\n",
    "And finally, let's do the `isEmpty` function:"
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
    "class Container c where\n",
    "    isEmpty  ::  c a -> Bool\n",
    "    contains ::  (Eq a) => c a -> a -> Bool\n",
    "    replace  ::  c a -> b -> c b"
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
    "`isEmpty` takes one input:\n",
    "- A container `c` that has some value of type `a` inside.\n",
    "\n",
    "The function takes the container and returns `True` if it contains a value and `False` if it doesn't. So it returns a value of type `Bool`."
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
    "Our type class is ready to go! \n",
    "\n",
    "And because each `->` (arrow) separates a value, and all values need to have a concrete type, we know that both `a` and `b` are concrete types by themselves. Because they are alone between arrows.\n",
    "\n",
    "Using the same reasoning, we know that `c a` and `c b` have to be concrete types. And because `a` and `b` are concrete types, this means that `c` is a type constructor that takes a concrete type and returns a concrete type.\n",
    "\n",
    "We can see this if we check the kind of our type class:"
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
       "</style><span class='get-type'>Container :: (* -> *) -> Constraint</span>"
      ],
      "text/plain": [
       "Container :: (* -> *) -> Constraint"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    ":k Container"
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
    "Now that we have our type class, let's create the instances for the `Box` type:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
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
       "</style><span class='get-type'>Box :: * -> *</span>"
      ],
      "text/plain": [
       "Box :: * -> *"
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
       "</style><span class='get-type'>Container :: (* -> *) -> Constraint</span>"
      ],
      "text/plain": [
       "Container :: (* -> *) -> Constraint"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "-- class Container c where\n",
    "--     isEmpty  :: c a -> Bool\n",
    "--     contains :: (Eq a) => c a -> a -> Bool\n",
    "--     replace  :: c a -> b -> c b\n",
    "\n",
    "instance Container Box where\n",
    "\n",
    "    isEmpty Empty = True\n",
    "    isEmpty _     = False\n",
    "    \n",
    "    contains (Has x) y = x == y\n",
    "    contains Empty   _ = False\n",
    " \n",
    "    replace _ x = Has x\n",
    "    \n",
    "\n",
    ":k Box\n",
    ":k Container"
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
    "Notice that we create an instance for `Box`, not `Box a`. For the `Eq` type class, we applied `Box` to the type variable `a` to obtain the concrete type `Box a` because the `Eq` type class needed a concrete type as a parameter. But `Container` takes a constructor of kind `* -> *`, which is the same kind as `Box`. So we have to pass `Box` without applying it to anything.\n",
    "\n",
    "The actual implementation of the functions is pretty straightforward. Because `Box` has two constructors, we have two formulas per function.\n",
    "\n",
    "Now let's create the instance for the `Present` type:"
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
       "</style><span class='get-type'>Present :: * -> * -> *</span>"
      ],
      "text/plain": [
       "Present :: * -> * -> *"
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
       "</style><span class='get-type'>Container :: (* -> *) -> Constraint</span>"
      ],
      "text/plain": [
       "Container :: (* -> *) -> Constraint"
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
       "</style><span class='get-type'>Present String :: * -> *</span>"
      ],
      "text/plain": [
       "Present String :: * -> *"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "-- class Container c where\n",
    "--     isEmpty  :: c a -> Bool\n",
    "--     contains :: (Eq a) => c a -> a -> Bool\n",
    "--     replace  :: c a -> b -> c b\n",
    "\n",
    "\n",
    "instance Container (Present t) where\n",
    "    \n",
    "    isEmpty (EmptyPresent _) = True\n",
    "    isEmpty _                = False\n",
    "    \n",
    "    contains (PresentFor _ x) y = x == y\n",
    "    contains (EmptyPresent _) _ = False\n",
    "    \n",
    "    replace (PresentFor tag _) x = PresentFor tag x\n",
    "    replace (EmptyPresent tag) x = PresentFor tag x\n",
    "\n",
    "\n",
    ":k Present\n",
    ":k Container\n",
    ":k Present String"
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
    "Now, the instance is for the `Present t` type constructor. This is because `Present` by itself has kind `* -> * -> *`, but because `Container` takes a type constructor of kind `* -> *`, we have to apply `Present` to a type—like `Present String`—to obtain the kind we need. And because we want to be able to use any type as a tag, we use the type variable `t`.\n",
    "\n",
    "So, this part is important. The `t` in `Present t` is the tag. And the whole `Present t` type constructor is `c`. We can treat the `Present t` type constructor as `c` because it's a type that never changes. We don't change the tag's type in any of the functions. But we do modify the type of the contents in the `replace` function. When we use `replace`, the type of the contents can change from `a` to `b`, so we can't treat them as a constant type like `t`. That's why they are parameters to the `c` type constructor, so we can change the type in the `replace` function if we need to.\n",
    "\n",
    "Same as before, the actual implementation of the functions are straight forward."
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
    "And to rip the rewards of our work, here are a few examples using our new type class behaviors:"
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
       "True"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "PresentFor \"Tommy\" \"Arduino\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "\"WROOONG!\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "\"WROOONG!\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "Has False `contains` False         -- True\n",
    "\n",
    "isEmpty (Has 'a')                  -- False\n",
    "\n",
    "PresentFor \"Tommy\" 5 `contains` 5  -- True\n",
    "\n",
    "PresentFor \"Tommy\" 5 `replace` \"Arduino\"   -- PresentFor \"Tommy\" \"Arduino\"\n",
    "\n",
    "\n",
    "guessWhat'sInside :: (Container a, Eq b) => a b -> b -> String\n",
    "guessWhat'sInside x y =\n",
    "  if x `contains` y \n",
    "    then \"You're right!!\"\n",
    "    else \"WROOONG!\"\n",
    "\n",
    "guessWhat'sInside (PresentFor \"Mary\" \"A Raspberry Pi!\") \"A Ponny!\"  -- **Mary's Dissapointment increasses**\n",
    "guessWhat'sInside (Has 1) 15"
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
    "Understanding this type class and instances was the trickiest part of the lesson. It might take a while to fully grasp what we just saw. But don't worry, if something doesn't click, it will with some practice. That's why it's important to do the homework.\n",
    "\n",
    "Now, let's learn about subclassing. After everything we went through, this is a piece of cake."
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
    "## Exploring the `Ord` type class (Subclassing)"
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
    "We never talked about subclassing before, but you already know how it works.\n",
    "\n",
    "Let's see it in practice while defining an instance for the `Ord` type class.\n",
    "\n",
    "If we run the info command on the `Ord` type class (`:i Ord`), we would get something like this:"
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
    "type Ord :: * -> Constraint         -- Takes a concreate type\n",
    "class Eq a => Ord a where           -- That \"Eq a =>\" is new!! 🤔\n",
    "  compare :: a -> a -> Ordering \n",
    "  (<) :: a -> a -> Bool             -- A bunch of functions\n",
    "  (<=) :: a -> a -> Bool\n",
    "  (>) :: a -> a -> Bool\n",
    "  (>=) :: a -> a -> Bool\n",
    "  max :: a -> a -> a\n",
    "  min :: a -> a -> a\n",
    "  {-# MINIMAL compare | (<=) #-}    -- We can only implement \"compare\" or \"<=\".\n",
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
    "Everything checks out. Except for that `Eq a =>`. We've seen this in both functions and instances. But never on type class definitions.\n",
    "\n",
    "This (`Eq a =>`) means what you'd imagine:"
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
    "**To make a type `a` an instance of `Ord`, first we have to make it an instance of `Eq`! Meaning that `Eq` is a prerequisite for `Ord`. In other words, `Eq` is a superclass of `Ord` or `Ord` is a subclass of `Eq`.**"
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
    "Superclasses allow simpler signatures to be inferred. By saying that a type is an instance of `Ord`, not only do we know that it has the behaviors of `Ord`, but also the behaviors of `Eq`. Also, this allows us to use behaviors of the `Eq` type class to define the instances of the `Ord` type class. Which is actually something that happens in this case. The `Ord` type class uses functions provided by the `Eq` type class.\n",
    "\n",
    "We can't see it because the info command doesn't show the whole type class definition. Same as when we run the info command for the `Eq` type class, it doesn't show the mutually recursive definitions of `==` and `/=` that we just wrote.\n",
    "\n",
    "Still, even though we can't see them, we know there are a bunch of function definitions defined in terms of each other. That's why we can implement the entire instance by only defining `compare` or `<=`.\n",
    "\n",
    "The info command doesn't show all that code because we, the developers, don't care about it. We only want to know:\n",
    "- Which behaviors come with the type class. To see if it's what we need.\n",
    "- The kind of the type class and minimum behaviors we need to implement. To only implement those. \n",
    "- If it depends on another type class. To implement that one before this one.\n",
    "- And, finally, which types are already an instance of this type class. To see which types can already use those behaviors.\n",
    "\n",
    "And that's what the info command shows us."
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
    "So, to make a type an instance of `Ord`, first, we have to make it an instance of `Eq`. Luckily, we already created a few instances for `Eq` before, so we're already halfway through if we want to create `Ord` instances for any of those types.\n",
    "\n",
    "For example, if we want to create an instance of `Box a` for the `Ord` type class, we have to implement one of the functions needed for the minimal complete definition! In this case, we chose the `compare` function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
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
       "LT"
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
    }
   ],
   "source": [
    "-- type Ord :: * -> Constraint  \n",
    "-- class Eq a => Ord a where   \n",
    "--   compare :: a -> a -> Ordering \n",
    "\n",
    "instance (Ord a) => Ord (Box a) where\n",
    "  Has x `compare` Has y = x `compare` y\n",
    "  Empty `compare` Has _ = LT\n",
    "  Has _ `compare` Empty = GT\n",
    "  Empty `compare` Empty = EQ\n",
    "  \n",
    "\n",
    "Has 9 >= Has 5\n",
    "Empty `compare` Has 0\n",
    "Empty < Empty"
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
    "This is what is happening here:\n",
    "\n",
    "- If both boxes have some value inside, we compare the values. And because we're applying the `compare` function to `x` and `y` of type `a`, we need to add the constraint that the `a` type has to be an instance of `Ord`.\n",
    "- If one of the boxes is `Empty` and the other isn't, it doesn't matter what's inside the one that has something. It will always be greater than the `Empty` one. Because I said so.\n",
    "- If both are `Empty`, of course, they are equal."
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
    "And Boom! that's it!\n",
    "\n",
    "We created:\n",
    "- The `Eq` type class with 3 different instances.\n",
    "- The `WeAccept` type class with 4 instances.\n",
    "- Then, the `Container` type class with 3 instances.\n",
    "- And finally, we made a type an instance of the `Ord` type class.\n",
    "\n",
    "**Congratulations! 🎉 You know everything needed to work with type classes!!**\n",
    "\n",
    "As the final section of this lesson, we'll learn how and when to automatically derive instances. Saving us some precious time and reducing the amount of code we have to maintain."
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
    "## Deriving"
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
    "Derived instances are an automatic way of making a type an instance a type class. This is possible because many common type classes are usually implemented the same way. And some clever guys with PhDs figured out how to generate this code based on the type's definition.\n",
    "\n",
    "This is limited to `Eq`, `Ord`, `Enum`, `Show`, and others defined in either the Prelude or a standard library—libraries that come with Haskell and that we'll explore in future lessons. For now, think that all the type classes we used until now, and that we didn't create ourselves, can be derived."
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
    "To use this feature, add the `deriving` keyword at the end of your type declaration with the names of all the type classes you want to derive. For example, if we do this:"
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
   "outputs": [],
   "source": [
    "data Choice = No | Idk | Yes deriving (Eq, Ord, Show, Bounded, Enum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
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
       "\"Yes\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "No"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "Idk"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "Yes /= No             -- Are these values different?   (Behavior from Eq)\n",
    "\n",
    "Yes > No              -- Is Yes bigger than No?        (Behavior from Ord)\n",
    "\n",
    "show Yes              -- Transform Yes to String       (Behavior from Show)\n",
    "\n",
    "(minBound) :: Choice  -- Smallest value of type Choice (Behavior from Bounded)\n",
    "\n",
    "succ No               -- Successor of No               (Behavior from Enum)"
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
    "And that's it!! Your `Choice` type has the behaviors provided by all those type classes.  \n",
    "\n",
    "So, if we could do that from the start, why in the world would you care for manually deriving instances?\n",
    "\n",
    "Well... One reason is that not all type classes can be derived. And another is that deriving can sometimes go wrong."
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
    "### Deriving can go wrong"
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
    "Each type class has its own set of rules for deriving instances. For example, when deriving the `Ord` type, value constructors defined earlier are smaller. So, in this case:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
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
       "GT"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "data PaymentMethod = Cash | Card | CC deriving (Eq, Ord)\n",
    "\n",
    "Cash > Card\n",
    "Card < CC\n",
    "CC `compare` Cash"
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
    "`Cash` is smaller than `Card`, which is smaller than `CC`.\n",
    "\n",
    "And in this case:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
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
       "LT"
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
    "data Box a = Empty | Has a deriving (Eq, Ord)\n",
    "\n",
    "Has 5 `compare` Has 6\n",
    "Has \"Hi\" >= Has \"Hello!\""
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
    "If a value constructor has a parameter (`Has a`), and two values are made from the same constructor (`Has 5` and `Has 6`), the parameters are compared (like we did when we defined the instances ourselves)."
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
    "Those are the rules the compiler follows to automatically create the `Ord` instance for your type. Other type classes have other rules. We won't go over the rules of each type class, but I'll provide a [link](https://www.haskell.org/onlinereport/haskell2010/haskellch11.html) with a short explanation in the interactive lesson. In case you want to learn more."
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
    "Now, let's say we want to use a type to manage lengths for Civil engineering software.\n",
    "\n",
    "We work with both meters and kilometers, but because we don't want to accidentally mix those and get a potentially catastrophic error, we define a data type with two constructors. One for meters and one for kilometers. Both contain a value of type `Double`. We'll also derive the `Eq` type class."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "outputs": [],
   "source": [
    "data Length = M Double | Km Double deriving (Eq)"
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
    "But, as soon as we start using this data type, we find a little problem. We know that 1000 Meters equals 1 Kilometer, but when we test this in our code, we get that it's not!:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
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
       "False"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "M 1000 == Km 1 -- False"
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
    "That's because when we derived `Eq`, Haskell generated this code:"
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
    "instance Eq Length where\n",
    "  (==) (M  x) (M  y) = x == y \n",
    "  (==) (Km x) (Km y) = x == y \n",
    "  (==) _      _      = False\n",
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
    "This works great if we're comparing meters to meters and kilometers to kilometers. But we have the wrong implementation to compare between constructors because Haskell doesn't know that the values of different constructors relate in any way!! Haskell just assumed that if the constructors are different, the values are too!\n",
    "\n",
    "So, in this case, we have to write the instance ourselves to take into account the relationship between the constructors. Like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
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
    }
   ],
   "source": [
    "data Length = M Double | Km Double\n",
    "\n",
    "instance Eq Length where\n",
    "  (==) (M  x) (M  y) = x == y\n",
    "  (==) (Km x) (Km y) = x == y\n",
    "  (==) (M  x) (Km y) = x == 1000 * y\n",
    "  (==) (Km x) (M  y) = x * 1000 == y\n",
    "\n",
    "\n",
    "M 3000 == Km 3   -- True\n",
    "Km 7   /= M 14   -- True"
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
    "That's why it's a good idea to be conscious of how each type class is derived. To know when you can derive them and when you have to write the instance by hand.\n",
    "\n",
    "And to finish the lesson, here are a few tips for real-world coding:"
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
    "### Tips for real-world coding"
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
    "- Everything I explained here today applies to all type classes."
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
    "- We don't define type classes that often. Usually, the ones that come with Haskell are all we need."
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
    "- We do implement instances quite a lot. And it's usually (but not always) a good idea to derive them. If you're in doubt, try automatic deriving and check your assumptions. You can always come back and manually define the instances."
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
    "- You can peek at a type class definition using `:i` on GHCi to see the minimum behaviors to implement when creating your instance. Implement those, and you're done."
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
  "vscode": {
   "interpreter": {
    "hash": "31f2aee4e71d21fbe5cf8b01ff0e069b9275f58929596ceb00d14d90e3e16cd6"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
