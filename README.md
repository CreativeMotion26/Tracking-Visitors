# 📈 Real-Time People Counting and Analysis

![Image](https://io.dropinblog.com/uploaded/blogs/34241363/files/featured/1-min_2.png)


This Python script allows you to count the number of people in a live video stream from a camera or a YouTube video URL. It uses the cvlib library for object detection, vidgear for video streaming, and matplotlib for real-time data analysis and graph plotting.

## Requirements

Before running the script, make sure you have the following Python packages installed:

  * cvlib
  * vidgear
  * matplotlib
  * csv
  * datetime

You can install these packages using pip with the following commands:

      
      pip install cvlib
      pip install vidgear
      pip install matplotlib
##

### People Counting and Data Logging

The script starts by initializing the video stream from a YouTube video URL. If you want to use a webcam, you can comment the YouTube URL line and uncomment the webcam source line.

The script then continuously reads frames from the video stream, detects people in the frames, and counts the number of people present. It performs the people counting every ninth frame to achieve an optimal frame rate.

The script keeps track of the people count at regular intervals (data_collection_interval) and logs this data along with timestamps into a CSV file (data_log.csv).
##
### Real-Time People Count Analysis

To visualize the people count data over time, you can use the second script provided. This script reads the data logged in the CSV file and plots a real-time graph using matplotlib and FuncAnimation.

To analyze the data, you need to run the first script first to collect the data and log it into data_log.csv. Then, you can run the second script to see the live graph showing the people count over time.

Please note that both scripts need to be run separately. The first script performs the live people counting and data logging, while the second script creates the real-time graph based on the logged data.

Make sure to adjust the data_collection_interval and print_interval variables in the first script to suit your data collection and printing needs. You can also customize the appearance of the graph in the second script by modifying the update_graph function.

##

**Important**: Ensure you have a stable internet connection when running the first script with a YouTube video URL as the video source. Also, make sure to comply with YouTube's terms of service when using their videos as a data source.

🕺 Happy People Counting and Real-Time Analysis!

##

## 💙 If you like this project, give it a ⭐️ and share it with friends!


### <a href="https://github.com/CreativeMotion26?tab=repositories">🔥 Do more fun projects!</a>
