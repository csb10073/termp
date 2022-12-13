import cv2
import mediapipe as mp
from PIL import ImageFont,ImageDraw,Image
import numpy as np
import random
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
abc = ["가위","바위","보"]

cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("카메라를 찾을 수 없습니다.")
      continue
    image.flags.writeable = False 
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    image_height,image_width,_=image.shape
    
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
          thumb_finger_state = 0
          if hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y * image_height:
              if hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y * image_height:
                  if hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * image_height:
                      thumb_finger_state = 1
          index_finger_state = 0
          if hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y * image_height:
              if hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y * image_height:
                  if hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height:
                      index_finger_state = 1

          middle_finger_state = 0
          if hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y * image_height:
              if hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y * image_height:
                  if hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * image_height:
                      middle_finger_state = 1

          ring_finger_state = 0
          if hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y * image_height:
              if hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y * image_height:
                  if hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y * image_height:
                      ring_finger_state = 1

          pinky_finger_state = 0
          if hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y * image_height:
              if hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y * image_height:
                  if hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y * image_height > hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y * image_height:
                      pinky_finger_state = 1
                      
          font = ImageFont.truetype("fonts/gulim.ttc", 80)
          image = Image.fromarray(image)
          draw = ImageDraw.Draw(image)

       
          text = ""
          if thumb_finger_state == 1 and index_finger_state == 1 and middle_finger_state == 1 and ring_finger_state == 1 and pinky_finger_state == 1:
              text = "보"
              computer = random.choice(abc)
              if computer == "가위":
                print('컴퓨터는 가위를 냈습니다')
                print('패배')
                break
              elif computer == "보":
                print("컴퓨터는 보를 냈습니다.")
                print("무승부")
                break
              elif computer == "주먹":
                print("컴퓨터는 주먹을 냈습니다.")
                print("승리")
                break
          elif thumb_finger_state == 1 and index_finger_state == 1 and middle_finger_state == 0 and ring_finger_state == 0 and pinky_finger_state == 0:
              text = "가위"
              computer = random.choice(abc)
              if computer == "가위":
                print('컴퓨터는 가위를 냈습니다')
                print('무승부')
                break
              elif computer == "보":
                print("컴퓨터는 보를 냈습니다.")
                print("승리")
                break
              elif computer == "주먹":
                print("컴퓨터는 주먹을 냈습니다.")
                print("패배")
                break
          elif   index_finger_state == 0 and middle_finger_state == 0 and ring_finger_state == 0 and pinky_finger_state == 0:
              text = "주먹"
              computer = random.choice(abc)
              if computer == "가위":
                print('컴퓨터는 가위를 냈습니다')
                print('승리')
                break
              elif computer == "보":
                print("컴퓨터는 보를 냈습니다.")
                print("패배")
                break
              elif computer == "주먹":
                print("컴퓨터는 주먹을 냈습니다.")
                print("무승부")
                break

          w, h = font.getsize(text)
    
          x = 50
          y = 50    

          draw.rectangle((x, y, x + w, y + h), fill='black')
          draw.text((x, y),  text, font=font, fill=(255, 255, 255))
          image = np.array(image)


          mp_drawing.draw_landmarks(
              image,
              hand_landmarks,
              mp_hands.HAND_CONNECTIONS,
              mp_drawing_styles.get_default_hand_landmarks_style(),
              mp_drawing_styles.get_default_hand_connections_style())
             
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
