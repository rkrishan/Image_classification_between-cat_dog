#!/usr/local/bin/python2.7

import argparse as ap
import cv2
import imutils
import numpy as np
import os
from sklearn.svm import LinearSVC
from sklearn.externals import joblib
from scipy.cluster.vq import *

# Load the classifier, class names, scaler, number of clusters and vocabulary
clf, classes_names, stdSlr, k, voc = joblib.load("/home/rams/Desktop/UI_task_List/Image_classification/myproject/myapp/bof.pkl")

class Classification:

    
    def imageClassification(self,test_image_path):

        # Get the path of the testing image(s) and store them in a list
        image_paths = []

        path=[test_image_path]
        image_paths=path

        # Create feature extraction and keypoint detector objects
        fea_det = cv2.FeatureDetector_create("SIFT")
        des_ext = cv2.DescriptorExtractor_create("SIFT")

        # List where all the descriptors are stored
        des_list = []

        for image_path in image_paths:
            im = cv2.imread(image_path)
            if im == None:
                print "No such file {}\nCheck if the file exists".format(image_path)
                exit()
            kpts = fea_det.detect(im)
            kpts, des = des_ext.compute(im, kpts)
            des_list.append((image_path, des))

        # Stack all the descriptors vertically in a numpy array
        descriptors = des_list[0][1]
        for image_path, descriptor in des_list[0:]:
            descriptors = np.vstack((descriptors, descriptor))

        test_features = np.zeros((len(image_paths), k), "float32")
        for i in xrange(len(image_paths)):
            words, distance = vq(des_list[i][1],voc)
            for w in words:
                test_features[i][w] += 1

        # Perform Tf-Idf vectorization
        nbr_occurences = np.sum( (test_features > 0) * 1, axis = 0)
        idf = np.array(np.log((1.0*len(image_paths)+1) / (1.0*nbr_occurences + 1)), 'float32')

        # Scale the features
        test_features = stdSlr.transform(test_features)


        # Perform the predictions
        predictions =  [classes_names[i] for i in clf.predict(test_features)]
        return predictions
        # Visualize the results, if "visualize" flag set to true by the user
        # if args["visualize"]:

        # print(predictions)
        # print(image_paths)
        # for image_path, prediction in zip(image_paths, predictions):
        #     image = cv2.imread(image_path)
        #     cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
        #     pt = (0, 3 * image.shape[0] // 4)
        #     cv2.putText(image, prediction, pt ,cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, [0, 255, 0], 2)
        #     cv2.imshow("Image", image)
        #     cv2.waitKey(0)

# def main():
#     obj=Classification()
#     image_path= 'dataset/test/lotus/image_0002.jpg'
#     ac = obj.imageClassification(image_path)
#     print(ac)
#
#
#
# if __name__ == '__main__':
#     main()
