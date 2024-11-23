{-# LANGUAGE TupleSections #-}

import Data.List as L
import Data.Map as M
import Data.Maybe
import Data.Tuple
import Text.Read

solve a = fmap (\b -> fromMaybe elemsInA $ L.findIndex (> b) sortedA)
    where sortedA  = (uncurry replicate . swap =<<) . M.toAscList . M.fromListWith (+) . fmap (,1) $ a
          elemsInA = length a

parse :: String -> Maybe ([Int], [Int])
parse s = case fmap words . lines $ s of
    (_:a:b:_) -> (,) <$> traverse readMaybe a
                     <*> traverse readMaybe b
    _         -> Nothing

run = fmap (uncurry solve) . parse

main :: IO ()
main = interact (maybe "" (unwords . fmap show) . run)
