{-# LANGUAGE TypeApplications #-}
{-# LANGUAGE NamedFieldPuns #-}
{-# LANGUAGE RecordWildCards #-}

module User.Actions.Battle where

data Golem = Golem { gAttack :: Int, gHp :: Int } deriving Show
data Player = Player { pAttack :: Int, pHp :: Int } deriving (Show)
data Battle = Fight | RunAway deriving (Show, Read)

battle :: IO Bool
battle = undefined