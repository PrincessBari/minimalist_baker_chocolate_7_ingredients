# OBJECTIVE:
# I wanted to web scrape minimalistbaker.com's recipe site after selecting the
# filters for "gluten free" and "7 ingredients or less"
#
# There were 24 pages of results with 20 recipes on each page. I carried out the 
# web scrape on pages 2-24, and only wanted it to print out the title and url if 
# "Chocolate" was in the title =)


import requests
from bs4 import BeautifulSoup

# There are 24 pages in total

page_counter = 2

while page_counter <= 24:

	url = f"https://minimalistbaker.com/recipe-index/?fwp_special-diet=gluten-free&fwp_simple-factor=7-ingredients-or-less&fwp_paged={page_counter}"
	# page 2: https://minimalistbaker.com/recipe-index/?fwp_special-diet=gluten-free&fwp_simple-factor=7-ingredients-or-less&fwp_paged=2
	# page 1: https://minimalistbaker.com/recipe-index/?fwp_special-diet=gluten-free&fwp_simple-factor=7-ingredients-or-less

	print('Recipes containing "Chocolate" in the title (if any) from ' + url + ":\n")

	r = requests.get(url)

	soup = BeautifulSoup(r.text, features="html.parser")

	object_title = soup.find_all("h3", {'class':'post-summary__title'})
	link_title = soup.find_all("a") 
	
	for an_object in object_title:

		all_info = an_object.find('a')
		 
		if "Chocolate" in all_info.text:

			print(all_info.text) 
			print(all_info.get('href'))
			print('-')	
			

	print("Number of total recipes found on page:", (len(object_title)))
	print("============" + "\n")


	page_counter = page_counter + 1
