# OBJECTIVE:
# I wanted to web scrape minimalistbaker.com's recipe site after selecting the
# filters for "gluten free" and "7 ingredients or less"
#
# There were 24 pages of results with 20 recipes on each page. I carried out the 
# web scrape on pages 2-24, and only wanted it to print out the title and url if 
# "Chocolate" was in the title =)
#
# My list of results that printed out in the Terminal can be found at the bottom 
# of this code


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


# RESULTS:

# Recipes containing "Chocolate" in the title (if any) from https://minimalistbaker.com/recipe-index/?fwp_special-diet=gluten-free&fwp_simple-factor=7-ingredients-or-less&fwp_paged=2:
#
# Creamy Chocolate Hazelnut Milk
# https://minimalistbaker.com/creamy-chocolate-hazelnut-milk/
# -
# Number of total recipes found on page: 20
# ============

# Recipes containing "Chocolate" in the title (if any) from https://minimalistbaker.com/recipe-index/?fwp_special-diet=gluten-free&fwp_simple-factor=7-ingredients-or-less&fwp_paged=3:

# Number of total recipes found on page: 20
# ============

# Recipes containing "Chocolate" in the title (if any) from https://minimalistbaker.com/recipe-index/?fwp_special-diet=gluten-free&fwp_simple-factor=7-ingredients-or-less&fwp_paged=4:

# Number of total recipes found on page: 20
# ============

# Recipes containing "Chocolate" in the title (if any) from https://minimalistbaker.com/recipe-index/?fwp_special-diet=gluten-free&fwp_simple-factor=7-ingredients-or-less&fwp_paged=5:

# Coffee Chocolate Nice Cream
# https://minimalistbaker.com/coffee-chocolate-nice-cream/
# -
# Number of total recipes found on page: 20
# ============

# Recipes containing "Chocolate" in the title (if any) from https://minimalistbaker.com/recipe-index/?fwp_special-diet=gluten-free&fwp_simple-factor=7-ingredients-or-less&fwp_paged=6:

# Vegan Chocolate Frosting (Oil-Free)
# https://minimalistbaker.com/vegan-chocolate-frosting-oil-free/
# -
# Easy No-Bake Chocolate Chip Cookies
# https://minimalistbaker.com/easy-no-bake-chocolate-chip-cookies/
# -
# 3-Ingredient Chocolate Fudge (Dairy-Free)
# https://minimalistbaker.com/3-ingredient-chocolate-fudge-dairy-free/
# -
# Number of total recipes found on page: 20
# ============

# Recipes containing "Chocolate" in the title (if any) from https://minimalistbaker.com/recipe-index/?fwp_special-diet=gluten-free&fwp_simple-factor=7-ingredients-or-less&fwp_paged=7:

# 5-Ingredient Honey Mama’s Chocolate Bars
# https://minimalistbaker.com/5-ingredient-honey-mamas-chocolate-bars/
# -
# Creamy Vegan Milk Chocolate (Low Sugar)
# https://minimalistbaker.com/creamy-vegan-milk-chocolate-low-sugar/
# -
# Adaptogenic Hot Chocolate (5 Minutes, Low Sugar)
# https://minimalistbaker.com/adapatogenic-hot-chocolate-low-sugar/
# -
# Number of total recipes found on page: 20
# ============

# Recipes containing "Chocolate" in the title (if any) from https://minimalistbaker.com/recipe-index/?fwp_special-diet=gluten-free&fwp_simple-factor=7-ingredients-or-less&fwp_paged=8:

# 5-Ingredient Almond Butter Dark Chocolate Snowballs
# https://minimalistbaker.com/5-ingredient-almond-butter-dark-chocolate-snowballs/
# -
# 5-Ingredient Vegan Chocolate Turtles
# https://minimalistbaker.com/5-ingredient-vegan-chocolate-turtles/
# -
# 10-Minute Chocolate Truffles (Date-Sweetened)
# https://minimalistbaker.com/10-minute-chocolate-truffles-date-sweetened/
# -
# Number of total recipes found on page: 20
# ============

