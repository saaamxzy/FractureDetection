from util import *

ds = dicom.read_file("test4.dcm")
img = ds.pixel_array # retrieve the image array

nrows, ncols = img.shape
sig = (nrows / 229.0, ncols / 187.0)
# set the value of sigma according to the image's scale

img = ndimage.gaussian_filter(img, sigma=sig, order=0, truncate=2.0)

# plt.imshow(img, interpolation='nearest', cmap=pylab.cm.bone)
# plt.savefig('./gaussian', bbox_inches='tight')
# j = 4000

# while j < 14000:
image = img 


global_thresh = threshold_otsu(image)
print('global threshold: ', global_thresh)
#8413
binary_global = image > global_thresh # temp threshold

# fig, axes = plt.subplots(nrows=3, figsize=(7, 8))
# ax = axes.ravel()
plt.gray()

save_image(binary_global, None, './test_images/img')

# plt.imshow(binary_global)
# plt.axis('off')


#plt.savefig('./test_images/img')
#plt.show()
	# j += 100

