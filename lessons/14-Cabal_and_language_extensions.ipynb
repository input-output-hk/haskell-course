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
    "# Cabal and Language Extensions"
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
    "## Outline \n",
    "\n",
    "- Cabal\n",
    "    - Introduction to Cabal\n",
    "    - Creating a new Haskell project\n",
    "    - Going over the Cabal file using an external library\n",
    "    - Building and running our executable\n",
    "- Language extensions and Pragmas\n",
    "    - NumericUnderscores\n",
    "    - TypeApplications"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-danger\">\n",
    "    <b>\n",
    "    The video and written lessons differ because the video format allows for explanations through exemplification, and the written one is more suitable for sequential explanations. \n",
    "    </b> \n",
    "    Use this to your advantage! 😃 If something doesn't make sense in one medium, maybe it will in the other!\n",
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
    "## Cabal"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "tags": []
   },
   "source": [
    "[Cabal](https://cabal.readthedocs.io/en/stable/intro.html) is a system for building and packaging Haskell libraries and programs. The name **cabal** stands for *Common Architecture for Building Applications and Libraries*.\n",
    "\n",
    "The term cabal is overloaded. It can refer to either: cabal-the-spec (.cabal files), cabal-the-library (code that understands .cabal files), or cabal-the-tool (the `cabal-install` package which provides the `cabal` executable);\n",
    "\n",
    "Because these three usually work in tandem, we're going to refer to all three as a single \"thing\" called Cabal."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-info\">\n",
    "This lecture assumes you already have Cabal installed in your system; If you don't, please refer to the previous \"Installing Haskell Locally\" lesson. \n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Cabal makes it easier for developers to:\n",
    "- Use other developer's packages\n",
    "- Create and share their own libraries\n",
    "- Configure how to build and run tests and executables\n",
    "- etc."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "By default, Cabal uses [Hackage](https://hackage.haskell.org/) as the place to look for libraries needed by the developer.\n",
    "\n",
    "Hackages is a central package archive that has thousands of Haskell libraries and programs ready for you to use them."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Cabal uses a local index of Hackage to resolve dependencies, so you always want to keep it updated. To do that, you can run:\n",
    "\n",
    "```\n",
    "cabal update\n",
    "```\n",
    "\n",
    "(See [here](https://cabal.readthedocs.io/en/stable/cabal-commands.html#cabal-update) the documentation.)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, we're ready to start our first Haskell project! 😄"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Creating a new Haskell project"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "To create a new Haskell project that follows the cabal architecture, we use the `cabal init` command:\n",
    "\n",
    "```\n",
    "cabal init\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "When we run this command, Cabal is going to start asking a bunch of questions about the software we want to build. **You can change everything later by modifying the `.cabal` file, so don't worry too much about it!**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "After answering all those questions, Cabal will create files and folders inside your current directory. So make sure to create a directory and go inside before running `cabal init`!\n",
    "\n",
    "Depending on your chosen options, you might have a different folder structure. But it should look mostly like this:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "```\n",
    "Project\n",
    "    |-- app\n",
    "    |    |-- Main.hs\n",
    "    |-- CHANGELOG.md\n",
    "    |-- Project.cabal\n",
    "    |-- LICENSE\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- The `Project` folder is the folder containing your Haskell project\n",
    "- The `app` folder contains the source code for your application (by default, a single `Main.hs` file.\n",
    "- The `CHANGELOG.md` file to record the changes between versions.\n",
    "- The `Project.cabal` file contains all the configuration to build and execute your executables, library, and tests (if any).\n",
    "- The `LICENESE` file containing the license of the software"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Although this is likely how Cabal creates your project, it's common for Haskell projects to have the next folder structure:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "```\n",
    "Project\n",
    "    |-- app\n",
    "    |    |-- Main.hs\n",
    "    |-- src\n",
    "         |-- ...\n",
    "    |-- CHANGELOG.md\n",
    "    |-- Project.cabal\n",
    "    |-- LICENSE\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The difference is that most of the source code is inside the `src` folder, and the `app` folder only contains the `Main` action.\n",
    "\n",
    "It doesn't make a real difference in the final result, so do as you please.\n",
    "\n",
    "And now that we have our project ready to go, here there are a few key commands:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- `cabal build`: It builds your executable or library based on the contents of the source code and the `.cabal` file.\n",
    "- `cabal exec Project`: It executes `Project`. The actual name of the executable is inside the `.cabal` file.\n",
    "- `cabal run`: It runs `cabal build` and `cabal exec` in sequence. This is a convenient command to avoid the repetitive work of running the same two commands every time we change something.\n",
    "- `cabal test`: Runs the tests specified in the `.cabal` file. (We won't work with tests in this lesson.)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As you can see, everything depends on the `.cabal` file. So let's learn about it!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Going over the Cabal file"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The `.cabal` file contains rules in a similar format as YAML files. Let's see the most common ones, starting with the informational:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "```\n",
    "cabal-version:      3.0\n",
    "-- The cabal-version field refers to the version of the .cabal\n",
    "-- specification and can be different from the cabal-install\n",
    "-- (the tool) version and the Cabal (the library) version you\n",
    "-- are using.\n",
    "-- The way we write this (ForestGame.cabal) file changes over\n",
    "-- time with new versions. By stating the version we use, Cabal\n",
    "-- will be able to interpret it.\n",
    "-- Starting from the specification version 2.2, the cabal-version\n",
    "-- field must be the first thing in the cabal file.\n",
    "\n",
    "\n",
    "-- The name of the package.\n",
    "name:               ForestGame\n",
    "\n",
    "-- The package version.\n",
    "-- See the Haskell package versioning policy (PVP) for standards\n",
    "-- guiding when and how versions should be incremented.\n",
    "-- https://pvp.haskell.org\n",
    "-- PVP summary:     +-+------- breaking API changes\n",
    "--                  | | +----- non-breaking API additions\n",
    "--                  | | | +--- code changes with no API change\n",
    "version:            0.1.0.0\n",
    "\n",
    "-- A short (one-line) description of the package.\n",
    "synopsis:           A cool game\n",
    "\n",
    "-- A longer description of the package.\n",
    "description:        This game is really, reeeally cool! Trust me.\n",
    "\n",
    "-- The license under which the package is released.\n",
    "license:            MIT\n",
    "\n",
    "-- The file containing the license text.\n",
    "license-file:       LICENSE\n",
    "\n",
    "-- The package author(s).\n",
    "author:             Robertino Martinez\n",
    "\n",
    "-- An email address to which users can send suggestions, \n",
    "-- bug reports, and patches.\n",
    "maintainer:         robertino.martinez@iohk.io\n",
    "\n",
    "-- Category to find our package if we upload it to Hackage\n",
    "category:           Game\n",
    "\n",
    "-- The type of build used by this package. Leave it as it is\n",
    "-- or remove it entirely. We won't use Custom builds.\n",
    "build-type:         Simple\n",
    "\n",
    "-- Extra doc files to be distributed with the package, such\n",
    "-- as a CHANGELOG or a README.\n",
    "extra-doc-files:    CHANGELOG.md\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As you can see, we're adding information about ourselves and the package, but no instructions on how to process the source code yet.\n",
    "\n",
    "Now, let's see we want to build the executable of our game. For that, we can use the `executable` sections. Let's see one:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "```\n",
    "executable ForestGame\n",
    "    main-is:          Main.hs\n",
    "    other-modules:    Forest.Level1\n",
    "                    , User.Actions.Move\n",
    "    build-depends:    base   ^>=4.16.4.0\n",
    "                    , random ^>=1.2.1.1\n",
    "    hs-source-dirs:   app, src\n",
    "    default-language: Haskell2010\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We indicate what is part of the `executable` section using indentation. Let's go over one by one:\n",
    "\n",
    "- `executable ForestGame`: Indicates that we're specifying an executable called ForestGame.\n",
    "- `main-is`: We specify where the main module resides.\n",
    "- `other-modules`: We specify auxiliary modules used by our executable.\n",
    "- `build-depends`: Declares the library dependencies (with version) required to build the current package component. In this case, we depend on the `base` and `random` libraries. (see the video of this lesson to know how we use them.)\n",
    "- `hs-source-dirs`: Root directories for the module hierarchy. In this case, instead of using only `app`, we chose to use `app` and `src` to contain our source code.\n",
    "- `default-language`: The version of Haskell we want to use."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "With only the informational and executable instructions, we have everything needed for Cabal to be able to build our executable.\n",
    "\n",
    "Although, we also have the option to create:\n",
    "- [A library](https://cabal.readthedocs.io/en/stable/cabal-package.html#library),\n",
    "- [Tests suites](https://cabal.readthedocs.io/en/stable/cabal-package.html#test-suites),\n",
    "- And more executables if we wanted to. (For example, if we wanted to have \"development\" and \"production\" executables that differ in some way.)\n",
    "\n",
    "\n",
    "You can configure A LOT with Cabal. Usually, the best course of action is to figure out what you want to do and search [Cabal's documentation](https://cabal.readthedocs.io/en/stable/index.html) to see how to do it."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Building and running our executable"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now that we have our cabal file, we can build and execute our software without worrying about resolving dependencies, downloading packages, etc.\n",
    "\n",
    "We can just run:\n",
    "\n",
    "```\n",
    "cabal build\n",
    "```\n",
    "\n",
    "And Cabal will do everything for us! 😄🙌\n",
    "\n",
    "And once everything is built, we can run any executable with:\n",
    "\n",
    "```\n",
    "cabal exec ForestGame\n",
    "```\n",
    "\n",
    "Of course, while developing, you'd have to build+execute quite a lot. That's why Cabal has a special command for that:\n",
    "\n",
    "```\n",
    "cabal run\n",
    "```\n",
    "\n",
    "When running `cabal run`, Cabal will check if any source code changed, and if it did, it will rebuild only the files that changed and then run the executable! Extremely convenient! 😎"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-info\">\n",
    "For a more step-by-step explanation with a real-world example, take a look at the corresponding video lesson! 😃 \n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Language extensions and Pragmas"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Usually, in most mainstream programming languages, your language for a specific version always works the same. For example, Python 3.7 and 3.10 are different, but Python 3.7 will always have the same syntax and functionality. The only way you can change how Python works or its syntax is by changing the version of the language.\n",
    "\n",
    "Haskell is different. Haskell has language extensions.\n",
    "\n",
    "Language extensions are a way to modify how the Haskell compiler interprets your code. By activating language extensions, you essentially change the Haskell language to have a particular feature you want or need. This way, you can tailor the language to your taste or use case!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can add language extensions by specifying them in your `.cabal` file or by adding a **Language Pragma** to the top of the file you want the extension to be active.\n",
    "\n",
    "The syntax to add a language pragma to a Haskell file is by adding this statement at the top of the file:\n",
    "\n",
    "```\n",
    "{-# LANGUAGE extension_name #-}\n",
    "```\n",
    "\n",
    "Let's see a few examples!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### NumericUnderscores"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's say we're working with an app that uses big numbers, such as a game:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "15049231"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "userGems = 15894231\n",
    "\n",
    "purchase gems item = gems - item\n",
    "\n",
    "level1Vest = 52000\n",
    "level2Vest = 147000\n",
    "level3Vest = 845000\n",
    "tank = 314159265358\n",
    "\n",
    "-- Usage example:\n",
    "purchase userGems level3Vest"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It works. But because we're using large numbers, it's easy to mess up. It's hard to tell the number at a glance. One more zero looks kind of the same! 🤷‍♂️\n",
    "\n",
    "That's when the `NumericUnderscores` language extension comes in.\n",
    "\n",
    "This language extension adds support for expressing underscores in numeric literals. That is, underscores in numeric literals are ignored when `NumericUnderscores` is enabled. For instance, the numeric literal 1_000_000 will be parsed into 1000000 when `NumericUnderscores` is enabled. The underscores are only there to assist human readers.\n",
    "\n",
    "So, if we activate the extension, we can rewrite our code like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "15049231"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "{-# LANGUAGE NumericUnderscores #-}\n",
    "\n",
    "userGems = 15_894_231\n",
    "\n",
    "purchase gems item = gems - item\n",
    "\n",
    "level1Vest = 52_000\n",
    "level2Vest = 147_000\n",
    "level3Vest = 845_000\n",
    "tank = 314_159_265_358\n",
    "\n",
    "-- Usage example:\n",
    "purchase userGems level3Vest"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As you can see, the final result didn't change. But we effectively changed Haskell's syntax so that numeric values can look different (can have underscores)!\n",
    "\n",
    "Now, let's use a language extension that does a more significant change: `TypeApplications`."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### TypeApplications"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "`TypeApplications` allows you to instantiate one or more of a polymorphic function’s type arguments to a specific type.\n",
    "\n",
    "For example, the function `read` is of type:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
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
       "</style><span class='get-type'>read :: forall a. Read a => String -> a</span>"
      ],
      "text/plain": [
       "read :: forall a. Read a => String -> a"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    ":t read"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " The `forall a.` part indicates that all `a` are the same type. And `Read a =>` indicates that the same type is an instance of the `Read` type class.\n",
    " \n",
    "So, if we do:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "Prelude.read: no parse"
     ]
    }
   ],
   "source": [
    "read \"4\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In this JupyterNotebook, we get that `Prelude.read: no parse` error. But in a real scenario, we'd get a long error that starts with:\n",
    "\n",
    "```\n",
    "Ambiguous type variable ‘a0’ arising from a use of ‘parse’\n",
    "  prevents the constraint ‘(Read a0)’ from being solved.\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We get an error because the literal `4` could be any numeric value, and we're not indicating which one. So the compiler doesn't know which instance of `Read` to use. Should it use the `Int` instance? The `Integer` instance? `Float`? `Double`?\n",
    "\n",
    "One way to solve this specific scenario is to use the `::` operator like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "(read \"4\") :: Int"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We're explicitly expressing that the `read \"4\"` expression should evaluate to an `Int`, so now the compiler knows it should use the `Read Int` instance.\n",
    "\n",
    "Now, instead of doing this, we can use the `TypeApplications` language extension and use the `@` keyword to apply the function to a type like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "{-# LANGUAGE TypeApplications #-}\n",
    "\n",
    "read @Int \"4\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What does means comes back to the `read` type signature. If we compare the type signature of `read` and `read @Int`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
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
       "</style><span class='get-type'>read :: forall a. Read a => String -> a</span>"
      ],
      "text/plain": [
       "read :: forall a. Read a => String -> a"
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
       "</style><span class='get-type'>read @Int :: String -> Int</span>"
      ],
      "text/plain": [
       "read @Int :: String -> Int"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "{-# LANGUAGE TypeApplications #-}\n",
    "\n",
    ":t read\n",
    ":t read @Int"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We see that we're specializing the type variable `a` to `Int`.\n",
    "\n",
    "This works in more complex scenarios. In the following example, we define the `Number` type that holds either a whole number, a decimal number, or a string of an unidentified number:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
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
       "</style><span class='get-type'>WHOLE :: forall a b. a -> Number a b</span>"
      ],
      "text/plain": [
       "WHOLE :: forall a b. a -> Number a b"
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
       "</style><span class='get-type'>WHOLE @Int :: forall b. Int -> Number Int b</span>"
      ],
      "text/plain": [
       "WHOLE @Int :: forall b. Int -> Number Int b"
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
       "</style><span class='get-type'>WHOLE @Int @Float :: Int -> Number Int Float</span>"
      ],
      "text/plain": [
       "WHOLE @Int @Float :: Int -> Number Int Float"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "{-# LANGUAGE TypeApplications #-}\n",
    "\n",
    "data Number a b = WHOLE a | DECIMAL b | NAN String deriving (Show)\n",
    "\n",
    ":t WHOLE\n",
    ":t WHOLE @Int\n",
    ":t WHOLE @Int @Float"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "And if you want to specify the type of the second parameter (`b`) but leave the first type as a polymorphic one, you can use another language extension called `PartialTypeSignatures` that allows you to put wildcards in types:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {
    "scrolled": true
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
       "</style><span class='get-type'>DECIMAL @Int :: forall b. b -> Number Int b</span>"
      ],
      "text/plain": [
       "DECIMAL @Int :: forall b. b -> Number Int b"
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
       "</style><span class='get-type'>DECIMAL @_ @Float :: forall _. Float -> Number _ Float</span>"
      ],
      "text/plain": [
       "DECIMAL @_ @Float :: forall _. Float -> Number _ Float"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "{-# LANGUAGE TypeApplications #-}\n",
    "{-# LANGUAGE PartialTypeSignatures #-}\n",
    "\n",
    "data Number a b = WHOLE a | DECIMAL b | NAN String deriving (Show)\n",
    "\n",
    ":t DECIMAL @Int\n",
    ":t DECIMAL @_ @Float -- Now the \"a\" type is shown as \"_\"."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's see this in a way that makes a real difference in the final result.\n",
    "\n",
    "We create the `parse` function that takes in a `String` and parses it into a value of type `Number a b` depending if it represents a `WHOLE` number, a `DECIMAL` number, or if it couldn't identify the number (`NAN`):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "parse :: (Read a, Read b) => String -> Number a b\n",
    "parse inp\n",
    "  | isNumber && isDecimal = DECIMAL $ read inp\n",
    "  | isNumber = WHOLE $ read inp\n",
    "  | otherwise = NAN inp\n",
    " where\n",
    "  validChar = \".0123456789\"\n",
    "  isNumber = all (`elem` validChar) inp\n",
    "  isDecimal = '.' `elem` inp"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, if we try to use this function without indicating the type:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "Prelude.read: no parse"
     ]
    }
   ],
   "source": [
    "parse \"98\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We get the same error we got before because GHC can't infer the type of `98`. \n",
    "\n",
    "If we indicate the types, everything works fine. But not only that! **By specializing the variables `a` and `b` types when applying the `parse` function, we get to choose what kind of precision we want when parsing a whole or a decimal number!**:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "WHOLE (-9223372036854775808)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "WHOLE 9223372036854775808"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "DECIMAL 1.2345679"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "DECIMAL 1.23456789"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "NAN \"para bailar la bamba!!\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "longWhole = \"9223372036854775808\"\n",
    "longDecimal = \"1.23456789\"\n",
    "\n",
    "--     'a'       'b'   \n",
    "parse @Int             longWhole\n",
    "parse @Integer         longWhole\n",
    "parse @_       @Float  longDecimal\n",
    "parse @_       @Double longDecimal\n",
    "parse @Int     @Double \"para bailar la bamba!!\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### The `@` symbol"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The `@` symbol is also used to pattern-match an entire structure (like a list, record type, etc.) while pattern-matching for its parts."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In the example below, the `counts` function takes in a list and returns a list of tuples with the unique value and how many times the value is in the list.\n",
    "\n",
    "When we pattern match to extract the first value `(x:_)`, we also add `list@` that creates a variable named `list`, which is equal to the entire list `x:xs`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('s',3),('u',2),('c',2),('e',1),('f',1),('l',2),('y',1)]"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "counts :: Eq a => [a] -> [(a, Int)]\n",
    "counts [] = []\n",
    "counts list@(x:_) = (x, length (filter (== x) list)) : counts (filter (/= x) list)\n",
    "\n",
    "counts \"successfully\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The main difference between when we use the `@` sign to apply a type or to pattern match is the space to is left: \n",
    "- Pattern matching: it has no space to its left `list@(x:xs)`\n",
    "- Apply type: it has a space `read @Int`\n",
    "\n",
    "That's how the compiler knows which is which."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "There are a ton of language extensions ([see this list for reference](https://downloads.haskell.org/ghc/latest/docs/users_guide/exts/table.html)), and we'll use new ones when needed. But for now, make sure to do your homework!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-danger\">\n",
    "The homework is based on the example in the video lesson. If you feel lost, take a look at the part where I explain the example's code.\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## That's it for today! Make sure to do the homework! 😁"
   ]
  }
 ],
 "metadata": {
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
