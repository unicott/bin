import cv2
import sys
import os

print 'Arguments: ', str(sys.argv)

imName = sys.argv[1]
imInterpolation = '0'
if (len(sys.argv) > 2):
	imInterpolation = sys.argv[2]

outputFolder = 'output'
outputXXHDPI = outputFolder + "/drawable-xxhdpi"
outputXHDPI = outputFolder + "/drawable-xhdpi"
outputHDPI = outputFolder + "/drawable-hdpi"
outputMDPI = outputFolder + "/drawable-mdpi"

factor2 = 1./3. * 2
factor1_5 = 1./3. * 1.5
factor1 = 1./3.

def createFolders():
	print 'Create folders...'
	if not os.path.exists(outputFolder):
		os.makedirs(outputFolder)
		print 'Create output folder...'
	if not os.path.exists(outputXXHDPI):
		os.makedirs(outputXXHDPI)
		print 'Create xxhdpi folder...'
	if not os.path.exists(outputXHDPI):
		os.makedirs(outputXHDPI)
		print 'Create xhdpi folder...'
	if not os.path.exists(outputHDPI):
		os.makedirs(outputHDPI)
		print 'Create hdpi folder...'
	if not os.path.exists(outputMDPI):
		os.makedirs(outputMDPI)
		print 'Create mdpi folder...'

createFolders()

print 'imName = ', imName

if (imName != ''):
	image = cv2.imread(imName, -1)
	height, width, depth = image.shape
	interp = cv2.INTER_NEAREST
	if (imInterpolation == '1'):
		interp = cv2.INTER_LINEAR
	elif (imInterpolation == '2'):
		interp = cv2.INTER_AREA
	elif (imInterpolation == '3'):
		interp = cv2.INTER_CUBIC
	elif (imInterpolation == '4'):
		interp = cv2.INTER_LANCZOS4
	print 'interpolation = ', interp
	xhdpi = cv2.resize(image, (0,0), fx=factor2, fy=factor2, interpolation=interp)
	hdpi = cv2.resize(image, (0,0), fx=factor1_5, fy=factor1_5, interpolation=interp)
	mdpi = cv2.resize(image, (0,0), fx=factor1, fy=factor1, interpolation=interp)
	cv2.imwrite(outputXXHDPI + "/" + imName, image)
	cv2.imwrite(outputXHDPI + "/" + imName, xhdpi)
	cv2.imwrite(outputHDPI + "/" + imName, hdpi)
	cv2.imwrite(outputMDPI + "/" + imName, mdpi)
else:
	print 'No image is set'

