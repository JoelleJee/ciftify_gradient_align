#!/bin/bash

## software env
module load NiaEnv/2019b # this allows python to load
module use /home/a/arisvoin/edickie/quarantine/modules/
module load edickie_quarantine connectome-workbench/1.4.2
source /scratch/a/arisvoin/edickie/virtual_envs/brainspace_cifti_0200404_03/bin/activate

## set up a trap that will clear the ramdisk if it is not cleared
function cleanup_ramdisk {
    echo -n "Cleaning up ramdisk directory /$SLURM_TMPDIR/ on "
    date
    rm -rf /$SLURM_TMPDIR
    echo -n "done at "
    date
}

# trap the termination signal, and call the function 'trap_term' when
# that happens, so results may be saved.
trap "cleanup_ramdisk" TERM


sub_no=$1

# name all the folders
dconn_input_dir=/scratch/a/arisvoin/jjee/dconn
gradients_txt_out=/scratch/a/arisvoin/edickie/hcp_gradients_20200404/gradients_txt
gradients_dscalar_out=/scratch/a/arisvoin/edickie/hcp_gradients_20200404/gradients_dscalar
average_gradients_dscalar=${gradients_dscalar_out}/average/average_cortex_gradients.dscalar.nii


# make directory for the subject in the separated folder
dconn=${dconn_input_dir}/$sub_no
mkdir -p $dconn

sub=$dconn

source ~/.virtualenvs/gradients/bin/activate
#
python ~/code/ciftify_gradient_align/code/01_build_gradients.py \
   --procustes-align ${average_gradients_dscalar} \
   $sub ${gradients_txt_out}

# get the subject's gradients.txt
sub_grad_dir=${gradients_txt_out}/$sub_no
sub_day1_orig=$(ls $sub_grad_dir | grep REST1 | grep orig)
sub_day2_orig=$(ls $sub_grad_dir | grep REST2 | grep orig)
sub_day1_proc=$(ls $sub_grad_dir | grep REST1 | grep proc)
sub_day2_proc=$(ls $sub_grad_dir | grep REST2 | grep proc)

# get the subject's dconn
dconn_dir=${dconn_input_dir}/$sub_no
dconn_day1=$(ls $dconn_dir | grep REST1)
dconn_day2=$(ls $dconn_dir | grep REST2)

# make subject directory to store dscalar.nii
dscalar_day1_dir=${gradients_dscalar_out}/day1/$sub_no
mkdir -p $dscalar_day1_dir
dscalar_day2_dir=${gradients_dscalar_out}/day2/$sub_no
mkdir -p $dscalar_day2_dir


wb_command -cifti-convert -from-text \
$sub_grad_dir/$sub_day1_orig \
$dconn_dir/$dconn_day1 \
$dscalar_day1_dir/${sub_day1_orig%%.*}.dscalar.nii \
-reset-scalars

wb_command -cifti-convert -from-text \
$sub_grad_dir/$sub_day2_orig \
$dconn_dir/$dconn_day2 \
$dscalar_day2_dir/${sub_day2_orig%%.*}.dscalar.nii \
-reset-scalars

wb_command -cifti-convert -from-text \
$sub_grad_dir/$sub_day1_proc \
$dconn_dir/$dconn_day1 \
$dscalar_day1_dir/${sub_day1_proc%%.*}.dscalar.nii \
-reset-scalars

wb_command -cifti-convert -from-text \
$sub_grad_dir/$sub_day2_proc \
$dconn_dir/$dconn_day2 \
$dscalar_day2_dir/${sub_day2_proc%%.*}.dscalar.nii \
-reset-scalars
