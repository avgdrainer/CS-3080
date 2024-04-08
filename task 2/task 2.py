import requests, bs4, openpyxl

class Author:
  contributions = {"2021": 0, "2022": 0, "2023": 0}
  total = sum(contributions.values())

  def __init__(self, name):
      self.name = name
    
  def tally(self, year):
      contributions[year] += 1



def main():

  authors = {} #"name": object maybe
  urls[]
  
  for url in urls:
    year = 0
    names = getNames(url, year)
    countNames (names, year, authors)

  topContributors(authors)
  sendExcel(authors)

#creates a BeautifulSoup object, scans for all contributors, places in list
#scrape the year of the website
def getNames(url, year):

#takes list of names, for each unique name creates an author object, adds to author list
# for each instance of that name in the list, increment Author.contributions, del list element
def countNames(names, authors, year):

  for name in names:
    if name in authors:
      authors[name].tally(year)
    else:
      authors[name] = Author(name)
      authors[name].tally(year)

#iteratres through authors[] to find top three, del all other authors
def topContributors(authors):

  
  if len(authors) < 3:
    print("not enough contributors for a top three. exiting program...")
    exit()
  elif len(authors) == 3:
    return authors:
  else:
    for author in authors:
      #use sort on list(authors.values()), something like sort(list(authors.values()), key = element.total)
      
    

#prints the top three authors' number of contributions in an Excel spreadsheet
def sendExcel(authors):






main()

