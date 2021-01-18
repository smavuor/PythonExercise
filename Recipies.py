


from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uRq

myURL="https://www.k-ruoka.fi/reseptit"

#Open the connection for grabbing the page

uClient = uRq(myURL)
page_html = uClient.read()
uClient.close


# Html parsing
page_soup = soup(page_html, "html.parser")

#Takes the product
recipes = []
recipes = page_soup.findAll("li", {"class" : "recipe-card"})
names = []
url = []
ingredients = []

#take recipe names
for recipe in recipes:
    names.append(recipe.h3.text)
    url.append("https://www.k-ruoka.fi" + recipe.a["href"])

def searchIngredients(i):
    item_ingredients=[]
    uClient = uRq(url[i])
    page2_html = uClient.read()
    uClient.close
    page_ingredients = soup(page2_html, "html.parser")


    ingredients = page_ingredients.findAll("span", {"class" : "recipe-ingredient-name"})

    for ingredient in ingredients:
        item_ingredients.append(ingredient.text)

    return item_ingredients

