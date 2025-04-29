-- Question 1
-- Investigate the `Bounded` type class. What behaviours it provides?


-- Question 2
-- The types Int and Word bellong to the same type classes. What is the difference
-- between them? Check maybe the maxBound and minBound parameter for both types.


-- Question 3
-- Investigate the `Enum` type class. What behaviours provides?


-- Question 4
-- Add the most general type signatures possible to the functions below.
-- Then uncomment the functions and try to compile.

--f1 x y z = show (x / y) ++ z

--f2 x = if x == maxBound then minBound else succ x


-- Question 5
-- Investigate the numeric type classes to figure out which behaviors they provide to change between numeric types.
