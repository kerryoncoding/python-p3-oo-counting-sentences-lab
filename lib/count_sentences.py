#!/usr/bin/env python3

# class MyString:
#   def __init__(self, value = " "):
#       self.value = value

#   def get_value(self):
#       return self._value

#   def set_value(self, value):
#     if (type(value) == str):
#       self._value = value
#     else:
#       print("The value must be a string.") 

#   value = property(get_value, set_value)

#   def is_sentence(self):
#     if (self._value[-1] == "."):
#       return True
#     else:
#       return False

#   def is_question(self):
#     if (self._value[-1] == "?"):
#       return True
#     else:
#       return False
#   def is_exclamation(self):
#     if (self._value[-1] == "!"):
#       return True
#     else:
#       return False

#   def count_sentences(self):
#     value = self.value
#     for char in ["!", "?"]:
#       value = value.replace(char, ".")
#     sentences = [item for item in value.split(".") if item]
#     return len(sentences)
  
  
class MyString:
  def __init__(self, value = ""):
    self._value = value
    
  def get_value(self):
    return self._value

  def set_value(self, stringVal):
    if (type(stringVal) == str):
      self._value = stringVal
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)

  def is_sentence(self):
    return self._value.endswith(".")

  def is_question(self):
    return self._value.endswith("?")

  def is_exclamation(self):
    return self._value.endswith("!")

  def count_sentences(self):
    value = self.value
    for punc in ['!','?']:
        value = value.replace(punc, '.')
    
    sentences = [s for s in value.split('.') if s]
    
    return len(sentences)

