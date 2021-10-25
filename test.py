signed_integer = -100
  
# Adding 2^32 to convert signed to unsigned integer
unsigned_integer = signed_integer+2**32
print(unsigned_integer)
print(type(unsigned_integer))