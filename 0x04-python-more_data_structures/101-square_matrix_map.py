#!/usr/bin/python3
def square_matrix_map(matrix=[]):
  """deletes keys with a specific value in a dictionary"""
    return (list(map(lambda x: list(map(lambda y: y**2, x)), matrix)))
