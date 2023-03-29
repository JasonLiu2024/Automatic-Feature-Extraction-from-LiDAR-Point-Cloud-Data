# GeometryProcessing_SP2023
In this project, I analyze a mesh. This mesh is reconstructed from point cloud obtained by Lidar (light detection and ranging)

<span style="color:#33FF9E">

# 🟩Latest Update on: # Tuesday March 28, 2023
Did
1. Met with Professor Frachetti and Jack to discuss the features lines I drew manually
>Professor Frachetti reviewed my hand-drawn lines
>1. lines drawn by me are not very useful as ground truth
><br>&emsp;I do not have expertise, so I miss many features an archaeologist pick up
><br>&emsp;Archaeologists can make good conclusions about what an incomplete feature might be. I cannot do that without expertise
2. Examined ground truth data we have
>There are two sites: Tashbulak (TBK) and Tugunbulak (TGB)
><br>both sites have radar data. However, only TBK's image quality (at the time of the meeting) is good for direct comparison against feature lines
><br>TBK radar data shows underground walls that form a grid-like pattern.
><br>&emsp;They are most likely rooms (that share walls)
><br>&emsp;From mesh reconstruction, we identifies large squares in TGB that are not obvious in in-person excavations
><br>&emsp;We also have a correspondence between those rooms and grid-like patterns visible on the surface
3. Tasks:
>I will crop out a small chunk of TBK for which rada data is available.
>1. Reconstruct mesh at high accuracy level
>2. Colorize the mesh by curvature
>3. Generate feature lines
>4. Analyze radar data
><br>&emsp;The radar data works similar to MRI. At different depths, we get cross-sections of the landscape, in which high-density materials such as walls are indicated in darker colors. 
><br>&emsp;This means that one certain height, some walls show up and some does not
><br>&emsp;For analysis, we overlay these cross-sections so we can see all walls at once
>5. Georeference the radar data and the TBK mesh, so that we can accurately overlay them and compare
><br>&emsp;At the moment, we can use contour-like roads along the hillside (they show up very clearly in the reconstructed mesh) for alignment
4. TBK_FeatureLines_230314.ipynb
>Organized and recorded results from Tuesday March 14, 2023
5. TBK_GroundTruth_Radar.ipynb
>Started
><nr>Exported TBK radar data as PNG image
6. Reconstructed mesh with **Higher** definition from TBK and TGB point clouds

More Updates at: https://github.com/JasonLiu2024/GeometryProcessing_SP2023/blob/master/Open3D_Test/Log*.ipynb

# High Level Design
Archaeology is an inherently human problem. In the past, human ingenuity and labor dominated this field. But in recent years, new technology in hardware gives archaeologists access to previously unobtainable data with great accuracy. However, such data in its raw form can be hard to interpret. With computational methods in Computer Graphics, Image Anlysis, and Machine Learning, we can transform and break down data so that archaeology researchers can apply their expertise. 
<br>This project to use compututational geometry methods to analyze point cloud data from an archaeological excavation site. From this analysis, we hope to gain insight on features, especially architectural structures, of archaeological insight that may not be visible to human eyes. 
# Files
1. CrestCODE
Tool wrote in C++ Code
<br>This code comes from project 'Fast and Robust Detection of Crest Lines on Meshes' http://www2.riken.jp/brict/Yoshizawa/Research/Crest.html
<br>Authors: Shin Yoshizawa, A. G. Belyaev, H.-P. Seidel
<br>Link to Code: http://www2.riken.jp/brict/Yoshizawa/Research/Programs/CrestCODE.tar.gz
<br>To use CrestCODE for this project, DO:
>1. Unzip the folder. This gives CrestCODE folder
>2. In Terminal, cd to CrestCODE/CCode directory
>3. Run below commands:
><br>make
><br>mv setCurvature ../
>Note: 'make' is a linux command. To use it on Windows, You may need to install the relevant files, like WinGW
>4. Return to CrestCODE

Problems:
>1. the .jar viewer does not work
>2. the code needs to be run from command line
>3. running 'make' gives compilation errors (but the code does work)
2. CrestCODE_mod
<br>In this file, I copy CrestCODE's content. I attempt to modify CrestCODE's contents.
3. Open3D_Test
>1. Jupyter Notebook project files
>2. Mesh analysis data
4. ReferenceImages
<br>Collection of mesh analysis results (images) in the beginning of this project.
5. libigl_Tutorials_WK2
<br>Jupyter Notebook project files, to test out libigl's functionalities
6. .gitignore
<br>Mesh files ignored. 
# Contributors
Jason Liu: wrote code in Open3D_Test and carried out mesh analysis
# Setup and How to Run
1. Clone the entire directory. 
2. Follow instructions found in Instructions.ipynb
# Dependencies

