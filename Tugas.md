### Tugas 1 Publisher and Subscriber
#### Steps:
1. Buat program berisi ros node yang mengirimkan data 1 - 100 tiap 1 detik ke topic /tugas 
2. Tipe data yang dikirimkan adalah Int32
3. Buat program berisi ros node yang menerima data dari topic /tugas dan menampilkan data tersebut di layar.
4. Bilangan yang habis dibagi 5 ditampilkan dua kali di layar

**note:** 
```python
# untuk menjeda program selama 1 detik dapat menggunakan library time dan juga rospy.rate()
import time 

time.sleep(1) # menjeda program selama 1 detik

# atau
r = rospy.rate(1)
while True:
    # .
    # ..
    r.sleep() # menjeda program selama 1 detik

# untuk menghitung sisa bagi gunakan operator %
# contoh
a = 81
b = 9
print(a % b) # hasilnya 0
```


---
---




### Tugas 2 Service
#### Steps:
1. Buat srv dengan nama "tugas" yang berisi :
```
float64 panjang
float64 lebar
---
float64 luas
```
2. Buat program berisi ros node dengan nama "server" yang menerima data srv dengan nama "tugas" dan merespons dengan mengembalikan luas persegi panjang
3. Buat program berisi ros node dengan nama "client" yang mengirimkan data srv dengan nama "tugas" dan menampilkan luas persegi panjang di layar
4. panjang dan lebar boleh menggunakan random, boleh diinputkan melalui terminal, dan boleh di define di program

**note: jangan lupa edit CMakeLists.txt** 

---
---

### Tugas 3 Action 


---
---


#### Coba mandiri Publisher & Subscriber:
**Lengkapi code**

Publisher
```python
import rospy
import cv2 
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np


def send_image(img, pub):
    msg_frame = CvBridge().cv2_to_imgmsg(img, encoding="passthrough")
    # publish pesan dibawah
    ...

def on_shutdown():
    rospy.loginfo("Shutdown")
    cap.release()

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    
    # write the needed ROS Code here:
    # 1. Initialize the node
    # 2. Initialize the publisher named pub
    ...
    rospy.on_shutdown(on_shutdown)
    r = rospy.Rate(30)
    pub =  ...


    while not rospy.is_shutdown():
        ret, frame = cap.read()
        send_image(frame, pub)
        r.sleep()
    
```

subscriber
```python
import rospy
import cv2 
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np


def img_callback(data):
    # write the needed ROS Code here:
    # 1. Convert the image message to cv2 image 
    img = ...
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    

def on_shutdown():
    rospy.loginfo("Shutdown")
    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    
    # write the needed ROS Code here:
    # 1. Initialize the node
    # 2. Initialize the subscriber
    ...
    rospy.on_shutdown(on_shutdown)
    ...

    rospy.spin()
```
**tambahkan kedua program pada CMakelist.txt**
