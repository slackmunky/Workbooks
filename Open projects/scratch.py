class NoCustomAttributes:
  pass

attributeless = NoCustomAttributes()

try:
  attributeless.fake_attribute
except AttributeError:
  print("This text gets printed!")

attributeless.fake_attribute = "Not attributeless anymore."
print(attributeless.fake_attribute)