# Recipes containing "Chocolate" in the title (if any) from https://minimalistbaker.com/recipe-index/?fwp_special-diet=gluten-free&fwp_simple-factor=7-ingredients-or-less&fwp_paged=9:

# Easy 5-Ingredient Protein Bars (Peanut Butter Chocolate!)
# https://minimalistbaker.com/easy-5-ingredient-protein-bars-peanut-butter-chocolate/
# -
# Date-Sweetened Chocolate Frosting (Plant-Based, 5 Ingredients)
# https://minimalistbaker.com/date-sweetened-chocolate-frosting/
# -
# Number of total recipes found on page: 20
# ============

# Recipes containing "Chocolate" in the title (if any) from https://minimalistbaker.com/recipe-index/?fwp_special-diet=gluten-free&fwp_simple-factor=7-ingredients-or-less&fwp_paged=10:

# No-Bake Fudgy Chocolate Cake Bites
# https://minimalistbaker.com/no-bake-fudgy-chocolate-cake-bites/
# -
# Chocolate Peanut Butter Freezer Fudge (4 Ingredients!)
# https://minimalistbaker.com/chocolate-peanut-butter-freezer-fudge-4-ingredients/
# -
# Number of total recipes found on page: 20
# ============

# Recipes containing "Chocolate" in the title (if any) from https://minimalistbaker.com/recipe-index/?fwp_special-diet=gluten-free&fwp_simple-factor=7-ingredients-or-less&fwp_paged=11:

# Naturally Sweetened Vegan Chocolate Mousse
# https://minimalistbaker.com/naturally-sweetened-vegan-chocolate-mousse/
# -
# Feel Good Hot Chocolate
# https://minimalistbaker.com/feel-good-hot-chocolate/
# -
# Number of total recipes found on page: 20
# ============

# Recipes containing "Chocolate" in the title (if any) from https://minimalistbaker.com/recipe-index/?fwp_special-diet=gluten-free&fwp_simple-factor=7-ingredients-or-less&fwp_paged=12:

# 5-Ingredient Vegan Dark Chocolate Bars
# https://minimalistbaker.com/5-ingredient-vegan-dark-chocolate-bars/
# -
# 5-Ingredient Chocolate Coconut Butter Cups
# https://minimalistbaker.com/5-ingredient-chocolate-coconut-butter-cups/
# -
# Number of total recipes found on page: 20
# ============

# Recipes containing "Chocolate" in the title (if any) from https://minimalistbaker.com/recipe-index/?fwp_special-diet=gluten-free&fwp_simple-factor=7-ingredients-or-less&fwp_paged=13:

# White Chocolate Peanut Butter Eggs
# https://minimalistbaker.com/white-chocolate-peanut-butter-eggs/
# -
# Tahini Chocolate Banana Soft Serve
# https://minimalistbaker.com/tahini-chocolate-banana-soft-serve/
# -
# Dark Chocolate Hemp Energy Bites
# https://minimalistbaker.com/dark-chocolate-hemp-energy-bites/
# -
# 5-Ingredient White Chocolate Truffles
# https://minimalistbaker.com/5-ingredient-white-chocolate-truffles/
# -
# Number of total recipes found on page: 20
# ============

# Recipes containing "Chocolate" in the title (if any) from https://minimalistbaker.com/recipe-index/?fwp_special-diet=gluten-free&fwp_simple-factor=7-ingredients-or-less&fwp_paged=14:

# 3-Ingredient Vegan Chocolate Malt
# https://minimalistbaker.com/3-ingredient-vegan-chocolate-malt/
# -
# 7-Minute Vegan Chocolate Syrup
# https://minimalistbaker.com/7-minute-vegan-chocolate-syrup/
# -
# Number of total recipes found on page: 20
# ============

