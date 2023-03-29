# GeometryProcessing_SP2023
In this project, I analyze a mesh. This mesh is reconstructed from point cloud obtained by Lidar (light detection and ranging)

<span style="color:#33FF9E">

#🟩Latest Update on: # Tuesday March 28, 2023
Did
1. Met with Professor Frachetti and Jack to discuss the features lines I drew manually
2. Examined ground truth data we have
>There are two sites: Tashbulak (TBK) and Tugunbulak (TGB)
3. Tasks:
>I will crop out a small chunk of TBK for which rada data is available.
>1. Reconstruct mesh at high accuracy level
>2. Colorize the mesh by curvature
>3. Generate feature lines
>4. Analyze radar data
4. TBK_FeatureLines_230314.ipynb
5. TBK_GroundTruth_Radar.ipynb
6. Reconstructed mesh with **Higher** definition from TBK and TGB point clouds

#🟩More Details and History at: https://github.com/JasonLiu2024/GeometryProcessing_SP2023/blob/master/Open3D_Test/Log*.ipynb

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

