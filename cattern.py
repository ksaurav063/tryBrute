li1= ['___AAAA___','__BBBBB___','___CCCCc__','__DDDDD___','__EEEEEE__','__FFFFFF__','___GGGGG__','_HH____HH_','__IIIIII__','__JJJJJJ__','_KK___KK__','__LL______','_M______M_','__N____N__','___OOOO___','__PPPPPP__','___QQQQ___','__RRRRRR__','___SSSSS__','__TTTTTT__','_UU____UU_','_VV____VV_','_WW____WW_','_XX____XX_','_YY____YY_','__ZZZZZZ__']
li2= ['__AA__AA__','__BB__BB__','__CC______','__D____D__','__EE______','__FF______','__G_______','_HH____HH_','____II____','____JJ____','_KK__kK___','__LL______','_M_M__M_M_','__NN___N__','__OO__OO__','__PP___PP_','_QQ____QQ_','__RR___RR_','__SS______','____TT____','_UU____UU_','_VV____VV_','_WW____WW_','__XX__XX__','__YY__YY__','_____ZZ___']
li3= ['__AAAAAA__','__BbbbB___','_CC_______','__D_____D_','__EEEEE___','__FFFFF___','_G___GGGG_','_HHHHHHHH_','____II____','____JJ____','_KKKK_____','__LL______','_M__MM__M_','__N_N__N__','_OO____OO_','__PPPPP___','-QQ_QQ_QQ_','__RRRRR___','___SSSS___','____TT____','_UU____UU_','__VV__VV__','_WW_WW_WW_','____XX____','____YY____','____ZZ____']
li4= ['__AA__AA__','__BB__BB__','__Cc______','__D____D__','__EE______','__FF______','__G____GG_','_HH____HH_','____II____','_J__JJ____','_KK__KK___','__LL______','_M______M_','__N__N_N__','__OO__OO__','__PP______','___QQQQ___','__RR__RR__','______SS__','____TT____','_UU____UU_','___V__V___','_WWW__WWW_','__XX__XX__','____YY____','___ZZ_____']
li5= ['__AA__AA__','__BBBBB___','___CCCCC__','__DDDDD___','__EEEEEE__','__FF______','___GGGGGG_','_HH____HH_','__IIIIII__','__JJJJ____','_KK___KK__','__LLLLLL__','_M______M_','__N___NN__','___OOOO___','__PP______','_______QQ_','__RR___RR_','__SSSSS___','____TT____','__UUUUUU__','____VV____','_WW____WW_','_XX____XX_','____YY____','__ZZZZZZ__']

def cattrn(word):
    lis1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    k = len(word)
    for c in word:
        c = c.upper()
        for i,v in enumerate(lis1):
            if v == c:
                print(li1[i])
                print(li2[i])
                print(li3[i])
                print(li4[i])
                print(li5[i])
                print('\n')
                
            
cattrn('tryBrute')
