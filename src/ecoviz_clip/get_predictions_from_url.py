from io import BytesIO
import requests

def getPredictionsFromURL(image_url, model_checkpoint="openai/clip-vit-large-patch14"):
    # get prediction model checkpoint
    detector = pipeline(model=model_checkpoint, task="zero-shot-image-classification")
    # Set a user-agent to prevent blocking by some websites
    headers = {'User-Agent': 'Mozilla/5.0'}
    # Attempt to fetch the image from the URL
    response = requests.get(image_url, headers=headers)
    # Check if the request was successful and the content is an image
    if response.status_code == 200 and 'image' in response.headers['Content-Type']:
        try:
            # Open the image and predict its category using CLIP
            image = Image.open(BytesIO(response.content))
            predictions = detector(image, candidate_labels=candidate_labels)
            # Convert predictions to a dictionary for easier access
            prediction_dict = {pred["label"]: pred["score"] for pred in predictions}
            # Ensure all candidate labels are in the dictionary, even if they have a score of 0
            for label in candidate_labels:
                prediction_dict.setdefault(label, 0)
        except IOError:
            # Handle errors in opening the image
            print(f"Could not process image {image_url}")
            prediction_dict = {label: 0 for label in candidate_labels}
    else:
        # Handle failed requests or non-image content
        print(f"Failed to fetch or identify image from {image_url}")
        prediction_dict = {label: 0 for label in candidate_labels}
    return prediction_dict