-- dartCalculator score
-- This is a function that takes an Int as input, in the form of a score. For the assignment we need to
-- output a result in the form of a combination of a*x, b*y, c*z, where a, b and c can range from [1, 3] and x, y, z can range from [1, 20].
-- We can see a, b and c as weights for each x, y, z.
-- We recognize that there is a rather limited set amount of cases as to how we can set up the weights, so the solution here is to set up lists using list
-- comprehension, one for each combination of weighs. Since the order does not matter, that is the problem
-- only wants us to present one solution if there is one, we have only 9 lists to take into account. We step into each list and try to match it with the given
-- score.
-- If there is a match we output the x, y, z in a list and concat it with a list with a, b, c. That is to be certain for our next problem which one is a single
-- which one is a double and which one is a tripple.
-- If there is no match, the function will instead just return a list with a single list element that holds the value of 181, which denotes impossibility.
-- Futhermore the next function will know if just a single element is in the list (That is a, b, c are discarded) that we found no solution. It should then
-- just print out "impossible" 

dartCalculator :: Int -> [[Int]]
dartCalculator 1 = [[1], [1]]        -- Todo: Fixa så att denna del fungerar
dartCalculator 2 = [[1,1], [1,1]]
dartCalculator score
  | length (singleList)   >= 1 =   [(head singleList)]   ++ [[1, 1, 1]]
  | length (oneDList)     >= 1 =   [(head oneDList)]     ++ [[2, 1, 1]]
  | length (twoDList)     >= 1 =   [(head twoDList)]     ++ [[2, 2, 1]]
  | length (threeDList)   >= 1 =   [(head threeDList)]   ++ [[2, 2, 2]]
  | length (oneTList) 	  >= 1 =   [(head oneTList)]     ++ [[3, 1, 1]]
  | length (twoTList) 	  >= 1 =   [(head twoTList)]     ++ [[3, 3, 1]]
  | length (threeTlist)	  >= 1 =   [(head threeTlist)]	 ++ [[3, 3, 3]]
  | length (oneDTwoTlist) >= 1 =   [(head oneDTwoTlist)] ++ [[2, 3, 3]]
  | length (twoDoneTlist) >= 1 =   [(head twoDoneTlist)] ++ [[2, 2, 3]]
  | otherwise = [[181]] -- Impossible case
  where singleList   = [[x, y, z] | x <- [1..20], y <- [1..20], z <- [1..20], x + y + z == score]
  	oneDList     	   = [[x, y, z] | x <- [1..20], y <- [1..20], z <- [1..20], x*2 + y + z == score]
  	twoDList     	   = [[x, y, z] | x <- [1..20], y <- [1..20], z <- [1..20], x*2 + y*2 + z == score]
  	threeDList   	   = [[x, y, z] | x <- [1..20], y <- [1..20], z <- [1..20], x*2 + y*2 + z*2 == score]
  	oneTList     	   = [[x, y, z] | x <- [1..20], y <- [1..20], z <- [1..20], x*3 + y + z == score]
  	twoTList     	   = [[x, y, z] | x <- [1..20], y <- [1..20], z <- [1..20], x*3 + y*3 + z == score]
  	threeTlist   	   = [[x, y, z] | x <- [1..20], y <- [1..20], z <- [1..20], x*3 + y*3 + z*3 == score]
  	oneDTwoTlist 	   = [[x, y, z] | x <- [1..20], y <- [1..20], z <- [1..20], x*2 + y*3 + z*3 == score]
  	twoDoneTlist 	   = [[x, y, z] | x <- [1..20], y <- [1..20], z <- [1..20], x*2 + y*2 + z*3 == score]

 -- handleZip -- A function that formats the dartCalculator calculation into a list of tupples if there
 -- is indeed a match.

handleZip :: [[Int]] -> [String]
handleZip lists
  | length (lists)  == 1 = ["impossible"] 
  | otherwise = handleString zipped []
  where zipped = zip (head lists) (last lists)

-- handleString -- A helper function that handles the zipping recursively using tail recursion.
handleString :: [(Int, Int)] -> [String] -> [String]
handleString (x:xs) res
  | snd x == 1 = handleString xs (res ++ ["single "  ++ (show (fst x))])
  | snd x == 2 = handleString xs (res ++ ["double "  ++ (show (fst x))])
  | otherwise  = handleString xs (res ++ ["triple " ++ (show (fst x))])
handleString [x] res
  | snd x == 1 = res ++ ["single " ++  (show (fst x))]
  | snd x == 2 = res ++ ["double " ++  (show (fst x))]
  | otherwise  = res ++ ["triple " ++  (show (fst x))]
handleString [] res = res

printHelp :: [String] -> String -> String
printHelp (x:xs) res = printHelp xs (res ++ x ++ "\n")  
printHelp [x] res = (res ++ x) 
printHelp [] res = res

main = do
	input <- getLine -- Input the score
	putStr( printHelp (handleZip (dartCalculator (read input :: Int))) [] )

	-- [x, y, z | x <- [1..20], y <- [1..20], z <- [1..20], x + y + z == score]