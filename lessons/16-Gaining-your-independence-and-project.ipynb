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
    "# Gaining your independence 💪"
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
    "* Small tips and tricks\n",
    "    * REPL\n",
    "    * Hackage\n",
    "    * Hoogle\n",
    "    * `undefined`\n",
    "    * Type Holes\n",
    "* Section's Final Project"
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
    "## REPL"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Remember that you always have the repl available to you. And If you enter the REPL using `cabal repl`, you can also import and explore modules you downloaded using Hackage. If you want to see how it works, see the example in the video version."
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
    "## Hackage\n",
    "\n",
    "\n",
    "## https://hackage.haskell.org/"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Hackage is the Haskell community's central package archive. At the time of writing this lesson, there are over 16 thousand Haskell packages available in Hackage.\n",
    "\n",
    "We already saw how you can use it with Cabal to add libraries to your projects. But in the video lesson, we'll explore how to find and choose libraries and explore the documentation."
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
    "## Hoogle\n",
    "\n",
    "\n",
    "## https://hoogle.haskell.org/"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Hoogle allows you to search a commonly used subset of Haskell libraries by either function name or approximate type signature. \n",
    "\n",
    "This is useful in several scenarios, for example:\n",
    "\n",
    "1. If you want to print a string to the console but forget the name of the function, searching for \"String -> IO ()\" will provide all functions with a signature that matches your intention. \n",
    "2. If you want to use a function but forget from which module it is, you can search for the function, and it will tell you where it is.\n",
    "3. If you want to work with some concept, like natural numbers or web sockets, you can try searching those terms to see if any library, type, module, function, or type class roughly matches the name."
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
    "## `undefined`"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "If we look for `undefined` in Hoogle, we'll see that, in theory, it's just a fancy error. It's a value that, as soon as you evaluate it, halts your program. Of course, as we saw in the Handling Errors lesson, we don't like runtime errors! So, why I'm sharing it as a tip?\n",
    "\n",
    "In practice, `undefined` is a great tool to keep the type checker assisting you while working on a half-baked code. Let's see how."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Let's say we want to create a function that reads a CSV file, transforms the content into JSON format, and writes a new file with the new contents. \n",
    "\n",
    "First, we create newtype wrappers for both CSV and JSON values. To avoid mixing CSV and JSON values by accident and allow the compiler to provide more specific hints. Even if the underlying value in both cases is just a String.\n",
    "\n",
    "Then, because we don't want our program to crash if, for some reason, the reading and writing of files or the conversion fails, we'll catch the errors and return an Either:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "```haskell\n",
    "newtype CSV = CSV String \n",
    "newtype JSON = JSON String\n",
    "\n",
    "csvFileToJsonFile :: FilePath -> IO (Either String JSON)\n",
    "csvFileToJsonFile ...\n",
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
    "Ok, now we can start implementing the function. Because we're just starting and we don't have a clear idea of how we want to implement this, we'll go step by step. I'll behave naively to showcase the usefulness of `undefined`. \n",
    "\n",
    "Let's start by printing a message to the console and reading the file:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "```haskell\n",
    "csvFileToJsonFile :: FilePath -> IO (Either String JSON)\n",
    "csvFileToJsonFile = do\n",
    "  putStrLn \"Reading CSV file\"\n",
    "  rawCSV <- readFile  -- ❌ typecheck: Error here!\n",
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
    "If we write this, we get this error:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "```\n",
    "The last statement in a 'do' block must be an expression\n",
    "  rawCSV <- readFile\n",
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
    "Which is not the error we would expect. Especially because there's an even more fundamental error that the type checker is not telling us about because it's stuck in this one.\n",
    "\n",
    "We could be making huge mistakes like this one:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "```haskell\n",
    "csvFileToJsonFile :: FilePath -> IO (Either String JSON)\n",
    "csvFileToJsonFile = do\n",
    "  putStrLn \"Reading CSV file\"\n",
    "  askldj56jklsdjf564lkjsdlf  -- Cat walked on the keyboard 🐈\n",
    "  rawCSV <- readFile         -- ❌ typecheck (oblivious to the previous line): Error here!\n",
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
    "And we wouldn't know because the type checker is stuck with the same error as before.\n",
    "\n",
    "This is one of the cases when `undefined` is handy. If we add an `undefined` as the last statement of the `do` block, we're essentially telling the type checker: \"trust me, bro, from here on, everything is fine. Don't sweat it.\"\n",
    "\n",
    "So, the type checker, assuming everything is fine there, will continue to analyze the rest of our code and give us useful information.\n",
    "\n",
    "In this case, if we do this:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "```haskell\n",
    "csvFileToJsonFile :: FilePath -> IO (Either String JSON)\n",
    "csvFileToJsonFile = do\n",
    "  putStrLn \"Reading CSV file\" -- ❌ typecheck: Wrong type!\n",
    "  askldj56jklsdjf564lkjsdlf   -- ❌ typecheck: What's wrong with you?\n",
    "  rawCSV <- readFile          -- ❌ typecheck: Where's the readFile's argument?\n",
    "  undefined\n",
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
    "We get a bunch of helpful errors that help us realize that there's a line with gibberish, that we didn't specify the argument name of the `csvFileToJsonFile` function, and that we didn't provide the argument to the `readFile` function. So, we fix them:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "```haskell\n",
    "csvFileToJsonFile :: FilePath -> IO (Either String JSON)\n",
    "csvFileToJsonFile fp = do\n",
    "  putStrLn \"Reading CSV file\"\n",
    "  rawCSV <- readFile fp\n",
    "  undefined\n",
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
    "Now, we have no type errors, and we can be reasonably certain that everything up until `undefined` is ok."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Another use of `undefined` is to check the behaviors during development. For example, we still have to parse the contents to CSV, convert them into JSON, and then write the new file. And on top of that, we have to do error handling. \n",
    "\n",
    "Instead of writing the whole thing and checking that everything works at the end, we can check the values in intermediate steps by running the code with the `undefine` there. For example, we can check the content of the files by printing them:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "```haskell\n",
    "csvFileToJsonFile :: FilePath -> IO (Either String JSON)\n",
    "csvFileToJsonFile fp = do\n",
    "  putStrLn \"Reading CSV file\"\n",
    "  rawCSV <- readFile fp\n",
    "  print rawCSV\n",
    "  undefined\n",
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
    "Now, we open a REPL and run `csvFileToJsonFile \"somefile.csv\"` and we get the contents of the file printed at the console, and after that, we get an exception:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "```\n",
    "*** Exception: Prelude.undefined\n",
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
    "Because `undefined` is just a fancy error, we'll get a runtime error if we run the program. Of course, by the time you're done with the code, there has to be no `undefined` left. `undefined` is just a tool for your convenience during a development session. You could get fired if you ship an `undefined` value to production.\n",
    "\n",
    "But! We don't care at this point because we're mid-development, and we just want to check if everything we coded so far is fine."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Finally, one last good use case for `undefined` is to use it as an implementation TODO. For example, let's say we keep going with our function:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "```haskell\n",
    "csvFileToJsonFile :: FilePath -> IO (Either String JSON)\n",
    "csvFileToJsonFile fp = do\n",
    "  putStrLn \"Reading CSV file\"\n",
    "  rawCSV <- readFile fp\n",
    "  let csv = parseCSV rawCSV -- ❌ typecheck: Who is parseCSV? A friend of yours?\n",
    "  undefined\n",
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
    "At this point, we'd have an error because there's no `parseCSV` function. And there's no `parseCSV` function because we haven't implemented it yet.\n",
    "\n",
    "One option would be to implement `parseCSV` right away. That would be fine. But what if, halfway through implementing it, you realize you need to implement another function? And another one. This specific case wouldn't be that complicated. But you can see how, in more complex cases, by the time you finish implementing all the internal functions, you lose track of what you had in mind for the original one.\n",
    "\n",
    "So, if you have a rough idea of the overall structure of the original function, you can defer implementing the internal functions until you finish implementing the original function by creating the internal functions signatures and setting the actual implementation of it as undefined. Like this: "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "```haskell\n",
    "newtype CSV = CSV String deriving (Show)\n",
    "newtype JSON = JSON String deriving (Show)\n",
    "\n",
    "csvFileToJsonFile :: FilePath -> IO (Either String JSON)\n",
    "csvFileToJsonFile fp = do\n",
    "  putStrLn \"Reading CSV file\"\n",
    "  rawCSV <- readFile fp\n",
    "  let csv         = parseCSV rawCSV\n",
    "      (JSON json) = csvToJson csv\n",
    "  writeFile \"newFile.json\" json\n",
    "  undefined\n",
    "\n",
    "parseCSV :: String -> CSV\n",
    "parseCSV = undefined\n",
    "\n",
    "csvToJson :: CSV -> JSON\n",
    "csvToJson = undefined\n",
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
    "And now, each `undefined` is like a TODO item. The first indicates that you still have to add error handling. And the other two that you still have to implement those functions. You essentially split the work into three, and you can start tackling your TODOs one by one."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Now, let's move to the final tip of the lesson: Type holes!"
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
    "## Type holes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Typed holes are a feature of GHC specifically designed to help you figure out what code to write when you're unsure.\n",
    "\n",
    "It works like this:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Let's say you're implementing a function that parses a list of `String`s into valid emails:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "```haskell\n",
    "newtype Email = Email String deriving Show\n",
    "\n",
    "parseEmails :: [String] -> [Email]\n",
    "parseEmails = undefined\n",
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
    "This function verifies that the user input is a valid email by checking it contains the `@` sign. And then, it has to normalize them by converting all characters into lowercase.\n",
    "\n",
    "Ok. So, let's start easy by just straight-up converting Strings into Emails without doing anything.\n",
    "\n",
    "If we change the undefined to an underscore, we get a pretty interesting error:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "```haskell\n",
    "newtype Email = Email String deriving Show\n",
    "\n",
    "parseEmails :: [String] -> [Email]\n",
    "parseEmails = _\n",
    "```\n",
    "-------------------------------------------------------------\n",
    "```\n",
    "• Found hole: _ :: [String] -> [Email]\n",
    "• In an equation for ‘parseEmails’: parseEmails = _\n",
    "• Relevant bindings include\n",
    "    parseEmails :: [String] -> [Email]\n",
    "      (bound at /Users/roberm/scratchpad/typedHoles.hs:99:1)\n",
    "  Valid hole fits include\n",
    "    parseEmails\n",
    "    mempty\n",
    "  Valid refinement hole fits include\n",
    "    map _\n",
    "    concatMap _\n",
    "    (<$>) _\n",
    "    fmap _\n",
    "    ($) _\n",
    "    const _\n",
    "    pure _\n",
    "    head _\n",
    "    last _\n",
    "    id _\n",
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
    "This is what type holes bring to the table in Haskell. By putting an underscore in our unfinished code, we asked the type checker for hints about what could be done there. The type checker brings all the information it can:\n",
    "\n",
    "- It tells us what's the type of the hole.\n",
    "- Where the hole is.\n",
    "- What are relevant bindings (in this case, the only relevant binding is the same function we're defining, but if we have a `where` clause or `let` bindings, those would show up as well).\n",
    "- Then, it shows us which values in our scope perfectly fit the hole.\n",
    "- Finally, it tells us which functions and constructors don't fit perfectly but could take us one step closer to the final answer."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "In this case, we know we have to `map` over the list of `String`s, so we take the first \"refinement hole\" suggestion and write `map` with an underscore (a new type hole) in front:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "```haskell\n",
    "newtype Email = Email String deriving Show\n",
    "\n",
    "parseEmails :: [String] -> [Email]\n",
    "parseEmails = map _\n",
    "```\n",
    "---\n",
    "```\n",
    "• Found hole: _ :: String -> Email\n",
    "• In the first argument of ‘map’, namely ‘_’\n",
    "  In the expression: map _\n",
    "  In an equation for ‘parseEmails’: parseEmails = map _\n",
    "• Relevant bindings include\n",
    "    parseEmails :: [String] -> [Email]\n",
    "      (bound at /Users/roberm/scratchpad/typedHoles.hs:100:1)\n",
    "  Valid hole fits include Email\n",
    "  Valid refinement hole fits include\n",
    "    ($) _\n",
    "    const _\n",
    "    pure _\n",
    "    return _\n",
    "    ($!) _\n",
    "    (Map.!) _\n",
    "    head _\n",
    "    last _\n",
    "    id _\n",
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
    "Now, we get a new set of the same information but for our new hole. And, if we look at the \"Valid hole fits\", we see that the `Email` constructor is there!\n",
    "\n",
    "If we wrap a string with the `Email` value constructor, we get a value of type `Email`, which is exactly what we set out to do!\n",
    "\n",
    "So, we take the type hole suggestion and write the `Email` constructor after `map`:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "```haskell\n",
    "newtype Email = Email String deriving Show\n",
    "\n",
    "parseEmails :: [String] -> [Email]\n",
    "parseEmails = map Email\n",
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
    "And voilá! Our function compiles.\n",
    "\n",
    "But we're far from finished here. We said we wanted to filter emails that didn't contain the `@` sign, so let's do that. \n",
    "\n",
    "Of course, we want to filter the emails before constructing them, so we'll use function composition to add the `filter` function before the `map` function: "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "```haskell\n",
    "newtype Email = Email String deriving Show\n",
    "\n",
    "parseEmails :: [String] -> [Email]\n",
    "parseEmails = map Email . filter _\n",
    "```\n",
    "---\n",
    "```\n",
    "• Found hole: _ :: String -> Bool\n",
    "• In the first argument of ‘filter’, namely ‘_’\n",
    "  In the second argument of ‘(.)’, namely ‘filter _’\n",
    "  In the expression: map Email . filter _\n",
    "• Relevant bindings include\n",
    "    parseEmails :: [String] -> [Email]\n",
    "      (bound at /Users/roberm/scratchpad/typedHoles.hs:94:1)\n",
    "  Valid hole fits include\n",
    "    null\n",
    "    read\n",
    "  Valid refinement hole fits include\n",
    "    (==) _\n",
    "    (/=) _\n",
    "    (>) _\n",
    "    (<=) _\n",
    "    (>=) _\n",
    "    (<) _\n",
    "    ($) _\n",
    "    head _\n",
    "    last _\n",
    "    id _\n",
    "    (Some refinement hole fits suppressed; use -fmax-refinement-hole-fits=N or -fno-max-refinement-hole-fits)\n",
    " ```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Ok. So, we need a predicate. But, this time, the typed hole has a little message at the bottom. This is because it has more suggestions than the maximum allowed by default. One thing we could do to get more hints is to disable this maximum allowed by writing a pragma with the flag indicated right there like this:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "```haskell\n",
    "{-# OPTIONS_GHC -fno-max-refinement-hole-fits #-}\n",
    "\n",
    "newtype Email = Email String deriving Show\n",
    "\n",
    "parseEmails :: [String] -> [Email]\n",
    "parseEmails = map Email . filter _\n",
    "```\n",
    "---\n",
    "```\n",
    "• Found hole: _ :: String -> Bool\n",
    "• In the first argument of ‘filter’, namely ‘_’\n",
    "  In the second argument of ‘(.)’, namely ‘filter _’\n",
    "  In the expression: map Email . filter _\n",
    "• Relevant bindings include\n",
    "    parseEmails :: [String] -> [Email]\n",
    "      (bound at /Users/roberm/scratchpad/typedHoles.hs:94:1)\n",
    "  Valid hole fits include\n",
    "    null\n",
    "    read\n",
    "  Valid refinement hole fits include\n",
    "    (==) _\n",
    "    (/=) _\n",
    "    (>) _\n",
    "    (<=) _\n",
    "    (>=) _\n",
    "    (<) _\n",
    "    ($) _\n",
    "    notElem _\n",
    "    elem _\n",
    "    any _\n",
    "    all _\n",
    "    const _\n",
    "    pure _\n",
    "    return _\n",
    "    ($!) _\n",
    "    head _\n",
    "    last _\n",
    "    id _\n",
    " ```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "Now, we have more options in the \"refinement hole fits\" sections. And, if we look at them, we're reminded that we could use `elem`. We know that `elem` is a predicate that returns true if the element is inside the list, which is what we needed. We substitute `_` with `elem _` and keep going:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "```haskell\n",
    "{-# OPTIONS_GHC -fno-max-refinement-hole-fits #-}\n",
    "\n",
    "newtype Email = Email String deriving Show\n",
    "\n",
    "parseEmails :: [String] -> [Email]\n",
    "parseEmails = map Email . filter (elem _)\n",
    "```\n",
    "---\n",
    "```\n",
    "• Found hole: _ :: Char\n",
    "• In the first argument of ‘elem’, namely ‘_’\n",
    "  In the first argument of ‘filter’, namely ‘(elem _)’\n",
    "  In the second argument of ‘(.)’, namely ‘filter (elem _)’\n",
    "• Relevant bindings include\n",
    "    parseEmails :: [String] -> [Email]\n",
    "      (bound at /Users/roberm/scratchpad/typedHoles.hs:95:1)\n",
    "  Valid hole fits include\n",
    "    maxBound\n",
    "    minBound\n",
    "  Valid refinement hole fits include\n",
    "    head _\n",
    "    last _\n",
    "    id _\n",
    "    pred _\n",
    "    succ _\n",
    "    toEnum _\n",
    "    read _\n",
    " ```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "This case is pretty obvious. We need a character to check if it is part of the `String`, and we know which character that is:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "```haskell\n",
    "{-# OPTIONS_GHC -fno-max-refinement-hole-fits #-}\n",
    "\n",
    "newtype Email = Email String deriving Show\n",
    "\n",
    "parseEmails :: [String] -> [Email]\n",
    "parseEmails = map Email . filter (elem '@')\n",
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
    "We're done with the filtering! Now, let's normalize the emails. Because we have to normalize the strings before wrapping them with the `Email` constructor, we do the same as before and compose a type hole:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "```haskell\n",
    "{-# OPTIONS_GHC -fno-max-refinement-hole-fits #-}\n",
    "\n",
    "newtype Email = Email String deriving Show\n",
    "\n",
    "parseEmails :: [String] -> [Email]\n",
    "parseEmails = map (Email . _) . filter (elem '@')\n",
    "```\n",
    "---\n",
    "```\n",
    "• Found hole: _ :: String -> String\n",
    "• In the second argument of ‘(.)’, namely ‘_’\n",
    "  In the first argument of ‘map’, namely ‘(Email . _)’\n",
    "  In the first argument of ‘(.)’, namely ‘map (Email . _)’\n",
    "• Relevant bindings include\n",
    "    parseEmails :: [String] -> [Email]\n",
    "      (bound at /Users/roberm/scratchpad/typedHoles.hs:98:1)\n",
    "  Valid hole fits include\n",
    "    show\n",
    "    reverse\n",
    "    cycle\n",
    "    init\n",
    "    tail\n",
    "    id\n",
    "    mempty\n",
    "    fail\n",
    "    read\n",
    "  Valid refinement hole fits include\n",
    "    (:) _\n",
    "    (++) _\n",
    "    max _\n",
    "    min _\n",
    "    map _\n",
    "    concatMap _\n",
    "    (<$>) _\n",
    "    fmap _\n",
    "    take _\n",
    "    drop _\n",
    "    ($) _\n",
    "    takeWhile _\n",
    "    dropWhile _\n",
    "    const _\n",
    "    filter _\n",
    "    (<>) _\n",
    "    mappend _\n",
    "    pure _\n",
    "    sequenceA _\n",
    "    foldMap _\n",
    "    return _\n",
    "    (<*>) _\n",
    "    (=<<) _\n",
    "    (<*) _\n",
    "    (<$) _\n",
    "    sequence _\n",
    "    ($!) _\n",
    "    asTypeOf _\n",
    "    scanl1 _\n",
    "    scanr1 _\n",
    "    showChar _\n",
    "    showString _\n",
    "    head _\n",
    "    last _\n",
    "    id _\n",
    "    mconcat _\n",
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
    "We get a huuuuuge list of options, but the one that clearly looks like the best option is to refine our hole with a `map`. We have a list of characters. So, maybe we can go through every character and return the lowercase version, one by one. So, we accept that suggestion and replace the `_` with `map _`:  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "```haskell\n",
    "{-# OPTIONS_GHC -fno-max-refinement-hole-fits #-}\n",
    "\n",
    "newtype Email = Email String deriving Show\n",
    "\n",
    "parseEmails :: [String] -> [Email]\n",
    "parseEmails = map (Email . map _) . filter (elem '@')\n",
    "```\n",
    "---\n",
    "```\n",
    "• Found hole: _ :: Char -> Char\n",
    "• In the first argument of ‘map’, namely ‘_’\n",
    "  In the second argument of ‘(.)’, namely ‘map _’\n",
    "  In the first argument of ‘map’, namely ‘(Email . map _)’\n",
    "• Relevant bindings include\n",
    "    parseEmails :: [String] -> [Email]\n",
    "      (bound at /Users/roberm/scratchpad/typedHoles.hs:100:1)\n",
    "  Valid hole fits include\n",
    "    id\n",
    "    pred\n",
    "    succ\n",
    "  Valid refinement hole fits include\n",
    "    max _\n",
    "    min _\n",
    "    ($) _\n",
    "    const _\n",
    "    pure _\n",
    "    return _\n",
    "    ($!) _\n",
    "    asTypeOf _\n",
    "    head _\n",
    "    last _\n",
    "    id _\n",
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
    "Ok. We know that we need a function that goes from character to character. But none of the provided ones seem to either fit perfectly or help us move in the right direction. But we have one more ace up our sleeve: Imports! \n",
    "\n",
    "We get those suggestions because those are the ones available in our environment. So, if we want more suggestions, we can add more to our environment. In this case, we want to work with characters, so a good initial idea would be to import a module full of functions to work with characters. The `Data.Char` module is the prime candidate. Let's do that and see which new options we get:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "```haskell\n",
    "{-# OPTIONS_GHC -fno-max-refinement-hole-fits #-}\n",
    "\n",
    "import Data.Char\n",
    "\n",
    "newtype Email = Email String deriving Show\n",
    "\n",
    "parseEmails :: [String] -> [Email]\n",
    "parseEmails = map (Email . map _) . filter (elem '@')\n",
    "```\n",
    "---\n",
    "```\n",
    "• Found hole: _ :: Char -> Char\n",
    "• In the first argument of ‘map’, namely ‘_’\n",
    "  In the second argument of ‘(.)’, namely ‘map _’\n",
    "  In the first argument of ‘map’, namely ‘(Email . map _)’\n",
    "• Relevant bindings include\n",
    "    parseEmails :: [String] -> [Email]\n",
    "      (bound at /Users/roberm/scratchpad/typedHoles.hs:100:1)\n",
    "  Valid hole fits include\n",
    "    id\n",
    "    pred\n",
    "    succ\n",
    "    toLower\n",
    "    toUpper\n",
    "    toTitle\n",
    "  Valid refinement hole fits include\n",
    "    max _\n",
    "    min _\n",
    "    ($) _\n",
    "    const _\n",
    "    pure _\n",
    "    return _\n",
    "    ($!) _\n",
    "    asTypeOf _\n",
    "    head _\n",
    "    last _\n",
    "    id _\n",
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
    "Behold! Between the new suggestions, there's a function that perfectly fits our hole with the name of `toLower`. It looks too enticing to ignore, so let's replace it:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "```haskell\n",
    "{-# OPTIONS_GHC -fno-max-refinement-hole-fits #-}\n",
    "\n",
    "import Data.Char\n",
    "\n",
    "newtype Email = Email String deriving Show\n",
    "\n",
    "parseEmails :: [String] -> [Email]\n",
    "parseEmails = map (Email . map toLower) . filter (elem '@')\n",
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
    "It compiles! And it looks like we finished implementing all the functionality we wanted. And if we test the function:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "```haskell\n",
    "parseEmails [\"luffy@onepiece.com\",\"ZorO@OnePiece.cOm\", \"son.goku\"]\n",
    "\n",
    "-- [Email \"luffy@onepiece.com\",Email \"zoro@onepiece.com\"]\n",
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
    "We see that it works as expected. \n",
    "\n",
    "As you can see, type holes can be really useful. Especially when you're working with many polymorphic values or nested structures. Just as a final remark, you can have more than one hole at a time and name them by adding the name right after the underscore (without a space in between). Make it easier to distinguish them."
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
    "## Section's Final Project (what we did so far)"
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
    "In this lesson, you're going to prove to yourself that you can code in Haskell.\n",
    "\n",
    "If you've been doing the homework by now, you have a couple of programs under your belt:"
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
    "* In lesson 9's homework, you built a closed and open maze (we called it Forest) solver.  \n",
    "* In lesson 11's homework, you had the opportunity to build a program that prints a tree-like graph representing a folder structure.\n",
    "* In lesson 14, we built a CLI game in which the user tries to escape from a forest before it runs out of stamina. And in the homework of the same lesson, you added a battle system to fight golems while trying to escape.\n",
    "* In lesson 15's homework, you went through and understood the code of a CLI program that you can use to manage your to-do list. And on top of that, you added error handling to fix the bugs I purposely hid in the code."
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
    "At every step of the way, we introduced new concepts, and I provided you with thorough guidance about what to take into account and how to approach those challenges. Now, it's time for you to build something by yourself.\n",
    "\n",
    "Here are the requirements:"
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
    "## Section's Final Project (project requirements)"
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
    "* Build a Tic-Tac-Toe game.\n",
    "* It has to be a CLI executable with the business logic implemented as a library.\n",
    "* There has to be a single-player (against the machine) and a multiplayer (two-player) mode.\n",
    "* The machine has to play randomly.\n",
    "* The board has to be printed nicely on the console.\n",
    "* Use any library you want. However, the provided solution will only use the `random` library and Haskell features explained up until now. So, if you're tempted to use more advanced features, you're likely overcomplicating it."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "notes"
    }
   },
   "source": [
    "The only way to learn how to code is by coding. So, make sure to do the project, and I'll see you on the next one."
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
