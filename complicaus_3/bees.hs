import Data.Bifunctor
import Data.Bool
import Data.Set as Set
import Text.Read

tuple2To3 (x, y, z) = (x, y)

solve ps = fmap (sizeRightPivot . flip Set.splitMember prices)
  where
    prices = Set.fromList ps
    sizeRightPivot = uncurry (+) . bimap Set.size (bool 0 1) . tuple2To3

parse :: String -> Maybe ([Int], [Int])
parse s = case lines s of
  (_ : ps : _ : cs) -> (,) <$> (traverse readMaybe $ words ps) <*> traverse readMaybe cs
  _ -> Nothing

run = fmap (uncurry solve) . parse

main = interact $ maybe "Invalid input" (unlines . fmap show) . run
