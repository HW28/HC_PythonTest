# Import the modules
from pathlib import Path
from datetime import datetime
import time
from textwrap import wrap
from functions import *

data_folder = Path("in/")
file_to_open = data_folder/"Python_exercise1.xlsx"
data = obtain_excel_data(file_to_open, "data_table")

for i in range(0, len(data)):

    msg = data.at[i, 'post_text']
    t = datetime.now()
    next_date = str(data.at[i, 'post_datetime'])
    date_str, hour_str = next_date.split(" ")
    year, month, day = date_str.split("-")
    hour, m, sec = hour_str.split(":")
    next_t = datetime(int(year), int(month), int(day), int(hour), int(m), int(sec))
    if next_t > datetime.now():
        delta_t = next_t - datetime.now()
        time.sleep(delta_t.seconds+1)
        print(datetime.now())
        if len(msg) > 200:
            img = data.at[i, 'post_img']
            chunk_size = 200 - 7
            msgs = wrap(msg, chunk_size)
            if not ('nan' in str(data.at[i, 'post_img'])):
                for j, m in enumerate(msgs):
                    index = " Part " + str(j + 1)
                    text = str(m) + str(index)
                    tweet_image(img, text, i)
            else:
                for j, m in enumerate(msgs):
                    index = " Part " + str(j + 1)
                    text = str(m) + str(index)

                    print("Warning!!! Tweet with ID." + str(i + 1) + " Unable to download image")
                    tweet_woimage(text)
        else:
            if not ('nan' in str(data.at[i, 'post_img'])):
                tweet_image(data.at[i, 'post_img'], data.at[i, 'post_text'], i)

            else:
                print("Warning!!! Tweet with ID."+str(i+1)+" Unable to download image")
                tweet_woimage(data.at[i, 'post_text'])
        print("Info:  Tweet with ID." + str(i+1) + " Sent")

    else:
        print("Error!!! Tweet with ID." + str(i+1) + ". It wasn't sent!!!")
        print("Time Pass Out "+str(next_t))
