{-# LANGUAGE LambdaCase #-}

import Data.List
import Data.Maybe

groupJust = fmap catMaybes . filter (/= [Nothing]) . groupBy (\_ x -> isJust x)

note = \case
    "#..." -> Just 1
    ".#.." -> Just 2
    "..#." -> Just 3
    "...#" -> Just 4
    _      -> Nothing

run = fmap reverse . groupJust . fmap note . lines

main = interact $ unlines . fmap (unwords . fmap show) . run
