import numpy as np
from initialization import * 
import math

from controller import Display,Robot



def is_on_M_line(x_current, y_current, x0, y0,m,n,threshold=0.05):
    goal_point_X=m
    goal_point_Y=n
    
    
    
       
    if x0 - goal_point_X != 0:
        dist = abs(y_current - ((x_current - x0) * (y0 - goal_point_Y) / (x0 - goal_point_X) + y0))
        return dist < 1
    else:
        dist = abs(x_current - goal_point_X)
        return dist < threshold
    
     
def align_to_M(heading, theta, turn_left=False):
    threshold = 5
    ts = 3  # turning speed
    if turn_left:
        ts *= -1  # turn left
    if abs(heading - theta%360) < threshold:
        return True
    else:
        update_motor_speed(input_omega=[ts, ts, ts])
        return False
        
def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def calculate_theta(x1, y1, x0, y0):
    if x1 == x0:
        return 180
    else:
        return math.degrees(math.atan((y1-y0) / (x1-x0))%360)+90      

def check_in_visited(gps_valuesX, gps_postitionY , visited_points):
    for point in visited_points:
        dist = math.sqrt((gps_valuesX-point[0])**2 + (gps_postitionY-point[1])**2)
        if dist < 0.5:
        #if(calculate_euclidean_distance(gps_valuesX, gps_postitionY, point[0], point[1])<0.5):
            return True
    return False
            
def point_ahead(a,b,x,y):
    goal_point_X = x
    goal_point_Y = y
    
    TIME_STEP = 32
    robot = init_robot(time_step=TIME_STEP)
    init_robot_state(in_pos=[0,0,0],in_omega=[0,0,0]) 
    prev = ""
    
    start_position=a,b
    goal_postition =x,y
    
    state = 'start'
    robot_speed = 8
    forward_left_speeds = [-1*robot_speed, -1*robot_speed, 2*robot_speed]
    far_from_wall_counter = 0
    close_to_wall_counter = 0
    x0, y0 = start_position
    step_back_counter = 0
    visited_points=[]
    while robot.step(TIME_STEP) != -1:
        gps_values,compass_val,sonar_value,encoder_value,ir_value = read_sensors_values()
        front_ir_values = ir_value[0], ir_value[3]
        right_ir_values = ir_value[2], ir_value[5]
        left_ir_values = ir_value[1], ir_value[4]
        left_sonar = sonar_value[2]
        right_sonar = sonar_value[0]
        front_sonar = sonar_value[1]
        print(state)
        update_robot_state()       
        # DEFINE STATE MACHINE HERE!
               
        if state == 'start':
            distance_threshold = 0.0001
            if(is_on_M_line(gps_values[0], gps_values[1], x0, y0,x,y)):
                prev = state
                state = 'align_robot_heading'
                print(state)
                
        elif state == 'align_robot_heading':
            theta = calculate_theta(goal_postition[0], goal_postition[1], x0, y0)
            is_aligned = align_to_M(get_bearing_in_degrees(compass_val), theta=theta)
            print(theta)
            if is_aligned:
                prev = state
                state = 'move_to_goal'
                print(state)
        
                
        elif state == 'move_to_goal':
            update_motor_speed(input_omega=[-1*robot_speed, robot_speed, 0])
            difference = abs(front_ir_values[1] - front_ir_values[0])
            if (front_ir_values[0] + front_ir_values[1]) / 2 < 1000:
                prev = state
                state = 'wall_following'
                print(state)
                
            elif(calculate_euclidean_distance(gps_values[0], gps_values[1], goal_postition[0], goal_postition[1])< 0.5):
                state = 'end'
                print(state)
                        
        elif state == 'end':
            print(state)
            is_aligned = align_to_M(get_bearing_in_degrees(compass_val), theta=90)
            if is_aligned:
                update_motor_speed(input_omega=[0, 0, 0]) #end
            return print("srthstrh ")
                          
        elif(calculate_euclidean_distance(gps_values[0], gps_values[1], goal_postition[0], goal_postition[1])< 0.5):
            state = 'end'
            print(state)
            update_motor_speed(input_omega=[0, 0, 0])
            return "srtggae "
        
    
lst =[(-18, -14), (-14, -10), (-14, -6), (-10, -2), (-10, 2), (-10, 6), (-6, 10), (-2, 10), (2, 6)]    
# for i in range(len(lst)-1):
    # a =lst[i][0] 
    # b =lst[i][1]
    # x =lst[i+1][0]
    # y =lst[i+1][1]
    # abcd=point_ahead(a,b,x,y)
sgbs=point_ahead(-18,-14,-14,-10)
print("adfg")
sergf=point_ahead(-14,-10,-14,-6)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    