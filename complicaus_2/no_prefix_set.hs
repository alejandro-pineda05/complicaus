-- Source: HackerRank
-- URL: https://www.hackerrank.com/challenges/no-prefix-set/problem
-- Solution by Alejandro Domínguez Muñoz

import Control.Monad
import Data.Bifunctor
import Data.List as L
import Data.Set as S
import Data.Maybe

solve = traverse (uncurry (flip isPrefixOf')) . pairs

pairs = uncurry fmap . first (,)
    <=< mapMaybe uncons . tails . fmap snd . S.toDescList . S.fromList . fmap (\s -> (length s, s))

isPrefixOf' xs ys | xs `isPrefixOf` ys = Left ys
                  | otherwise          = Right ()

parse = L.drop 1 . lines

run = solve . parse

main = interact $ either ("BAD SET\n" <>) (const "GOOD SET") . run
