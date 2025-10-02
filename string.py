def LvL1(st,m):
    if m == 'upper':
        return("uppered: "+st.upper())
    if m == 'lower':
        return("lowered: "+st.lower())
    if m == 'capitalize':
        return("capitalized: "+st.capitalize())

print(LvL1('прИвеТ_Мир!','upper'))
print(LvL1('прИвеТ_Мир!','lower'))
print(LvL1('прИвеТ_Мир!','capitalize'))

a = '12345'
try: 
    print(a.index('!'))
except Exception as e: 
    print(e.args)

def LvL2(st):
    return(st.count("о")+st.count("О"),st.replace("круто","awensome",1))


print(LvL2("Ботать-это_круто.Очень_круто!"))


def LvL3(st):
    return(st.split(','),"".join(st))
    

print(LvL3("1,2,3,4,5"))


def LvL4(st):
    print(st.strip())
    print(st.lstrip())
    print(st.rstrip())
    print('{0} {1}'.format(st,'999'))
    if st.isdigit():
        return(f"{st} - {st.isdigit()} number")
    if st.isalpha():
        return(f"{st} - {st.isalpha()} literal")

print(LvL4('    123    '))
print(LvL4('   asdfs   '))


boss = "__PyTHOn;is;AweSOMe"

def LvL5(st):
    st = st.replace(";"," ")
    st = st.lstrip("_")
    st = st.capitalize()
    return(st)
print(LvL5(boss))
