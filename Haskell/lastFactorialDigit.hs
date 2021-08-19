-- factorial
-- Simple factorial function that returns n factorial n-1, that is n times the next factorial
-- or 1 if the factorial of 0 i reached.

factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial n-1

-- factorialCalls
-- The idea is to make it so the function takes an integer N that determines exactly how
-- many times the faculty of a certain integer should be calculated. This is then to be inserted
-- into a tail-recursive list. Lastly the idea is to have this list brought back to a function that
-- should take the list and just print every entry.

factorialCalls :: Integer -> [Integer] -> [Integer]
factorialCalls 0 xs = xs
factorialCalls n xs =
	factorialCalls (n-1) (xs) --(factorial (read number :: Integer)):xs 

-- getNumber
-- An attempt to get a function that will return a number / or string, whatever, to work.

getNumber :: String
getNumber = do number <- getLine


main = do
	numberOfEntries <- getLine
	print(factorialCalls (read numberOfEntries :: Integer) []) -- Gör en rekursiv printare 