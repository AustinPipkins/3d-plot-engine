# Three Dimensional Plotting Engine
The goal of this project is to create a three dimensional dot plot engine that would take an input file consisting of three dimensional coordinates (x, y, z) and output this data in a two dimenstional projection that can be rotated using isometric perspective. This is primarily to understand the mathematics of isometric projection and not an exercise of library usage. All of the linear algebra is handled by numpy and graphics UI is handled by graphics.py / pygame (originally done in grpahics.py to demonstrate that no third party plotting engine is used, only the two dimensional GUI elements are used). 

<br>
The controls (WASD) can manipulate two two-dimensional planes of rotation, the XY axis and the XZ axis. These two degrees of freedom allow for all angles to be visible. The controls (EQ) can manipulate the zoom, increasing or decreasing the size of the projection.

# Mathematical Approach
No research was conducted for this project. I knew that linear algebra would assist in speed, but aside from this, I knew nothing on how it is done traditionally. All of the equasions for this project are derived by hand. The approach that I took in the end consisted of drawing a "unit axis" (drawn vectors representing the x axis, y axis, and z axis all of size 1) with all input angles. The inputs (rotation for XY and XZ planes) are measured in radians. The XZ plane is allotted the range [pi/2, -pi/2] where a pi/2 rotation represents seeing the projection from the top looking down, and -pi/2 represents seeing the projection from the bottom looking up. The XY plane is allotted the range [0, 2*pi] where a rotation of 0 represents (when XZ is 0) the x axis pointing directly at the viewer, and the y axis pointing towards the right (0 and 2pi appear the same). I made a table of XZ/XY combinations (increments of pi/4) and drew what the coorisponding "unit axis" would appear as in two dimensional space. With this table, I made new tables showing the lengths of each axis in the i/j dimension (i/j representing the two dimensional output whereas the x/y/z notation represents the mathematical input coordinates). There are 6 of these tables: xi, xj, yi, yj, zi, zj. Each of these tables are structured in the same was as the "unit axis" table is formatted, but the values represent how long said axis is in the given i/j direction. A two input function is then derived for each of these tables. My values are as below:
<br><br>
xi = sin(XZ)cos(XY)<br>
xj = -sin(XY)<br>
yi = sin(XZ)sin(XY)<br>
yj = cos(XY)<br>
zi = -cos(XZ)<br>
zj = 0<br>
<br><br>
Placing the input data points into an nx3 matrix and multiplying said matrix by the translation matrix defined by a 3x2 matrix consisting of the values above (given some constant values for XZ and XY), we get our projection. Adding an nx2 matrix consisting of an offset of screen_width/2 and screen_height/2 will center this projection, letting (0, 0, 0) appear in the middle fo th screen. Changing the value of the nx2 matrix would allow for a pan operation, but that is not the goal of this project.

Multiplying all of the values of the 3x2 matrix by the screen size based on column stretches the image appropriately for the screen, and multiplying all values by a zoomfactor will influence the size of the output projection.

# Controls
W/S for rotating the XZ axis
A/D for roating the XY axis
E/Q for zooming in/out

# Purpose
The aim was to use this engine to visualize how the chord C major would appear. Since a two dimensional shape can be drawn via two frequencies (let the x position be defined by the first frequency, and the y position be defined by the second frequency), a chord consisting of three frequencies can be drawn in three dimensional space can be visualized with three input frequencies in three dimensional space (visualized by an isometric projection engine).

The result isn't as cool as I thought, but with hindsight, this result was predictable :P

The plot engine can also very easily visualize three dimensional mathematical functions. Lines can be drawn with a bit of a tweek. Every two points represents the start and end of a line.

# Demo

```bash
pip install -r requirements.txt
python old_dot_plot.py dot_data/simple_cube.data               
python old_dot_plot.py dot_data/c_major.data                   
python old_dot_plot.py dot_data/wave_function.data             
python old_line_plot.py line_data/simple_line_house.data       
python old_line_plot.py line_data/c_major.data                 
python new_dot_plot.py dot_data/simple_cube.data               
python new_dot_plot.py dot_data/c_major.data                   
python new_dot_plot.py dot_data/wave_function.data             
python new_line_plot.py line_data/simple_line_house.data       
python new_line_plot.py line_data/c_major.data       

```