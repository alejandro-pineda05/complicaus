{-# LANGUAGE BangPatterns #-}

import Data.Bifunctor
import Data.List
import Data.Maybe

solve :: String -> String
solve w = fromMaybe w $ do
  (start, rem') <- uncons w
  (end, mid) <- uncons $ reverse rem'
  let n = length mid
  return $
    if n > 8
      then
        [start] <> show n <> [end]
      else w

parse = drop 1 . lines

run = fmap solve . parse

main = interact $ unlines . run