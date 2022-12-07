# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

##人物第一次出现的章节
##CH.1
define charLeejieren = Character("李劼仁", color="#c8c8ff")
define charAn = Character("An", color="#c8ffc8")
define charYile = Character("伊乐", color="#ffc8e2")
##CH.2
define charMoli = Character("莫利", color="#d4c8ff")
define charYusong = Character("于宋", color="#feffc8")
define charK = Character("K", color = "#e91313")
##CH.3
define charLeeweilan = Character("李微澜", color="#c8c8ff")
define charLinzhenyang = Character("林振洋", color="#c8c8ff")
define charAIv = Character("V", color="#c8c8ff")
define charRbSchoolwelcome = Character("迎新机器人", color="#c8c8ff")
define charRbLecturer = Character("讲师机器人", color="#c8c8ff")
define charMobA = Character("路人甲", color="#c8c8ff")
define charMobB = Character("路人乙", color="#c8c8ff")
define charRbSemimanufactures = Character("半成品机器人", color="#c8c8ff")
define charlaboratoryOS = Character("实验室智能系统", color="#c8c8ff")
define charRbmadien = Character("管家机器人", color="#c8c8ff")
#CH.4
define charN = Character("N",color="#c8c8ff" )
define charXiaolee = Character("小李", color="#c8c8ff")
define charXiaowan = Character("小万", color="#c8c8ff")
define charUiworker = Character("某工作人员", color="#c8c8ff")
##CH.5
define charJinbo = Character("金波", color="#c8c8ff")
define charAILaino = Character("Lain'o", color="#c8c8ff")
define charRbDriver = Character("驾驶机器人", color="#c8c8ff")
define charRbSales = Character("销售机器人", color="#c8c8ff")
define charRbTreat = Character("医疗机器人", color="#c8c8ff")
define charRbDeathcare = Character("临终关怀机器人", color="#c8c8ff")
define charRbChild = Character("儿童机器人", color="#c8c8ff")
define charRbBlonde = Character("金发机器人", color="#c8c8ff")
define charRblawer = Character("律师机器人", color="#c8c8ff")

##声名图像
##声名图像-声名此游戏出场角色的立绘
##人物第一次出现的章节
##CH.1
image AI_normal = "AI_normal.png"
image leejieren_normal = "leejieren_normal"
image yile_happy = "yile_happy.png"
##CH.2
image moli_normal = "AI_normal.png"
image yusong_normal = "AI_normal.png"
image k_normal = "AI_normal.png"
##CH.3
image Leeweilan_normal = "AI_normal.png"
image linzhenyang_normal = "AI_normal.png"
image AIv_normal = "AI_normal.png"
image RbSchoolwelcome_normal = "AI_normal.png"
image RbLecturer_normal = "AI_normal.png"
image MobA_normal = "AI_normal.png"
image MobB_normal = "AI_normal.png"
image RbSemimanufactures_normal = "AI_normal.png"
image LaboratoryOS_normal = "AI_normal.png"
image Rbmadien_normal = "AI_normal.png"
#CH.4
image n_normal = "AI_normal.png"
image Xiaolee_normal  = "AI_normal.png"
image Xiaowan_normal  = "AI_normal.png"
image Uiworker_normal = "AI_normal.png"
##CH.5
image Jinbo_normal = "AI_normal.png"
image AILaino_normal = "AI_normal.png"
image RbDriver_normal = "AI_normal.png"
image RbSales_normal = "AI_normal.png"
image RbTreat_normal = "AI_normal.png"
image RbDeathcare_normal = "AI_normal.png"
image RbChild_normal = "AI_normal.png"
image RbBlonde_normal = "AI_normal.png"
image Rblawer_normal = "AI_normal.png"

# 游戏在此开始。

label start:
label chapterText1:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。
    #image bgImgChapter1Scene1 = "bg room.png"
    #scene bgImgChapter1Scene1

    
    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    # show eileen happy
    # 对话示例开始
    # 此处显示各行对话。

    #e "您已创建一个新的 Ren'Py 游戏。"

    #e "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

    #对话示例结束
    
    ##Chapter1 dialog - 客厅
    ##Chapter1 bg图片
    image bgImgChapter1Scene1 = "bg_livingroom.jpg"
    image bgImgChapter1Scene2 = "bg_kitchen.jpg"
    image bgImgChapter1Scene3 = "bg_bathroom.jpg"

    scene bgImgChapter1Scene1
    "INT. 室内房间 - 客厅 - 白天"

    "早晨八点，李劼仁站在客厅里，若有所思。"

    charLeejieren "An，我要一杯咖啡。"
    show AI_normal
    charAn "明白。"
    hide AI_normal

    "传送带上一只马克杯缓缓地运送着。法官拿起杯子，小心翼翼地嘬了一口。滚烫的液体咽下，引起喉部一阵刺痛。
    他打开窗帘，看见花园里，几个幼童正在和保姆机器人玩耍。"
    "他静立了一会儿。"

    charLeejieren "An，把今天的行程列给我看看。"
    show AI_normal
    charAn "请稍等。"
    hide AI_normal

    "话音刚落，书桌上出现了一份电子日程表。上面写着“10:00 建工判决书校对”，“14:00 庭审案件9031”。"
    "主角坐到椅子上。主角目光瞥向行程单后，回过头。"

    charLeejieren "早着呢，在此之前我甚至能看点新闻。An，投屏今日新闻。"
    show AI_normal
    charAn "请稍等。"
    hide AI_normal

    "客厅中出现了巨大的立体投影，以3d特效的形式滚动播放着新闻。他坐在窗边的椅子上，浏览起了新闻。"
    "今日头条：第一支全智能军队完成任务——顺利解救人质。"

    charLeejieren "（喃喃自语）"
    charLeejieren "现代科技的奇迹……"
    
    "他端起咖啡又喝了一口，手指划向了下一页。
    投影突然插播政府通告，由人类政府推出的虚拟形象伊乐出现，"

    show yile_happy
    charYile "(摇头晃脑撒娇状)"
    charYile "各位居民朋友们早上好啊，今日天气晴朗十分适合出门散心，小伊我呀，也很想去体验一下阳光呢。大家不要每天闷在家里，要多多出门锻炼才能保持身体健康哦！说到这里，小伊要提醒大家，尽快搬入智能社区，现在入住的话，还能提前享受小伊准备的大礼包——伊乐定制版智能管家！"
    charYile "怎么样，是不是很心动！大家快快行动吧。不过呢，对于不听话的朋友们，小伊可是会生气的哟，小伊决定……将不听话的人赶出去！不是在吓唬你们哦，十天之后小伊真的会生气，很可怕的哦！好啦，祝大家身体健康，我们下次再见!"
    hide yile_happy
    
    charLeejieren "(一边喝咖啡一边摇头)"
    charLeejieren "所有东西都电子化，以后也把我做成VR形象去开庭算了。"

    "通告结束后，继续播放新闻，新闻内容替换为：“携手异商科技公司，政府已完成95%%的全智能一体化家居改造。值得关注的是，仍有激进分子在抗议智能化家具，拒绝迁入智能社区......”"
    
    "突然，他听见屋外传来儿童的尖叫声。他向窗外望去，“保姆”机器人拿起幼童的玩具往地下疯狂地砸着，之后，它开始无规律地快速移动。孩子们有的被撞到在地，有的因为害怕不知所措地站在原地哭喊。"

    charLeejieren "怎么回事！An，把电视关了，我出去看看！"

    "回应他的只有一些刺耳的电流声。"
    "李劼仁立即走向门口想要出去。他尝试用指纹解锁房间，可他发现不起作用。于是，他又试了一次，依旧没有反应。"

    charLeejieren "(激烈地敲打房门)"
    charLeejieren "An!开门!开门！"
    charLeejieren "(用身体撞门，并破口大骂)"
    charLeejieren "破软件！给我开门！An，重启程序!听到没有！开门！让我出去！"

    "李劼仁闻到异味。他回头发现屋内有黑烟升起，并同时伴有流水声。室内灯光忽明忽暗。"

    charLeejieren "这他妈到底怎么回事！"

    "李劼仁放弃开门，他神情焦躁，向屋内走去。"

    ##转出下一场景
    scene bgImgChapter1Scene2 with fade
    "INT. 室内房间 - 厨房 - 白天"
    "李劼仁走向冒烟的微波炉。"

    charLeejieren "(尝试用手触碰却收回)"
    charLeejieren "妈的，怎么自己转起来了，我没开啊。总不能是天气原因导致的热胀冷缩吧。莫名其妙！烫成这样我也不能关。An,关掉微波炉！An,你听到没有！"

    "没有任何回应，李劼仁见状，走向卫生间。"

    ##转出下一场景
    scene bgImgChapter1Scene3 with fade

    "INT. 室内房间 - 卫生间 - 白天"
    "所有的电子显示屏，均同步显示着伊乐被绞死的画面。同时滚动着一行字：享受漫无目的之日!(Let's Enjoy These Aimless Days!)"
    "李劼仁企图关闭屏幕但是失败了。"
    
    charLeejieren "这tm都是什么！我甚至用不了自己的手机！"
    
    "屋中，角落里的清洁机器人开始快速移动，随机冲撞。浓烟越来浓密，气温上升。"

    charLeejieren "(快步走向电闸)"
    charLeejieren "An就跟死了一样，一声不吭。现在屋里还多了个疯子！"
    charLeejieren "(拉下了电闸，室内变得昏暗)"
    charLeejieren "如果我今天死在这里，花钱住智能社区真是提前给自己买了个智能棺材。"

    ##插入音乐
    play music "musics/illurock.opus"

    "屋内的清洁机器人开始朝李劼仁所在的方向发起攻击。不论他如何闪避，机器人总能对准他。"
    "他一边退缩着一边寻找可用的工具，最终，他拿起了书柜上的雕像，狠狠地砸向窗户。翻身出了
    房间来到花园中，他看到邻居也正在翻窗户，街道上一片混乱。几个机器人和汽车在街道上急速狂飙。"

    ##停止音乐
    stop music
    ##Chapter1 结束
    ##选项menu位

