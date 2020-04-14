# ciftify_gradient_align

**Gradient based cifti alignment (BCB)** - 
Construct and align gradients from rfMRI dtseries.

The aim of this project was to set up a pipeline to use BrainSpace to calculate gradients.\
Data used were the resting state fMRI from HCP S1200 Release.\
Our approach in calculating the gradients was validated by observing unique individual subject's gradients.\
Gradients were aligned using Procrustes alignment method, although aligning with joint embedding and/or MSM is a future goal.\
\
<img src="https://user-images.githubusercontent.com/29262872/79281194-3f3b8380-7e80-11ea-989e-91fec0d5cfea.png" width="400"/>\
Computed gradients from a random subject and average dconn provided by HCP S1200.\
\
Currently BCB project for Joelle Jee (@joellejee)


## Dependencies
**Brainspace:** De Wael RV, Benkarim, O., Paquola, C., Lariviere, S., Royer, J., Tavakol, S., …, Bernhardt, B.C. (2019). BrainSpace: a toolbox for the analysis of macroscale gradients in neuroimaging and connectomics datasets. bioRxiv.

**Connectome-Workbench:** Marcus DS, Harwell J, Olsen T, Hodge M, Glasser MF, Prior F, Jenkinson M, Laumann T, Curtiss SW, Van Essen DC. Informatics and data mining tools and strategies for the human connectome project. Front Neuroinform 2011;5:4.

**Nibable:** Brett, Matthew, Markiewicz, Christopher J., Hanke, Michael, Côté, Marc-Alexandre, Cipollini, Ben, McCarthy, Paul, … freec84. (2020, April 8). nipy/nibabel: 2.5.2 (Version 2.5.2). Zenodo. http://doi.org/10.5281/zenodo.3745545

**Numpy:** Stéfan van der Walt, S. Chris Colbert and Gaël Varoquaux. The NumPy Array: A Structure for Efficient Numerical Computation, Computing in Science & Engineering, 13, 22-30 (2011), DOI:10.1109/MCSE.2011.37

**Ciftify:** Glasser MF, Sotiropoulos SN, Wilson JA, Coalson TS, Fischl B, Andersson JL, Xu J, Jbabdi S, Webster M, Polimeni JR, Van Essen DC, Jenkinson M, WU-Minn HCP Consortium. The minimal preprocessing pipelines for the Human Connectome Project. Neuroimage. 2013 Oct 15;80:105-24. PubMed PMID: 23668970; PubMed Central PMCID: PMC3720813.

**qbatch:** Devenyi, G.A., Pipitone, J. (2020). Execute shell command lines in parallel on Slurm, S(un|on of) Grid Engine (SGE) and PBS/Torque clusters. Qbatch (Version 2.2).
