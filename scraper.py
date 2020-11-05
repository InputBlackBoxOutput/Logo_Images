# Program to scrape images from logodix.com
# Written by Rutuparn Pawar (InputBlackBoxOutput)

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import os
import string

# ---------------------------------------------------------------------------------------------------
headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    } 

path = ""

# ---------------------------------------------------------------------------------------------------
# Get all logo images from the webpages
def logo_scraper(logolist):
  for each in logolist:
    print(f"Current logo: {each}")
    url = f"https://logodix.com/{each}"
    response = requests.request("GET", url, headers=headers)
    soup = BeautifulSoup(response.text, features="html.parser")
    images = soup.find_all("img", src=True)

    image_src = [x['src'] for x in images]
    image_src = [x for x in image_src if x.endswith('.jpg') or x.endswith('.png') ]

    try:
      os.mkdir(path + each)
    except:
      pass

    imcount = 1
    for image in tqdm(image_src[1:-27]):
        imageFilename = path + f"{each}/{imcount}.png"

        with open(imageFilename, 'wb') as f:
            res = requests.get("https://logodix.com/" + image)
            f.write(res.content)
        imcount += 1

    print(f"\t\t{imcount-1} images scraped")

# Some logos have url != name
def scrape_special():
    special = [ "dunkin-donuts", "guns-n-roses", "kelloggs", "kirkland-ellis", "latham-watkins", "lays", "lowes", "macys", "mcdonalds", "skadden-arps-slate-meagher-flom", "sothebys-international-realty", "adopt-a-petcom", "wendys"]

    logo_scraper(special)

def print_stats():
    print(f"Number of logos: {len(os.listdir(path))}")

    count = 0
    for each in os.listdir(path):
      if len(os.listdir(path + each)) == 0:
        print(each)

      count += len(os.listdir(path + each))

    print(f"Total number of images: {count}")

# ---------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    for each in string.ascii_lowercase:
        url = f"https://logodix.com/{each}-logos"

        response = requests.request("GET", url, headers=headers)
        print(f"Alphabet: {each} ==> {response}")
        soup = BeautifulSoup(response.text, features="html.parser")

        titles = soup.find_all("img", title=True)
        names = [x['title'] for x in titles]

        for i in range(len(names)):
            names[i] = names[i][:-5].replace(' ', '-').lower()

        logo_scraper(names)
        # print(names)

    # print_stats()
    # scrape_special()

    print("Done.")

# ---------------------------------------------------------------------------------------------------
# EOF