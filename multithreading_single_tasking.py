from threading import Thread   
from time import sleep
class myThread:
  def solve_ques(sefl): 
    sefl.q1()
    sefl.q2()
    sefl.q3() 

  def q1(self): 
        print("Solved Question 1") 
        sleep(3) 
  def q2(self): 
      print("Solved Question 2") 
      sleep(3)  
  def q3(self): 
      print("Solved Question 3") 
      sleep(3)
myt = myThread() 
t = Thread(target=myt.solve_ques) 
t.start() 

