-- A Haskell implementation of the problem busnumbers - https://open.kattis.com/problems/busnumbers
import Data.List

-- busNumbers
-- We have 3 things to keep track of, alreadyBound (called bindMode), and currentlyBinds (We call it seq for sequence) and lastnumber. 
-- That is if it has bounded with a "-" in a previous instance, and if it does so know etc (14, 15, 16) = 14- ... (Last sequential binding).

-- Basically we have 4 cases that can occur when we have 3 elements or more.
-- 1. They can be found to be sequentially ordered etc 14, 15, 16, and the mode is not in bindMode. In which
-- case a new binding has to be made 14-16 in this case (if the next element is not 17).
-- 2. They are sequentially ordered and already in binding mode, in which -16 (or more) has to be appended into the 
-- previous set of sequence.
-- 3. Not in a sequence and in binding mode, we have to close the sequence, etc (10 as previous value) 14, 15, 17 -> 10-15.
-- 4. Not in a sequence and not in binding mode, we can discard everything. Etc 14, 15, 17 -> DISCARD 14 15 17.
-- With two or one remaining elements we can just append them onto the return string.

busnumbers :: [String] -> Bool -> String -> Integer -> String
busnumbers (x:y:z:xs) bindMode os lastNumber	-- Checks 3 numbers for a binding, takes in last binding and last integer in that binding (if there was one).			
	| ((read x :: Integer) +1 == (read y :: Integer)) && ((read y :: Integer) + 1 == (read z :: Integer)) && (bindMode == False) && (lastNumber + 1 /= (read x :: Integer)) = busnumbers xs     True   (os ++ " " ++ x) (read z :: Integer)									-- Seq found, no binding mode: Binds first occurance
	| ((read x :: Integer) +1 == (read y :: Integer)) && ((read y :: Integer) + 1 == (read z :: Integer)) && (bindMode == False) && (lastNumber + 1 == (read x :: Integer)) = busnumbers (z:xs) True   (os ++ appendHelper lastNumber x y z bindMode) (read y :: Integer)
	| ((read x :: Integer) +1 == (read y :: Integer)) && ((read y :: Integer) + 1 == (read z :: Integer)) && (bindMode == True)  && (lastNumber + 1 /= (read x :: Integer)) = busnumbers xs     True   (os ++ "-" ++ (show lastNumber) ++ " " ++ x) (read z :: Integer)		-- Seq found, binding mode.
	| ((read x :: Integer) +1 == (read y :: Integer)) && ((read y :: Integer) + 1 == (read z :: Integer)) && (bindMode == True)  && (lastNumber + 1 == (read x :: Integer)) = busnumbers xs     True   (os) (read z :: Integer)
	| ((bindMode == True)  && lastNumber + 1 /= (read x :: Integer)) = busnumbers (y:z:xs) False (os ++ "-" ++ (show lastNumber) ++ " " ++ x) (read x :: Integer)  		-- Reason as to why these cases 5 do a recursion with y:z:xs or y:xs is because enough data is not known.																																																	-- Seg not found, in binding mode.
	| ((bindMode == True)  && lastNumber + 1 == (read x :: Integer)) = busnumbers (z:xs) False (os ++ appendHelper lastNumber x y z bindMode) (read y :: Integer) 		-- For instance 3 6 7 8 9 should return -> 3 6-9, but with the 3 first digits, if they are just discarded as non
	| ((bindMode == False) && lastNumber + 1 /= (read x :: Integer)) = busnumbers (y:z:xs) False  (os ++ " " ++ x) (read x :: Integer) 	-- prev: (read z :: Integer)								-- binding we get: 3 6 7-9 (which is an incorrect answer)																																																	-- Seq not found, binding mode.
  	| ((bindMode == False) && lastNumber + 1 == (read x :: Integer)) && (read x :: Integer) +1 == (read y :: Integer) = busnumbers (z:xs) False  (os ++ "-" ++ y) (read y :: Integer) 				-- Ändra
  	| ((bindMode == False) && lastNumber + 1 == (read x :: Integer)) = busnumbers (z:xs) False  (os ++ " " ++ x ++ " " ++ y) (read y :: Integer) 				-- Ändra
  	| otherwise = busnumbers xs     True   (os) (read z :: Integer)	-- "Skrivs detta ut har vi nått ett konstigt fall!"							 																								-- Ändra																																								
busnumbers (x:y:xs) bindMode os lastNumber																																-- Two variable case
	| (read x :: Integer) +1 == (read y :: Integer) && (bindMode == False) && (lastNumber + 1) == (read x :: Integer) = os ++ "-" ++ y
	| (read x :: Integer) +1 == (read y :: Integer) && (bindMode == False) && (lastNumber + 1) /= (read x :: Integer) && (lastNumber /= 1001) = os ++ " " ++ x ++ " " ++ y -- ++ (show lastNumber)
	| (lastNumber == 1001) = os ++  " " ++ x ++ " " ++ y -- Only to avoid error in starting case of two sequential digits. Etc, Input: 1 2 = 1 2, and not 1001 1 2 
	| (read x :: Integer) +1 == (read y :: Integer) && (bindMode == True)  && (lastNumber +1) == (read x :: Integer) = os ++ "-" ++ y
	| (read x :: Integer) +1 == (read y :: Integer) && (bindMode == True)  && (lastNumber +1) /= (read x :: Integer) = os ++ "-" ++ (show lastNumber) ++ " " ++ x ++ " " ++ y
	| (bindMode == False) = os ++ " " ++ x ++ " " ++ y 																													-- If bindmode is false, it does not matter if x and y are two seqeuntial numbers. Etc 174 175 -> 174 175 (not 174-175).
	| (bindMode == True) && (read x :: Integer) == lastNumber +1 = os ++ "-" ++ x ++ " " ++ y
	| otherwise = os ++ "-" ++ (show lastNumber) ++ " " ++ x ++ " " ++ y