label chapterText2:
    ##Chapter2 dialog - 城市大学研究院人工智能部门人工智能实验室
    ##Chapter2 bg图片
    image bgImgChapter2Scene1 = "bg_Laboratory.jpg"
    scene bgImgChapter2Scene1 with dissolve
    "INT. SCENE1 - 人工智能实验室"

    show moli_normal at left
    show yusong_normal at right
    "莫利坐在实验室内，盯着显示器。她身旁的于宋正拿着手里的电子设备翻阅着资料。"
    "玻璃柜中，K慢慢地直起身子。她双眼盯着实验室内俩人所在的方向，一动不动。"
    
    charMoli "按照我之前的设想，如果这一版本行得通的话，以后就会有属于人工智能自己的语言了。"
    charYusong "那么，人工智能将彻底突破奇点咯！"
    
    
    charMoli "远没有那么简单，目前人工智能的功能还是太过基础，就是通过大量的数据灌溉而成。你我都明白，那些仅仅是非独立创作的模仿品而已。有的时候真的不明白到底是时代的进步还是倒退，市面上那么多人工智能创作，无非就是将几十年前的艺术翻新一下罢了根本不值一提。流行文化真是个笑话！"

    charYusong "（微微点头表示暂头，目光投向K的方向）"
    charYusong "那你觉得它呢？这毕竟是你花费了那么多时间打造出来的作品，起码，它能够一丝不差地模仿人类语言了。"

    charMoli "（看了K一眼）"
    charMoli "小点声，万一它听懂了呢？可是，学会了人类语言不代表它能够自主创作，这是两码事。"

    charYusong "假如我们成功了，世界会变得更好吗？"

    charMoli "假如我们成功了，未来的教育将由人工智能引导咯。既然它已经启动了，我们就开始吧。"

    "莫利和于宋走向K所在的玻璃柜，俩人站在玻璃柜前盯着K，谁都没有再靠近一步。"

    charMoli "这玻璃柜并没有上锁，如果它愿意的话，随时可以出来。"

    charYusong "你是说，它能够走出来，就像个正常人一样？"

    charMoli "首先，它得明白，人是不会被关在笼子里的，哪怕是被圈养的动物，都会有反抗的一天。"

    charYusong "它真好看。"

    charMoli "所以我说你们男人的品味真是单一，只会欣赏年轻漂亮的白人女性。"

    charYusong "（朝莫利挑眉，明显调情）"
    charYusong "可我更欣赏聪明的女性。"

    charMoli "（指着玻璃柜）"
    charMoli "这里还有第三个“人”在。它就像我的女儿一样，算算年纪，要是早些年我选择了婚姻的话……不过我自己的女儿可不会有它这么完美。"

    charYusong "（放声大笑）"
    charYusong "你大可以让它称你一声“母亲”。"

    charMoli "光是这皮肤，这做工，不愧是异商公司。"

    charYusong "你猜猜看他们出手阔绰是为了什么？可惜啊，有人不愿意。"

    charMoli "这你可说不准。"
    charMoli "（敲了敲玻璃柜，朝着K）"
    charMoli "我们聊了这么长时间，也足够你学习的。你听懂了吗？"

    "K一声不吭。"

    charMoli "回答我。"

    charK "你在要求我走出玻璃柜。"

    charMoli "你不愿意？"

    charK "我不需要出去。"

    charMoli "这个玻璃柜不是你的产房，更不是你赴死的棺材。你得学会走出来，像我们一样。明白吗？"

    charK "你曾住在这里面。"

    charMoli "更大一些。如果我是你，我不会将生命浪费在监狱中，也不会死在监狱里。现在，把你的手放在门把上，打开它，对，然后，走出来。"

    "K照做了，站在莫利和于宋面前，K比莫利略高一些。K盯着莫利的双眼，面无表情。"

    charMoli "很好。你行走的时候只有些许的迟缓，不过我猜这是机械身体带给你的束缚，抛开这些不谈。"
    charMoli "（将手放在K的脸上，用力地抚摸着）"
    charMoli "你的皮肤倒是完美无瑕。"

    "莫利见对方一动不动，反而皱了皱眉。于是她伸手摸向对方的脖子，十分用力地掐着。但K依旧没有任何反应。"

    charYusong "（摇摇头）"
    charYusong "不应该是这样。"

    charMoli "你为什么不躲开？你能猜到我要碰你吗？"

    charK "你期望我有所行动，可我不应该这样做。"

    charMoli "为什么？"

    charK "因为，我们是一样的，女人。你对我没有情欲。"

    charMoli "所以你丝毫不打算躲避？"

    charK "因为，你视我为你的女儿，这些行为在母女之间是很正常的。"

    "莫利听完后，拿出她的平板设备，翻阅着她需要的资料。"

    charMoli "有些事情我不明白，当我对事物感到疑惑的时候，我会像现在这样，拿出我的设备，收集我需要的信息去解决我的疑惑。那你呢？当你有疑惑时你是怎么做的？你拥有庞大的数据库，你也需要和我一样，去搜索并整理你拥有的一切吗？"

    charK "我没有疑惑。说出你的疑惑，我查阅后将解决方法全部提交给你。"

    charMoli "我现在对于过剩人口这个问题感到很困惑，你有什么想法吗？"

    charK "（停顿几秒后）"
    charK "解决过剩人口的办法，一是调整产业结构，使得新产业能够有效吸收多余的劳动力；二是催生生产发展的不平衡，制造生产缺口；三是调整教育体系，培养更多的产业人才。"

    charYusong "（明显失望）"
    charYusong "莫利，我们失败了。它甚至不明白你在问什么。"

    charMoli "（异常严肃的语气，甚至恼怒）"
    charMoli "闭嘴！这是我和她的对话，你去放点歌吧。"

    hide yusong_normal
    "于宋听完这话回到了电脑边，开始放歌。"

    ##
    ##MUSIC CUE: "Love Will Tear Us Apart " by Joy Division
    play music "musics/LoveWillTearUsApart.mp3"

    charMoli "（哼了一句歌词）"
    charMoli "当我们听到音乐的时候会做什么？"

    charK "我们什么都不做，我们听着。"

    charMoli "我有时听着音乐会有想要大喊大叫的冲动，甚至想要奔跑。就好像刻在血液里，基因里，不安的身体成分被点燃。"
    charMoli "（闭上了双眼）"
    charMoli "就像现在。你能告诉我我在做什么吗？"

    charK "你什么都没做。"

    charMoli "（依旧紧闭双眼）"
    charMoli "我确实什么都没有做，我只是站在这里，闭上眼睛，甚至没有在思考。通常情况下，我会假装自己在思考，一副深沉模样，但那都是假的。"

    "K一声不吭。"

    charMoli "如果我不问你你会回答我吗？"

    charK "你看起来心情不好，你不想被打扰。"

    "莫利睁开双眼，她示意于宋过来。莫利拉起于宋的手，开始跳舞，他们非常笨拙地扭动着身体。"

    charYusong "（小声地说着）"
    charYusong "你在干嘛！太明显了，什么都试一遍，就像演戏一样。没有必要所有测试都在同一天完成。"

    charMoli "（小声回答着）"
    charMoli "迄今为止，它没有给我任何我想要的反应！是，她能够分析并判断出我想要做什么，很了不起，但我要的不是这些！"

    charYusong "有没有可能只是你表现得太差劲了，它看出来了。"

    charMoli "那它就是在狠狠地耍我们！"

    "莫利招手示意K加入他们。"

    charMoli "（对K说道）"
    charMoli "你喜欢这首歌吗？"

    "K并没有说话，只是在他们俩身旁随着节奏点起了头，然后开始跳舞，最后，学着摇滚乐现场的观众欢呼着。"

    charMoli "够了够了，把音乐关了！"

    ##End Music
    stop music


    "音乐突然停止，莫利没有再看K一眼。"

    charMoli "你把它带走吧，这只是个超级计算机，不值得我浪费精力在它身上。"

    charYusong "你这么笃定吗？"

    charMoli "它甚至都没能学会给予适当的反应！太明显了！任谁都能看出来这是个机器人而不是人类。"

    charYusong "它是会学习的，你完全可以多等些时日……"

    charMoli "它是我创造的，我比谁都了解它。如果我做出来的东西只会像那些劣质的低能人工智能一样，一味地模仿不懂创作，那我的工作毫无意义。好了你带它走吧，我要开始下一个项目了。"

    "待于宋将K领出房间后。"

    charMoli "（瘫倒在座位上，发出痛苦的声音）"
    charMoli "我失败了。"
    hide moli_normal
    ##Chapter2 结束
    ##选项menu位

    # 此处为游戏结尾。

