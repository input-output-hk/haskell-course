module User.Actions.Move (AvailableMoves (..), move) where

import Forest.Level1 (Forest (..))

data AvailableMoves = GoForward | GoLeft | GoRight deriving (Show, Read)

move :: Num a => (a, Forest a) -> AvailableMoves -> (a, Forest a)
move (s, FoundExit) _ = (s, FoundExit)
move (s, Trail a x _ _) GoLeft = (s - a, x)
move (s, Trail a _ x _) GoForward = (s - a, x)
move (s, Trail a _ _ x) GoRight = (s - a, x)