# Recipes containing "Chocolate" in the title (if any) from https://minimalistbaker.com/recipe-index/?fwp_special-diet=gluten-free&fwp_simple-factor=7-ingredients-or-less&fwp_paged=15:

# Easy Vegan Chocolate
# https://minimalistbaker.com/easy-vegan-chocolate/
# -
# Raw Double Chocolate Macaroons
# https://minimalistbaker.com/raw-double-chocolate-macaroons/
# -
# Dark Chocolate Quinoa Breakfast Bowl
# https://minimalistbaker.com/dark-chocolate-quinoa-breakfast-bowl/
# -
# 2-Ingredient Dark Chocolate Truffles
# https://minimalistbaker.com/2-ingredient-dark-chocolate-truffles/
# -
# Number of total recipes found on page: 20
# ============

# Recipes containing "Chocolate" in the title (if any) from https://minimalistbaker.com/recipe-index/?fwp_special-diet=gluten-free&fwp_simple-factor=7-ingredients-or-less&fwp_paged=16:

# Pretzel Peanut Butter Chocolate Pie
# https://minimalistbaker.com/pretzel-peanut-butter-chocolate-pie/
# -
# DIY Dark Chocolate Almond Bars
# https://minimalistbaker.com/diy-dark-chocolate-almond-bars/
# -
# 5-Ingredient Dark Chocolate Macaroons
# https://minimalistbaker.com/5-ingredient-dark-chocolate-macaroons/
# -
# Overnight Chocolate Chia Seed Pudding
# https://minimalistbaker.com/overnight-chocolate-chia-seed-pudding/
# -
# Number of total recipes found on page: 20
# ============

# Recipes containing "Chocolate" in the title (if any) from https://minimalistbaker.com/recipe-index/?fwp_special-diet=gluten-free&fwp_simple-factor=7-ingredients-or-less&fwp_paged=17:

# Vegan Mayan Drinking Chocolate
# https://minimalistbaker.com/vegan-mayan-drinking-chocolate/
# -
# No-Bake Vegan Brownies with Chocolate Ganache
# https://minimalistbaker.com/no-bake-vegan-brownies-with-chocolate-ganache/
# -
# 3-Ingredient Dark Chocolate Peppermint Mousse
# https://minimalistbaker.com/3-ingredient-dark-chocolate-peppermint-mousse/
# -
# Number of total recipes found on page: 20
# ============

# Recipes containing "Chocolate" in the title (if any) from https://minimalistbaker.com/recipe-index/?fwp_special-diet=gluten-free&fwp_simple-factor=7-ingredients-or-less&fwp_paged=18:

# Chocolate Peanut Butter Avocado Pudding
# https://minimalistbaker.com/chocolate-peanut-butter-avocado-pudding/
# -
# Chocolate Chia Recovery Drink
# https://minimalistbaker.com/chocolate-chia-recovery-drink/
# -
# No-Churn Vegan Chocolate Ice Cream
# https://minimalistbaker.com/no-churn-vegan-chocolate-ice-cream/
# -
# Chocolate Cherry Almond Milk
# https://minimalistbaker.com/chocolate-cherry-almond-milk/
# -
# Peanut Butter Chocolate Chip Granola
# https://minimalistbaker.com/peanut-butter-chocolate-chip-granola/
# -
# Chocolate Chocolate Chip Blizzards
# https://minimalistbaker.com/chocolate-chocolate-chip-blizzards/
# -
# Number of total recipes found on page: 20
# ============

# Recipes containing "Chocolate" in the title (if any) from https://minimalistbaker.com/recipe-index/?fwp_special-diet=gluten-free&fwp_simple-factor=7-ingredients-or-less&fwp_paged=19:

