import cv2
import sys
import os

print 'Arguments: ', str(sys.argv)

# read arguments
imName = sys.argv[1]
imInterpolation = '0'
if (len(sys.argv) > 2):
	imInterpolation = sys.argv[2]

# output folders constants
outputFolder = 'output'
outputXXHDPI = outputFolder + "/drawable-xxhdpi"
outputXHDPI = outputFolder + "/drawable-xhdpi"
outputHDPI = outputFolder + "/drawable-hdpi"
outputMDPI = outputFolder + "/drawable-mdpi"

# multipliers
t_const = 1./3.
mult_2 = t_const * 2
mult_15 = t_const * 1.5
mult_1 = t_const

# create folders structure function
def createFolders():
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

# validate arguments
if (imName != ''):
	# read image
	image = cv2.imread(imName, -1)

	if (image == None):
		sys.exit('No such image: ' + imName)

	# read image values
	height, width, depth = image.shape

	# pick interpolation algorithm
	interp = cv2.INTER_NEAREST
	if (imInterpolation == '1'):
		interp = cv2.INTER_LINEAR
		print 'INTER_LINEAR interpolation will be used'
	elif (imInterpolation == '2'):
		interp = cv2.INTER_AREA
		print 'INTER_AREA interpolation will be used'
	elif (imInterpolation == '3'):
		interp = cv2.INTER_CUBIC
		print 'INTER_CUBIC interpolation will be used'
	elif (imInterpolation == '4'):
		interp = cv2.INTER_LANCZOS4
		print 'INTER_LANCZOS4 interpolation will be used'
	else:
		print 'INTER_NEAREST interpolation will be used'
	
	# downscale original
	xhdpi = cv2.resize(image, (0,0), fx=mult_2, fy=mult_2, interpolation=interp)
	hdpi = cv2.resize(image, (0,0), fx=mult_15, fy=mult_15, interpolation=interp)
	mdpi = cv2.resize(image, (0,0), fx=mult_1, fy=mult_1, interpolation=interp)

	# save results
	cv2.imwrite(outputXXHDPI + "/" + imName, image)
	cv2.imwrite(outputXHDPI + "/" + imName, xhdpi)
	cv2.imwrite(outputHDPI + "/" + imName, hdpi)
	cv2.imwrite(outputMDPI + "/" + imName, mdpi)
else:
	print 'No image is set'

