# GeometryProcessing_SP2023 (Work-in-progress ReadME!)
In this project, I analyze a mesh. This mesh is reconstructed from point cloud obtained by Lidar (light detection and ranging)

<span style="color:#33FF9E">

# 🟩Latest Update on: Monday March 27, 2023
Did
1. GroundTruth_Blender.ipynb
>Drew updated feature lines!
><br>I examined the mesh more closely and drew updated feature lines!
><br>I found that Blender's clay_muddy.exr option for MATCAP shows a lot more details other options missed

More Updates at: https://github.com/JasonLiu2024/GeometryProcessing_SP2023/blob/master/Open3D_Test/Log*.ipynb

<br>230217
>Additional analysis to areas 5~11

230220
>Analyzed Enlarged versions for Areas 6, 8, and 11.
><br>Reconstructed mesh from point cloud, with varied 'Reconstruction Depth' values from 8 to 5
><br>Added curvature colorization (APSS, K1)

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

