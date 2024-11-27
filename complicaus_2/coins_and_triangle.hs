import Data.Maybe
import Text.Read

solve n = length . takeWhile (<= n) . scanl1 (+) $ [1..]

parse :: String -> [Int]
parse = mapMaybe readMaybe . drop 1 . lines

run = fmap solve . parse

main = interact $ unlines . fmap show . run 
