import requests  # For making API requests
import tkinter as tk  # For building the GUI

# Function to fetch and display the weather
def get_weather():
    city = city_entry.get()  # Get the city name from the entry field
    api_key = "ab4f0a879e8e285feff100fd1c1834a1"  # Replace with your actual API key
    
    # API URL for fetching weather
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        # Sending GET request to the API
        response = requests.get(base_url)
        data = response.json()
        
        # Check if the API response is successful
        if data["cod"] == 200:
            main = data["main"]
            weather = data["weather"][0]
            
            # Updating labels with the fetched weather data
            result_label.config(text=f"Weather in {city.title()}:")
            temp_label.config(text=f"Temperature: {main['temp']}°C")
            humidity_label.config(text=f"Humidity: {main['humidity']}%")
            desc_label.config(text=f"Description: {weather['description'].title()}")
        else:
            result_label.config(text="City not found. Please check the city name.")
            temp_label.config(text="")
            humidity_label.config(text="")
            desc_label.config(text="")
    except Exception as e:
        result_label.config(text="Error retrieving data. Please check your connection.")
        temp_label.config(text="")
        humidity_label.config(text="")
        desc_label.config(text="")

# Setting up the GUI window
root = tk.Tk()
root.title("Weather App")
root.geometry("300x200")

# City name input
city_entry = tk.Entry(root, width=20)
city_entry.pack(pady=10)
city_entry.insert(0, "Enter city name")

# Button to fetch weather data
fetch_button = tk.Button(root, text="Get Weather", command=get_weather)
fetch_button.pack(pady=5)

# Labels to display results
result_label = tk.Label(root, text="", font=("Helvetica", 10))
result_label.pack(pady=5)
temp_label = tk.Label(root, text="", font=("Helvetica", 10))
temp_label.pack()
humidity_label = tk.Label(root, text="", font=("Helvetica", 10))
humidity_label.pack()
desc_label = tk.Label(root, text="", font=("Helvetica", 10))
desc_label.pack()

# Run the GUI loop
root.mainloop()
