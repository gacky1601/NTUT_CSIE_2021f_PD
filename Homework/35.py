def process(s):
    data=s.split('[')
    mux = int(''.join(filter(str.isdigit,data[-2])))
    back = s[:-len(data[-1])-len(str(mux))-1]+data[-1] * mux
    return back

s = input()
while '[' in s:
    position=s.find(']')
    print(position)
    s=process(s[:position])+s[position+1:]
print(s)