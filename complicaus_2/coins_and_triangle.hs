-- Source: CodeChef
-- URL: https://www.codechef.com/problems/TRICOIN
-- Solution by Alejandro Domínguez Muñoz

import Data.Maybe
import GHC.Float
import Text.Read

-- Se sabe desde Gauss que 1 + 2 + 3 + ... + n = n(n + 1) / 2
-- La razón está en que la suma de los pares extremos de fuera
-- hacia dentro siempre da n + 1. Si n es par, esta suma se
-- repite n / 2 veces, dando la fórmula indicada. Si n es impar,
-- la suma se repite (n - 1) / 2 veces y también hay que añadir
-- el elemento intermedio de la serie, que es equivalente a
-- (n + 1) / 2, por lo que daría la fórmula
-- ((n - 1)(n + 1) + (n + 1)) / 2 = (n - 1 + 1)(n + 1) / 2 =
-- n(n + 1) / 2, que es la misma que la indicada anteriormente.
--
-- Sea c la cantidad de monedas para n niveles según la serie
-- anterior, es decir, c = n(n + 1) / 2. Siguiendo el problema,
-- tendríamos que la variable dependiente o incógnita es n y
-- la variable independiente es c. Si presentamos dicha expresión
-- bajo la forma de ecuación de segundo grado n^2 + n - 2c = 0,
-- podemos aplicar la fórmula de Bhaskara para aislar la incógnita.
-- La expresión resultante válida para valores positivos es
-- (-1 + sqrt(1 + 8c)) / 2 con redondeo a piso.
solve c = floorDouble $ (-1 + (sqrt . fromIntegral $ 1 + 8 * c)) / 2

parse :: String -> [Int]
parse = mapMaybe readMaybe . drop 1 . lines

run = fmap solve . parse

main = interact $ unlines . fmap show . run
