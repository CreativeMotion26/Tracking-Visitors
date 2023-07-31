import cv2 
import cvlib as cv
from cvlib.object_detection import draw_bbox
from vidgear.gears import CamGear
import yt_dlp
import time
from datetime import datetime
import csv


stream = CamGear(source='https://www.youtube.com/watch?v=y15aodvVY6c', stream_mode= True, logging=True).start()
#stream = CamGear(source=0, stream_mode= False).start() # webcam

count=0
people_data = {}

data_collection_interval = 10
print_interval = 10 

last_data_collection_time = time.time()
last_print_time = time.time()


csv_file = 'data_log.csv'


while True:
    start_time = time.time()
    
    frame = stream.read()
    count += 1 

    if count % 9 != 0:
        continue
    #Optimal Frame Rate
    
     
    frame=cv2.resize(frame,(640,480)) # (1020, 600) low size=hi quailty
    bbox,label,conf =cv.detect_common_objects(frame, confidence=0.3)
    frame=draw_bbox(frame,bbox,label,conf)
    
    # Count people
    p=label.count('person')
   
    # store data with the current time as the key
    current_time = int(time.time())
    people_data[current_time] = p
    
    cv2.putText(frame, "Current People: "+str(p),(100,95),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),2)
    #cv2.putText(frame, "Visitor People: "+str(visitor_count),(100,135),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),2)
    cv2.imshow("FRAME",frame)
   
   
    if cv2.waitKey(1)&0xFF==27:            #This line waits for a key press for 1, will continue executing without waiting for key press
       break                         #0xFF is a hexadecimal value representing 255 in decimal. This operation extracts the least significant 8 bits
   
    
    if time.time() - last_data_collection_time >= data_collection_interval:
            last_data_collection_time = time.time()
        
            with open(csv_file, 'a', newline='') as file:
                writer = csv.writer(file)
                for epoch, people_count in people_data.items():
                    timestamp = datetime.fromtimestamp(epoch).strftime('%Y-%m-%d %H:%M:%S')
                    
                    print(f"Time: {timestamp}, People Count: {people_count}")
                    writer.writerow([timestamp,people_count]) 
            
            
        
   
    #clear the data for the next minute
    people_data={}
    
    if time.time() - last_print_time >= print_interval:
        last_print_time = time.time()
    
stream.stop() # stream.lease()
cv2.destroyAllWindows()




#   pip install cvlib 
#   pip install vidgear
#   pip install tensorflow
#   pip install opencv-python
