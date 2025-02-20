import os
import cv2

# Use a known matching pair
sample_path = r"data/Altered/Altered-Hard/1__M_Right_index_finger_Obl.BMP"
real_image_path = r"data/Real/1__M_Left_index_finger.BMP"

# Load the sample and real images
sample = cv2.imread(sample_path)
real_image = cv2.imread(real_image_path)

if sample is None:
    print(f"Error: Unable to load sample image at {sample_path}")
    exit()

if real_image is None:
    print(f"Error: Unable to load real image at {real_image_path}")
    exit()

# Initialize SIFT
sift = cv2.SIFT_create()

# Detect keypoints and descriptors
keypoints_1, descriptors_1 = sift.detectAndCompute(sample, None)
keypoints_2, descriptors_2 = sift.detectAndCompute(real_image, None)

# Use FLANN-based matcher
matches = cv2.FlannBasedMatcher({'algorithm': 1, 'trees': 10}, {}).knnMatch(descriptors_1, descriptors_2, k=2)

# Apply ratio test to filter good matches
match_points = [p for p, q in matches if p.distance < 0.7 * q.distance]

# Calculate matching score
keypoints = min(len(keypoints_1), len(keypoints_2))
if keypoints == 0:
    print("No keypoints detected.")
else:
    match_score = len(match_points) / keypoints * 100
    print(f"Matching Score: {match_score}")

# Draw matches
result = cv2.drawMatches(sample, keypoints_1, real_image, keypoints_2, match_points, None)
cv2.imshow("Matches", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
