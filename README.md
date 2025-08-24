Fingerprint Matchmaking Using Deep Learning.

This project focuses on fingerprint matching using SIFT (Scale-Invariant Feature Transform) and FLANN-based matching techniques. The goal is to match fingerprint images from the SOCOFing dataset and calculate a matching score based on keypoint similarities.

Dataset:
The dataset used in this project is the SOCOFing dataset, which contains 6,000 fingerprint images, including real and altered fingerprints. You can download the dataset from the following link:

📂 Dataset Link: https://drive.google.com/file/d/19t-81kgHMuBrx7Mxieb6ihQPIHpEEXSe/view?usp=sharing

Dataset Structure
Real Fingerprints: High-quality, unaltered fingerprint images

Altered Fingerprints: Fingerprint images with various alterations (e.g., rotation, scaling, noise) to simulate real-world scenarios.

Setup Instructions
1. Clone the Repository
Clone this repository to your local machine using the following command:

bash
Copy
git clone https://github.com/arjunmuthukumar/fingerprint-matchmaking.git
cd fingerprint-matchmaking
2. Download the Dataset
Download the SOCOFing dataset from the provided Google Drive link.

Extract the dataset and place it in the data folder inside the project directory. The folder structure should look like this:

fingerprint-matchmaking/
├── data/
│   ├── Real/
│   ├── Altered/
│   │   ├── Altered-Easy/
│   │   ├── Altered-Medium/
│   │   └── Altered-Hard/
├── fingerprint_matching.py
├── README.md.

3. Install Dependencies
Ensure you have Python installed (preferably Python 3.8 or higher). Install the required libraries using the following command:


pip install opencv-python opencv-contrib-python
How to Use
Running the Code
Open the fingerprint_matching.py file and update the paths to the sample and real fingerprint images:

python
Copy:-

sample_path = r"data/Altered/Altered-Hard/1__M_Right_index_finger_Obl.BMP"
real_image_path = r"data/Real/1__M_Left_index_finger.BMP"
Run the script using the following command:

bash
Copy
python fingerprint_matching.py
The script will:

Load the sample and real fingerprint images.

Detect keypoints and extract descriptors using SIFT.

Match keypoints using FLANN-based matching.

Calculate and display the matching score.

Visualize the matched keypoints using OpenCV.

Output
Matching Score: A percentage score indicating the similarity between the two fingerprint images.

Visualization: A window displaying the matched keypoints between the sample and real fingerprint images.

Example
Here’s an example of the output you can expect:Matching Score: 85.0
A window will open showing the matched keypoints between the two fingerprint images.

Contributing
Contributions are welcome! If you’d like to improve this project, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
