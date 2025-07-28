def reverse(st):
    st = st.split()
    st2 = ""
    for wordNumber in range(len(st) - 1, -1, -1):
        if st2 != "":
            st2 += f' {st[wordNumber]}'
        else:
            st2 = st[wordNumber]
    return st2