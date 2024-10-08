def print_params(a=1,b='строка',c=True):

    print(a,b,c)
print_params()
print_params(2,'nik')
print_params(2,b = 25,c = [1,2,3])

values_list=[2.5,'anton',8]
values_dict={'a':2,'b':'nik','c':True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [5,'клон']
print_params(*values_list_2)