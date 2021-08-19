-- A Haskell implementation of the problem peragrams - https://open.kattis.com/problems/peragrams
-- A peragram is a word that can have it's letters permuted so the word becomes a palindrom, that is the reversing of the word
-- becomes the actual word. Our task is to determine how many letters need be removed in order for the word to become a peragram.
-- The idea is very simple for this, all we have to do is test every letter in the alphabet with the word. Because if we think 
-- about it we can always split up every even occurance of a letter onto each side, etc "BAABB" -> "ABBBA", which is a palindrome
-- because "A" has an even occurance, so 0 letters has to be removed.
-- We also see from the example that there can be ONE odd occurant in the alphabet, because we can just place the odd occurant
-- in the middle.
-- What we need to do is: 
-- 1. Count each oddOccurance. 
-- 2a) If there are odd occurances, feed back (the amount of odd occurances) -1, to factor in that one odd occurance can be placed in the middle. 
-- 2b) If no odd occurances, just give back 0. 


-- peragrams word alphaList numOfPeragrams
-- peragrams will be called with the arguments: <The Word> ['a'..'z'] 0
-- This means that the function will be called with the word to work on, an alphabetical list, and a starting number of 0 in
-- regards to matching paragrams. The function will recursively go through the second argument, the alphabetical list, and it will
-- use the helper function oddOccurance to determine if the candidate letter has an odd or an even occurance in the word.
-- If there is an odd occurance numOfPeragrans is incremented one step and we try next candidate letter.
-- If there is an even occurance we just try next candidate.
-- Once we have traversed the entire list of letters in the English Alphabet we just give back the number of odd occurances.

peragrams :: String -> [Char] -> Int -> String
peragrams word (x:xs) numOfPeragrams
  | oddOccurance x word = peragrams word xs (numOfPeragrams + 1)
  | otherwise = peragrams word xs numOfPeragrams
peragrams word [x] numOfPeragrams
  | oddOccurance x word  = show (numOfPeragrams) 	-- In a paragram the uneven character can be placed in the middle of the word
  | numOfPeragrams /= 0  = show (numOfPeragrams -1) -- 
  | otherwise = show (numOfPeragrams)
peragrams word [] numOfPeragrams 
  | numOfPeragrams > 0 = show (numOfPeragrams -1)
  | otherwise = show (numOfPeragrams)

-- oddOccurance c String
-- This is a helper function to peragrams that uses the occurances function to check how many occurances of a letter there is inside the
-- word we need to check. If this number of occurances is odd we return True, else we return False.
-- Etc oddOccurance A "AAB" = False.
-- Etc oddOccurance A "AAAB" = True.

oddOccurance :: Char -> String -> Bool
oddOccurance c str
  | (occurances c str 0) `mod` (2) == 1 = True
  | otherwise = False

-- occurances c word occurances
-- A simple helper function to oddOccurances, that matches each letter in the word with the candidate letter and return the amount
-- of matches. Etc: occurances A "AAA" 0 = 3.

occurances :: Char -> String -> Int -> Int
occurances c (x:xs) numOfOccurances
  | c == x = occurances c xs numOfOccurances +1
  | otherwise = occurances c xs numOfOccurances
occurances c [x] numOfOccurances
  | c == x = numOfOccurances +1
  | otherwise = numOfOccurances
occurances _ [] numOfOccurances = numOfOccurances

main = do
	start <- getLine  		
	let alphaList = ['a'..'z']													-- Takes in a string as IO and encapsulates it using the IO monad.
	putStrLn (peragrams start alphaList 0)

  -- peragrams does the computative bit, with the help of the two helper functions occurances and odd occurances.
  -- A string is then returned back which the putStrLn function can print as an answer.