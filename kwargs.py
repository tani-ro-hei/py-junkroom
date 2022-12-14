# キーワード引数と引数のアンパックのお勉強

dic = dict(zip("abcde", "98765"))

if dic == {'a': '9', 'b': '8', 'c': '7', 'd': '6', 'e': '5'}:

    def disp_args1(*args, **kwargs):
        print(f"{type(args)}: {args=}")
        print(f"{type(kwargs)}: {kwargs=}")
        print('-' * 30)

    disp_args1(dic)
    ''' (args が タプル: (dic,) となる)
    <class 'tuple'>: args=({'a': '9', 'b': '8', 'c': '7', 'd': '6', 'e': '5'},)
    <class 'dict'>: kwargs={}
    '''

    disp_args1(*dic)
    ''' (args が タプル: tuple(dic.keys()) となる)
    <class 'tuple'>: args=('a', 'b', 'c', 'd', 'e')
    <class 'dict'>: kwargs={}
    '''

    disp_args1(**dic)
    ''' (kwargs が 辞書: dic となる)
    <class 'tuple'>: args=()
    <class 'dict'>: kwargs={'a': '9', 'b': '8', 'c': '7', 'd': '6', 'e': '5'}
    '''

    def disp_args2(hoge=None, a=None, b=None, *args, **kwargs):
        print(f"{hoge=}\n{a=}\n{b=}")
        print(f"{type(args)}: {args=}")
        print(f"{type(kwargs)}: {kwargs=}")
        print('-' * 30)

    disp_args2(dic)
    ''' (hoge が 辞書: dic となる)
    hoge={'a': '9', 'b': '8', 'c': '7', 'd': '6', 'e': '5'}
    a=None
    b=None
    <class 'tuple'>: args=()
    <class 'dict'>: kwargs={}
    '''

    disp_args2(*dic)
    ''' (hoge, a, b までキーが渡り、args が タプル: ('d', 'e') となる)
    hoge='a'
    a='b'
    b='c'
    <class 'tuple'>: args=('d', 'e')
    <class 'dict'>: kwargs={}
    '''

    disp_args2(**dic)
    ''' (a, b だけ値が渡り、kwargs が 辞書: {'c': '7', 'd': '6', 'e': '5'} となる)
    hoge=None
    a='9'
    b='8'
    <class 'tuple'>: args=()
    <class 'dict'>: kwargs={'c': '7', 'd': '6', 'e': '5'}
    '''
