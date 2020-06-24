import pygame,sys

pygame.init()

screen = pygame.display.set_mode((500,500))

#加载字体
fonts = pygame.font.get_fonts()
print(fonts)

# ['arial', 'arialblack', 'bahnschrift', 'calibri', 'cambriacambriamath', 'cambria', 'candara', 'comicsansms', 'consolas', 'constantia', 'corbel', 'couriernew', 'ebrima', 'franklingothicmedium', 'gabriola', 'gadugi', 'georgia', 'impact', 'inkfree', 'javanesetext', 'leelawadeeui', 'leelawadeeuisemilight', 'lucidaconsole', 'lucidasans', 'malgungothic', 'malgungothicsemilight', 'microsofthimalaya', 'microsoftjhengheimicrosoftjhengheiui', 'microsoftjhengheimicrosoftjhengheiuibold', 'microsoftjhengheimicrosoftjhengheiuilight', 'microsoftnewtailue', 'microsoftphagspa', 'microsoftsansserif', 'microsofttaile', 'microsoftyaheimicrosoftyaheiui', 'microsoftyaheimicrosoftyaheiuibold', 'microsoftyaheimicrosoftyaheiuilight', 'microsoftyibaiti', 'mingliuextbpmingliuextbmingliuhkscsextb', 'mongolianbaiti', 'msgothicmsuigothicmspgothic', 'mvboli', 'myanmartext', 'nirmalaui', 'nirmalauisemilight', 'palatinolinotype', 'segoemdl2assets', 'segoeprint', 'segoescript', 'segoeui', 'segoeuiblack', 'segoeuiemoji', 'segoeuihistoric', 'segoeuisemibold', 'segoeuisemilight', 'segoeuisymbol', 'simsunnsimsun', 'simsunextb', 'sitkasmallsitkatextsitkasubheadingsitkaheadingsitkadisplaysitkabanner', 'sitkasmallsitkatextboldsitkasubheadingboldsitkaheadingboldsitkadisplayboldsitkabannerbold', 'sitkasmallsitkatextbolditalicsitkasubheadingbolditalicsitkaheadingbolditalicsitkadisplaybolditalicsitkabannerbolditalic', 'sitkasmallsitkatextitalicsitkasubheadingitalicsitkaheadingitalicsitkadisplayitalicsitkabanneritalic', 'sylfaen', 'symbol', 'tahoma', 'timesnewroman', 'trebuchetms', 'verdana', 'webdings', 'wingdings', 'yugothicyugothicuisemiboldyugothicuibold', 'yugothicyugothicuilight', 'yugothicmediumyugothicuiregular', 'yugothicregularyugothicuisemilight', 'dengxian', 'fangsong', 'kaiti', 'simhei', 'holomdl2assets', 'fzshuti', 'fzyaoti', 'lisu', 'stcaiyun', 'stfangsong', 'sthupo', 'stkaiti', 'stliti', 'stsong', 'stxihei', 'stxingkai', 'stxinwei', 'stzhongsong', 'youyuan', 'arialms', 'century', 'wingdings2', 'wingdings3', 'bookantiqua', 'centurygothic', 'haettenschweiler', 'garamond', 'monotypecorsiva', 'algerian', 'baskervilleoldface', 'bauhaus93', 'bell', 'berlinsansfb', 'bernardcondensed', 'bodonipostercompressed', 'britannic', 'broadway', 'brushscript', 'californianfb', 'centaur', 'chiller', 'colonna', 'cooperblack', 'footlight', 'freestylescript', 'harlowsolid', 'harrington', 'hightowertext', 'jokerman', 'juiceitc', 'kristenitc', 'kunstlerscript', 'lucidabright', 'lucidacalligraphy', 'lucidafaxregular', 'lucidahandwriting', 'magneto', 'maturascriptcapitals', 'mistral', 'modernno20', 'niagaraengraved', 'niagarasolid', 'oldenglishtext', 'onyx', 'parchment', 'playbill', 'poorrichard', 'ravie', 'informalroman', 'showcardgothic', 'snapitc', 'stencil', 'tempussansitc', 'vinerhanditc', 'vivaldi', 'vladimirscript', 'widelatin', 'twcen', 'twcencondensed', 'script', 'rockwellextra', 'rockwellcondensed', 'rockwell', 'rage', 'pristina', 'perpetuatitling', 'perpetua', 'papyrus', 'palacescript', 'ocraextended', 'maiandragd', 'lucidasanstypewriterregular', 'lucidasansregular', 'imprintshadow', 'goudystout', 'goudyoldstyle', 'gloucesterextracondensed', 'gillsansultracondensed', 'gillsansultra', 'gillsanscondensed', 'gillsans', 'gillsansextcondensed', 'gigi', 'frenchscript', 'franklingothicmediumcond', 'franklingothicheavy', 'franklingothicdemicond', 'franklingothicdemi', 'franklingothicbook', 'forte', 'felixtitling', 'erasmediumitc', 'erasitc', 'erasdemiitc', 'engravers', 'elephant', 'edwardianscriptitc', 'curlz', 'copperplategothic', 'centuryschoolbook', 'castellar', 'calisto', 'bradleyhanditc', 'bookmanoldstyle', 'bodonicondensed', 'bodoniblack', 'bodoni', 'blackadderitc', 'arialrounded', 'agencyfb', 'berlinsansfbdemi', 'lucidafax', 'twcencondensedextra', 'lucidasanstypewriter', 'lucidasanstypewriteroblique', 'lucidasansroman', 'extra', 'msoutlook', 'bookshelfsymbol7', 'msreferencesansserif', 'msreferencespecialty', 'dejavusansmonooblique', 'dejavusansmono', 'axurehandwritingbold', 'axurehandwritingbolditalic', 'axurehandwritingitalic', 'axurehandwriting', 'adobedevanagariregular', 'adobedevanagaribold', 'adobedevanagaribolditalic', 'adobedevanagariitalic', 'zwadobef', 'teamviewer15']

red = pygame.Color(255,0,0)

# 加粗 斜体
# 方式一:使用系统默认的字体来进行加载
#font = pygame.font.SysFont('stxinwei',40,False,False)
# 方式二: 自己准备一个字体文件，放在项目里引用
font = pygame.font.Font('./static/STXINWEI.TTF',40)
# 文字对象
text = font.render('得分',True,red)

# 加载背景音乐
bg_music = pygame.mixer.music.load('./static/girl.mp3')
#设置音量(0-1) 值越小，音量越小
pygame.mixer.music.set_volume(0.5)
# -1表示循环播放
pygame.mixer.music.play(-1)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(text,(20,20))
    pygame.display.flip()