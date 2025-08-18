from math import *
import random



landmarks  = [[20.0, 20.0], [80.0, 80.0], [20.0, 80.0], [80.0, 20.0]]
world_size = 100.0


class robot:
    def __init__(self, length = 20.0, bounded = False):
        self.x = random.random() * world_size # initial x coord
        self.y = random.random() * world_size # initial y coord
        self.orientation = random.random() * 2.0 * pi # initial heading
        self.length = length                          # length of robot
        self.forward_noise  = 0.0                     # error terms
        self.turn_noise     = 0.0                     # ...
        self.sense_noise    = 0.0                     # ...
        self.bearing_noise  = 0.0
        self.steering_noise = 0.0
        self.distance_noise = 0.0
        self.bounded = bounded
    
    def set(self, new_x, new_y, new_orientation):
        if self.bounded:
            if new_x < 0 or new_x >= world_size:
                raise ValueError, 'X coordinate out of bounds'
            if new_y < 0 or new_y >= world_size:
                raise ValueError, 'Y coordinate out of bounds'
        if new_orientation < 0 or new_orientation >= 2 * pi:
            raise ValueError, 'Orientation must be in [0, 2pi]'
        self.x = float(new_x)
        self.y = float(new_y)
        self.orientation = float(new_orientation)
    
    
    def set_noise(self,
                  new_b_noise  = 0.0,
                  new_st_noise = 0.0,
                  new_d_noise  = 0.0,
                  new_f_noise  = 0.0,
                  new_t_noise  = 0.0,
                  new_sn_noise = 0.0):

        self.forward_noise  = float(new_f_noise)
        self.turn_noise     = float(new_t_noise)
        self.sense_noise    = float(new_sn_noise)
        self.bearing_noise  = float(new_b_noise)
        self.steering_noise = float(new_st_noise)
        self.distance_noise = float(new_d_noise)
    
    def sense(self):
        '''
        Return the distance to each of the landmarks
        '''
        Z = []
        for i in range(len(landmarks)):
            dist = sqrt((self.x - landmarks[i][0]) ** 2 +
                        (self.y - landmarks[i][1]) ** 2)
            dist += random.gauss(0.0, self.sense_noise)
            Z.append(dist)
        return Z

    def sense_bearing(self, add_noise = 1):
        '''
        Unlike sense() above, this function returns the angle (in rad) between
        the robot and each of the landmarks
        '''
        Z = []

        for L in landmarks:
            bearing = atan2(L[0] - self.y, L[1] - self.x) - self.orientation

            if add_noise:
                bearing += random.gauss(0.0, self.bearing_noise)

            bearing %= (2.0 * pi)
            Z.append(bearing)

        return Z
    
    
    def move(self, turn, forward):
        '''Turns (in place) first, then moves'''
        if forward < 0:
            raise ValueError, 'Robot cant move backwards'         
        
        # turn, and add randomness to the turning command
        orientation = (self.orientation +
                       float(turn) +
                       random.gauss(0.0, self.turn_noise))
        orientation %= 2 * pi
        
        # move, and add randomness to the motion command
        dist = float(forward) + random.gauss(0.0, self.forward_noise)
        x = self.x + (cos(orientation) * dist)
        y = self.y + (sin(orientation) * dist)
        x %= world_size    # cyclic truncate
        y %= world_size
        
        # set particle
        res = robot()
        res.set(x, y, orientation)
        res.set_noise(self.bearing_noise,
                      self.steering_noise,
                      self.distance_noise,
                      self.forward_noise,
                      self.turn_noise,
                      self.sense_noise)
        return res


    def move_circular(self, motion, min_turn_threshold = 0.001):
        ''' 
        Unlike the move() function above, which is: 'rotate in place; move in
        a straight line', this move assumes movement with the wheels fixed at
        a given steering angle (alpha).

        @params
        motion: array: [steering_angle, distance]

        @return: a robot object with new [x, y, heading]
        '''
        alpha, d = motion
        # Add noise
        alpha += random.gauss(0., self.steering_noise)
        d += random.gauss(0., self.distance_noise)
        
        # turning angle:
        beta = (d / self.length) * tan(alpha)

        # if |beta| < min_turn_threshold, treat as straight line motion
        if abs(beta) >= min_turn_threshold:
            R = d / beta # turn radius
        else:
            R = 0

        # Center of turn radius
        cx = self.x - R * sin(self.orientation)
        cy = self.y + R * cos(self.orientation)

        # Update robot (x, y)
        if abs(beta) >= min_turn_threshold:
            x = cx + R * sin(self.orientation + beta)
            y = cy - R * cos(self.orientation + beta)
        else:
            x = self.x + d * cos(self.orientation)
            y = self.y + d * sin(self.orientation)

        # Update robot heading
        theta = (self.orientation + beta) % (2 * pi)

        result = robot()
        result.set(x, y, theta)
        result.set_noise(self.bearing_noise,
                         self.steering_noise,
                         self.distance_noise,
                         self.forward_noise,
                         self.turn_noise,
                         self.sense_noise)
        
        return result
            
    def Gaussian(self, mu, sigma, x):
        # calculates the probability of x for 1-dim Gaussian with mean mu and
        # var. sigma
        return (exp(-((mu - x) ** 2) / (sigma ** 2) / 2.0) /
                sqrt(2.0 * pi * (sigma ** 2)))
    
    
    def measurement_prob1(self, measurement):
        # calculates how likely a measurement should be
        prob = 1.0;
        for i in range(len(landmarks)):
            dist = (sqrt((self.x - landmarks[i][0]) ** 2 +
                         (self.y - landmarks[i][1]) ** 2))
            prob *= self.Gaussian(dist, self.sense_noise, measurement[i])
        return prob
    
    
    def measurement_prob(self, measurements):
        predicted_measurements = self.sense_bearing(0)

        # compute errors
        error = 1.0
        for i in range(len(measurements)):
            error_bearing = abs(measurements[i] - predicted_measurements[i])
            error_bearing = (error_bearing + pi) % (2.0 * pi) - pi
            error *= (exp(-(error_bearing ** 2) / (self.bearing_noise ** 2) /
                           2.0) /
                       sqrt(2.0 * pi * (self.bearing_noise ** 2)))

        return error
    
        
    def __repr__(self):
        return ('[x=%.6s y=%.6s orient=%.6s]'
                % (str(self.x), str(self.y), str(self.orientation)))



def eval(r, p):
    sum = 0.0;
    for i in range(len(p)): # calculate mean error
        dx = (p[i].x - r.x + (world_size/2.0)) % world_size - (world_size/2.0)
        dy = (p[i].y - r.y + (world_size/2.0)) % world_size - (world_size/2.0)
        err = sqrt(dx * dx + dy * dy)
        sum += err
    return sum / float(len(p))


