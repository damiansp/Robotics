import numpy as np


def matrix_exp6(se3mat):
    '''Computes the matrix exponential of an se3 representation of exponential
    coordinates
    Params:
    - se3mat: matrix in se3
    Returns: the matrix eponential of se3mat
    '''
    se3mat = np.array(se3mat)
    se3mat_3 = se3mat[:3, :3]
    omg_theta = so3_to_vec(se3mat_3)
    if near_zero(np.linalg.norm(omg_theta)):
        return np.r_[np.c_[np.eye(3), se3mat[:3, 3]], [[0, 0, 0, 1]]]
    theta = axis_ang3(omg_theta)[1]
    omg_mat = se3mat_3 / theta
    return np.r_[
        np.c_[
            matrix_exp3(se3mat_3),
            np.dot(
                (np.eye(3)*theta
                 + (1 - np.cos(theta))*omg_mat
                 + (theta - np.sin(theta))*np.dot(omg_mat, omg_mat)),
                se3mat[:3, 3]
            ) / theta],
        [[0, 0, 0, 1]]]


def so3_to_vec(so3mat):
    '''Converts an so(3) representation to a 3-vector
    Params:
    - so3mat: a 3x3 skew-symmetric matrix
    Returns: The 3-vector corresponding to so3mat
    '''
    return np.array([so3mat[2][1], so3mat[0][2], so3mat[1][0]])


def near_zero(z, tolerance=1e-6) -> bool:
    '''Determines whether a scalar is small enough to be treated as zero
    Params:
    - z: scalar to check
    - tolerance: max allowable delta from 0
    Returns: True if delta from 0 < tolerance
    '''
    return abs(z) < tolerance


def axis_ang3(expc3):
    '''Converts a 3-vector of exponential coords for rotation into axis-angle
    form
    Params:
    - expc3: A 3-vector of exponential coords for rotation
    Returns:
    - omg_hat: A unit rotation axis
    - theta: Corresponding rotation angle
    '''
    return (normailize(expc3), np.linalg.norm(expc3))


def matrix_exp3(so3mat):
    pass