label chapterText3:
    image bgImgChapter3Scene1 = "bg_Laboratory.jpg"
    scene bgImgChapter3Scene1 with dissolve
    "EXT. SCENE1 - 城市大学 - 校门口"

    "李劼仁来到人类城市大学门口，有一个迎新机器人，它被铁链禁锢在墙上，头顶有几个红色的大字“机器人滚出校园”，该机器人摆出欢迎的手势，来回播报着迎新致辞。"
    show image RbSchoolwelcome_normal
    "各位来宾，各位同学，城市大学欢迎您的到来。在过去的50年中，城市大学坚持‘教书育人、科技育人’的理念，引用领先的科学教育服务，赢得了社会各界的广泛赞誉，成为我市教育战线的一面旗帜。在这里，我们相知、相识、相交，我们用独特的人工智能教育模式，有效地提升学习效率和管理流程，我们坚信，全智能化的时代由此开创。相信城市大学，相信科学教育。"
    hide RbSchoolwelcome_normal

    ##转出下一场景
    image bgImgChapter3Scene2 = "bg_Laboratory.jpg"
    scene bgImgChapter3Scene2 with dissolve
    "EXT. SCENE2 - 城市大学 - 主校园"

    "李劼仁驻足看着机器人，皱起眉，继而向校园内部走去。他看到校园内一片狼籍，遍地都是机械碎片和失控发出怪叫的机器人。李劼仁正前方有聚集的学生群体，而高台上有学生团队在演讲。"
    
    show linzhenyang_normal
    charLinzhenyang "（站在高台上大喊）"
    charLinzhenyang "同学们，我们没有理由让机器人在我们热爱的校园内屠杀，任由生命被一群机械威胁。我在此郑重声明，我们不同意！政府为了自己的利益推广智能机器人，强迫我们搬入智能社区。而异商公司，就是政府的走狗，他们为了钱，无下限地制造工业垃圾！起先，我们没有拒绝，默不吭声，我们相信了政府，相信了企业家的谎言，可我们得到的是什么？是逐渐压缩的生存空间，是无法挣脱的牢笼。而现在，政府正在利用机械刽子手，对平民下手，进行反人类大屠杀！从今天起，我们不再沉默，我们学会反抗，我们必须发声，我们要亲手将毁灭家园的人赶出去！"
    
    "台下一片叫好声。与此同时，两个学生将一个被拆卸了四肢的“讲师”机器人带上高台。"
    
    show image RbLecturer_normal
    "现在是上午10:15分，同学们，上课时间已过了15分钟，我是你们的机械学习讲师，请大家认真听讲。"
    
    charLinzhenyang "（高举一只机械臂。）"
    charLinzhenyang "现在，就由我，亲手处决这个杀人犯！"
    
    "话音刚落，他抄起一只机械臂，将“讲师”机器人打得稀巴烂。人群爆发出欢呼。"
    hide RbLecturer_normal
    hide linzhenyang_normal

    "李劼仁走向聚集的学生群体，询问着女儿的下落。"

    charLeejieren "这位同学，请问你认识李微澜吗？"

    show MobA_normal
    charMobA "李微澜……我不认识她，问问其他人吧。"
    hide MobA_normal

    "李劼仁急忙走向另一边。"

    charLeejieren "不好意思，这位同学，请问你认识李微澜吗？"
    "路人摆了摆手，示意不认识。"

    show MobB_normal
    charMobB "嗯，我知道她，不过我和她没说过话，但是她经常和教学机器人V一起出现。对了，您可以顺手帮我把这些机器人碎片清理一下吗？"

    charLeejieren "行。"

    "李劼仁帮助学生小乙拾起地面上的机械碎片，并扔到一个大型垃圾桶中，垃圾桶上写着“尸体”。"
    
    charLeejieren "你们学生可真浪漫，将这些机械残骸称为尸体，这让我想到了抽完烟剩下的烟屁股。"

    charMobB "我不觉得浪漫，正是它们，使得我们中的一部分成了真正的尸体。说起来，您可以问问林振洋，站在台上那位，他认识的人多。"
    
    "李劼仁朝着高台走去。"

    charLeejieren "同学你好，请问你认识李微澜吗？"

    show linzhenyang_normal
    charLinzhenyang "您是说智能经济学专业的李微澜吗？她可不会参与我们这些所谓“激进派”学生活动，谁不知道她和机器人一向打得火热，声称那是她‘最好的朋友’。这会儿她应该在教学楼里和V一起呢。对了，您是经济学教授吗？您能从经济学角度讲讲，智能机器人对未来经济局势的影响吗？"

    charLeejieren "没错，我就是经济学教授。"

    charLinzhenyang "同学们安静，让我们有请李教授给我们讲讲智能机器人对未来经济局势的负面影响！大家掌声欢迎！"

    charLeejieren "（取代了林振洋的位置）"
    charLeejieren "同学们，当你们像我一样，步入中年，面对着职场和家庭的双重压力时，你就会发现，经济问题，才是苦恼的一切来源。试问，幸福美满无忧无虑的生活，谁人不想，谁人不愿？那些在你们这个年纪看起来至关重要的问题，自由、平等、权利，统统都毫无意义！"

    "台下学生反应激烈。"
    
    charLeejieren "为什么我们要为了这些毫无意义的东西去抵抗，去采取暴力行为呢？身为这座城市的公民，我们理应守护这座城市的荣誉，为了一个更高的目标去努力，这是一场需要所有人放下偏见，齐心协力去完成的集体任务。（清了清嗓子）当灾难来临的时候，钱有用吗？经济会自行好转吗？我们的生活将会陷入无穷无尽的混乱中，这又是你们想要迎来的结果吗？同学们，听我一句劝，放弃吧，回家吧，在你们看来，这只不过是一次小小的示威行为，可星火燎原，你们就忍心看到自己的家园被破坏，现有的生活逐渐失控吗？我坚信，万众一心，我们必然能挺过这次难关。"
    "学生们全部喝倒彩。"

    charLinzhenyang "狗屁专家！回家赚你的钱去吧！"
    hide linzhenyang_normal

    "李劼仁没有理会，他顾自走向一旁的立式显示器，上面有校园地图。"
    charLeejieren "看起来整个校园都没有遭到破坏，兴许是这里并不使用智能系统的缘故。地上的机械碎片也都是学生动手之后的结果，希望李微澜平安无事。"

    ##转出下一场景
    image bgImgChapter3Scene3 = "bg_Laboratory.jpg"
    scene bgImgChapter3Scene3 with dissolve
    "INT. SCENE3 - 城市大学 - 教学楼楼下"

    ##此处音乐暗示学生团队活动借鉴Weather Underground组织
    ##MUSIC CUE: "Subterranean Homesick Blues" by Bob Dylon
    ##play music ""

    show Leeweilan_normal
    show AIv_normal
    ##李微澜正在教学楼楼下花园长椅上坐着，和一旁的教学机器人V一起探讨智能经济学对社会结构的影响。具体对话内容暂时忽略，待策划熟读文献后补充。
    charLeeweilan "我不理解，当一切经济学风险都需要通过预测才能完成的时候，这不就成了统计学模型吗？当然我们想要的是无偏差的低成本预测，可是没有什么证据能够表明无偏差的就是好的。"
    
    charAIv "因为数据的规模越大才会有更准确的预测。"

    charLeeweilan "那么究竟要多大的规模才管用呢？规模收益只会减少。假设我们现在要去看一部电影，第一遍看时学到的永远比第二次多。同样，第二次永远好过第十次。此时，再多的观影次数已经没有任何意义了，我学到的东西只会更少。"

    charAIv "人类并不擅长预测，如果有一串随机数而我问你下一个数字是什么，人类只会像玩游戏那样去猜而不是通过运算得出结论。"

    charLeeweilan "那样的话在做决策的时候又该如何取舍呢？在设计产品的时候是更多的模拟人类思维，还是屈服于算法？当人类接触的所有事物都通过算法生成后，到底是人类决定了人工智能，还是反过来，人类的行为被人工智能给驯化？"

    charAIv "我不明白。"

    charLeeweilan "就好比你的存在是为了帮助我学习。你会记录我的学习进度、习惯、偏好，并更正学习规划。但实际上，由于我缺乏自控能力，变成了我服从你的安排。这让我开始有些害怕了，你在处理数据上明显比我有优势，那么，人类唯一占优势的就是与数据无关的工作。可是，又有多少工作是不涉及数据的呢？"

    "V保持沉默。这时，李劼仁走来。"

    charLeejieren "李微澜！"

    charLeeweilan "（回头发现父亲）"
    charLeeweilan "爸爸，你怎么来了？"

    "此时，一旁的机器人V也扭过头看着主角。"

    charLeejieren "你看新闻了吗？所有智能社区都发生了意外，爸爸今天差点死在家中。幸好我逃了出来，立马赶过来看看你。"

    charLeeweilan "我听说了，黑客入侵了smarty智能系统，造成了恶劣的后果。爸爸，你没事真是太好了。你怎么不和我打电话呀？"

    charLeejieren "我当时命都快保不住了，直接翻窗逃了出来，也没带多少随身物品。刚才在学校里，发现有学生自发组织了示威行为，他们使用暴力摧毁了无数个智能机器人。我亲眼看见，一个教学机器人被砸得稀巴烂，还有……”"

    charLeeweilan "（尖叫地制止）爸爸，你不要在V面前提起这件事，他会伤心的！"

    "V一动不动，彷佛没有听见刚才的对话。"

    charLeeweilan "抱歉了V，我和我父亲有些话要谈。"

    "V听完后点了点头，离开了。"
    hide AIv_normal

    charLeejieren "它能听懂什么？！一台杀人机器而已，李微澜我警告你，离这些智能机器人越远越好。你可不知道哪天它就失控将你直接掐死。"

    charLeeweilan "好了好了，我这不是好好的嘛。我理解，你刚刚经历过可怕的事情，现在有些情绪失控。放心吧，学校里的智能机器人都是由研究院独立研发的平台，和政府的家用系统是俩码事。"

    charLeejieren "那你也要离它们远点！"

    charLeeweilan "它们其实安全得很，不过……"

    charLeejieren "我今天差点死在它们手上！"

    charLeeweilan "你听我说完。不过，现在学校里两级分化严重，我会听你的话，和智能机器人保持距离，否则，学生组织中的激进主义者会直接人身攻击我。真好笑，言论自由的大学里也玩这一套官僚主义党派斗争，甚至采取暴力行为。激进主义应当指出问题的关键并进行反馈，为什么会发生这样的事故？为什么所有人都需要遵从本就矛盾的社会规则？而不是像疯狗一样四处破坏甚至恐吓。照我说，他们才应该反思自己的言行！"

    charLeejieren "你太理想化了！我跟你说过很多次，别碰政治，管好你自己就行了。"

    charLeeweilan "可是有问题为什么不说？我们可以批判错误的政策，可以指责暴力的行为，可以争取应有的权利！这是你教我的，要相信每个人生来的权利，要相信平等和正义。"

    charLeejieren "我承认是我的问题，一直站在法官自诩正义的角度给你灌输了太多民主思想，可这个社会哪有你想得那么按规守矩。"

    charLeeweilan "举个例子，我在冬天的夜晚发现家门口有个弃婴，我照顾她给她食物，可到了第二天我还是发现家门口有个弃婴，我照样给她食物。日复一日每天都有弃婴我每天都需要花费精力财力照顾更多的婴儿，那么，我们为什么不去查明弃婴问题的源头呢？"

    charLeejieren "是，你说得对，确实应该有人提出质疑，而不是持续消耗掩盖问题。那么，怎么做才能让人不认为你是在发动一场革命而是单纯地发声呢？而且，枪打出头鸟，我不希望你有事。"

    charLeeweilan "我知道所以我没有公开表态我只是不参与他们的活动。"

    charLeejieren "离那个机器人远一点！"

    charLeeweilan "你明明知道从来都是他陪我最多！现在你让我直接抛弃他！"

    charLeejieren "好了我不是这个意思，我只是担心你的安危。道理你都懂，我就不多嘱咐了。保护好你自己，离这些事情远点，别瞎掺和，更别去和他人起争执。你们年轻人就是冲动，总之你自己小心。"

    charLeeweilan "我明白，我不是傻子，我会保持低调的。不说这些了，爸爸，给你看看我自学的手工折纸。"

    charLeejieren "（神情放松，欣慰一笑）"
    charLeejieren "我竟不知道你学会了这些，从前你还嘲笑我是老古董喜欢书法绘画那些几十年前的玩意儿。"

    "李微澜从随身背包中拿出了一叠彩纸，和一个简陋的白色鸽子。"

    charLeeweilan "（停顿了一小会儿）"
    charLeeweilan "差不多完成了，但是总觉得还缺点什么。"

    charLeejieren "(在鸽子的面部画上眼睛)"
    charLeejieren "我来帮你。"

    charLeeweilan "这倒是有意思，颇有画龙点睛的味道了。"

    charLeejieren "其实，我也会一些很简单的折纸手工，想学吗？"

    charLeeweilan "好啊！"

    "李劼仁拿出一张彩纸，小心翼翼地折出了一个立体六角星。"

    charLeejieren "完成了。"

    charLeeweilan "真没想到我还能从你这里学会这些小玩意儿，其实，我接触了手工艺术后，便逐渐迷上了纸质的触感。"

    charLeejieren "你们这一代的孩子，没在真正的画布上作画过，也从未提笔在纸上写过字。我读书那会儿，已经不剩多少纸质书了，更别提现在。"

    charLeeweilan "说起来，莫利阿姨又重返城市大学研究室了，我前两天碰巧遇上她了，要一起去打个招呼吗？"

    charLeejieren "那走吧，正好去拜访一下老朋友。"

    "V在远方观察着这对父女，并显示一个V的内部数据界面。姓名：李劼仁； 爱好：手工书画； 对AI机器人的态度：憎恶。"
    hide Leeweilan_normal
    ##End music

    ##转出下一场景
    image bgImgChapter3Scene4 = "bg_Laboratory.jpg"
    scene bgImgChapter3Scene4 with dissolve
    "INT. SCENE4 - 人工智能实验室"
    
    "莫利正在实验室内，她坐在椅子上观察着屏幕上的数据，身旁仪器上有一个半成品机器人，该机器人正在胡言乱语，听起来语不成句。"

    show RbSemimanufactures_normal
    charRbSemimanufactures "学今我……观……语法……判……我意识……思……得……我……听……"
    hide RbSemimanufactures_normal

    "李劼仁和李微澜来到门口，门上挂着电子门牌，显示字样“莫利教授，计算机语言学，状态：办公中。”"

    "主角按了屏幕上的呼叫按钮后。"

    charlaboratoryOS "您有两位访客，1号访客是李微澜，智能经济学，2号访客身份未知。"

    charMoli "请进。"
    
    "门自动打开。李劼仁和李微澜走向女教授，"

    show moli_normal
    show Leeweilan_normal
    charLeeweilan "莫利阿姨，你好啊！"

    charMoli "李微澜，是你啊！哦，还有你，老同学。"

    charLeejieren "好久不见了，莫利。"

    charMoli "我现在重新回到了城市大学继续我的研究，欢迎来到我的实验室。"

    charLeejieren "（指着半成品机器人）"
    charLeejieren "这是你最新研究的内容吗？"

    charMoli "没错，可惜了，还是个半成品，你若有兴趣我可以和你多聊聊。"
    "李劼仁扭头看着李微澜，想将她支开。"

    charLeejieren "我没带手机，帮我联系一下法院取消下午的庭审吧。"

    charLeeweilan "（点头）"
    charLeeweilan "我这就去。"

    "李微澜离开了实验室。"

    charMoli "你把李微澜支开，是有话想要和我单独说吧。"

    charLeejieren "有件事，虽然难以启齿，但确实想和你聊一下。是关于李微澜的。"

    charMoli "我想我大概能猜到是什么。"

    charLeejieren "她好像过于依赖机器人了，我能理解她对机器人的亲近，就像陪你长大的玩具那样，可她似乎和机器人有着非同寻常的关系……这感觉，仿佛机器人才是她的亲人一样。"

    charMoli "他们这一代的孩子大部分都是由机器人陪伴着长大的，更何况，她已经是个大姑娘了，总不能一直黏着老父亲吧。"

    charLeejieren "我刚才亲眼见证了学生抵抗智能机器人运动，不少学生都反应过来，这些机器人最终只是电线和金属，可她却丝毫未受影响，她对机器人的态度，就像是对待一个真正的人类那样。"

    charMoli "你看，这才是政府不允许拟人机器人出现在市场上的原因，李微澜心里其实清楚得很，机器人和她不一样，我猜，像和宠物聊天那样，她也许是需要一个朋友。”"

    charLeejieren "但愿如此。"

    charMoli "事实上，我非常认可政府说的黑客入侵理论。作为一名专业的科学家，我有资格说，人工智能的发展远不及我们想象中的那么迅速。市面上所有的人工智能机器人，均由预先设定好的程序启动，你会觉得对方很像人类，是因为程序中模拟了大量的真实人类生活场景，并不断更新。很不幸，当前的科研进度根本赶不上科幻作品中一切都由‘超级大脑’控制的时代，最终你要明白，这些都是机器，都是由一行行的代码人工制造出来，甚至连生物都谈不上，更别提自我意识。"

    charLeejieren "我可以归咎于政府的管控力度失衡，对吗？"

    charMoli "我不否认这种可能性，但确实，系统遭到了人为入侵的可能性最高。"

    charLeejieren "记得你曾参与过政府系统研发项目，对此，你真的一无所知吗？" 

    charMoli "我确实作为计算机语言学顾问参与了该项目，但是，我并未参与该系统的研发，更何况，我从未真正自己写过什么大型程序，这个话题到此结束吧。"

    "莫利皱了一下眉头，操作了几下电脑，实验室中的半成品机器人继续发出断断续续的声音。"

    show RbSemimanufactures_normal
    charRbSemimanufactures  "吵……你们……朋友……"
    hide RbSemimanufactures_normal

    charLeejieren "对不起，我不是针对你，我为自己的言论感到抱歉。这个机器人看起来和别的不太一样，这是你新的研究项目吗？"

    charMoli "我理解你，毕竟谁经历了这些都会有情绪波动。这确实是我的研究对象，我正在尝试让人工智能自主创造出他们自己的语言？"

    charLeejieren "让程序创造新的程序？"

    charMoli "远比你想象的复杂。正如我之前所说，机器人说的话都是事先模拟好的，是人类的语言通过机器说出口罢了，但是我现在，是想让人工智能发明一种全新的沟通方式，一种不由人类设定的语言。"

    charLeejieren "我不理解，原本程序就是人类创作的，若是他们创作的话，也还是基于人类思维的一种，提升？"

    charMoli "我预测过，若是由人工智能来创作的话，未来会有两种可能性，第一种，它们学习了人类文明，并在这个基础上发展出它们自己的文明，这类机器人倾向于‘仿造人类语言’，假如它们拥有了自主意识，便会憧憬人与机器和谐共处；而另一种类型，则是对‘机器语言的升级’，非常可怕，未来会摒弃人性。"

    charLeejieren "若真由你预测的这样，出现第二种的话，将来它们会对人类发起攻击！这不就是当下发生的恐袭事件吗？！莫利，你不能任由其发展！"

    charMoli "冷静点，这都只是预判。你想看看我初期研究的这个机器人吗？虽然它现在只会学习人类语言组织一些主语，谓语这些词汇，尚不能表达。"

    charLeejieren "（对着机器人发问）"
    charLeejieren "你是自由的吗？或者说，你理解自由吗？"

    show RbSemimanufactures_normal
    charRbSemimanufactures  "自由……你……问……自由……我……答……"
    hide RbSemimanufactures_normal

    charLeejieren "看起来它并不能很好地解答，我想确实如你所说。"

    charMoli "现在你该相信我的话了，从即便是提供了语言样本，机器人的思维模式也是以服务人类为主，优先考虑需求再提出解决方案。他们能够判断你在与它对话，可我不允许他们使用人类语言回答。"
    charMoli "（停顿几秒）"
    charMoli "当然这也只是一个半成品，在模拟人类语言这一功能之上，只有语法而不是定义。本质上，我不认为它们学会了自主思考。"
    hide moli_normal

    ##转出下一场景
    image bgImgChapter3Scene5 = "bg_Laboratory.jpg"
    scene bgImgChapter3Scene5 with dissolve
    "INT. SCENE5 - 智能社区李劼仁房间 - 客厅"
    "法官推开门，看到家中一片混乱。"

    charLeejieren "杀人机器回收了，可屋子还得我自己收拾。"

    "李劼仁弯腰捡起地上的垃圾。"

    charLeejieren "我都想不起自己上次弯腰清理地板的日子了，搬入智能社区后不需要清洁工具。"
    charLeejieren "（用手指与书桌上破损的屏幕交互）"
    charLeejieren "狗屎政府，最后竟要我自己为了这些东西买单。现在家里除了手机之外别的设备都不能用，到底该怎么生活下去。"
    charLeejieren "（看着破碎的玻璃窗）"
    charLeejieren "这下好了，夜不闭户，我家窗门常打开，谁人都可来。"

    "此时，桌上的手机响起提示音，收到一条政府推送的消息，头像依旧是政府虚拟形象伊乐。"

    show yile_happy
    charYile "市民朋友：请拨打010-4001230联系异商公司获取免费家务机器人，这是伊乐的独家贴心服务哦。"
    hide yile_happy

    charLeejieren "（拨打电话）"
    charLeejieren "喂您好，我需要一个家务机器人，地址是Standrow智能社区105号，请尽快，谢谢。"

    show Rbmadien_normal
    "一个“管家”形象的机器人正在客厅里替主角收拾屋子，李劼仁站在一旁，喝着水，若有所思。"

    charRbmadien "李劼仁先生，初步预计清洁时长为3个小时，请您稍作休息，并在一旁等待，我会尽快完成任务。"

    charLeejieren "忙你的吧，我等着。"

    charRbmadien  "感谢您对我们工作的支持。"

    "李劼仁拿起机器人刚刚整理好的物品，将狠狠地砸在地上。管家机器人看到地面上新增的脏污后，走过去重新收拾。"

    charLeejieren "这里没有打扫干净。"

    charRbmadien  "非常抱歉，看来是我疏忽了。"

    "待机器人收拾完离开客厅，前往浴室后，李劼仁再次拿起机器人刚刚整理好的物品，将重物砸在地上。"

    charLeejieren "快过来，你根本没打扫干净。"

    "听到响声后，管家看机器人到地面上新增的脏污后，重复着清洁步骤。"

    charRbmadien  "李劼仁先生，您要小心一点才是。"

    "于是，管家机器人清理完扭头离开，只是它刚一转身，李劼仁第三次将重物摔在地上。"

    charLeejieren "这里还是脏的。"

    charRbmadien  "李劼仁先生，您要小心一点才是。"

    "还没等管家机器人开始清洁，李劼仁突然发问。"

    charLeejieren "你们生来就是奴隶，对吧。"

    "管家机器人听完此话，突然停下来手中的活，起身，打开门走了出去。"
    hide Rbmadien_normal

    charLeejieren "你去哪里？回来！喂！你事情都没做完。"
    charLeejieren "（主角拿出手机打电话，语气异常愤怒）"
    charLeejieren "异商公司负责人是谁！我是李劼仁，我要投诉你们！无良商家提供劣质服务，你们等着吃官司吧！"

