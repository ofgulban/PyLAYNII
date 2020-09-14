"""Simulate a simplistic cortical gray matter-like layer image."""

import os
import numpy as np
import nibabel as nb

# Metric file generated by LN2_LAYERS
FILE = "/home/faruk/gdrive/LAYNII/demo_big3/M_brain_rim_metric_equidist.nii.gz"

# Load image data
nii = nb.load(FILE)
data = nii.get_fdata()

# Make single layer in the middle
chunk1 = data[0:50, :, :]  # cut halfway of M
idx0 = chunk1 == 0
idx1 = chunk1 > 0.40
idx2 = chunk1 < 0.60

chunk1[: ,:, :] = 100
chunk1[idx1 * idx2] = 105
chunk1[idx0] = 0

# Make double layers
chunk2 = data[50:, :, :]  # cut the other half of M
idx0 = chunk2 == 0
idx1 = chunk2 > 0.20
idx2 = chunk2 < 0.40
idx3 = chunk2 > 0.60
idx4 = chunk2 < 0.80

chunk2[:, :, :] = 100
chunk2[idx1 * idx2] = 105
chunk2[idx3 * idx4] = 105
chunk2[idx0] = 0

# Put back the chunks
data[0:50, :, :] = chunk1
data[50:, :, :] = chunk2

# Save output
out = nb.Nifti1Image(data, affine=nii.affine)
nb.save(out, "/home/faruk/gdrive/LAYNII/demo_big3/M_brain_simulated_layers.nii.gz")

# With Gaussian noise
idx = data != 0
noise = np.random.normal(loc=0, scale=2, size=np.sum(idx))
data[idx] += noise
out = nb.Nifti1Image(data, affine=nii.affine)
nb.save(out, "/home/faruk/gdrive/LAYNII/demo_big3/M_brain_simulated_layers_noised.nii.gz")

print("Finished.")
