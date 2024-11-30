from utils.img import generate_mock_image

# Generate the PIL image with large font
image = generate_mock_image()

output_path = "mock_image.png"
image.save(output_path)
