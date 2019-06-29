# Auto-level-Generator-for-Mario
Generate whole new levels for the Nintendo Mario 1985 game using text-based representation of levels in an LSTM network.

This project was implemented using the concepts provided by Adam Geitgey in his article. The link to the article is given below:

https://medium.com/@ageitgey/machine-learning-is-fun-part-2-a26a10b68df3

## Pre-requisites
This project was implemented using the following libraries in Python 3:
* PIL
* OpenCV 
* csv
* resize-image
* skimage
* Keras framework for tensorflow

## How to Generate a level (Step by Step Working)
All python scripts are located in the "scripts" folder. The original 32 levels from the 1985 Mario Bros. game are located in the "Original_Levels" folder.

#### Step 1
Set working directory to "Auto-level-Generator-for-Mario/scripts". Now select a level from one of the originals in order to generate a whole new level that follows the same building blocks as the original. To do that, run the lines.py file as shown below:

```shell
$ python lines.py mario-1-1.gif
```
This will draw a grid structure that outlines each of the individual building blocks used in that level. The edited level with grid outline is located in "Edited" folder. Name will be "mario-1-1-edited.gif".

![](https://github.com/jawad3838/Auto-level-Generator-for-Mario/blob/master/Edited/mario-1-1-edited.gif)

#### Step 2
The next thing you need are the unique images of blocks that make up the level as seen above. These images are located in the "level1specs" folder. Note that these blocks only work for levels that are made of these. For levels with different color schemes, you need to extract the unique blocks separately. The individual blocks for extracted thus far are shown below:

![](https://github.com/jawad3838/Auto-level-Generator-for-Mario/blob/master/Scripts/Blocks.PNG)

The characters under each block are the ones that will be used to represent these blocks in the text representation of each level.

#### Step 3
Now we need to convert the original level to text form. Each box in the grid representation of the level is of size 16x16. Structural Similarity index (SSIM) is used to compare a block from the original level with each of the blocks in "level1specs" folder. If SSIM is high enough then that block is assigned a character corresponding to the one it was compared with. Use the following script to convert the grid level from Edited folder to text form:

```shell
$ python imageToText.py mario-1-1-edited.gif
```

|Original Level|
|---|
|![Original-Level](https://github.com/jawad3838/Auto-level-Generator-for-Mario/blob/master/Edited/mario-1-1-edited.gif)|

|Text-form|
|---|
|![Text-form](https://github.com/jawad3838/Auto-level-Generator-for-Mario/blob/master/Scripts/Text-form.PNG)|

Two text files are generated simultaneously for each level. One contains the original representation (mario-1-1-edited.csv) of the level and it is stored in "levels_CSV" folder and the other one is transposed (rotated) and is stored in the "levels_transposed" folder (mario-1-1-edited_trans.txt). The rotated text representation of the level is used in the LSTM network.

#### Step 4
Generate new text based representation using LSTM network.

```shell
$ python model.py mario-1-1-edited_trans.txt
```
The new text generated level is stored in "levels_prediction_textfiles" folder by the name "mario-1-1-edited_trans_new.txt".

#### Step 5
Now we need to rotate the text-based level back to original form and convert it into an image. The following script is responsible to execute these steps:

```shell
$ python generate_level.py mario-1-1-edited_trans.txt
```
|New Text-based Level|
|---|
|![New-text](https://github.com/jawad3838/Auto-level-Generator-for-Mario/blob/master/Scripts/New_level_text.PNG)|

|Converted to image|
|---|
|![Converted-To-Image](https://github.com/jawad3838/Auto-level-Generator-for-Mario/blob/master/Generated_levels/mario-1-1-edited_trans.png)|

The new level and its corresponding text representation are stored in "Generated_levels" folder by the name "mario-1-1-edited_trans.png" and "mario-1-1-edited_trans_upRight.csv" respectively. 

The model hasn't been trained yet as of yet and random text generation during training process was used to create the new levels due to which the generated level looks a bit messy. 

Further work will include a trained model that can generate new levels that are just as challenging and better-looking as the originals.

## Credits
The credit goes to Adam Geitgey for his detailed article regarding this topic in medium. Link is given below:

https://medium.com/@ageitgey/machine-learning-is-fun-part-2-a26a10b68df3
