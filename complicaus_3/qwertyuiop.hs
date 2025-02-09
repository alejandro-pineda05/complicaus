import Control.Monad
import Data.List as L
import Data.Map.Strict as Map
import Text.Read

rows = ["qwertyuiop", "asdfghjkl;", "zxcvbnm,./"]

shiftL row = zip row (L.drop 1 row)

shiftR row = zip (L.drop 1 row) row

changeL = Map.fromList $ (shiftL =<< rows)

changeR = Map.fromList $ (shiftR =<< rows)

data Direction = L | R deriving (Read, Show)

mapping d = flip Map.lookup $ case d of
  L -> changeL
  R -> changeR

solve d = traverse (mapping d)

parse :: String -> Maybe (Direction, String)
parse s = case lines s of
  (dir : input : _) -> (,) <$> readMaybe dir <*> pure input
  _ -> Nothing

run = uncurry solve <=< parse

main = interact $ maybe "Invalid input" id . run