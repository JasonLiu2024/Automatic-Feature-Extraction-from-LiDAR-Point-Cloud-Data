# GeometryProcessing_SP2023
In this project, I analyze a mesh. This mesh is reconstructed from point cloud obtained by Lidar (light detection and ranging)

<span style="color:#33FF9E">

# 🟩Latest Update on:# Wednesday April 5, 2023
Did:
1. Met with Professor Ju to discuss ways to make feature lines more useful
>We considered three approaches:
>1. Improving geometry-based methods
>>We can modify the CrestCODE code to analyze geometry in a more effective way. We can develop a method to ignore tiny bumps (noise) and only draw feature lines for large/distinct (useful) features
>2. Improving analysis of feature lines
>>We can find a way to filter noise (short, spaced-out feature lines for tiny bumps on the ground–which are not actual features)
>3. Alternative methods
>>We discussed the idea of using shading to recognize features. Professor Ju suggested the 'view dependent' method from *apparent ridges* paper. I will look into it!
>
>We discussed our next step and how it fits in the project as a whole
>1. We will focus on extracting features recognizable by human eye
>>More can be done to make the feature line outputs cleaner (less noisy)
>2. Using results from 1., we will incorporate human evaluation (archaeological expertise) as a filter
>>The human eye can distinguish between tiny bumps on the ground from larger features with some geometric shape, such as a rectangular mound
>><br>But it takes archaeological expertise to tell whether this rectangular mound is of archaeological value
>><br>In short: if a human can tell a feature is not useful, it very likely is not
>><br>But if a human can tell a feature is useful, it takes an archaeology expert to know this feature has actual archaeology value
>
>We discussed ways to improve our current geometry-based methods:
>1. Professor Ju suggests I can identify 'strong features.' 
>>When we value the k value in feature line extraction, some features disappear, but some stay through a range of k values
>>Features lines of 'strong features' fall into the latter category
>>I can extract feature lines at different values of k, and visualize the 'strength' of different features
>
>We compared the feature line output against the radar image (see Comparison_230330.ipynb)
>>We found that features visible on the LiDAR scan (as indicated by feature lines) correspond to their indication on the radar datar
>><br>However, we need better geographical alignment of the radar data and the LiDAR scan
2. Tested CrestCODE on even smaller patch (<50k vertices)
>The algorithm took forever to run
><br>I will try again (leave computer running for a few hours) to see if I get any output
>>It's possible that lack of optimization is to blame
>><br>When I compile the code with 'make,' warnings indicate that some compilation levels are not supported (CrestCODE_warnings.ipynb)
3. Documented compilation warnings for CrestCODE
>File: CrestCODE_Warnings.ipynb

# 🟩More Details and History at: https://github.com/JasonLiu2024/GeometryProcessing_SP2023/blob/master/Open3D_Test/Log*.ipynb

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

