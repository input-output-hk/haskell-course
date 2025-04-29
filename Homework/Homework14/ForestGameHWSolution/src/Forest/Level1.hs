module Forest.Level1 (Forest (..), level1forest) where

data Forest a = FoundExit | Trail a (Forest a) (Forest a) (Forest a) deriving (Show)

level1forest :: (Num a, Ord a) => Forest a
level1forest =
  Trail
    3_000
    ( Trail
        7_000
        (Trail 3_000 FoundExit FoundExit FoundExit)
        (Trail 4_000 FoundExit FoundExit FoundExit)
        (Trail 5_000 FoundExit FoundExit FoundExit)
    )
    ( Trail
        3_000
        (Trail 3_000 FoundExit FoundExit FoundExit)
        (Trail 9_000 FoundExit FoundExit FoundExit)
        (Trail 5_000 FoundExit FoundExit FoundExit)
    )
    ( Trail
        5_000
        (Trail 3_000 FoundExit FoundExit FoundExit)
        (Trail 4_000 FoundExit FoundExit FoundExit)
        (Trail 1_000 FoundExit FoundExit FoundExit)
    )
