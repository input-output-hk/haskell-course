{-# LANGUAGE TypeApplications #-}

module Main where

import Forest.Level1 (Forest (..), level1forest)
import System.Random (randomRIO)
import User.Actions.Move (AvailableMoves, move)
import User.Actions.Battle (battle)

main :: IO ()
main = do
  startingStamina <- randomRIO @Int (10_000, 20_000)
  putStrLn "\nYou're traped in a Forest, try to scape! Remember that you loose stamina with each step you take."
  gameLoop (startingStamina, level1forest)
 where
  gameLoop (_, FoundExit) = putStrLn "YOU'VE FOUND THE EXIT!!"
  gameLoop (s, _) | s <= 0 = putStrLn "You ran out of stamina and died -.-!"
  gameLoop (s, forest) = do
    let continueLoop = do
          putStrLn $ "\nYou have " ++ show s ++ " stamina, and you're still inside the Forest. Choose a path, brave adventurer: GoLeft, GoRight, or GoForward."
          selectedMove <- getLine
          gameLoop $ move (s, forest) (read @AvailableMoves selectedMove)
    battleDice <- randomRIO @Int (0, 3)
    case battleDice of
      2 -> do
        r <- battle
        if r then continueLoop else return ()
      _ -> continueLoop