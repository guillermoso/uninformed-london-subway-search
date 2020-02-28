from UninformedSearch import UninformedSearch

searchAlgorithm = UninformedSearch()

successNode = searchAlgorithm.search(strategy=1, start="1", goal="9")

successNode.backTrack()

