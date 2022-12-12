import random
abc = ["가위","바위","보"]
computer = random.choice(abc)
play = int(input("가위바위보를 할 준비가 됐으면 1번을 누르세요"))
if play==1:
  while True:
    player=int(input("가위바위보를 시작합니다. 가위바위보를 그만 두려면 2번을 누르세요"))
    if player=='가위':
      if computer == '가위':
        print('컴퓨터는 가위를 냈습니다')
        print('무승부')
      elif computer == '바위':
        print("컴퓨터는 바위을 냈습니다")
        print("패배")
      elif computer == '보':
        print("컴퓨터는 보를 냈습니다")
        print("승리")
        
      
      
    if player=='바위':
      if computer == '가위':
        print('컴퓨터는 가위를 냈습니다')
        print('승리')
      elif computer == '바위':
        print("컴퓨터는 바위을 냈습니다")
        print("무승부")
      elif computer == '보':
        print("컴퓨터는 보를 냈습니다")
        print("패배")
      
    if player=='보':
      if computer == '가위':
        print('컴퓨터는 가위를 냈습니다')
        print('패배')
      elif computer == '바위':
        print("컴퓨터는 바위을 냈습니다")
        print("승리")
      elif computer == '보':
        print("컴퓨터는 보를 냈습니다")
        print("무승부")
 
