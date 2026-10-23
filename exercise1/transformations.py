# Funktionen zur Berechnung von Koordinatentransformationen in 2D und 3D
#
# M. Blaich; 13.10.2023;

import numpy as np


def rot(theta):
    """
    Liefert eine 2D-Rotationsmatrix mit Drehwinkel theta zurück.
    """
    return np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])

def rotx(theta):
    """
    Liefert eine elementare 3D-Rotationsmatrix mit Drehwinkel theta um die Drehachse x zurück.
    """
    return np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
    ])

def roty(theta):
    """
    Liefert eine elementare 3D-Rotationsmatrix mit Drehwinkel theta um die Drehachse y zurück.
    """
    return np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])

def rotz(theta):
    """
    Liefert eine elementare 3D-Rotationsmatrix mit Drehwinkel theta um die Drehachse z zurück.
    """
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

def rot2trans(r):
    """
    Wandelt die Rotationsmatrix r in eine homogene Transformationsmatrix um und liefert diese zurück.
    Erwartet eine 2x2 oder 3x3 Rotationsmatrix.
    """
    dim = r.shape[0]
    if dim == 2:
        t = np.eye(3)
        t[:2, :2] = r
    elif dim == 3:
        t = np.eye(4)
        t[:3, :3] = r
    else:
        raise ValueError("Eingabematrix muss 2x2 oder 3x3 sein.")
    return t

def trans(t):
    """
    Liefert eine homogene Translationsmatrix mit Translation t zurück.
    t ist ein Tupel der Größe 2 (für 2D) oder 3 (für 3D).
    """
    dim = len(t)
    if dim == 2:
        t_matrix = np.eye(3)
        t_matrix[:2, 2] = t
    elif dim == 3:
        t_matrix = np.eye(4)
        t_matrix[:3, 3] = t
    else:
        raise ValueError("Eingabe-Tupel muss Größe 2 oder 3 haben.")
    return t_matrix
