from string import Template

message = 'World'
temp = Template('Hello $wld')
print(temp.substitute(wld=message))