busnumbers [x] bindMode os lastNumber																																	-- Single variable, can either bind with previous or not. We just check the last number for a binding and/or bindmode. 
	| (bindMode == True) && ((read x :: Integer) == lastNumber + 1) = os ++ "-" ++ x
	| (bindMode == True) && ((read x :: Integer) /= lastNumber + 1) = os ++ "-" ++ (show lastNumber) ++ " " ++ x 
	| otherwise = os ++ " " ++ x	
busnumbers [] True  os lastNumber = os ++ "-" ++ (show lastNumber)																										-- If for instance there are 3 variables left and they bind -> Reducing to zero variables, we have to bind last num. 
busnumbers [] False os _ = os 																																			-- If emptied string, and everything is handled, just feed back the result.  	

-- 
appendHelper :: Integer -> String -> String -> String -> Bool -> String
appendHelper prevLast x y z False
	| ((read x :: Integer) +1 == (read y :: Integer)) && prevLast +1 == (read x :: Integer) = "" -- "-"
	| otherwise = " " ++ y

appendHelper prevLast x y z True
	| (prevLast +1 == (read x :: Integer)) && (read x :: Integer) + 1 == (read y :: Integer) = "-" ++ y -- We know that z does not bind with y.
	| (read x :: Integer) +1 == (read y :: Integer) = "-" ++ y 
	| otherwise = "-" ++ x ++ " " ++ y

-- findSeqIndex - Helper function to busnumbers
-- Takes in the last number that formed a previous sequence, and recursively looks for the index of the last integer in the list that satisfies the sequence.
-- In a sentence this will allow busnumbers to know how many superflous busnumbers there are and to be able to drop them.
-- etc (findSeqIndex [2, 3, 4, 5, 8, 10] 1 0) has the starting value one and will match 1 through 5 into a sequence, but stop at 8. The function will then return
-- the number of items to drop in order to get to 5 in this case, the last sequence number.

findSeqIndex :: [String] -> Integer -> Integer -> Integer
findSeqIndex xs 5 5 = 0

trimOne :: String -> String
trimOne (x:xs) = xs
trimOne x = []

-- endFormat returnString
-- This is a function that makes sure that there is no " " or "-" left open when writing the cases in the busnumbers function.
-- The function simply reverses the list, removes what is not supposed to be there using recursion, and returns the original list
-- using double reversion, first on the input and later on the handled result. 

endFormat :: String -> String
endFormat (x:xs)
  | x == ' ' || x == '-' = endFormat xs
  | otherwise = reverse (x:xs)

-- TODO: endFormat2
-- En Funktion som kollar och formaterar genom att kolla så att "  ", "- ", " -", "--" inte förekommer.
-- Den filtrerar alla dubbla förekomster av " " och "-"

endFormat2 :: String -> Char -> String -> String
endFormat2 (x:xs) c res
  | x == ' '  && c == ' ' = endFormat2 xs x res
  | x == '-'  && c == '-' = endFormat2 xs x res
  | x == ' '  && c == '-' = endFormat2 xs x res
  | x == '-' && c == ' ' = endFormat2 xs x res
  | otherwise = endFormat2 xs x (x:res)
endFormat2 _ _ res = reverse res

conCat' :: [String] -> String -> String -- Testfunction for sorting IO
conCat' (x:xs) os = conCat' xs (os ++ x)
conCat' [x] os = (os ++ x)
conCat' [] os = os

makeInteger :: [String] -> [Integer] -> [Integer] 
makeInteger (x:xs) os = makeInteger xs (os ++ [(read x :: Integer)])
makeInteger [x] os = os ++ [(read x :: Integer)]
makeInteger [] os = os

makeStrings :: [Integer] -> [String] -> [String]
makeStrings (x:xs) os = makeStrings xs (os ++ [(show x)])
makeStrings [x] os = os ++ [(show x)]
makeStrings [] os = os

--conCatOneLine :: [String] -> String


main = do
	numberOfEntries <- getChar													-- Takes a char and encapsulates it inside of the IO. 
	getLine																		-- Remove first line.
	start <- getLine  															-- Takes in a string as IO and encapsulates it using the IO monad.
	let sortedStrings = makeStrings (sort (makeInteger (words start) [])) []
	-- let busNumberStrings = sort (words start)									-- Splits the busnumbers into string entries in a list, seperated by " ".
	putStrLn ( endFormat2 (endFormat (reverse (trimOne (busnumbers sortedStrings False "" 1001)))) 'a' "")		-- * Calls the busnumbers function which does all the calculations and is
																					-- * then using the print function to print out the result in a list. The 
																					-- * False flag i used since it will enter the function in "non-binding" mode
																					-- * and 0 represents an unvalid previous bus number.	


