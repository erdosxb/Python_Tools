from MyQR import myqr

#图片及素材都在当前目录下
#图片二维码
# myqr.run(
#         words='https://www.baidu.com',
#         picture='Sources/shiyanlouLogo.png',
#         colorized=True,
#         save_name='artistic.png',
#         )

#原始二维码
#myqr.run('https://www.baidu.com/')

#动图二维码
myqr.run(
        words='https://www.baidu.com',
        picture='Sources/Acat.gif',
        colorized=True,
        save_name='artistic_cat.gif',
        )
