import ctypes
import os
import random
import requests

from bs4 import BeautifulSoup

possible_searches = ["hot anime girl",
                     "cursed images",
                     "weird desktop background",
                     "buffed dudes",
                     "cringe images",
                     "furries",
                     "fat dude",
                     "ugly dog",
                     "unfashionable clothes",
                     "cringy memes",
                     "hot af anime girl",
                     "Fortnite dances in public",
                     "Weird fan fiction",
                     "Bad 3D animation",
                     "Distorted memes",
                     "Awkward family photos",
                     "Overly edgy usernames",
                     "Terrible puns",
                     "Unintentionally bad art",
                     "Embarrassing childhood photos",
                     "Low-budget cosplay",
                     "Dramatic social media posts",
                     "Cringe-inducing TikToks",
                     "Weird food combinations",
                     "Unintentionally funny product names",
                     "Over-the-top reaction videos",
                     "Misused memes",
                     "Excessive emoji usage",
                     "Painful pickup lines",
                     "Corny jokes",
                     "Unintentionally funny YouTube videos",
                     "Over-the-top reaction videos",
                     "Misused memes",
                     "Excessive emoji usage",
                     "Painful pickup lines",
                     "Corny jokes",
                     "Unintentionally funny YouTube videos",
                     "Bizarre conspiracy theories",
                     "Fails in cooking shows",
                     "Unintentionally funny commercials",
                     "Cheesy romantic movies",
                     "Failed magic tricks",
                     "Unintentionally funny product reviews",
                     "Exaggerated Instagram poses",
                     "Failed attempts at being trendy",
                     "Ridiculous Instagram filters",
                     "Funny autocorrect fails",
                     "Inappropriate memes in serious contexts",
                     "Weird pet costumes",
                     "Unintentionally funny news headlines",
                     "Social media challenges gone wrong",
                     "Faux pas in professional emails",
                     "Hilariously bad video game dialogue",
                     "Misinterpreted song lyrics",
                     "Ridiculous product packaging",
                     "Unintentionally funny user-generated content",
                     "Failed DIY projects",
                     "Weird fashion trends",
                     "Cheesy pickup lines",
                     "Social media influencers gone wrong",
                     "Hilarious internet browser search history",
                     "Funny mistranslations",
                     "Over-the-top wedding photoshoots",
                     "Awkward online dating profiles",
                     "Exaggerated gym selfies"]

word = random.choice(possible_searches)

unfinished = True

while unfinished:
    try:
        url = 'https://www.google.com/search?q={0}&tbm=isch'.format(word)
        content = requests.get(url).content
        soup = BeautifulSoup(content,'lxml')
        images = soup.findAll('img')


        url = images[1].get('src')
        print(url)

        # Define the local path where you want to save the image
        local_image_path = "local_image.jpg"

        # Download the image from the URL
        response = requests.get(url)
        with open(local_image_path, 'wb') as f:
            f.write(response.content)

        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.abspath(local_image_path), 3)
        unfinished = False
    except:
        unfinished = True