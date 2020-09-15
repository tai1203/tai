username = input('請輸入用戶名')
password = input('請輸入口令: ')

#會要求重複輸入一次
#import getpass
#password = getpass.getpass('請輸入口令: ')

if username == 'admin' and password == '123456' :
    print('身份驗證成功')
else:
    print('身份驗證失敗')