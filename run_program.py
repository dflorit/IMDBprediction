from util import Util

class Main:

	def __init__(self):
		self.u = Util()
		self.dataFile = self.u.read_file('Data/movie_metadata.csv')
		self.u.displayAllTrends()
		print "ello"
		


'''


imdb_scoreCol = getColumn(imdb_score)
facenumber_in_posterCol = getColumn(facenumber_in_poster)
budgetCol = getColumn(budget)
print budgetCol[0]
budgetCol1 = []
scoreBudget = []
for i in range(len(budgetCol)):
	print i
	if budgetCol[i] == "":
		print "hellooooo"
	else:
		print "Boooooooo"
		budgetCol1.append(int(budgetCol[i]))
		scoreBudget.append(float(imdb_scoreCol[i]))
	
print budgetCol1

#plot2D(facenumber_in_posterCol, imdb_scoreCol, "Number of faces in poster", "IMDB score")
plot2D(budgetCol1, scoreBudget, "Budget", "IMDB score")

'''

m = Main()
