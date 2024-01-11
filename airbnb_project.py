import pandas as pd

data = pd.read_csv("airbnb_listings.csv")
city_options = ['Dublin City', 'Dn Laoghaire-Rathdown', 'Fingal', 'South Dublin']

def find_place():
    while True:
        print("Hello, welcome. I'm your agent in Ireland!")
        city = input(f"Where do you want to go?(options: {', '.join(city_options)}) ").title()
        while city not in city_options:
            print("Invalid city. Please choose from the provided options.")
            city = input(f"Where do you want to go? (options: {', '.join(city_options)}) ").title()

        accommodates = int(input("How many people? (from 1 to 16) "))
        beds = int(input("How many beds? (from 1 to 10) "))
        

        criteria = (data['neighbourhood_cleansed'] == city) & (data['accommodates'] >= accommodates) & (data['beds'] >= beds)
        results = data[criteria]

        if results.empty:
            print(f'No suitable places found in {city} based on the specified criteria.')
        else:
            print(f'\nSuitable places in {city} for {accommodates} people, and {beds} beds:\n')
            print(results[['name', 'accommodates', 'beds', 'price']])

        repeat_search = input("Do you want to repeat the search? (yes/no) ").lower()
        if repeat_search != 'yes':
            print("Thank you for using our service. Happy to help you. See you soon.")
            break  
if __name__ == "__main__":
    find_place()
