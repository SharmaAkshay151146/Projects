from requests import get
from bs4 import BeautifulSoup
import pandas as pd 
from time import *
from time import sleep
from random import randint
from warnings import *
from IPython.core.display import clear_output
import matplotlib.pyplot as plt

url ='https://www.imdb.com/search/title/?release_date=2019&sort=num_votes,desc&page=1'
response = get(url)
#print(response.text[:500])
html_soup = BeautifulSoup(response.text, 'html.parser')
movie_containers = html_soup.find_all('div', class_='lister-item mode-advanced')

# List to store the scraped data in 
names = []
years = []
imdb_ratings = []
metascores = []
votes = []
pages = [str(i) for i in range(1,3)]
from_year = int(input("Enter the starting year: "))
to_year = int(input("Enter the ending year: "))
years_url = [str(i) for i in range(from_year, to_year+1)]
start_time = time()
requests = 0

for year_url in years_url:
	# For every page in the interval 1-2
	for page in pages:
		# Make a get request
		response = get('http://www.imdb.com/search/title?release_date=' + year_url + '&sort=num_votes,desc&page=' + page)

		# Pause the loop
		sleep(randint(8,15))

		# Monitoring
		requests += 1
		elapsed_time = time() - start_time
		print('Request:{}; Frequency:{} requests/s'.format(requests, requests/elapsed_time))
		clear_output(wait=True)

		# Throw a warning for non-200 status codes
		if response.status_code != 200:
			warn('Request: {}; Status code: {}'.format(requests, response.status_code))


		# Break the loop if no(requests) > expected
		if requests > 72:
			warn('Number of requests was greater than expected')
			break 

		page_html = BeautifulSoup(response.text, 'html.parser')

		mv_containers = page_html.find_all('div', class_='lister-item mode-advanced')

		for container in mv_containers:
			if container.find('div', class_='ratings-metascore') is not None:
				name = container.h3.a.text
				names.append(name)
				year = container.h3.find('span', class_='lister-item-year').text
				years.append(year)
				imdb = float(container.strong.text)
				imdb_ratings.append(imdb)

				m_score = container.find('span',class_='metascore').text
				metascores.append(int(m_score))

				vote = container.find('span', attrs={'name':'nv'})['data-value']
				votes.append(int(vote))

movie_ratings = pd.DataFrame({'movie':names,
	'year':years,
	'imdb':imdb_ratings,
	'metascore':metascores,
	'votes':votes})


movie_ratings = movie_ratings[['movie', 'year', 'imdb', 'metascore', 'votes']]
movie_ratings.head()
movie_ratings.loc[:,'year'] = movie_ratings['year'].str[-5:-1].astype(int)
movie_ratings.describe().loc[['min','max'],['imdb','metascore']]
movie_ratings['imdb_per_100'] = movie_ratings['imdb'] * 10
#movie_ratings.to_csv('movie_ratings.csv')

plt.hist(movie_ratings['imdb'], range(0,10), histtype='bar', rwidth=0.8)
plt.xlabel('IMDB Ratings')
plt.ylabel('No. of Movies')
plt.title('IMDB Rating Trend')
plt.legend()
plt.show()
