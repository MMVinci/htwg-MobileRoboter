from exercise1.transformations import *
import numpy as np

def exercise_21_a_t_ab():
    """
    :return: The 3D transformation matrix T^A_B from task 2.1.
    """
    theta_ab = np.radians(180)
    r_ab = rotz(theta_ab)
    t_ab = trans((-2, 0, 0))
    t_a_b = rot2trans(r_ab)
    t_a_b[:3, 3] = t_ab[:3, 3]  # Setze die Translation in die Transformationsmatrix
    return t_a_b


def exercise_21_a_t_bc():
    """
    :return: The 3D transformation matrix T^B_C from task 2.1.
    """
    theta_bc = np.radians(270)
    r_bc = rotz(theta_bc)
    t_bc = trans((-4, -1, 0))
    t_b_c = rot2trans(r_bc)
    t_b_c[:3, 3] = t_bc[:3, 3]
    return t_b_c


def exercise_21_a_t_ac():
    """
    :return: The 3D transformation matrix T^A_C from task 2.1.
    """
    theta_ac = np.radians(90)
    r_ac = rotz(theta_ac)
    t_ac = trans((2, 1, 0))
    t_a_c = rot2trans(r_ac)
    t_a_c[:3, 3] = t_ac[:3, 3]
    return t_a_c


def exercise_21_b_t_ac():
    """
    :return: The 3D transformation matrix T^A_C calculated from T^A_B and T^B_C.
    """
    return exercise_21_a_t_ab() @ exercise_21_a_t_bc()


def exercise_21_c_t_ca():
    """
    :return: The 3D transformation matrix T^C_A calculated from the inverse of T^A_C.
    """
    t_a_c = exercise_21_a_t_ac()
    t_c_a = np.linalg.inv(t_a_c)  # Berechne die Inverse von T^A_C
    return t_c_a


def exercise_21_d(pb):
    """
    Transforms the point P from coordinate system B to A in 3D.
    :param pb: The point P in coordinates with respect to B. P is not in homogenous representation.
    :return: P after the transformation. The result is not in homogenous representation.
    """
    t_a_b = exercise_21_a_t_ab()
    pb_hom = np.append(pb, 1)
    pa_hom = t_a_b @ pb_hom
    return pa_hom[:3]