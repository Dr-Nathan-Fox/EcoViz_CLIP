import pandas as pd

from ecoviz_clip import getPredictionsFromURL

def processImagesFromDF(image_df):
    # Initialize an empty list to hold data about each image
    data = []
    # Iterate over each row in the DataFrame of images
    for index, row in image_df.iterrows():
        print(f"Processing image {index + 1}: {row['file_name']}")
        # Get prediction scores for the current image
        prediction_scores = getPredictionsFromURL(row['url'])
        # Append a dictionary with the image name, URL, and prediction scores to the list
        data.append({"Image Name": row['file_name'], "Image URL": row['url'], **prediction_scores})
    # Convert the list of data into a DataFrame for further processing or analysis
    return pd.DataFrame(data)