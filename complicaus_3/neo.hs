import Control.Monad
import Data.Bifunctor
import Data.List

indexes = (,) <$> [1 .. 5] <*> [1 .. 5]

both f = bimap f f

absDiff x y = abs (x - y)

run =
  maybe "Invalid input" show
    . fmap (\((x, y), _) -> absDiff x 3 + absDiff y 3)
    . find (\(_, c) -> c == '1')
    . zip indexes
    . join
    . words

main = interact run