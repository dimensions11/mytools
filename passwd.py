
def gen_password(length=8,num=(2,2,2,2)):
    """
    生成指定长度的密码，密码类型之和不能大于密码长度。
    :param length:  密码长度，整数： 10，默认8
    :param num:     密码类型，整数元组: (小写，大写，数字，特殊符号)，默认（2,2,2,2）
    :return:        生成的密码字符串
    """
    from random import choice, seed
    from datetime import datetime
    import string

    if length < 8:
        raise Exception("password length should not less than 8")

    tmp_all = sum(num)
    if tmp_all > length:
        raise Exception("num sum should not larger than length")

    data = [
        [string.ascii_lowercase,num[0]],
        [string.ascii_uppercase, num[1]],
        [string.digits, num[2]],
        [string.punctuation, num[3]],
    ]
    seed(int(datetime.now().timestamp()))
    pwd = []
    count = 0
    while count != length:
        method = choice(data)
        if method[1] > 0 :
            pwd.append(choice(method[0]))
            method[1] -= 1
            count += 1
        elif length >= tmp_all and count >= tmp_all:
            method = choice(data[:3])
            pwd.append(choice(method[0]))
            count += 1

    return ''.join(pwd)


def pwd_special_char_url_encode(pwd=''):
    """
    把密码中的特殊字符使用url转义，以用于各种网络相关配置中
    :param pwd: 密码字符串
    :return:    特殊字符url转义后的字符串
    """
    from urllib import parse

    # 密码分解为字典
    dd={}
    for k,v in enumerate(pwd):
        dd[k]=v

    # 使用urlencode将字典转义
    a = parse.urlencode(dd).encode()

    #处理字典转义后的字符串，初次分割，结果为字符串列表
    cc = a.split(b'&')

    # 处理字典转义后的字符串，再次分割，结果为列表的列表,子列表【位置，字符】
    ee = list( map(lambda x: x.split(b'='),cc) )
    #print(ee)

    # 处理字典转义后的字符串，列表转字典
    ee2={}
    for k,v in ee:
        ee2[int(k)]=v.decode()

    # 字典转最终列表
    result=[]
    for i in range(len(ee2)):
        result.append(ee2[i])

    # 合并转义后的最终列表并返回密码
    return ''.join(result)



if __name__ == "__main__":
    #print(genPassword(10,(3,3,3,1)))
    #print(genPassword(20,(3,3,3,11)))

    pwd = gen_password(8)
    print(pwd)
    result = pwd_special_char_url_encode(pwd)
    print(result)


