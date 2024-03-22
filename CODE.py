import cv2
import numpy as np

def compare_granules(image1, image2):
    # Load images
    img1 = cv2.imread(image1, 0)  # Read images as grayscale
    img2 = cv2.imread(image2, 0)

    # Check if images are loaded successfully
    if img1 is None or img2 is None:
        print("Error: Could not load images.")
        return

    # Resize images to the same size (optional, if needed)
    img1 = cv2.resize(img1, (500, 500))
    img2 = cv2.resize(img2, (500, 500))

    # Get dimensions
    h, w = img1.shape

    # Define granule size

    granule_size = 2

    # Initialize sets
    positive = set()
    negative = set()
    boundary = set()

    # Iterate over each 2x2 block in both images
    for i in range(0, h - granule_size + 1, granule_size):
        for j in range(0, w - granule_size + 1, granule_size):
            # Extract granules
            granule1 = img1[i:i+granule_size, j:j+granule_size]
            granule2 = img2[i:i+granule_size, j:j+granule_size]

            # Compare granules
            if np.array_equal(granule1, granule2):
                positive.add((i, j))
            else:
                similar_pixels = np.sum(granule1 == granule2)
                if similar_pixels == 0:
                    negative.add((i, j))
                else:
                    boundary.add((i, j))

    return positive, negative, boundary

# Example usage
image1_path = r"C:\Users\soham\python prog\image_pros\Major\final intrim\f1.jpg"
image2_path = r"C:\Users\soham\python prog\image_pros\Major\final intrim\f1.jpg"

positive_set, negative_set, boundary_set = compare_granules(image1_path, image2_path)

print("Positive set:", positive_set)
print("Negative set:", negative_set)
print("Boundary set:", boundary_set)
