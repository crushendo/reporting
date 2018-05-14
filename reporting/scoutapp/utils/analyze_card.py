import cv2
import numpy as np
from matplotlib import path
import os

# This program uses OpenCV to read a water sensitive paper card and analyzes the droplet
# size and distribution in order to provide data for maximizing agricultural spraying
# efficiency.

class blobDetector():
    def main(self, image_path):
        blobs = blobDetector()
        img, params = blobs.initialize(image_path)
        psi, ppi, totalpix = blobs.scale(img)
        single_keypoints, xlist, ylist = blobs.single_drops(img, params)
        total_area, singles_list, total_drops = blobs.find_contours(img, xlist, ylist, image_path)
        num_median_in, num_average_in, num_stdev_in, vol_median_dia_in, vol_mean_dia_in, \
            coverage_per = blobs.analysis(total_area, singles_list, totalpix, psi,
                                          total_drops, ppi)
        return num_median_in, num_average_in, num_stdev_in, vol_median_dia_in, vol_mean_dia_in, \
            coverage_per

    # Readies OpenCV and reads the image file
    def initialize(self, image_path):
        cwd = os.getcwd()
        print(cwd)
        print(type(image_path))
        image_path = "media/" + str(image_path[3:-2])
        print(image_path)
        img = cv2.imread(image_path)
        params = cv2.SimpleBlobDetector_Params()
        return img, params

    # Needs serious optimization
    # Uses the user-defined size of the card to calculate the scale of the image in pixels per inch
    def scale(self, img):
        card_length = "3"
        card_height = "2"
        sqin = float(card_height) * float(card_length)
        img_copy = img
        # Split the image into an array to get its dimensions
        height, width, channels = img_copy.shape
        # Black out the white background using thresholding. Going pixel by pixel, split its
        # color into RGB components and if one is found to be sufficiently high enough in each
        # (and therefore white background), change this pixel to black
        for i in range(height):
            for j in range(width):
                blue = img_copy[i, j, 0]
                green = img_copy[i, j, 1]
                red = img_copy[i, j, 2]
                if blue > 200:
                    if green > 230:
                        if red > 230:
                            img_copy[i, j] = [0, 0, 0]
                            continue
                # If the pixel is adjasent to a black pixel, be tighter with the thresholding.
                # This helps get all of the border pixels which may be less clear
                if img_copy[i - 1, j, 0] == 0 or img_copy[i, j - 1, 0] == 0 or img_copy[i - 1, j - 1, 0] == 0:
                    if blue > 150:
                        if green > 150:
                            if red > 130:
                                img_copy[i, j] = [0, 0, 0]
        # To pick up border pixels on the opposite side of the card, start on that side and work
        # backwards. Working straight left to right would cover the border pixels on the right side
        # before getting to the easier to pick up background pixels
        for i in range(height - 1, -1, -1):
            for j in range(width - 1, -1, -1):
                blue = img_copy[i, j, 0]
                green = img_copy[i, j, 1]
                red = img_copy[i, j, 2]
                if i == height - 1:
                    continue
                if img_copy[i + 1, j, 0] == 0 or img_copy[i, j + 1, 0] == 0 or img_copy[i + 1, j + 1, 0] == 0:
                    if blue > 150:
                        if green > 150:
                            if red > 130:
                                img_copy[i, j] = [0, 0, 0]
        # Get a total count of all pixels making up the card
        totalcount = 0
        for i in range(height):
            for j in range(width):
                blue = img_copy[i, j, 0]
                green = img_copy[i, j, 1]
                red = img_copy[i, j, 2]
                if red == 0 and green == 0 and blue == 0:
                    continue
                else:
                    totalcount += 1
        # Use the user defined card dimensions and the total pixel count to calculate the
        # scale of the image in pixels per inch and square inch. Return these values for later use
        psi = float(totalcount) / sqin
        ppi = psi ** (0.5)
        totalpix = totalcount
        return psi, ppi, totalpix

    # This method sets up the parameters in SimpleBlobDetector to find 'single droplets:' spots
    # on the spray paper which are indicitive of a complete droplet of water which is not touching
    # or blending with spots made by other droplets. It then runs OpenCV and identifies each
    # of these points and creates a list of their properties, and separate lists for storing
    # their x and y coordinates for locating them later.
    # However, the SimpleBlobDetector is good at identifying these single droplets, but poor at
    # precisely measuring their complete surface area. Therefore, this method identifies the
    # locations of these single droplets, and a later method will analyze the spray care at these
    # points and more precisely measure the exact size of the droplets at these points
    def single_drops(self, img, params):
        # Minimum Area
        params.filterByArea = True
        params.minArea = 10

        # Circularity
        params.filterByCircularity = True
        params.minCircularity = 0

        # Inertia
        params.filterByInertia = True
        params.minInertiaRatio = 0.2

        # Convexity Parameters
        params.filterByConvexity = True
        params.minConvexity = 0.93
        params.maxConvexity = 1

        # Set up detector
        detector = cv2.SimpleBlobDetector_create(params)
        # Detect blobs
        single_keypoints = detector.detect(img)
        single_drops = len(single_keypoints)
        print("single drops: " + str(single_drops))
        # Create list of xy coordinates of all single blob centers
        i = 0
        xlist = []
        ylist = []

        print int(len(single_keypoints))
        while i < int(len(single_keypoints)):
            x = int(single_keypoints[i].pt[0])
            y = int(single_keypoints[i].pt[1])
            print x
            print y
            xlist.append(x)
            ylist.append(y)
            i += 1
        return single_keypoints, xlist, ylist

    # This method uses the findContours OpenCV function and the locations of the single droplets
    # identified by the single_drops() method to measure the size of all droplets on the spray
    # card, and separate out all of the singles for statistical analysis. The area of all droplets
    # will be used to calculate the total coverage area.
    def find_contours(self, img, xlist, ylist, image_path):
        print("entering find_contours()")
        image_path = "media/" + str(image_path[3:-2])
        img = cv2.imread(image_path)
        # First convert the image to greyscale to make thresholding simpler
        imgrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Then threshold the image and separate out the contours found into a list
        ret, thresh = cv2.threshold(imgrey, 160, 255, 0)
        image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        total_drops = len(contours)
        # Draw a binary image of the spray card
        im_with_contours = cv2.drawContours(img, contours, -1, (0, 0, 255), 1)
        # The heirarchy list details the exact position of the contours found, and whether they
        # are encapsulated by other contours. We must reshape this multi-dimensional array to
        # make it easier to work with, and then store this in a new list 'hlist'
        hlength = len(contours)
        hierarchy.shape = (hlength, 4)
        hlist = hierarchy.tolist()

        # Analyze the spray card, looking for droplets
        i = 0
        singles_list = []
        total_area = 0
        while i < len(contours):
            # Determine if contour is in appropriate hierarchy. Filter out contours which are
            # likely concentric or aberrations within a droplet or group of droplets.
            # Needs foolproofing: what if some images have blobs at a different hierarchy level?
            print hlist[i][3]
            if hlist[i][3] != 0:
                i += 1
                continue
            cnt = contours[i]
            # Convert contour to path
            contours[i].shape = (int(contours[i].shape[0]), int(contours[i].shape[2]))
            p = path.Path(contours[i])
            # Go through all of the identified blobs. If the current contour is a single blob,
            # add it to both the singles_list for size distribution analysis, and to the total
            # area for calculating coverage percentage. If not, just add it to the total coverage
            # area.
            j = 0
            while j < len(xlist):
                x = xlist[j]
                y = ylist[j]
                if p.contains_points([(x, y)]):
                    singles_count = len(singles_list)
                    singles_list.append(cv2.contourArea(cnt))
                    del xlist[j]
                    del ylist[j]
                    break
                j += 1
            total_area += cv2.contourArea(cnt)
            i += 1
            print "i = " + str(i)
        print 'length of singles list: ' + str(len(singles_list))
        return total_area, singles_list, total_drops

    # This method uses all of the droplet data gathered previously and performs statistical
    # analysis to characterize the droplet size distribution.
    def analysis(self, total_area, singles_list, totalpix, psi, total_drops, ppi):
        # Calculate the total coverage area as a percentage
        print total_area
        print totalpix
        coverage_per = float(total_area / totalpix)
        print "Coverage percentage: " + str(coverage_per)
        # Take a list of all of the single droplets and convert to a list of areas
        # sorted by size (in square micrometres)
        print 'length of singles list: ' + str(len(singles_list))
        print type(singles_list[3])
        sorted_list_pix = sorted(singles_list)
        print type(sorted_list_pix)
        print("Sorted List Pix: \n")
        print(sorted_list_pix)

        #TODO: Something is going wrong here. Find the spreading factor and compare it to
        # whatever's going wrong here
        # Convert list of pixel areas to square inches
        sorted_list = [x / psi for x in sorted_list_pix]
        # Convert list of spot areas to droplet areas using USDA spread factor
        areas_list = [(0.53549306 * x) - (0.000084839 * x * x) for x in sorted_list]
        # Convert list of droplet areas to droplet diameters
        diameters_list = [x / 3.14159 for x in areas_list]
        print("diameters list: /n")
        print(diameters_list)
        # Calculate the Numerical Mean, Median, and Standard Deviation
        num_median = np.median(diameters_list)
        num_average = np.mean(diameters_list)
        num_stdev = np.std(diameters_list)
        list_length = len(sorted_list)

        # Calculate the Volume Median Diameter
        vol_total = 0
        h = 0
        while h < len(sorted_list):
            vol_total = vol_total + (diameters_list[h] / 2) ** 3 * 3.14159 * 1.3333333
            h += 1

        vol_counter = 0
        i = 0
        print("vol_total: " + str(vol_total))
        # VMD: convert to volume from pix and count until reach median volumetrically
        while vol_counter < (vol_total / 2):
            vol_counter = vol_counter + (diameters_list[i] / 2) ** 3 * 3.14159 * 1.3333333
            i += 1
        print("vol counter: " + str(vol_counter))
        if vol_counter != (vol_total / 2):
            i -= 1
            #vol_median_dia = (diameters_list[i] + (diameters_list[i+1])) / 2
            vol_median_dia = (diameters_list[i])
        else:
            i -= 1
            vol_median_dia = (diameters_list[i])

        # Calculate the Volume Mean Diameter
        j = 0
        numerator = 0
        denominator = 0
        while j < len(sorted_list):
            numerator = numerator + (diameters_list[j]) ** 4
            denominator = denominator + (diameters_list[j]) ** 3
            j += 1
        vol_mean_dia = numerator / denominator

        # Calculate the blob density in droplets per square inch
        drop_density = total_drops / (totalpix / psi)
        # Convert diameter statistics calculated from pixels to inches
        num_median_in = num_median / ppi
        num_average_in = num_average / ppi
        num_stdev_in = num_stdev / ppi
        vol_median_dia_in = vol_median_dia / ppi
        vol_mean_dia_in = vol_mean_dia / ppi
       
        print("ppi: " + str(ppi))
        print("psi: " + str(psi))
        print num_median_in
        print num_average_in
        print num_stdev_in
        print vol_mean_dia_in
        print vol_median_dia_in
        return num_median_in, num_average_in, num_stdev_in, vol_median_dia_in, vol_mean_dia_in, coverage_per


if __name__ == "__main__":
    blobs = blobDetector()
    blobs.main()
