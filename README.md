Forensic Vision AI: Fingerprint Identification System
A lightweight fingerprint matching system using SIFT and FLANN for forensic and biometric applications.

📁 Dataset
Uses the SOCOFing dataset (6,000 real + altered fingerprints):
🔗 Download SOCOFing Dataset (https://drive.google.com/file/d/19t-81kgHMuBrx7Mxieb6ihQPIHpEEXSe/view?usp=sharing)

After downloading, place the folders inside data/ like this:

data/
├── Real/
└── Altered/
    ├── Altered-Easy/
    ├── Altered-Medium/
    └── Altered-Hard/

⚙️ Setup
1.Clone the repo:

    -git clone https://github.com/arjunmuthukumar/Forensic_Vision_AI_Fingerprint_Identification_System.git
    -cd Forensic_Vision_AI_Fingerprint_Identification_System
2.Install dependencies:
bash

    -git clone https://github.com/arjunmuthukumar/Forensic_Vision_AI_Fingerprint_Identification_System.git
    -cd Forensic_Vision_AI_Fingerprint_Identification_System

3.Add the dataset to the data/ folder (as shown above).


▶️ Run
Edit fingerprint_matching.py to set your image paths:

    -sample_path = "data/Altered/Altered-Hard/1__M_Right_index_finger_Obl.BMP"
    -real_image_path = "data/Real/1__M_Right_index_finger.BMP"


Then run:

    -python fingerprint_matching.py


The script will:

    -Detect and match fingerprint keypoints
    -Show a matching score (%)
Display matched keypoints in a window

📜 License
MIT License — see LICENSE for details.

Built for education, research, and forensic prototyping.
Not intended for real-world law enforcement use without expert validation. 
