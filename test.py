from google_images_download import google_images_download

# Set the keyword you want to search for
word = "cursed memes"

# Set the arguments for the search
arguments = {"keywords": word, "format": "jpg", "limit": 1, "print_urls": True}

# Download the images
response = google_images_download.googleimagesdownload()
paths = response.download(arguments)