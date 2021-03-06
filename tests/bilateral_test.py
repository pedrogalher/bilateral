import numpy as np
import pyximport; pyximport.install()
from bilateral import cython_bilateral3d
from scipy import ndimage
import nibabel as nib
import os

def testit():
    folder='/home/denest/Share/'
    name='20140113_112804LAGUNOVAVV21011939.nii'


    f = nib.load(os.path.join(folder,name))
    im = f.get_data()
    hdr = f.get_header()
    mrx = hdr.get_sform()

    print im.dtype
    #im=np.array(im, dtype='float64', order='C')
    print im.dtype

    crop=slice(100,-100)
    vol = np.array(im[...,6][crop,crop,110:-110], dtype='float64', order='C')
    filtered_image=np.copy(vol)

    for i in range(1):
    	print i

    	
    	print vol.shape

    	filtered_image=cython_bilateral3d.bilateral3d_optimized( filtered_image, 
    											  [0.7,0.7,0.5],
    											  1,
    											  40)
        #print np.max(filtered_image2),np.min(filtered_image2),np.mean(filtered_image2)
        


        nib.nifti1.save(nib.Nifti1Image(filtered_image, mrx), 
                        folder+name[:-4]+'_filtered%s.nii'%(i))
        
        nib.nifti1.save(nib.Nifti1Image(vol, mrx), 
                        folder+name[:-4]+'_notfiltered.nii')
        
        nib.nifti1.save(nib.Nifti1Image(filtered_image-vol, mrx), 
                        folder+name[:-4]+'_noise%s.nii'%(i))
    

"""
for i,int_sigma in zip(range(2),(40.,30.)):
	filtered_image=bilateral3d.bilateral3d(filtered_image,[0.9,0.9,0.8],1,int_sigma)
	image.savenii(filtered_image,mrx,folder+name[:-4]+'_filtered%s.nii'%(i+1))
"""


"""

img_filtered=bilateral_generic(im,[0.9,0.9,0.8],1,40)
image.savenii(filtered_image,mrx,folder+name[:-4]+'_filtered%s.nii'%(i+1))

"""