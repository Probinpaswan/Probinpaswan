import cv2

# Define the dimensions of the output video
video_width = 640
video_height = 480

# Open the text file and read in the characters
with open("input.txt", "r") as file:
    content = file.read()

# Convert each character to a binary value and map to black or white pixels
pixels = []
for char in content:
    binary_value = format(ord(char), "08b")  # Convert character to 8-bit binary string
    for bit in binary_value:
        if bit == "0":
            pixels.append(0)  # Black pixel
        else:
            pixels.append(255)  # White pixel

# Create a video writer object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
output_video = cv2.VideoWriter("output.mp4", fourcc, 25, (video_width, video_height))

# Create a black and white pixel image from the pixel values and add it to the video
for i in range(0, len(pixels), video_width * video_height):
    frame_pixels = pixels[i : i + video_width * video_height]
    frame_pixels = np.array(frame_pixels).reshape(video_height, video_width)
    frame = cv2.cvtColor(frame_pixels, cv2.COLOR_GRAY2BGR)
    output_video.write(frame)

# Release the video writer object and close the file
output_video.release()
