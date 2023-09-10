#!/usr/bin/env python3

class MyString:
  def __init__(self, value = "this"):
    self.value = value

  def get_value(self):
    return self._value

  def set_value(self, value):
    if (type(value) == str):
      self._value = value
    else:
      print("The value must be a string.") 

  def is_sentence(self):
    if (self._value[-1] == "."):
      return True
    else:
      return False

  def is_question(self):
    if (self._value[-1] == "?"):
      return True
    else:
      return False
  
  def is_exclamation(self):
    if (self._value[-1] == "!"):
      return True
    else:
      return False

  value = property(get_value, set_value)

