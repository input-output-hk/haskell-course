{-# LANGUAGE ScopedTypeVariables #-}

module Homework15B where

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
-- IMPORTANT: Read the README.md file before completing the homework.
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------

-- 1. Write a function that takes a list and returns the head if the list is not empty.
-- If the list is empty, return Nothing.

headMaybe :: [a] -> Maybe a
headMaybe = undefined

-- 2. Write a function that takes a list of Maybe values and returns a list of all the Just values.
-- If there are no Just values, return an empty list.

catMaybes :: [Maybe a] -> [a]
catMaybes = undefined

-- 3. Write a function that tries to read from a file and returns the contents of the file.
-- If the file does not exist, return Nothing.

readFileMaybe :: FilePath -> IO (Maybe String)
readFileMaybe = undefined

-- 4. Write a function that checks all the requirements for a password using the
-- Either type with a custom data type for errors.
-- The requirements are:
-- - The password must be at least 10 characters long.
-- - The password must contain at least one digit.
-- - The password must contain at least one uppercase letter.
-- - The password must contain at least one lowercase letter.

data PasswordError = WrongConstructor

passwordLongEnough :: String -> Either PasswordError String
passwordLongEnough = undefined

passwordHasDigit :: String -> Either PasswordError String
passwordHasDigit = undefined

passwordHasUppercase :: String -> Either PasswordError String
passwordHasUppercase = undefined

passwordHasLowercase :: String -> Either PasswordError String
passwordHasLowercase = undefined

passwordRequirements :: String -> Either PasswordError String
passwordRequirements = undefined
