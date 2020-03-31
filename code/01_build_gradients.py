"""
Usage: 
  build_gradients.py <dconn_directory>
  
Arguments:
  <dconn_directory>   Path to directory that contains dconn file.

"""

from brainspace.gradient import GradientMaps
import os
import numpy as np
from docopt import docopt
from glob import glob
from threading import Thread
import nibabel as nib



def reorder_embeddings_to_dense(emb, out_order, corr_out, ndim = 6):
    '''note - we are only taking the first 6 dimensions'''
    emb_reorder = np.zeros((emb.shape[0],ndim))
    for i,new_val in enumerate(out_order.astype(int)):
        if new_val < ndim:
            if corr_out[i] < 0:
                emb_reorder[:,new_val] = emb[:,i]*-1
            else:
                emb_reorder[:,new_val] = emb[:,i]
    return emb_reorder

def compare_embending_to_dense(emb, densed_emb):
    total_emb_comp = emb.shape[1]
    out_order = np.empty((total_emb_comp))
    corr_out = np.empty((total_emb_comp))
    for i in range(total_emb_comp):
        cross_cor = np.corrcoef(np.transpose(emb[:,i]), np.transpose(densed_emb))[0, 1:]
        best_match = np.nanargmax(abs(cross_cor))
        out_order[i] = best_match
        corr_out[i] = cross_cor[best_match]
        
    return out_order, corr_out

def build_gradients(sub_file, average_grad):
    
    # load the dconn file and compute gradients
    dconn = nib.load(sub_file)
    gm = GradientMaps(n_components=10, random_state=0)
    gm.fit(dconn.get_data())
    
    # check if the shape of the gradients is correct.
    sub_grad = gm.gradients_
    if sub_grad.shape[0] < sub_gra.shape[1]:
        sub_grad = np.transpose(sub_grad)
    
    # reorder the gradients
    out_order, corr_out = compare_embending_to_dense(sub_grad, average_grad)
    sub_grad = reorder_embeddings_to_dense(sub_grad, out_order, corr_out, ndim = 10)
    
    return sub_grad
    
def align_to_average(sub_dconn, average_dconn):
    
    # load the dconn file and compute gradients
    sub_dconn = nib.load(sub_dconn)
    
    # create a GradientMaps object to store the aligned gradients
    aligned = GradientMaps(kernel = "normalized_angle",
                           alignment = "joint")

    aligned.fit([average_dconn, sub_dconn])
    
    return aligned.gradients_
    

def build_and_align(sub_dconn, average_dconn, average_grad, sub_no):
    
    # format name for gradient file
    grad_name = os.path.basename(sub_dconn)
    grad_name = grad_name.replace(".dconn.nii", "_gradients.txt")
    grad_name = os.path.join("/scratch/a/arisvoin/jjee/gradients_txt", 
                             sub_no,
                             grad_name)
    
    # first build subject's gradients
    sub_grad = build_gradients(sub_dconn, average_grad)
    
    # save as textfile
    np.savetxt(grad_name, sub_grad)
    
    # format appropriate filename for aligned gradients
    # aligned_name = grad_name.replace("_gradients.txt",
                                     # "_gradients_aligned.txt")
    
    # align the subject's gradients to the average gradients
    # aligned_grad = align_to_average(sub_dconn, average_dconn)
    
    # write the aligned gradients as a text file
    # np.savetxt(aligned_name, aligned_grad)
    
    
if __name__== '__main__':
    dconn_dir = docopt(__doc__)["<dconn_directory>"]
    dconn_files = glob(os.path.join(dconn_dir, "*.dconn.nii"))
    
    # get subject number
    sub_no = os.path.basename(os.path.normpath(dconn_dir))
    
    # read pre-computed average dconn
    average_dconn = "/scratch/a/arisvoin/jjee/dconn/average/average.dconn.nii"
    average_dconn = nib.load(average_dconn)
    
    # read pre-computed average gradients
    average_grad = "/scratch/a/arisvoin/jjee/gradients_txt/average/average_gradients.txt"
    average_grad = np.loadtxt(average_grad)
    
    # create subject subdirectories to store gradients
    sub_grad_dir = os.path.join("/scratch/a/arisvoin/jjee/gradients_txt/", sub_no)
    if not os.path.exists(sub_grad_dir):
        os.makedirs(sub_grad_dir)

    for dconn in dconn_files:
        t = Thread(target=build_and_align, args=(dconn, average_dconn, average_grad, sub_no))
        t.start()
    