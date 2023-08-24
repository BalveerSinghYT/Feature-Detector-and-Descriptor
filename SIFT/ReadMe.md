# SIFT Feature Detector and Descriptor

## Introduction
SIFT (Scale-Invariant Feature Transform) is a feature detection algorithm in computer vision to detect and describe local features in images. It was published by David Lowe in 1999. The algorithm is patented in the US patent 6,711,293, which expired in 2020. The algorithm can be used for object recognition, image stitching, 3D modeling and much more. The algorithm works as follows:

1. Scale-space extrema detection: Identify potential interest points using a scale-space pyramid.
2. Keypoint localization: Refine the interest points to eliminate low contrast points and edge responses.
3. Orientation assignment: Assign an orientation to each key point based on local image gradient directions.
4. Keypoint descriptor: Create feature vectors based on the image gradients at the key points.

## Implementation

1. Install the required library using the following command:
```
pip install opencv-python
```
2. Run the following command to execute the code:
```
python SIFT.py
```
3. The output image will be displayed as:
   <p align="center"><img src="https://github.com/BalveerSinghYT/Feature-Detector-and-Descriptor/assets/44961536/be7ecd0c-4d22-454d-b70e-07510b93abe2"></p>

## References
1. **Explanation by  Dr. Mubarak Shah:** https://www.youtube.com/watch?v=NPcMS49V5hg
2. **Original Paper:** https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=cc58efc1f17e202a9c196f9df8afd4005d16042a

