# Haskell Course

[Versión en 🇪🇸 traducida por la comunidad](https://github.com/input-output-hk/haskell-course/tree/main/ES-translation)

> *The easiest way to learn Haskell* - R.M.

**This course is designed to teach non-engineers (e.g., self-taught/bootcamp coders) Haskell from zero to productive in an interactive, easy-to-follow way.** The course doesn't contain content specific to Marlowe or Plutus, but it will cover all the Haskell you'll needed to work with them.

For a more detailed explanation, keep reading or watch the introduction video:
[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://youtu.be/H1vbUKMKvnM)

## How much should I study if I only wish to use Marlowe/Plutus?

In the [outline](#what-well-cover) below, there are clear stopping points (for both Marlowe and Plutus) where we deem you to know enough Haskell to effectively use the technology.

## How to read/watch the lessons

To go through the **interactive lessons**, go to your chosen lesson's outline inside "[What we'll cover](#what-well-cover)" and click on the button that looks like the one below. If the page loads with a "500: Internal Server Error" just refresh it, and it should be fine. At the top, you will see a console that displays the progress of preparing your interactive lesson. During this time, you can scroll down and look at the lesson, that is displayed non-interactively.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F01-Introduction-to-haskell.ipynb)

And to see the **video lessons**, click on the button that looks like this:

[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://youtu.be/H1vbUKMKvnM)

## To do the homework

1. Clone this repository.
2. Create a [GitPod](https://www.gitpod.io/) account.
3. Click this button to create a remote dev environment: [![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=flat&logo=visual-studio-code&logoColor=white)](https://gitpod.io/#https://github.com/input-output-hk/haskell-course)
4. Select the `Homework/HomeworkXX` folder with the homework you want to complete.
5. Follow the instructions inside the `Homework.hs` or `Main.hs` file.
6. **Check the solutions in the `solutions` branch!**

#### Repository structure

    Haskell-Course
        |   |
        |   |---- Homework
        |          |
        |          |---- Homework01 (Homework for lesson 01)
        |          |---- Homework02 (Homework for lesson 02)
        |          ...
        |
        |-------- lessons (Lessons in Jupyter notebook format. Access through Binder.)
                   |
                   |---- 1-Introduction-to-haskell
                   |---- 2-Functions-Data-Types-and-Signatures

Everything else can be safely ignored

## To hang out and discuss with other students

- [IOG's technical community (check out the #ask-haskell channel!)](https://discord.gg/inputoutput)

## FAQ

[FAQ](FAQ.md)

## Proposed changes for next iteration/version

[Changes](Changes.md)

## What we'll cover

**This is a tentative outline. Changes can (and will) be made as we advance with the course and gather feedback from students.**

**If there are no buttons on a lesson, it means that it's not published yet.**

---

### BEGINNER SECTION - GETTING STARTED WITH HASKELL - 🥚⟶🐣
In this section, we get familiar with basic concepts and Haskell syntax.

---

### 1. Intro and tools [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F01-Introduction-to-haskell.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://youtu.be/pkU8eiNZipQ)

- Intro to the course and lectures
  - What we’ll cover
  - Repository structure
- Intro to Haskell
  - How to open and use JupyterLab
  - Purely functional programming language
  - Basic syntax
  - Haskell Type system
  - Laziness
  - GHC (and GHCi)
- GitPod
  - How to open and use GitPod
  - Example of how to complete a homework assignment.

### 2. Data types, Signatures, and Polymorphism [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F02-Functions-Data-Types-and-Signatures.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://youtu.be/RABzYje2d2A)

- Pragmatic intro to types
- Type signature
  - Function’s signatures
  - Variables in Haskell
    - Parameters in functions
    - Names/Definitions
- Infix and prefix functions
- Data Types in depth
  - Int, Integer
  - Float, Double
  - Rational
  - Bool
  - Char
  - Lists
  - Strings
  - Tuples + Tuples VS Lists
- Polymorphic values and type variables

### 3. Conditions and helper constructions [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F03-Conditions-and-helper-constructions.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=G0XPELNZuws)

- If-then-else
- Guards
- `let` expressions
- `where`
- Should I use `let` or `where`?
- Things to keep in mind

### 4. Pattern matching and Case [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F04-Pattern-matching.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=sQPGN4b95DU)

- What is pattern matching
- Pattern matching on
  - Function implementations
  - Lists
  - Tuples
- Case

### 5. Improving and combining functions [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F05-Improving-and-combining-functions.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://youtu.be/E-OEw4FKdf4)

- Higher-order functions
  - The `filter` function
  - The `any` function
- Lambda functions
- Precedence and associativity
- Curried functions
  - Partial application
- Composing and applying functions
  - The `$` operator
  - The `.` operator
- Point-free style

### 6. Recursion [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F06-Recursion-and-folds.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=wzvbUxSykXM)

- Why Recursion?
- Thinking Recursively
  - `sum` and `product`
- Steps to create your own recursive function
- Examples of recursion
  - `and`, `length`, `reverse`, `drop`, `take`, `map`, `filter`
- Extracting the `foldr` pattern
- The `foldl` function
- The `foldl'` function
- When to use `foldr`, `foldl`, and `foldl'`

### 7. Intro to Type Classes [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F07-Intro-to-Type-Classes.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=dGNd0GmsYWU)

- The awesomeness of type classes
- What are type classes
- Common type classes
  - `Eq`, `Ord`
  - `Num`, `Integral`, `Floating`
  - `Read`, `Show`
- The most general valid type
- Multiple constraints

### 8. Creating Non-Parameterized Types [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F08-Creating-non-parameterized-types.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=mAZC1w_VfEs)

- Type synonyms
  - How to define type synonyms
  - Why use type synonyms
- Defining new types
  - Creating new types with `data`
  - Using new types
  - Value parameters
- Record syntax

### 9. Creating Parameterized and Recursive Types [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F09-Creating-parameterized-and-recursive-types.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=wPV94aZIOGQ)

- Type Parameters
  - Prameteryzing `type` synonyms
  - Prameteryzing `data` types
- Recursive data types
  - `Tweet` me a river
  - A `Sequence` of `Node`s
  - A `Tree` of `Node`s
- Kinds
- The `newType` keyword

### 10. Creating Type Classes and Instances [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F10-Creating-Type-Classes-and-Instances.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=I6tmM3wNGEI)

- Overloading
- Steps to create Type Classes and Instances
- The `Eq` type class
  - Defining the Type Class
  - Defining multiple instances
  - Improving our `Eq` type class with mutual recursion (and Minimal Complete Definitions)
  - Defining an instance for a parameterized type.
- The `WeAccept` Type Class
- The `Container` Type Class
- Exploring `Ord` type class (Subclassing)
- Deriving
  - Deriving can go wrong

### 11. Basic IO  [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F11-Basic-IO.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=0xQ8j6h8bNc)

- Pure functions
- Introduction to IO actions
- IO actions under the hood
- IO actions in practice
  - The `()` type
- Interacting with the user
  - `getChar`, `getLine`, and `putStrLn`
- Actions are first-class values
- Composing IO actions (`>>` and `>>=` operators)
- The `do` block
  - Using `let`, nesting do-blocks, escaping `IO` and `return`
- The `main` action
- Concepts and syntax recap

---

### BEGINNER SECTION - GAINING INDEPENDENCE - 🐣⟶🐥
In this section, we learn about Haskell tooling and the necessary concepts to start working on our own projects.

---

### 12. Installing Haskell Locally [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F12-Installing-Haskell-and-first-program.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=hSN5mxITv0A&list=PLNEK_Ejlx3x1D9Vq5kqeC3ZDEP7in4dqb&index=13)

- Installing Haskell
    - Installing GHCup
    - Installing GHC, Cabal, Stack, and HLS with GHCup
    - Installing VSCode Extensions
- Creating our first program
    - Writing the simplest Haskell program
    - Compiling and running our program

### 13. Modules [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F13-Modules.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=R64sCXU0Ru0&list=PLNEK_Ejlx3x1D9Vq5kqeC3ZDEP7in4dqb&index=14)

- Importing Modules
    - Controlling environments
    - Controlling namespaces
- Creating our own Modules
- The `Prelude` and Standard Libraries

### 14. Cabal and language extensions [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F14-Cabal_and_language_extensions.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=AvpMOMSSZHs&list=PLNEK_Ejlx3x1D9Vq5kqeC3ZDEP7in4dqb&index=15)

- Cabal
    - Introduction to Cabal
    - Creating a new Haskell project
    - Going over the Cabal file using an external library
    - Building and running our executable
- Language extensions and Pragmas
    - Introduction
    - `NumericUnderscores`
    - `TypeApplications`

### 15. Handling Errors [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F15-Handling-Errors.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=QkUCHFG1hK8&list=PLNEK_Ejlx3x1D9Vq5kqeC3ZDEP7in4dqb&index=16)

- There're always `Exception`s to the rule
- Speed-running `Exception`s with a dumb self-driving 🤖 car 🚗
  - I'm the `Exception` cause I have `class` 😎
  - `throw` all the `Exception`s you want. I'll `catch` them all!
- `Maybe` give me a value? 🙏
  - Benefits of optional values
- Ok, you `Either` give me a value or a reason why you didn't!
- From `Exception`s to optional values
- Tradeoffs
  - So, what should I use?

### 16. Learning on your own and final section project [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F16-Gaining-your-independence-and-project.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=ObZ_1eap5MY&list=PLNEK_Ejlx3x1D9Vq5kqeC3ZDEP7in4dqb&index=17)

- Small tips and tricks 🤹
  - REPL
  - Hackage
  - Hoogle
  - `undefined`
  - Type Holes 🕳️
- Section's Final Project 🥳

---

### BEGINNER SECTION - BASIC ABSTRACTIONS & EFFECTS - 🐥⟶🐓
In this section, we learn about a few of the most useful and talked about Abstractions in Haskell and how we deal with effects in general (not only `IO`).

---

### 17. Semigroup and Monoid [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F17-Semigroup-and-Monoid.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=-O1ZApHPvkg&list=PLNEK_Ejlx3x1D9Vq5kqeC3ZDEP7in4dqb&index=18)

- What does it mean to abstract a pattern?
- Why abstracting patterns (in general)?
- Teaser: Why abstracting `Semigroup` and `Monoid`?
- The `Semigroup` type class
- The `Monoid` type class
- What can I do with `Semigroup` and `Monoid`?

### 18. Functor [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F18-Functor.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=Fb4qD5PWEs8&list=PLNEK_Ejlx3x1D9Vq5kqeC3ZDEP7in4dqb&index=19)

- Abstracting the `map` function
- The `Functor` type class
- Defining `Functor` instances
- Seemingly unintuitive `Functor` instances
  - The `Either a` functor 🤔
  - The `(,) a` functor 🤨
  - The `(->) r` functor 🤯
- Defining the `<$>` operator and *lifting* 🏋️ a function
- `Functor` nesting dolls 🪆
- Extra functions and `Functor` as defined in `base`


### 19. Applicative and Effects [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F19-Applicative.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=7vxhNfNWP3k&list=PLNEK_Ejlx3x1D9Vq5kqeC3ZDEP7in4dqb&index=20)

- Why `Applicative` functors?
    - Our journey until now
    - The limits of Functor
- Function application at the `Functor` level 🥇
- Being `pure` 😇
- The `Applicative` type class
- The `Applicative` laws
- 🎆 Programming with effects 🎆
- Extra functions and `Applicative` as defined in `base`

### 20. Monad [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/input-output-hk/haskell-course/HEAD?labpath=%2Flessons%2F20-Monad.ipynb) [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=BFgmrO-c0Ec&list=PLNEK_Ejlx3x1D9Vq5kqeC3ZDEP7in4dqb&index=21)

- Why `Monad`s?
- Extracting the pattern for:
    - `Maybe`
    - `Either e`
    - `Log`
- Abstracting the `Monad` Type Class
- The abstraction `Monad`chy
- The `Monad`ic laws
- `Monad` as defined in `base`
- You have to `do` what you have to `do`

### 21. Reader, Writer, and State Monads

- Introduction
- Logs `Writer` (based on `Log`)
    - Incentive
    - Generalizing `Log`
    - Helper fucntions
- Environment `Reader`
    - Interacting with a (fake) database
    - Extracting the pattern
    - Using the `Reader` Monad
- The `State` of things
    - Implementing a vending machine
    - Extracting the pattern
    - Using the `State` Monad

### 22. Final project

- TODO

---

#### 🥳 CONGRATULATIONS! 🥳 You can call yourself a (beginner) Haskell developer!
Thank you for going on this journey with me! Please feel free to give us feedback through issues, email, or Twitter. And share this course if you find it valuable. 😄🙌

---

### Where can you go from now?

It depends on your preferences. You could:

- If you're interested in Cardano, explore Marlowe, Plutus, Atlas, CardanoAPI, and other Cardano-related tools and libraries.
- Start your own project and learn what you need on the way (e.g., a server, a compiler, a full-stack app using IHP)
- Read Haskell books and sources that go into more advanced subjects. See recommended resources here.
- Learn about specific subjects, for example (organized roughly by difficulty):
  1. Explore the `base` library and understand all types and type classes.
  1. Learn about Testing (unit vs property testing and QuickCheck).
  1. Explore how to deal with Concurrency and Parallelism.
  1. Learn about Parsers (Parser combinators, `Alternative` type class, `MonadPlus`, Parsec library).
  1. Learn how Haskell deals with data structures under the Hood.
  1. Monad Transformers and Free monads.
  1. Generic programming.
  1. Meta programming with Template Haskell.
  1. Type-level programming.

---


