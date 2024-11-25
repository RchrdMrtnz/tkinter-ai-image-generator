import customtkinter as ctk  # pip install customtkinter
import tkinter
import os
from PIL import Image, ImageTk
import requests, io
from image_generator.generate_image import generate_image_urls  # Import the function

def generate():
    user_prompt = prompt_entry.get("0.0", tkinter.END).strip()
    user_prompt += " in style: " + style_dropdown.get()
    n = int(number_slider.get())

    # Get the URLs using the imported function
    image_urls = generate_image_urls(user_prompt, n)

    if not image_urls:
        print("No images were generated. Check for errors.")
        return

    # Create a folder with the name of the prompt
    folder_name = prompt_entry.get("0.0", tkinter.END).strip().replace(" ", "_")
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    images.clear()
    for idx, url in enumerate(image_urls):
        response = requests.get(url)
        image = Image.open(io.BytesIO(response.content))
        photo_image = ImageTk.PhotoImage(image)
        images.append((photo_image, image))  # Save both PhotoImage and the Image object

        # Save the downloaded image in the folder
        image.save(os.path.join(folder_name, f"image_{idx + 1}.png"))

    update_image(0)

def update_image(index):
    global current_index
    current_index = index

    canvas.image = images[index][0]  # Display the current image
    canvas.create_image(0, 0, anchor="nw", image=images[index][0])

    # Update the button states based on the index
    prev_button.configure(state="normal" if index > 0 else "disabled")
    next_button.configure(state="normal" if index < len(images) - 1 else "disabled")
    download_button.configure(state="normal")

def next_image():
    if current_index < len(images) - 1:
        update_image(current_index + 1)

def prev_image():
    if current_index > 0:
        update_image(current_index - 1)

def download_image():
    if images:
        image = images[current_index][1]  # Get the current Image object
        folder_name = prompt_entry.get("0.0", tkinter.END).strip().replace(" ", "_")
        save_path = os.path.join(folder_name, f"image_{current_index + 1}.png")
        image.save(save_path)
        print(f"Image saved as {save_path}")

def update_slider_label(value):
    slider_value_label.configure(text=f"{int(float(value))}")

root = ctk.CTk()
root.title("AI Image Generator")

ctk.set_appearance_mode("dark")

input_frame = ctk.CTkFrame(root)
input_frame.pack(side="left", expand=True, padx=20, pady=20)

prompt_label = ctk.CTkLabel(input_frame, text="Prompt")
prompt_label.grid(row=0, column=0, padx=10, pady=10)
prompt_entry = ctk.CTkTextbox(input_frame, height=10)
prompt_entry.grid(row=0, column=1, padx=10, pady=10)

style_label = ctk.CTkLabel(input_frame, text="Style")
style_label.grid(row=1, column=0, padx=10, pady=10)
style_dropdown = ctk.CTkComboBox(input_frame, values=["Realistic", "Cartoon", "3D Illustration", "Flat Art"])
style_dropdown.grid(row=1, column=1, padx=10, pady=10)

number_label = ctk.CTkLabel(input_frame, text="# Images")
number_label.grid(row=2, column=0, padx=10, pady=10)

# Slider to select the number of images
number_slider = ctk.CTkSlider(input_frame, from_=1, to=10, number_of_steps=9, command=update_slider_label)
number_slider.grid(row=2, column=1, padx=10, pady=10)

# Label to display the slider value
slider_value_label = ctk.CTkLabel(input_frame, text="5")  # Initial slider value
slider_value_label.grid(row=2, column=2, padx=10, pady=10)

# Navigation and download buttons
button_frame = ctk.CTkFrame(input_frame)
button_frame.grid(row=3, column=0, columnspan=3, sticky="news", padx=10, pady=10)

prev_button = ctk.CTkButton(button_frame, text="←", command=prev_image, state="disabled")
prev_button.grid(row=0, column=0, padx=5)

download_button = ctk.CTkButton(button_frame, text="Download", command=download_image, state="disabled")
download_button.grid(row=0, column=1, padx=5)

next_button = ctk.CTkButton(button_frame, text="→", command=next_image, state="disabled")
next_button.grid(row=0, column=2, padx=5)

generate_button = ctk.CTkButton(input_frame, text="Generate", command=generate)
generate_button.grid(row=4, column=0, columnspan=3, sticky="news", padx=10, pady=10)

canvas = tkinter.Canvas(root, width=1024, height=1024)
canvas.pack(side="left")

# Global variables
images = []
current_index = 0

root.mainloop()
