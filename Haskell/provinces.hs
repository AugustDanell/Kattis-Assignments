province :: [String] -> String
province (x:y:z:xs)
	|  money >= 8 = "Province or Gold"
	|  money >= 6 = "Duchy or Gold"
	|  money == 5 = "Duchy or Silver"
	|  money >= 3 = "Estate or Silver"
	|  money == 2 = "Estate or Copper"
	|  otherwise =  "Copper"
	where money = (read x :: Integer) * 3 + (read y :: Integer) * 2 + (read z :: Integer)


main = do
	input <- getLine
	let inputs = words input
	putStrLn (province inputs)