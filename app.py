import streamlit as st
import pandas as pd


# Set background image for the app
def set_bg_image(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url({image_url});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# Set the background image for alcohol-themed content
background_image = "pexels-pixabay-301692.jpg"
set_bg_image(background_image)

# Expanded and detailed sample data with images, additional fields, and food pairings
data = {
    'Category': ['Wine', 'Wine', 'Wine', 'Wine', 'Beer', 'Beer', 'Beer', 'Beer', 'Whiskey', 'Whiskey', 'Whiskey',
                 'Whiskey', 'Gin', 'Gin', 'Tequila'],
    'Name': ['Chardonnay', 'Merlot', 'Cabernet Sauvignon', 'Pinot Noir', 'IPA', 'Lager', 'Pilsner', 'Stout', 'Bourbon',
             'Scotch', 'Rye', 'Irish Whiskey', 'Gin Martini', 'London Dry Gin', 'Patron'],
    'Description': [
        'A popular white wine with notes of citrus, apple, and pear. A refreshing choice for a sunny day.',
        'A red wine known for its bold flavors of blackberries, cherries, and spices. Pairs well with rich meats.',
        'A full-bodied red wine with dark fruit flavors and hints of oak. Best enjoyed with grilled steaks.',
        'A smooth red wine with a balance of acidity and fruitiness. Ideal for casual gatherings or light meals.',
        'A hoppy beer with a bitter taste, often paired with savory food like burgers and fries.',
        'A light, crisp lager beer, perfect for casual drinking on a hot day.',
        'A clean, crisp beer with a smooth finish and balanced bitterness, ideal for pairing with salads.',
        'A dark, rich beer with roasted malt flavors, best enjoyed with hearty meals like stews or barbecues.',
        'A rich, amber whiskey with caramel, vanilla, and oak flavors. Excellent for sipping after dinner.',
        'A smoky scotch whiskey with notes of peat, sea salt, and vanilla. A drink for seasoned whiskey lovers.',
        'A spiced whiskey with a peppery finish and rye grain character. A good choice for cocktails.',
        'A smooth, slightly sweet whiskey with hints of honey and vanilla. Great for sipping on its own.',
        'A refreshing cocktail made with gin, vermouth, and an olive. A timeless classic.',
        'A classic gin known for its juniper-forward flavor and dry finish. Perfect for a gin and tonic.',
        'A premium tequila made from 100% blue agave, offering a smooth taste with a touch of sweetness.'
    ],
    'Top Rank': [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 1],
    'Alcohol Content': ['13-15%', '13-15%', '13-15%', '12-14%', '6-7%', '4-5%', '4-5%', '5-6%', '40%', '40%', '40%',
                        '40%', '40%', '40%', '40%'],
    'Effect': [
        'Light and refreshing, elevates mood and promotes relaxation.',
        'Medium-bodied, provides a rich and warming sensation, ideal for socializing.',
        'Full-bodied, creates a warming feeling with a slight buzz, perfect for celebration.',
        'Smooth, enhances conversation and creates a pleasant buzz without overpowering.',
        'Bitter and intense, provides a quick energetic buzz, perfect for pairing with savory food.',
        'Crisp and clean, gives a refreshing lift, especially during outdoor events.',
        'Smooth and balanced, great for light social events or meals.',
        'Rich and bold, creates a deep, satisfying warmth, perfect for winter nights.',
        'Bold and warming, ideal for creating a relaxed yet confident vibe.',
        'Smoky and complex, ideal for those who enjoy deep, contemplative drinking.',
        'Spicy, invigorates the senses and works well in cocktails that awaken your palate.',
        'Smooth, sweet, and mellow, perfect for unwinding after a busy day.',
        'Refreshing and aromatic, ideal for uplifting moods at parties or gatherings.',
        'Classic and dry, offers a refreshing experience with a strong, balanced kick.',
        'Smooth and mellow, ideal for sipping and slowly enjoying during social gatherings.'
    ],
    'Origin': ['France', 'France', 'USA', 'USA', 'USA', 'Germany', 'Czech Republic', 'UK', 'USA', 'Scotland', 'Canada',
               'Ireland', 'France', 'UK', 'Mexico'],
    'Price Range': ['$10-$20', '$12-$25', '$20-$40', '$18-$30', '$6-$10', '$5-$9', '$4-$8', '$8-$12', '$40-$60',
                    '$50-$100', '$30-$50', '$35-$60', '$40-$70', '$10-$15', '$20-$40'],
    'Best Pairing': [
        'Grilled seafood, salads, or light chicken dishes.',
        'Red meats, pasta with tomato-based sauces, or cheese.',
        'Steak, grilled vegetables, or dark chocolate.',
        'Roast chicken, pork, or pasta with creamy sauces.',
        'Spicy food, burgers, or rich cheeses.',
        'Salads, grilled chicken, or fish.',
        'Sushi, salads, or light fish dishes.',
        'Barbecue, burgers, or chili.',
        'Dark chocolate, smoked meats, or grilled steaks.',
        'Cheese, smoked meats, or rich desserts.',
        'BBQ ribs, grilled meats, or classic cocktails.',
        'Chocolate, apple pie, or on its own for sipping.',
        'Classic with olives, or in a cocktail like gin and tonic.',
        'Citrus salads, seafood, or served in a martini.',
        'Grilled meats, nachos, or sipping after a meal.'
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)


# Price conversion function
def price_to_value(price_range):
    price_map = {
        "$5-$9": 7,
        "$6-$10": 8,
        "$8-$12": 10,
        "$10-$15": 12,
        "$12-$25": 18,
        "$20-$40": 30,
        "$30-$50": 40,
        "$35-$60": 50,
        "$40-$60": 50,
        "$50-$100": 75,
        "$40-$70": 55
    }
    return price_map.get(price_range, 0)


# Side dish price mapping
side_dish_prices = {
    'Wine': {
        'Cheese': 8, 'Olives': 5, 'Grilled Vegetables': 12, 'Bread': 3, 'Chocolate': 7
    },
    'Beer': {
        'Fries': 4, 'Nachos': 6, 'Pretzels': 3, 'Chicken Wings': 10, 'Onion Rings': 5
    },
    'Whiskey': {
        'Dark Chocolate': 7, 'Smoked Meats': 12, 'Nuts': 5, 'Cheese': 8, 'Popcorn': 4
    },
    'Gin': {
        'Olives': 5, 'Citrus Salad': 7, 'Shrimp Cocktail': 15, 'Crab Cakes': 12, 'Caprese Salad': 10
    },
    'Tequila': {
        'Tacos': 8, 'Guacamole': 5, 'Ceviche': 12, 'Nachos': 6, 'Churros': 4
    }
}

# Currency conversion rates (static for this example)
currency_rates = {
    'EUR': 1.0,  # Euro (default)
    'GBP': 0.85,  # British Pound
    'CHF': 0.92,  # Swiss Franc
    'INR': 90.0,  # Indian Rupee
    'JPY': 140.0,  # Japanese Yen
    'CNY': 7.0,  # Chinese Yuan
    'SGD': 1.35,  # Singapore Dollar
    'MYR': 4.4,  # Malaysian Ringgit
    'THB': 35.0  # Thai Baht
}


# Function to convert price to selected currency
def convert_currency(amount, currency):
    return amount * currency_rates[currency]


# Streamlit app main function
def main():
    st.title("PR's Daaru Kharcha Calulator")

    # Sidebar for user inputs
    category = st.sidebar.selectbox('Select the Category', ['Wine', 'Beer', 'Whiskey', 'Gin', 'Tequila'])
    selected_drink = st.sidebar.selectbox('Select a Drink', df[df['Category'] == category]['Name'])
    selected_currency = st.sidebar.selectbox('Select Currency',
                                             ['EUR', 'GBP', 'CHF', 'INR', 'JPY', 'CNY', 'SGD', 'MYR', 'THB'])

    # Get drink information
    selected_drink_info = df[df['Name'] == selected_drink].iloc[0]

    # Display drink information
    st.write(f"**Drink**: {selected_drink}")
    st.write(f"**Description**: {selected_drink_info['Description']}")
    st.write(f"**Alcohol Content**: {selected_drink_info['Alcohol Content']}")
    st.write(f"**Effect**: {selected_drink_info['Effect']}")
    st.write(f"**Origin**: {selected_drink_info['Origin']}")
    st.write(f"**Price Range**: {selected_drink_info['Price Range']}")
    st.write(f"**Best Pairing**: {selected_drink_info['Best Pairing']}")

    # Side dish options
    side_dishes = list(side_dish_prices[category].keys())

    selected_side_dish = st.sidebar.selectbox('Select a side dish', side_dishes)

    # Get side dish price
    side_dish_price = side_dish_prices[category][selected_side_dish]

    # Display side dish pairing
    st.write(f"**Selected Side Dish**: {selected_side_dish}")
    st.write(f"Enjoy your {selected_drink} with {selected_side_dish} for a perfect pairing experience!")

    # Calculate total cost
    drink_price = price_to_value(selected_drink_info['Price Range'])
    total_price = drink_price + side_dish_price

    # Convert total price to selected currency
    total_price_in_selected_currency = convert_currency(total_price, selected_currency)

    # Display total price and classify as Cheap, Affordable, or Expensive
    st.subheader(f"Total Bill: {selected_currency} {total_price_in_selected_currency:.2f}")
    if total_price_in_selected_currency < 30:
        st.write("**Rating**: Cheap")
    elif 30 <= total_price_in_selected_currency < 60:
        st.write("**Rating**: Affordable")
    else:
        st.write("**Rating**: Expensive")


# Run the app
if __name__ == '__main__':
    main()
