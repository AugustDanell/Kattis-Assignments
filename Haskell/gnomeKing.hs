-- Gnomeking https://open.kattis.com/problems/oddgnome
gnome :: [String] -> [String]
gnome _ = []

makeInteger :: [String] -> [Integer] -> [Integer] 
makeInteger (x:xs) os = makeInteger xs (os ++ [(read x :: Integer)])
makeInteger [x] os = os ++ [(read x :: Integer)]
makeInteger [] os = os


makeStrings :: [Integer] -> [String] -> [String]
makeStrings (x:xs) os = makeStrings xs (os ++ [(show x)])
makeStrings [x] os = os ++ [(show x)]
makeStrings [] os = os

main = do
	numberOfEntries <- getChar													-- Takes a char and encapsulates it inside of the IO. 
	getLine																		-- Remove first line.
	start <- getLine  															-- Takes in a string as IO and encapsulates it using the IO monad.

	gnome makeStrings ((sort (makeInteger (words start) [])) [])

