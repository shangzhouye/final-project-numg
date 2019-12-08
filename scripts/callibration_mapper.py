import numpy as np

callibration_pixel_pts = np.array([[507,341],[57,361],[49,144],[503,129]])
to_use = np.copy(callibration_pixel_pts)
physical_pts = np.array([[0.455,-0.494],[0.455,0.725],[1.064,0.725],[1.064,-0.494]])
num_pts = len(callibration_pixel_pts)


virtual_pts = np.zeros((num_pts,2))
err = np.zeros(num_pts)

def callibration(x_pix,y_pix,its):
  print("Running")
  p_balls = np.zeros((num_pts,2))
  R = np.array([[0,1],[-1,0]])
  for i in range(num_pts):
    p_balls[i] = np.copy([x_pix,y_pix])
    # print(p_balls)
    p_balls[i][0] = - p_balls[i][0]

    p_balls[i] = np.matmul(R,p_balls[i])
    #here's where the unique per callubration point stuff start
    off_set = callibration_pixel_pts[i]
    off_set[0] = -off_set[0]
    off_set = np.matmul(R,off_set)
    p_balls[i] = p_balls[i] - off_set
    p_balls[i] = p_balls[i] * 0.0023
    p_balls[i] = p_balls[i] - physical_pts[i]
    p_balls[i] = -p_balls[i]

  x_phys = np.average(p_balls[:,0])
  y_phys = np.average(p_balls[:,1])
  x_actual = physical_pts[its][0]
  y_actual = physical_pts[its][1]
  # print("from pix: {}, {}\ngot phys: {}, {}\nreal phys:{}, {}".format(x_pix,y_pix,x_phys,y_phys,x_actual,y_actual))

  err = np.sqrt(np.square(x_phys-x_actual)+np.square(y_phys-y_actual))
  return x_phys,y_phys,err

if __name__ == '__main__':
  for i in range(num_pts):
    x = to_use[i][0]
    y = to_use[i][1]
    print((x,y))
    phys_guess_x,phys_guess_x,err = callibration(x,y,i)
    print(err)