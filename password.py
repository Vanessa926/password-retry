password = 'a123456'
i = 0
while i < 3:
    user = input('請輸入密碼:') 
    if user == password:
        print('登入成功')
        break 
    else:
        number = 2 - i
        print('密碼錯誤！還有', number, '次機會')
        i = i + 1