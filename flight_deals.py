import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def get_cheapest_flight_price():
    
    # Get the current date
    today = datetime.now()

    # Initialize the variables to store the cheapest flight price and the cheapest flight date
    cheapest_price = None
    cheapest_date = None

    # Loop through the next 6 months
    for _ in range(6):
        
        # Calulate the start and end dates for each month (from 15th to 14th of the next month)
        start_date = today.replace(day=15)
        end_date = start_date.replace(month=start_date.month % 12 + 1, day=14)

        # Format the dates for the URL
        start_date_str = start_date.strftime("%d/%m/%Y")
        end_date_str = end_date.strftime("%d/%m/%Y")
        
        # Construct the URL with the formatted dates
        url = f"https://www.skyscanner.co.nz/transport/flights/chc/nan/{start_date_str}/{end_date_str}/"

        # Send a get request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            
            # Parse the HTML content of the webpage using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all the elements that contain the flight prices
            price_elements = soup.find_all('span', class_='from-price')

              # Extract the text content of the price elements
            prices = [float(price_element.text.strip()[1:]) for price_element in price_elements]

             # Find the minimum price for this month
            min_price_for_month = min(prices)

            # Update the cheapest price and date if it's the first iteration or if the current price is cheaper
            if cheapest_price is None or min_price_for_month < cheapest_price:
                cheapest_price = min_price_for_month
                cheapest_date = start_date.strftime("%b %d, %Y")

                # Move to the next month
        today = end_date + timedelta(days=1)

    return cheapest_price, cheapest_date

if __name__ == "__main__":
    cheapest_price, cheapest_date = get_cheapest_flight_price()

    if cheapest_price:
        print(f"The cheapest flight price from Christchurch to Nadi in the next 6 months is NZD {cheapest_price:.2f}.")
        print(f"Cheapest date: {cheapest_date}")
    else:
        print("Failed to get the cheapest flight price. Please try again later.")
