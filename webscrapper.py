import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.scrapethissite.com/pages/simple"


def scrape_countries():
    response = requests.get(URL)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    countries = soup.find_all("div", class_="country")

    with open("output/countries.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["country", "population"])

        for country in countries:
            name = country.find("h3", class_="country-name")
            population = country.find("span", class_="country-population")

            if name and population:
                writer.writerow([
                    name.text.strip(),
                    population.text.strip()
                ])

    print(f"{len(countries)} countries saved.")


if name == "__main__":
    scrape_countries()