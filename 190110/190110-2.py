'''
Problem2
관리자가 자료를 정리하다가 대소문자를 거꾸로 썼다고 한다.
당신에게 자료를 올바르게 고쳐달라고 한다.
대소문자를 바꿔서 출력하여 관리자에게 보여주면 된다.

예시)
data_err = "jAMES jUSTINE mARTINE mARY uNIX lINUX jAVA cOTLINE tOMAS sCRIPT mOONJAEIN"

결과)
James Justine Martine Mary Unix Linux Java Cotline Tomas Script Moonjaein
'''
data_err = "jAMES jUSTINE mARTINE mARY uNIX lINUX jAVA cOTLINE tOMAS sCRIPT mOONJAEIN"
data_change = data_err.swapcase()
print(data_change)