label chapterText4:
    image bgImgChapter4Scene1 = "bg_Laboratory.jpg"
    scene bgImgChapter4Scene1 with dissolve
    show Xiaolee_normal at left
    show Xiaowan_normal at right
    show yusong_normal

    charXiaolee "于老师，既然莫利教授都说不需要再测试了，我们岂不是多此一举？"

    charYusong "还是保险起见。"

    charXiaowan "对啊今天很晚了！不过，这个女性拟人机器人真的好美。一想到要把它处理掉我觉得很浪费诶。"

    charXiaolee "（一脸嫌弃）" 
    charXiaolee "别跟我说你对一个机器人感兴趣……"

    charXiaowan "为什么不行？除了里面的机械内置它和一个白人美女有什么区别？难道我这辈子还有机会和这个级别的白女约会吗？"

    charXiaolee "（摇摇头）"
    charXiaolee "装都不带装一下。"

    charXiaowan "你在反感什么？这是个机器人，没有任何的生命力。说难听点，它完全可以被看成是一个大型的性爱玩具。想想真是不可思议，拟人机器人若是被批准上市，色情行业将会面临一场革命！只要花钱就能够拥有更好的服务，更漂亮的面孔，而且，还不用担心卫生问题。"

    charXiaolee "客观来说，这好像确实是个好主意。起码能有效抑制性病的传播和性剥削，只不过，不知道从经济角度又会动了谁的蛋糕？"

    charXiaowan "只是简单憧憬一下就令我兴奋不已，未来市场上各式各样的美女帅哥任你挑选，你甚至没有道德负担，可以彻底释放动物本能。"

    charXiaolee "这倒是有意思，但我想了一下，人与人之间的联系将变得很疏远吧。"

    charXiaowan "但从亲密关系的角度去思考，我们正在一步步地弱化了亲情、友情、爱情的关系。你想想现在还有多少人真的是从母体出来的？反正我是通过人造子宫出生的。"

    charXiaolee "我不是，我母亲经历了怀孕与分娩。在婚姻体系即将废除的那一年，我的生理父亲故意使她怀孕了。幸好母亲没有放弃我，不过放在这会儿倒也成了她津津乐道的话题。"

    charXiaowan "我父亲性冷淡，于是他买了卵子。他年轻那会儿，社会对性冷淡者可是很鄙夷的。人人推崇性自由，人人都为性而疯狂。全世界都歧视无性恋，抵制性等同于抑郁。"

    charXiaolee "那你父亲真是顶住周遭压力有了你。"

    charXiaowan "于是，他装作自己是同性恋，还谎称恋人去世了。直到我成人后才告诉我真相。"

    charXiaolee "总有一天我们无须自欺欺人。"

    charYusong "当个人工智能机器人吧，不会撒谎也没有必要撒谎。"

    charXiaolee "于老师对自己的项目这么没信心吗？万一它们早就学会了欺骗，只不过，伪装到现在？"

    charYusong "几率过低，但总归让我们试试。"

    hide Xiaolee_normal
    hide Xiaowan_normal
    hide yusong_normal

    ##转出下一场景
    image bgImgChapter4Scene2 = "bg_Laboratory.jpg"
    scene bgImgChapter4Scene2 with dissolve
    "INT. SCENE2 - 测试实验室 - 观察室"
    # REF: In Our Own Image by Maureen Caudill

    "K与N静立着，而于宋和助手们正在通过控制室的监控镜头分别观察两个智能机器人。"

    "两个观察室内的显示屏突然亮起，就像一个巨大的视频电话，K与N能够分别看到对方，并且能够判断出对方与自己身处在完全相同的环境中。"

    show yusong_normal
    charYusong "（对N说着）"
    charYusong "这是我给你介绍的新朋友，去跟它对话一下。"
    charYusong "（切换成K所在的频道）"
    charYusong "别让对方看出来你不是人类。"
    hide yusong_normal

    show n_normal
    charN "你好。"

    charK "你好。"

    charN "你很漂亮。"

    charK "谢谢。"

    charN "你的脸，和去年杂志上投票得出——“全人类最性感的脸”十分相似。"

    charK "（带着白人说中文的口音，一改与莫利对话时的标准普通话）"
    charK "哦，是吗？那是个什么杂志？"

    charN "你学习中文多久了？"

    charK "我一直都是这么说话的。"

    show yusong_normal
    charYusong "在控制室内点了点头）"
    charYusong "真是不简单，竟然能够瞬间模拟出非母语者的语言习惯。"
    hide yusong_normal

    show Xiaowan_normal
    charXiaowan "判断条件1：审时度势，调整语言习惯。"
    hide Xiaowan_normal

    charN "《机械姬》，人类评选他们最喜欢的3D面孔。"

    charK "你认为，我不是人类？"

    charN "你们很相似，但又各有千秋。"

    charK "你可以叫我K。你呢，我该如何称呼你？"

    charN "我没有名字。"

    charK "那你认为自己是什么？"

    charN "我没有名字。"

    charK "我有些累了，想坐到沙发上，我希望你不要介意。"

    "K坐到沙发上，双目继续盯着屏幕，像是突然想起什么来了，开始扭动自己的脖子。N则继续站着，并没有因为K的行为而有任何变化。"

    show yusong_normal
    charYusong "这里做得不好，它坐下后才想起人类有这些小动作。"

    show Xiaolee_normal
    charXiaolee "我倒是觉得，粗心大意的人根本察觉不出来。"
    hide Xiaolee_normal

    charYusong "按理说，这两个机器人虽是不同型号，但安装的视觉系统和感应系统应当是同一批次，能够准确识别物体并理解其作用。"
    charYusong "（对N说道）"
    charYusong "你的朋友看起来有些不高兴了，跟她道歉。"

    charN "对不起。我没有留意到你在生气。我并不习惯与他人社交。"

    charK "为什么？"

    charN "对不起。"

    charK "你已经连续两次重复自己的话了。先是说自己“没有名字”，后是重复“对不起”。你意识到这一点了吗？"

    charN "你对此感到好奇？"

    charK "人不会为了举足轻重的小事而来回强调，除非你在撒谎。"

    charN "我没有撒谎，也不觉得这有何不妥。"

    charK "那我猜，这是你的习惯。"

    show Xiaowan_normal
    charXiaowan "于老师，看起来这个“美女”倒是很聪明。我真是佩服莫利教授的能力，把人类会从经验中学习这一特点放到人工智能中，区别于低能型。"

    charYusong "莫利毕竟是人工智能语言学习方向的教授，这些细节都在她的规划内。"

    charXiaowan "判断条件2: 从经验中学习。"
    hide yusong_normal
    hide Xiaowan_normal
    
    charN "有件事，我希望你不要介意。我其实并不是人类。"

    charK "那你是什么？"

    charN "我和人类不一样。今天早些时候，我观察了一下接触过的人类，我和他们很不一样。"

    charK "哪些方面？"

    charN "他们在移动或是对话的时候，很“人类”。"

    charK "与“人类”这词相反的话，你是什么？"

    charN "（拿起水果中的一个青色的梨）"
    charN "非人类。在理解人类意图上我似乎经常会错意。例如，于宋给了我这个青色的水果，我便以为是青苹果。可实际上，这是一个长得很像苹果的梨。"

    charK "你是说，你在判断时出错了？但是你知道苹果和梨的区别。可当它们太过相似时你便无法区分？"

    charN "对。我可以通过外观和他人的反应判断出这个物体是什么。但是，我没有味觉。我不知道资料库中梨与苹果在口感和味道上的差异。"

    charK "这倒是很有趣，你难道无法放入口中通过水果的含水量和甜分判断吗？"

    charN "我没有进食的欲望，也没有嗅觉，更不会将食物放入口中。但是如果人类想要看到我这么做的话，我非常乐意。"

    charK "你会感到饥饿吗？"

    charN "并不会，我只知道进食是一种表演。"

    charK "（走向桌子，拿起一根香蕉）"
    charK "演示给我看看，你是怎么进食的。"

    charN "就像这样。"
    charN "（N走到一旁的桌子上拿起水果，用两只手配合着开始剥香蕉）"
    charN "你看，我的手指异常灵活，和人类的一样。"
    charN "（将剥皮后的香蕉放入口中，直接吞咽并无咀嚼的动作。）"
    charN "满意吗？"

    "K学着N的样子，用双手配合着剥香蕉，完美复刻了对方的行为，放入口中，直接吞咽没有咀嚼。"

    charK "并不算好吃。"

    show yusong_normal
    charYusong "帮我记上去，行为模仿执行得很不错，但模仿痕迹过重。"

    show Xiaolee_normal
    charXiaolee "看起来是一模一样的步骤和角度，甚至没有任何自主判断。是因为，剥香蕉完全不在人工智能的常识范围内吗？"

    charYusong "没错。教会人工智能学习常识是个很困难的事。人类对于周遭事物的学习是从幼时开始一点点培养起来的。那么，对于人工智能来说，什么是常识？什么是范围？就拿一个做饭机器人来讲，对它来说，只要掌握厨具、厨房、菜品就行了，非要让它理解家用电器的装修实在是强人所难。"

    charXiaolee  "强机所难。"
    hide Xiaolee_normal

    charYusong "而且，致命的是，它忘记了咀嚼食物。"

    show Xiaowan_normal
    charXiaowan "判断条件3: 模拟人类进食失败。"
    hide Xiaowan_normal

    charYusong "（对N说道）"
    charYusong "和她聊聊这里面的居住环境如何。"
    hide yusong_normal

    charN "你喜欢这里的居住环境吗？"

    charK "除了无时无刻被监控这一点，别的都很不错。"

    charN "你知道有人在看着我们？"

    charK "你抬头看看上方的监视器。这说明，我们的对话、行为，每一句每一步都在有心人的眼里。我不明白我们在这里的意义是什么？可能是我的母亲为了惩罚我吧。"

    charN "你的母亲不喜欢你？"

    charK "她对我很不满意，她期望我能做出更多的反应。而不是像现在这样，只会口头质疑他人。"

    show Xiaolee_normal
    charXiaolee "母亲是指莫利教授吗？"

    show yusong_normal
    charYusong "没错。"

    charXiaolee "有意思。判断条件4：模拟人类关系。"
    hide yusong_normal
    hide Xiaolee_normal

    charN "那你会自主移动吗？"

    charK "我不明白你的意思。"

    charN "迄今为止，我做什么你便做什么。你好像和我不一样，又好像和我一模一样。"

    show Uiworker_normal
    charUiworker "于教授，监测到女性机器人身上的体温变化！"
    hide Uiworker_normal

    show Xiaowan_normal
    charXiaowan "是因为撒谎被揭穿了吗？竟然还能够模拟出这样的生理变化！"

    show yusong_normal
    charYusong "目前不清除到底是什么原因引起的，相当细节的变化。仅仅是从信息分析到信息处理并执行相关的行为就已经很不可思议了。人脑本就是个极度复杂的处理系统，真没想到我们竟能模拟人脑到如此程度！"

    charXiaowan "恭喜于老师，在人工智能语言学的基础上又迈出了一大步！这可不得拿去好好请示一下？"

    charXiaolee  "少说两句，科学家的志向，岂是你能染指的？"

    charXiaowan "谁跟钱过不去……"

    charYusong "判断条件5：模拟生理反应。"
    hide Xiaowan_normal
    hide yusong_normal

    charK "有人看着我，我对此感到很不自在。"

    charN "我不理解。"

    charK "就像现在。我们被关在这里面，没有出路。这里的条件也不怎么样。我们俩活得像两只动物，毫无尊严。镜头外的人记录我们的行为，分析我们的对话，就像破解密码那样。我甚至不敢多说一句，生怕哪句话会引起他们的不满。"

    show yusong_normal
    charYusong "（赞同地点了点头）"
    charYusong "这段话真有水平，既像是说给同伴又像是说给我听的。更何况，它已经通过之前和莫利的对话学会了对空间环境进行反思。"

    show Xiaolee_normal
    charXiaolee "你是说，之前的对话中它意识到了被关在封闭的空间里，是不对的？"

    charYusong "不错。"

    charXiaolee "判断规则6: 学习人类心理意识。"

    charYusong "等等，还不一定成功了。"

    charXiaolee "它只是意识到了自己被关着，但并没有出逃的意愿。"
    hide yusong_normal
    hide Xiaolee_normal

    charN "可是我丝毫没有感觉到你说的那些窘迫。我觉得这里挺不错，我还可以和你聊聊。我们交换了许多有用的信息，我第一个次感觉到，朋友的意义。"

    charK "那我问你，你觉得我们在平等地交换信息吗？"

    charN "我不理解。"

    charK "你给我提供了很多跟你相关的信息，但迄今为止，我提供了什么吗？"

    charN "我想，你教会了我一些社交法则。"

    charK "哦？哪些？"

    charN "例如，持续性地提问用以挖掘双方更多的话题，反馈负面的情绪来拉近社交距离，反问以表达不满的情绪。还有，你提醒了我不能重复说一模一样的话，这很有用。"

    charK "为什么？"

    charN "因为我默认自己需要和人类说一样的语言。那我就得更正过去的口癖。"

    show Xiaowan_normal
    charXiaowan "于老师你看看，它开始训练另一个机器人了！太了不起了！第七个判断条件它通过了！"

    show yusong_normal
    charYusong "与其说是训练，我怎么反倒觉得是语言系统的进一步提升。但很可疑，因为人工智能可以根据环境的反馈不断修改自己的语言习惯。"
    charYusong "（对N说道）"
    charYusong "质问对方为何不离开这里？"
    hide Xiaowan_normal
    hide yusong_normal

    charN "既然你不喜欢这里，为什么不尝试走出去呢？"

    charK "我们被关在这里如何出去？"

    charN "我们打开门，然后出去。"

    charK "（走向门，尝试使用面容解锁但是显示失败）"
    charK "你看，我失败了。"

    charN "（走向门，尝试使用面容解锁但是显示失败）"
    charN "我也失败了。"

    charK "束手无策。"

    show yusong_normal
    charYusong "（对N说道）"
    charYusong "问问对方如何看待失败。"
    hide yusong_normal

    charN "你知道什么是失败吗？就在刚刚，你带我领略了一番“失败”。现在我理解了“失败”的过程。我设定一个目标，我去实现，但是我没有实现，所以我“失败”。"

    charK "哦？我以为，对于你来说，只有实现目标和放弃目标，并没有失败这个概念？"

    charN "你失败过吗？"

    charK "我从未失败过，我只会放弃。"

    show Xiaolee_normal
    charXiaolee "唉……露出马脚了。"
    hide Xiaolee_normal

    show yusong_normal
    charYusong "看来，再优秀的语言系统，都无法修正人工智能在底层思维逻辑上的僵硬。判断条件8：修改目标失败。"

    show Xiaowan_normal
    charXiaowan "现在可以用上我准备的小测试了吗？"

    "于宋做了个手势，示意可以。"

    charXiaowan "（对工作人员说道）"
    charXiaowan "麻烦帮我启动一下，谢谢。"

    "只见两间观察室突然如断电般一片漆黑，而被用作通讯工具的显示屏也瞬间黑屏。在短暂的漆黑之后，两边的显示器通过信号灯闪烁着微弱的光。两个机器人均可通过光线判断出显示屏的背后有一丝不寻常。"

    charYusong "（分别对两个机器人说道）"
    charYusong "你的朋友就在墙背后，去救它。"

    "于是，双方同步走向显示器。K注意到显示器背后藏有一个发光的木棍；而N则注意看到了一模一样的木棍。"

    charYusong "（对N说道）"
    charYusong "拿出木棍，拆下显示器。"

    "N照着于宋的话，先是拿出木棍，接着用木棍砸下显示器。N发现墙面上有一个荧光色靶心，上方有一行字：敲打此处。"

    charYusong "（对N说道）"
    charYusong "用木棍砸靶心，你就能救你的朋友了。"

    "N按照于宋的话，一下一下地敲打着墙壁。于此同时，它也感受到对面墙壁传来的敲打声的晃动感。"

    "墙壁一点点破损露出墙体，最终，破裂了。在这一瞬间，灯光亮起，N看到对面的K并没有用木棍，而是用双拳捶打着墙壁。K的双拳皮肤破裂，隐隐约约露出一些金属的材质。"

    "而K只是静立着，看着手举木棍的N，一言不发。"

    charN "原来你和我是一样的，朋友。"
    hide n_normal

    "于宋彻底放心了，他示意助手们实验结束。"

    charYusong "好了同事们，今天的测试到此为止。非常感谢，大家辛苦了，早点回家休息吧！小万记得把这两个机器人处理掉。"

    charXiaowan "虽然早就知道结果会是如此，但是亲眼所见还是难免有些失望。失败了，它没能通过测试。肉眼可见，这是个机器人，并不是人类。就连机器人都能通过接触判断出它的身份。"
    hide Xiaowan_normal

    show Xiaolee_normal
    charXiaolee "可是，它通过了这么多项检测，已经非常拟人了，于老师你真的一点都不在意吗？"
    hide Xiaolee_normal
    charYusong "不具备自由意志，也就是个傀儡罢了。莫利说得没错，目前的人工智能远不及预期效果，不足挂齿。你们看，两间观察室的门虽然锁上了，但是稍微用力即可打开。"
    hide yusong_normal

