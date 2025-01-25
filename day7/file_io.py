#file input and output are here in this code io---input output
#alll thing are just file

# open read close

f=open("/workspaces/python/day6/function_recurssion.py","r")
data=f.read()
print(data)
print(type(data))
f.close()
del data
