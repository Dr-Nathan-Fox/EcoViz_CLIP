from io import BytesIO
import matplotlib.pyplot as plt
import requests

def displayImageWithPrediction(row)->None:
    """
    Fetches and displays an image from a URL, along with its predicted category.

    Parameters:
    - row: A row from the DataFrame, containing at least 'Image URL' and 'Prediction' fields.
    """
    # Specify a User-Agent to simulate a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Fetch the image with headers
    response = requests.get(row['Image URL'], headers=headers)
    try:
        img = Image.open(BytesIO(response.content))

        # Display the image using matplotlib
        plt.figure(figsize=(5, 5))  # Adjust the figure size as needed
        plt.imshow(img)
        plt.axis('off')  # Hide the axis for a cleaner display
        plt.title(f"Prediction: {row['Prediction']}")  # Show the prediction as the title
        plt.show()
    except Exception as e:
        print(f"An error occurred while processing the image: {e}")