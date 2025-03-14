from PIL import Image

def remove_rgba_color(input_image_path, output_image_path, target_rgba_color):
    image = Image.open(input_image_path)

    new_image = Image.new("RGB", image.size)
    dd = []
    w, j = 0,0
    for y in range(image.height):
        for x in range(image.width):
            current_color = image.getpixel((x, y))
            if current_color != target_rgba_color:
                dd.append(current_color)

    new_image.putdata(dd)
    new_image.save(output_image_path, "PNG")




if __name__ == "__main__":
    input_image_path = "logo.png"  # Replace with your input image path
    output_image_path = "output_image.png"  # Replace with your desired output image path
    target_rgba_color = (0,159, 227)  # Replace with the RGBA color you want to remove

    remove_rgba_color(input_image_path, output_image_path, target_rgba_color)
