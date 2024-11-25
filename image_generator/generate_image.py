import os
import openai

def generate_image_urls(prompt, n):
    """
    Generates images using the OpenAI API and returns the URLs of the generated images.

    Args:
        prompt (str): The descriptive text to generate the image.
        n (int): The number of images to generate.

    Returns:
        list: A list of URLs of the generated images.
    """
    # Set the API key
    openai.api_key = os.getenv("OPENAI_API_KEY")

    try:
        # Generate images using the API
        response = openai.Image.create(
            prompt=prompt,
            n=n,
            size="1024x1024"
        )

        # Extract URLs of the generated images
        image_urls = [data["url"] for data in response["data"]]
        return image_urls

    except openai.error.AuthenticationError:
        print("Authentication error: Check your API key.")
        return []
    except openai.error.InvalidRequestError as e:
        print(f"Request error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

# Example usage
if __name__ == "__main__":
    prompt = "cat wearing red cape"
    n = 2  # Change the value depending on how many images you want to generate

    image_urls = generate_image_urls(prompt, n)
    print("Generated image URLs:", image_urls)