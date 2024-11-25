# Tkinter AI Image Generator

This project is a simple GUI-based AI image generator built using **Tkinter** and **CustomTkinter** for the interface, and the OpenAI API for generating images based on user prompts. The application allows users to:

- Enter a prompt to describe the desired image.
- Select a style for the image (e.g., Realistic, Cartoon, etc.).
- Choose the number of images to generate.
- Navigate through generated images.
- Save generated images to a folder named after the prompt.

This project is beginner-friendly and serves as a great introduction to combining Python-based GUIs with APIs.

---

## Features

1. **Prompt-based Image Generation**: Generate AI images by providing descriptive prompts.
2. **Customizable Styles**: Choose from predefined styles like Realistic, Cartoon, 3D Illustration, and Flat Art.
3. **Batch Image Generation**: Generate multiple images at once.
4. **Interactive Navigation**: Navigate through generated images using Previous and Next buttons.
5. **Image Saving**: Automatically saves images in a folder named after the prompt.

---

## Requirements

Make sure you have the following installed:

- Python 3.7+
- Libraries:
  - `customtkinter`
  - `tkinter` (comes pre-installed with Python)
  - `requests`
  - `Pillow`
  - `openai`

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/tkinter-ai-image-generator.git
   cd tkinter-ai-image-generator
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` is not available, you can manually install the required libraries:

   ```bash
   pip install customtkinter requests pillow openai
   ```

3. Set up the OpenAI API key:

   - Obtain an API key from [OpenAI](https://platform.openai.com/).
   - Set an environment variable for the API key:

     **For Windows**:
     ```cmd
     set OPENAI_API_KEY=your_openai_api_key
     ```

     **For Mac/Linux**:
     ```bash
     export OPENAI_API_KEY=your_openai_api_key
     ```

4. Run the application:

   ```bash
   python main.py
   ```

---

## Usage

1. **Enter a Prompt**: Describe the image you want to generate in the text box.
2. **Select a Style**: Choose a style from the dropdown menu.
3. **Set the Number of Images**: Use the slider to set how many images to generate.
4. **Generate**: Click the "Generate" button to create images.
5. **Navigate Images**:
   - Use the **←** and **→** buttons to view previous or next images.
   - Click **Download** to save the currently displayed image.

---

## Project Structure

- `main.py`: The main script containing the GUI and logic.
- `image_generator/generate_image.py`: Contains the function for communicating with the OpenAI API to generate image URLs.

---

## Notes

- Ensure you have a valid OpenAI API key with sufficient quota.
- Generated images are saved in a folder named after the entered prompt.
- The application runs entirely on your local machine and requires internet connectivity to use the OpenAI API.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Acknowledgements

This project is inspired by the [YouTube video](https://youtu.be/cWn2g96O3KE) that demonstrates building a Tkinter-based application. Special thanks to the creator for the idea and guidance.
