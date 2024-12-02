-- Source: Codeforces Gym
-- URL: https://codeforces.com/gym/102951/problem/A
-- Solution by Alejandro Domínguez Muñoz

{-# LANGUAGE TupleSections #-}

import Data.List

solve = maximum . fmap (uncurry pythagoras) . (=<<) pairsWithFirst . tails

pairsWithFirst (x:xs) = fmap (x,) xs
pairsWithFirst _      = []

pythagoras (x, y) (x', y') = ((x - x') ^ 2) + ((y - y') ^ 2)

parse :: String -> Maybe [(Int, Int)]
parse = fmap (uncurry zip) . listToTuple . fmap (fmap read . words) . drop 1 . lines

listToTuple :: [[a]] -> Maybe ([a], [a])
listToTuple [x, y] = Just (x, y)
listToTuple _      = Nothing

run :: String -> Maybe Int
run = fmap solve . parse

main :: IO ()
main = interact (maybe "" show . run)