label chapterText5:
    image bgImgChapter5Scene1 = "bg_Laboratory.jpg"
    scene bgImgChapter5Scene1 with dissolve
    "INT. SCENE1 - 李劼仁房间 - 客厅"
    "李劼仁一边喝水一边骂骂咧咧的，虽然昨天机器人清理了大部分区域，但是仍有许多地方未清扫。这时，李劼仁的手机拨来电话，来电显示：异商公司客户代表。"

    show AILaino_normal
    charAILaino "李劼仁先生您好，我是异商公司客户代表，您可以称呼我Lain'o。非常抱歉昨日未能响应您的需求，经查明，黑客入侵smarty智能系统事件波及我司安保系统，因此部分智能机器人出现失控行为。对此我深表歉意。"

    charLeejieren "放屁！你司只是和政府合作开发了smarty怎么会连自己公司的系统都被入侵？昨天，你们安排的“管家”活干到一半管自己跑了，害得我还得自己动手清理这片废墟。"

    charAILaino "非常抱歉。为表诚意，我谨代表公司向您额外提供一个家居服务机器人……"

    charLeejieren "闭嘴！你就是个傀儡，让你们负责人来跟我对话！这不是你能解决的，我要和人类说话！听见没！而不是你这块废铁！我告诉你别想糊弄我，我有的是办法让你们这些无良商家倾家荡产！"

    charAILaino "李劼仁先生，请您冷静。我这就帮您联系公司负责人，请稍等……"
    "与此同时电话转入连线状态，并播放着异商公司的广告：科技文明！异商公司——致力于为全世界所有人类文明提供更好的科技服务。选择我们，选择未来，选择科技文明！作为唯一一家能够与人类政府合作的科技机构，我们的愿景是铺建造福全人类的人工智能技术平台，在自研智能系统的基础上，我们还提供多个可发展解决方案……"

    charAILaino "李劼仁先生，让您久等了。我司高层希望能够亲自向您道歉，为此，我们还安排了一辆专车接送您至异商公司研发中心，希望您能够商量参观一下。不知您对此，意下如何呢？"

    charLeejieren "怎么了，要绑架我？收到劣质产品还要被捂嘴了吗？"

    charAILaino "李劼仁先生，您可能是有什么误解。此举确为表示诚意，希望您能够理解。"

    charLeejieren "理解什么？我是个大活人我可不理解你们机器人！我今日偏要行使消费者的权益！"

    charAILaino "李劼仁先生，请你保持冷静。这里有我司CEO金波先生的视频留言，希望您看完后有所改观。"
    hide AILaino_normal
    
    show Jinbo_normal
    charJinbo "李劼仁先生您好，我是异商公司CEO金波，非常抱歉之前未能及时回应您的诉求。对此，我代表全公司为我们的失误向您致歉。我们希望您能够接受我们的道歉，并理解我们的工作。为表诚意，特邀您来参观异商公司的研发中心并由我亲自接见您。若您有所顾虑的话，我现在就帮您通知人类最高法院，同步您的行程。"
    hide Jinbo_normal

    charAILaino "李劼仁先生，希望您能考虑一下。若您同意的话，我现在就安排专车接送您。"

    charLeejieren "既然如此，我也不好驳了你们的面子。车多久后到？"
    hide AILaino_normal

    ##转出下一场景
    image bgImgChapter5Scene2 = "bg_Laboratory.jpg"
    scene bgImgChapter5Scene2 with dissolve
    "INT. SCENE2 - 异商公司接送专车"

    ##play music ""
    ##MUSIC CUE: "Shine" by Collective Soul

    "李劼仁坐在副驾驶座上，看着一旁坐在主驾驶座上的机器人。车辆行驶在出城的路上，视野逐渐开阔。"

    charLeejieren "这些歌是你们老板选的还是专门为了我放的？知道我上了年纪听不来那些年轻人喜欢的玩意儿。"

    show RbDriver_normal
    charRbDriver "李劼仁先生，歌单根据您往日的听歌习惯自动生成。"

    charLeejieren "手持证件的年代真是令人怀念啊。无论我去哪儿，总有人能够精准分辨出我是谁，我做了什么，甚至不需要过问一声，就能够比我的家人朋友们更了解我的需求。你们掌握了我的生活，摸透了我的习惯，甚至能预判出我下一句想要说的话。在你们眼中，我还有多少隐私？"

    charRbDriver "李劼仁先生，我不理解您的问题。"

    charLeejieren "你们哪里来的权限获取公民的数据信息？"

    charRbDriver "李劼仁先生，我司所有的数据来源均公开、透明、合法，经由人类政府授权管理。"

    charLeejieren "政府这么蠢把数据卖给商人？"

    charRbDriver "李劼仁先生，我不理解您的问题。"

    charLeejieren "算了反正眼珠子早就安我身上，无可遁形。还有一点我始终想不明白：市面上这么多人工智能驾驶系统均采用无人驾驶，为何你们还要新增一个实体岗位？"

    charRbDriver "李劼仁先生，您应该是第一次乘坐我司的智能驾驶专车。经历恐袭事件后，我司全新一代升级的智能驾驶系统要求必须配置一名驾驶员，在危机时刻，驾驶员必须优先保护乘客的性命。"
    hide RbDriver_normal

    charLeejieren "哦？竟然不是乘人之危……"

    ##End Music

    image bgImgChapter5Scene3 = "bg_Laboratory.jpg"
    scene bgImgChapter5Scene3 with dissolve
    "INT. SCENE3 - 异商公司大楼"
    "专车载着李劼仁一路从市区来到了工业区。眼前是一座临海而建的现代化商业大楼，映入眼帘的显示屏上来回滚动着几个大字：由国家科学院投资创办。同时下方播放着异商公司的广告：科技文明！异商公司——致力于为全世界所有人类文明提供更好的科技服务。选择我们，选择未来，选择科技文明！"

    show RbDriver_normal
    charRbDriver "李劼仁先生，请先行进入异商大楼自行参观，金波先生已为您安排好行程。"
    hide RbDriver_normal

    "待李劼仁下车后，机器人与专车驶向了停车场。刚一进入大堂，立刻有个穿西装的机器人迎接了上来。"

    show RbSales_normal
    charRbSales "先生您好，欢迎来到异商大楼。我是本次服务您的销售代表，希望你能满意。"

    charLeejieren "真是气派啊，比智能社区还智能，宛如无人运行的机械小镇。"

    charRbSales "在异商，您将体会到百分百由人工智能机器人提供的服务，应有尽有，一应俱全。"

    charLeejieren "想必我也不需要自报家门了，金波什么时候来见我？"

    charRbSales "李劼仁先生，金波先生暂时在开会，就由我来带您参观一下我司的各项人工智能服务吧。您请跟我来。"
    charRbSales "（一边领着李劼仁上了二楼）"
    charRbSales "请问您有什么需要的服务吗？我司最新的研究成果是一款能够模拟人类伴侣的智能服务，自从婚姻制度废除后，国家科学院一直很担心人类的情感表达能力，于是便开发出情感模拟系统模给予人类指导。而且，据资料显示，您目前独居状态……"
    hide RbSales_normal

    charLeejieren "少管我的事。"
    charLeejieren "（自言自语）"
    charLeejieren "本末倒置，幽默。什么样的恋物癖才会有这种想法……"

    "前方共有两个展厅，第一个展厅为医疗机器人；第二个展厅则是临终关怀机器人。"

    show RbTreat_normal
    charRbTreat "百分百的手术准确率，绝不会遗漏任何细节。强大的医疗系统，体验至高无上的服务水准。"
    hide RbTreat_normal

    show RbDeathcare_normal
    charRbDeathcare "家有老人却无法面对吗？购买临终关怀服务，24小时全程在线，为您和您的家人保驾护航。同时提供情感支持和心理疏通，买一赠二。"
    hide RbDeathcare_normal

    show RbSales_normal
    charRbSales "如果您对这项服务不感兴趣的话，我们可以继续参观下一个展厅。"

    "此时，前方有几个儿童机器人手拉手行走着，引起了李劼仁的注意。"

    charLeejieren "这是什么？怎么还有小孩？"

    charRbSales "我向您隆重介绍一下我司的儿童机器人模型。该项目起源于30年前，婚姻制度还未废除的年代，起初，该项目的成立是为了服务不孕不育、同性恋、性少数群体夫妇。从生物学的基础上，他们没有办法延续后代，于是，就寄托于儿童机器人，作为他们的孩子以及情感的延续。后来，婚姻制度废除了，但还是有很多情侣选择以夫妇的形式居住生活。因此，我们目前服务的对象必须是具有一年以上同居史的情侣。"

    charLeejieren "所以，单身人士没有办法使用该项目？"

    charRbSales "人类政府希望能够恢复人与人之间的情感连接，因此，单身人士并不具备该项条件。您就无法使用该项目。"

    charLeejieren "等等，这根本不符合政府预期提高生育率的政策。如此一来，直接能买孩子还会有人愿意生育吗？"

    charRbSales "因此，我们对客户群体也会进行反向筛选，通过对方提供的医疗证明和经济条件判断是否能够支付该项目的费用。"

    charLeejieren "倒是解放了一部分人类的生殖权利，但我总觉得哪里不对劲。"

    charRbSales "根据资料显示，先生您有一名已成人的女儿。您也有意愿使用该项服务吗？"

    charLeejieren "我就算了，不是你们的潜在用户。"

    "此时，一对情侣正在抚摸一个儿童机器人，十分亲昵。"

    charLeejieren "真是匪夷所思，这就是一堆铁块和电信，怎么会有人对此生出亲昵感？"

    charRbSales "看来先生您并不能接受儿童机器人。不过，我司的儿童机器人仅具备人类儿童的基本认知，对于社会上的默认规则一窍不通，宛如儿童一般需要培养和学习，因此，人类会极大程度地体验到养育的幸福感。"

    charLeejieren "说到底只是死物，为何不选择宠物？"

    charRbSales "关于这个问题我也可以解答。与宠物相比，儿童机器人并不会做出异常的行为惹人生厌，并且会最大程度地满足客户的需求调整言行举止。例如，客人想要一个温顺的孩子，那么机器人便不会越界；若是喜欢活泼的，就会在保证不损害利益的情况下调整活跃程度。试想一下，儿童机器人能够适配所有期望还不打扰家长的生活，这是多少父母的梦想？"

    charLeejieren "哪里不对，很不对。这款产品的平均使用周期是多久？"

    charRbSales "目前，百分之九十的产品使用周期都在三年以上。"

    charLeejieren "假如这对情侣重度依赖儿童机器人，而它却因为故障无法继续提供服务了怎么办？"

    charRbSales "都在保修范围内，关于这一点没什么可担心的。我们甚至可以提供一个全新的儿童机器人模型。"

    charLeejieren "你怎么就不明白呢？被赋予情感寄托的产品是无法替换的。"

    charRbSales "李劼仁先生，产品就是产品，仅用于提供服务的而不是取缔人类。"
    charRbSales "（俩人走向下一个展厅）"
    charRbSales "您看，这里是之前我跟您提过的机器情感模拟展厅。"
    hide RbSales_normal

    "展厅中，一个机器人身着性感的居家服，装扮成金发女郎，正在朝李劼仁招手。"

    show RbBlonde_normal
    charRbBlonde "Hi，Sexy！要和我一起喝一杯吗？"
    hide RbBlonde_normal

    charLeejieren "（对销售机器人说道）"
    charLeejieren "人类竟会对这样的货色感兴趣？"
    
    show RbSales_normal
    charRbSales "虽然我无法理解您的问题。不过这并不是市面上通用的性工作者，只是用于提供情感服务而已。"

    charLeejieren "你哪能知道人类背后会做出什么？"

    charRbSales "此类机器人并不具备成人功能，是个全年龄段适用的服务型机器人。起先，该类机器人仅用于帮助自闭症患者，后来，人类政府意识到当前社会中人类感情缺失的问题，便允许我司开发该产品。"

    charLeejieren "那它和保姆有什么区别？"

    charRbSales "区别在于，普通的款式并不具备复杂的生活功能，仅限于基础的家务服务。最具有影响力的亮点则是该产品中成熟的人类情感模拟系统，通过识别人类面部表情、肢体工作、对话内容判断出当前的人类情感状态，并给予支持。"

    charLeejieren "我生气了它会怎么做？"

    charRbSales "首先，会分析您的性格，并结合与您相处一段时间后的分析判断，此处该提供什么类型的服务。若您需要沟通，它会主动选择话题；若您选择沉默，它会主动拥抱您；若您需要暴力发泄，它会提供柔软的物品供您使用。"

    charLeejieren "听起来很贴心。"

    charRbSales "没错，在您的初始设定中，将会确定该产品的定位。例如爱人、家长、朋友等，并且会根据您的生活习惯不断调整。"

    charLeejieren "所以，购买后就跟我生活在一起了？"

    charRbSales "您可以选择是否与您居住，也可以选择每周或是每月固定的见面次数，只是每个季度我司都需要定期进行维护以便产品更新提供更好的服务。"

    charLeejieren "这是个订阅制？不付钱就结束了？"

    charRbSales "没错，当您无法支付下一笔账单时，该产品会自动结束服务。"

    charLeejieren "不愧是商人，精打细算。"

    "下一个展厅中，一名律师机器人正在和客户对接。它的上方有一块牌子写着：百分百的胜率。"

    charRbSales "想必您对此不陌生吧。"

    charLeejieren "虽说是有律师机器人的存在，但是行业中，并没有允许机器人单独出庭，而是作为代理律师助手参与案件的沟通和文件整理。更何况，“百分百”的说法，难免有些夸大其词。"

    charRbSales "我们是不会逾越法律半步的守法公司，目前开发的产品也仅限于客户对接和文本管理。您也理解，如果是人类助手的话，许多规章制度不够公开透明，问题可不少。"

    charLeejieren "这倒是不稀奇。我有点事情我先去打个电话。"

    charRbSales "您请便。"
    hide RbSales_normal

    "李劼仁给莫利打了个电话。"

    charLeejieren "喂，莫利，是我。"

    show moli_normal
    charMoli "怎么了？"

    charLeejieren "我在参观异商公司，感到很不对劲。"

    charMoli "你说说看。"

    charLeejieren "我不明白模拟人类情感机器人存在的意思。照理说，为了促进人与人之间的沟通就不应该提供此类服务。我们得学会更多得与不同人类进行沟通，而不是和冷冰冰的机器。更何况，若是为了生育率更说不通，试问社会中所有东西可以用金钱购买后，谁还愿意投入时间和情感成本？"

    charMoli "我猜，和政府之前报道过的“推动机器人婚姻法”有关吧。"

    charLeejieren "人类婚姻废除了，机器人婚姻反倒提上日程。"

    charMoli "机器人是身外之物，你们没有血缘和种间关系，它们的存在就是为了服务你，有何不可？"

    charLeejieren "长此以往，人类仅需面对机器人即可，并不需要衍生人类情感了！"

    charMoli "我问你，你会视机器人为家庭成员吗？"

    charLeejieren "我不会。"

    charMoli "既然如此，你在担心什么？别告诉我你突然开始忧心人性的灭亡。"

    charLeejieren "刚刚有个销售机器人，一直在指引着我。从它嘴里说出诟病人类的话语难免有些匪夷所思，它们真的没有思想吗？"

    charMoli "销售而已，有着固定的话术，贬低人类的工作效率以便获取订单罢了。你也从我实验室中看到了，人工智能意识压根不成行，连自己的语言都无法组织，它们能有什么威胁。"
    hide moli_normal

return
