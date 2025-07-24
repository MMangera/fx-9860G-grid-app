# fx-9860G-grid-app
A grid app to make any screen in the fx-9860GIII calculator.
# Usage
## App
To run the app, run `gridapp.py`. For the first use, type `n` in response to `Load last save? (y/n)`. Click on the squares to light them up, signalling that they will be filled in on the final screen. Press `TAB` to erase pixels if you want to fix a mistake that you made earlier. `TAB` simply toggles the mode, which you can see in red at the bottom of the screen. Every 45 seconds it autosaves into `lastsave.txt` if the app force-stops, but when you press `SPACE` to exit it also autosaves. If you are not done simply type `y` as the answer to `Load last save? (y/n)` at the start. After you press `SPACE`, the program asks you if you want to split the answer into separate files for your fx-9860GIII calculator. If you have finished your screen and you do want this (as Python files on your calculator only accept up to 150 lines), type `y`; otherwise type `n`. If you typpe `y`, there will be a new folder in the directory called `APPANS`. Move this to your graphics calculator and you should be able to run it just fine.
## Tools
You might notice there is a file called `load_from_result.py`. If you run this, you can give the folder name and you can convert the `casioplot` Python file(s) into a load for the grid app. This is very useful if you want a permanent save.
