s = "WSx74321!"

print(any(a.isalnum() for a in s))
print(any(a.isalpha() for a in s))
print(any(a.isdigit() for a in s))
print(any(a.islower() for a in s))
print(any(a.isupper() for a in s))


# str.isalnum()
# print 'ab123'.isalnum() True
# print 'ab123#'.isalnum() False

# str.isalpha()
# print 'abcD'.isalpha() True
# print 'abcd1'.isalpha() False

# str.isdigit()
# print '1234'.isdigit() True
# print '123edsd'.isdigit() False

# str.islower()
# print 'abcd123#'.islower() True
# print 'Abcd123#'.islower() False

# str.isupper()
# print 'ABCD123#'.isupper() True
# print 'Abcd123#'.isupper() False

# str.isspace()
# print ' '.isspace() True
# print ''.isspace() False

# str.istitle()
# "000".istitle() #False
# "John".istitle() #True
# "john".istitle() #False
# "CamelCase".istitle() #False
# "Camel Case".istitle() #True