# 6-Ingredient Vegan Chocolate Silk Pie
# https://minimalistbaker.com/6-ingredient-vegan-chocolate-silk-pie/
# -
# Double Peanut Butter Chocolate Chip Cookies
# https://minimalistbaker.com/double-peanut-butter-chocolate-chip-cookies/
# -
# Chocolate-Covered Pretzel Peanut Butter
# https://minimalistbaker.com/chocolate-covered-pretzel-peanut-butter/
# -
# Number of total recipes found on page: 20
# ============

# Recipes containing "Chocolate" in the title (if any) from https://minimalistbaker.com/recipe-index/?fwp_special-diet=gluten-free&fwp_simple-factor=7-ingredients-or-less&fwp_paged=20:

# Super Thick DIY Chocolate Almond Milk
# https://minimalistbaker.com/super-thick-diy-chocolate-almond-milk/
# -
# Soft & Chewy Gluten-Free Chocolate Chip Cookies
# https://minimalistbaker.com/soft-chewy-gluten-free-chocolate-chip-cookies/
# -
# Vegan Peppermint Drinking Chocolate
# https://minimalistbaker.com/vegan-peppermint-drinking-chocolate/
# -
# Number of total recipes found on page: 20
# ============

# Recipes containing "Chocolate" in the title (if any) from https://minimalistbaker.com/recipe-index/?fwp_special-diet=gluten-free&fwp_simple-factor=7-ingredients-or-less&fwp_paged=21:

# Chocolate Chip Almond Butter Granola Bars
# https://minimalistbaker.com/chocolate-chip-almond-butter-granola-bars/
# -
# Chocolate Hazelnut No-Bake Cookies
# https://minimalistbaker.com/chocolate-hazelnut-no-bake-cookies/
# -
# Triple Chocolate Avocado Shake
# https://minimalistbaker.com/triple-chocolate-avocado-shake/
# -
# Dairy-Free Chocolate Ice Cream
# https://minimalistbaker.com/dairy-free-chocolate-ice-cream/
# -
# Gluten-Free Green Tea Crepes & White Chocolate-Coconut Filling
# https://minimalistbaker.com/gluten-free-green-tea-crepes-white-chocolate-coconut-filling/
# -
# Pretzel Frozen Hot Chocolate
# https://minimalistbaker.com/pretzel-frozen-hot-chocolate/
# -
# Number of total recipes found on page: 20
# ============

# Recipes containing "Chocolate" in the title (if any) from https://minimalistbaker.com/recipe-index/?fwp_special-diet=gluten-free&fwp_simple-factor=7-ingredients-or-less&fwp_paged=22:

# Vegan Brownie Chocolate Ice Cream
# https://minimalistbaker.com/vegan-brownie-chocolate-ice-cream/
# -
# Number of total recipes found on page: 20
# ============

# Recipes containing "Chocolate" in the title (if any) from https://minimalistbaker.com/recipe-index/?fwp_special-diet=gluten-free&fwp_simple-factor=7-ingredients-or-less&fwp_paged=23:

# Dark Chocolate Sweet Potato Chips
# https://minimalistbaker.com/dark-chocolate-sweet-potato-chips/
# -
# Ginger Hot Chocolate
# https://minimalistbaker.com/ginger-hot-chocolate/
# -
# Creamy Chocolate Breakfast Shake
# https://minimalistbaker.com/creamy-chocolate-breakfast-shake/
# -
# Boozy Pumpkin White Hot Chocolate (2 Ways)
# https://minimalistbaker.com/boozy-pumpkin-white-hot-chocolate/
# -
# Number of total recipes found on page: 20
# ============

# Recipes containing "Chocolate" in the title (if any) from https://minimalistbaker.com/recipe-index/?fwp_special-diet=gluten-free&fwp_simple-factor=7-ingredients-or-less&fwp_paged=24:

# Chocolate Cashew Cookie Larabar Pops
# https://minimalistbaker.com/chocolate-cashew-cookie-larabar-pops/
# -
# Number of total recipes found on page: 6
# ============