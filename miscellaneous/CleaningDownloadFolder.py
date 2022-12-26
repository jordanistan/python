# One of the messiest things in this world is the download folder of a developer. When writing a blog, working on a project, something similar we just download images and save them with ugly and funny names like asdfg.jpg.

# This python script will clean your download folder by renaming and deleting certain files based on some condition.

# Libraries:- OS

import os
folder_location = '~\\Downloads\\demo'

os.chdir(folder_location)
list_of_files = os.listdir()

## Selecting All Images
images = [content for content in list_of_files if content.endswith(('.png','.jpg','.jpeg'))] 

for index, image in  enumerate(images):
    os.rename(image,f'{index}.png')


## Deleting All Images
################## Write Your Script Here ######## Try To Create Your Own Code 