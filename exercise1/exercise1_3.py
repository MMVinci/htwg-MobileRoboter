from transformations import *
import numpy as np

# Exercise 2.2 from lecture
def exercise_22_a_t_oa():
    """
    :return: The homogenous transformation matrix T^O_A from Task 2.2.
    """
    theta_oa = np.radians(0)
    r_oa = rot(theta_oa)
    t_oa = trans((1, 1))
    print(t_oa)
    t_o_a = rot2trans(r_oa)
    t_o_a[:2, 2] = t_oa[:2, 2]
    print(t_o_a)
    return t_o_a


def exercise_22_a_t_ob():
    """
    :return: The homogenous transformation matrix T^O_B from Task 2.2.
    """
    theta_oa = np.radians(30)
    r_oa = rot(theta_oa)
    t_oa = trans((3, 2))
    print(t_oa)
    t_o_a = rot2trans(r_oa)
    t_o_a[:2, 2] = t_oa[:2, 2]
    print(t_o_a)
    return t_o_a


def exercise_22_b(pb):
    """
    Transforms the point P from coordinate system B to O.
    :param pb: The point P in coordinates with respect to B. P is not in homogenous representation.
    :return: P after the transformation. The result is not in homogenous representation.
    """
    t_o_b = exercise_22_a_t_ob()
    pb_hom = np.append(pb, 1)
    pa_hom = t_o_b @ pb_hom
    return pa_hom[:2]


def exercise_22_c_t_ab():
    """
    :return: The homogenous transformation matrix T^A_B calculated from T^O_A and T^O_B.
    """
    t_o_a = exercise_22_a_t_oa()
    t_o_b = exercise_22_a_t_ob()

    t_a_o = np.linalg.inv(t_o_a)

    t_a_b = t_a_o @ t_o_b
    return t_a_b


def exercise_22_d(pb):
    """
    Transforms the point P from coordinate system B to A.
    :param pb: The point P in coordinates with respect to B. P is not in homogenous representation.
    :return: P after the transformation. The result is not in homogenous representation.
    """
    t_a_b = exercise_22_c_t_ab()
    pb_hom = np.append(pb, 1)
    pa_hom = t_a_b @ pb_hom
    return pa_hom[:2]


def exercise_22_e(pa):
    """
    Performs the rotation of p^A with T^A_B.
    :param pa: The point P in coordinates with respect to B. P is not in homogenous representation.
    :return: P after the operation. The result is not in homogenous representation.
    """
    t_a_b = exercise_22_c_t_ab()
    pa_hom = np.append(pa, 1)
    pa_hom = t_a_b @ pa_hom
    return pa_hom[:2]
