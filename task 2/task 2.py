class Author:
  contributions = {"2021": 0, "2022": 0, "2023": 0}
  total = contributions["2021"] + contributions["2022"] + contributions["2023"]

  def __init__(self, name):
      self.name = name
    
  def tally(self, year):
      contributions[year] += 1

#ISSUES
#what if the same author publishes in different year? how to not create a new object


def main():

  authors = []
  urls[]
  
  for url in urls:
    year = 0
    names = getNames(url, year)
    countNames (names, year, authors)

  topContributors(authors)
  sendExcel(authors)

#creates a BeautifulSoup object, scans for all contributors, places in list
#scrape the year of the website
def getNames(url, year)


#takes list of names, for each unique name creates an author object, adds to author list
# for each instance of that name in the list, increment Author.contributions, del list element
def countNames(names, authors, year)

#iteratres through authors[] to find top three, del all other authors
def topContributors(authors)

#prints the top three authors' number of contributions in an Excel spreadsheet
def sendExcel(authors)






main()

