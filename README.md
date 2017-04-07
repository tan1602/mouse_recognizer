# mouse_recognizer

# This is a haar classifier to recognize computer mouse from only one angle , image of mouse is also provided to check the position of mouse

# Content
   - folder:-
         - info
         - data
         - negetives
   - files:-
         - bg.txt
         - positives.vec
         - mouse_detect.py
         
# info:-
   - This folder contain data and sample files so created using negetive images and one learning inage.#
# data:-
   - This folder contain xml files for differnt stage of training and one main file cascade which will use in sccript
# negetives:-
   - This folder contain so many image which are not of mouse used to train background for detection
# bg.txt:-
   - This file contain path for all negetive images to used in training the cascade . bg stands for background
# positives.vec:-
   - This file is also another parameter for training cascade.
# mouse_detect.py:-
   - This is a python script to detect mouse. Run it put mouse infront of screen as given on image of mouse provided and it will detect.
