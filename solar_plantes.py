import cv2;

img = cv2.imread('solar-system.jpg') 

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Mercury",
            (110,220),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Venus",
            (190,220),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Earth",
            (280,220),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,0)
            )

cv2.putText(img,
            "Mars",
            (380,220),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Jupiter",
            (500,220),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,0)
            )

cv2.putText(img,
            "Saturn",
            (780,220),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Uranus",
            (970,220),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Neptune",
            (1110,220),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.imshow("output",img)

cv2.waitKey(0)

cv2.imwrite("solar_systemwithname.jpg",img)