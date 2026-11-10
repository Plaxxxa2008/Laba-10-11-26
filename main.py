for i in range(67):
    for s in '67':
        print(s)
print('give me ten else i ll go to army')
a = int(input('Введи число и оно превратиться в 0'))
print(a-a)
def resheto(n):
    a=[1]*(n+1)
    a[0]=0
    a[1]=0
    st=2
    while st**2 <= n:
        if a[st]:

            for i in range(st * st, n + 1, st):
                            a[i] = 0
        st += 1
    for i in range(len(a)):
        if a[i]:
            print(i)
resheto(140)
print('ghp_vY7v8N9m0K1L2J3I4H5G6F7E8D9C0B1A2z3y')
