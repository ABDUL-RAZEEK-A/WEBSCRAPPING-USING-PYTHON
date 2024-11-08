import requests

    # Find the paragraph
    paragraph = soup.find('p')
    if paragraph:
        print("Paragraph:", paragraph.text.strip())
    else:
        print("No paragraph found")

    # Find the image
    image = soup.find('img')
    if image:
        image_url = image.get('src')
        print("Image URL:", image_url)

        # Download the image
        try:
            image_response = requests.get("image_url", stream=True)
            image_response.raise_for_status()  # Raise an exception for bad status codes

            # Get the filename from the URL
            filename = os.path.basename(image_url)

            # Create a directory to store the image if it doesn't exist
            image_dir = 'images'
            if not os.path.exists(image_dir):
                os.makedirs(image_dir)

            # Save the image to the directory
            with open(os.path.join(image_dir, filename), 'wb') as f:
                for chunk in image_response.iter_content(1024):
                    f.write(chunk)

            print("Image downloaded and saved to", os.path.join(image_dir, filename))
        except requests.exceptions.RequestException as e:
            print("Error downloading image:", e)
    else:
        print("No image found")

except requests.exceptions.RequestException as e:
    print("Error fetching URL:", e)
except Exception as e:
    print("Error:", e)
