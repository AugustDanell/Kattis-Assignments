licenseToLaunch :: [String] -> Integer -> Integer -> Integer -> Integer
licenseToLaunch (x:xs) bestDay currentDay indexBest
  |  (read x :: Integer) < bestDay = licenseToLaunch xs (read x :: Integer) (currentDay+1) currentDay
  |  otherwise = licenseToLaunch xs bestDay (currentDay+1) indexBest
licenseToLaunch [x] bestDay currentDay indexBest
  |  (read x :: Integer) < bestDay = currentDay
  |  otherwise = indexBest
licenseToLaunch [] bestDay _ indexBest = indexBest

main = do
	input <- getLine
	days <- getLine

	let licensedDays = (read input :: Integer)
	let daySeq = words (days)

	putStrLn (show (licenseToLaunch daySeq licensedDays 0 0))