from moviepy.editor import VideoFileClip
from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import filedialog, messagebox
import os


def create_poster():
    # Ask the user to select the input video file
    input_video = filedialog.askopenfilename(title="Select Input Video")

    # Check if a video file is selected
    if not input_video:
        messagebox.showinfo("Information", "No input video selected.")
        return

    # Get the directory and file name from the input path
    input_dir = os.path.dirname(input_video)
    input_filename = os.path.splitext(os.path.basename(input_video))[0]

    # Set the output path using the input directory and file name
    output_poster = os.path.join(input_dir, input_filename + '.jpg')

    # Load the video file and scale it down if necessary
    max_width, max_height = 350, 520
    video = VideoFileClip(input_video)
    if video.size[0] > max_width or video.size[1] > max_height:
        video = video.resize((max_width, max_height / video.size[0] * video.size[1]))

    # Extract frames
    frames = []
    for t in range(0, int(video.duration), 1):
        frames.append(video.get_frame(t))

    # Create the poster image
    height, width = video.size
    n_frames = len(frames)
    rows, cols = int(n_frames ** 0.5), int(n_frames ** 0.5) + 1  # Change the number of rows and columns as per your preference
    h_gap, v_gap = 12, 12  # Set the horizontal and vertical gap between frames
    poster = Image.new('RGB', (cols * (width + h_gap) - h_gap, rows * (height + v_gap) - v_gap), (0, 0, 0))
    draw = ImageDraw.Draw(poster)

    x, y = 0, 0
    for i, frame in enumerate(frames):
        img = Image.fromarray(frame)
        poster.paste(img, (x, y))
        x += width + h_gap
        if (i + 1) % cols == 0:
            x = 0
            y += height + v_gap

    # Save the poster image
    poster.save(output_poster)

    messagebox.showinfo("Information", "Poster saved successfully!")


def main():
    # Create a Tkinter root window
    root = tk.Tk()

    # Create a button to trigger the poster creation
    button = tk.Button(root, text="Create Movie Poster", command=create_poster)
    button.pack()

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
