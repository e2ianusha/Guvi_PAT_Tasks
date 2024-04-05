import requests

def get_breweries_by_state(state):
    url = f"https://api.openbrewerydb.org/breweries?by_state={state}"
    response = requests.get(url)
    breweries = response.json()
    return breweries

def main():
    states = ["Maine", "Alaska", "New York"]

    for state in states:
        print(f"\nBreweries in {state}:\n")
        breweries = get_breweries_by_state(state)
        for brewery in breweries:
            print(brewery["name"])

        print(f"\nTotal number of breweries in {state}: {len(breweries)}\n")

        cities = set(brewery["city"] for brewery in breweries)
        print(f"Number of cities with breweries in {state}: {len(cities)}")
        for city in cities:
            print(f"{city}: {sum(brewery['city'] == city for brewery in breweries)} breweries")

        websites = sum("website_url" in brewery for brewery in breweries)
        print(f"\nNumber of breweries with websites in {state}: {websites}\n")

if __name__ == "__main__":
    main()
