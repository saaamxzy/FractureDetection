from util import *

if __name__ == '__main__':
	for i in range(18,21):
		print 'Working on # ' + str(i)
		ds = dicom.read_file("./images_to_read/test_" + str(i) + ".dcm")
		img = ds.pixel_array # retrieve the image array
		img = img[50:-50, 50:-50] # discard the black borders
		# Uncomment to see original .dcm images
		# save_image(img, 
		#  	pylab.cm.bone, './original_images/original_' + str(i))

		nrows, ncols = img.shape
		sig = (nrows / 229.0, ncols / 187.0)
		# set the value of sigma according to the image's scale

		img = ndimage.gaussian_filter(img, sigma=sig, order=0, truncate=2.0)

		# plt.imshow(img, interpolation='nearest', cmap=pylab.cm.bone)
		# plt.savefig('./gaussian', bbox_inches='tight')

		global_thresh = threshold_otsu(img)
		th = global_thresh
		binary_global = img > th

		# fig, axes = plt.subplots(nrows=3, figsize=(7, 8))
		# ax = axes.ravel()
		plt.gray()

		# To find the leftmost, rightmost, upmost and downmost black pixel
		rows_z, cols_z = np.where(binary_global == False)
		leftmost_z = cols_z.min()
		rightmost_z = cols_z.max()
		upmost_z = rows_z.min()
		downmost_z = rows_z.max()

		# Debugging statements
		# print binary_global
		# print 'image dimension: ', binary_global.shape
		# print leftmost_z, rightmost_z, upmost_z, downmost_z

		# To crop out the unwanted white borders
		h,w = binary_global.shape
		x_offset = w // 4
		x_left_bound = w // 2 - x_offset
		x_right_bound = w // 2 + x_offset
		y_offset = h //4
		y_up_bound = h // 2 - y_offset
		y_down_bound = h // 2 + y_offset

		if not x_left_bound < leftmost_z < x_right_bound:
			binary_global[0:h,0:leftmost_z+1] = False
		if not x_left_bound < rightmost_z < x_right_bound:
			binary_global[0:h, rightmost_z-1:w] = False
		if not y_up_bound < upmost_z < y_down_bound:
			binary_global[0:upmost_z+1, 0:w] = False
		if not y_up_bound < downmost_z < y_down_bound:
			binary_global[downmost_z-1:h, 0:w] = False

		# Uncomment to see the binary image
		# save_image(binary_global, None, './test_images/img' + str(i))

		mask = binary_global > 0.8 * binary_global.mean()

		all_labels = measure.label(mask)
		blobs_labels, n_labels = measure.label(mask, background=0, return_num=True)
		sizes = ndimage.sum(mask, blobs_labels, range(n_labels + 1))

		if sizes.size > 1:
			temp = sizes.copy()
			temp.sort()
			minsize = temp[-2]
			mean_vals = ndimage.sum(img, blobs_labels, range(1, n_labels + 1))
			mask_size = sizes < minsize + 1
			remove_pixel = mask_size[blobs_labels]
			blobs_labels[remove_pixel] = 0

		# None-zeros
		# To find all none zero fields
		rows, cols = np.nonzero(blobs_labels)
		leftmost = cols.min()
		rightmost = cols.max()
		upmost = rows.min()
		downmost = rows.max()

		width = rightmost - leftmost
		height = downmost - upmost

		w_z = rightmost_z - leftmost_z
		h_z = downmost_z - upmost_z

		rect = make_rect(leftmost, upmost, width, height)

		# Uncomment to see rectangles on grey scale image
		# save_image(blobs_labels, 
		#	'nipy_spectral', './out_images/img'+str(i)+'_cct', rect=rect)

		save_image(ds.pixel_array, 
			pylab.cm.bone, './final_images/img_final_' + str(i), rect=rect)

		#save_image(binary_global, None, './test_images/img' + str(i))

		# plt.imshow(binary_global)
		# plt.axis('off')
		#plt.savefig('./test_images/img')
		#plt.show()

