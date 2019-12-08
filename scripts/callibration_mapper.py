import numpy as np

callibration_pixel_pts = np.array([[507,341],[57,361],[49,144],[503,129]])
physical_pts = np.array([[0.455,-0.494],[0.455,0.725],[1.064,0.725],[1.064,-0.494]])
num_pts = len(callibration_pixel_pts)


virtual_pts = np.zeros((num_pts,2))
err = np.zeros(num_pts)

for i in range(num_pts):
  p_ball_1 = np.array([callibration_pixel_pts[i][0],callibration_pixel_pts[i][1]])
  p_ball_2 = np.copy(p_ball_1)
  p_ball_3 = np.copy(p_ball_1)
  p_ball_4 = np.copy(p_ball_1)

  R = np.array([[0,1],[-1,0]])
  T = np.zeros((4,4))
  #average from one side
  p_ball_1[0] = -p_ball_1[0]
  p_ball_1 = np.matmul(R,p_ball_1)
  off_set_1 = callibration_pixel_pts[i]
  off_set_1[0] = -off_set_1[0]
  off_set_1 = np.matmul(R,off_set_1)

  p_ball_1 = p_ball_1 - off_set_1
  p_ball_1 = p_ball_1 * 0.0023
  p_ball_1 = p_ball_1 - physical_pts[0] 
  p_ball_1 = -p_ball_1

  #average from the side 2
  p_ball_2[0] = -p_ball_2[0]
  p_ball_2 = np.matmul(R,p_ball_2)
  off_set_2 = np.array([-361,-57])
  p_ball_2 = p_ball_2 + off_set_2
  p_ball_2 = p_ball_2 * 0.0023
  p_ball_2 = p_ball_2 - physical_pts[1]  
  p_ball_2 = -p_ball_2

  # #average from the side 3
  # p_ball_3[0] = -p_ball_3[0]
  # p_ball_3 = np.matmul(R,p_ball_3)
  # off_set_3 = np.array([-361,-57])
  # p_ball_2 = p_ball_2 + off_set_2
  # p_ball_2 = p_ball_2 * 0.0023
  # p_ball_2 = p_ball_2 - physical_pts[1]  
  # p_ball_2 = -p_ball_2

  print("averaged guy")
  averaged = (p_ball_1 + p_ball_2) * .5
  virtual_pts[i] = averaged
  print(averaged)
  err[i] = np.sqrt(np.square(virtual_pts[i][0]-physical_pts[i][0])+np.square(virtual_pts[i][1]-physical_pts[i][1]))

print(err)