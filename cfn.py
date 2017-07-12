basedir = './101'
 38 for fn in os.listdir(basedir):
 39   #if not os.path.isdir(os.path.join(basedir, fn)):
 40   #  continue
 41   print('changing name...')
 42   fn_l = fn.split("_")
 43   key = fn_l[0]
 44   if not key.isdigit():
 45     continue
 46   os.rename(os.path.join(basedir, fn),
 47             os.path.join(basedir, key))
