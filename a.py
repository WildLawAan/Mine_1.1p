import time,pygame


def MINE1():
    pyblo5 = pygame.image.load("mine1.jpeg")
    pygame.init()
    pygame.mixer.Sound.play(once)

    display_width = 800
    display_height = 800

    ourScreen = pygame.display.set_mode((display_width, display_height))

    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            ourScreen.blit(pyblo5, (0, 0))
        pygame.display.flip()
    pygame.quit()
    print(" ")
    print("엔터를 눌러주세요")
    u = input()

    def inputs2(item):
        print("   어디서 열쇠를 찾아 보시겠습니까?")
        a2 = input("  1.가방   2.책상서랍   3.침대   4.문:")
        if a2 == '1':
            print("교과서 몇권이 다인것 같다......")
            print("그러고 보니 책상서랍에 뭔가 깜빡한게 있었던것 같은데....")
            return inputs2(item)
        elif a2 == '2':
            if item == [] or item == ['key']:
                print("아!........")
                print(" '러브레터' 를 입수했습니다!")
                print("맞다……. 오늘 그애에게 고백할 생각이었는데…… ")
                print("아직 뭐가 뭔지 혼란스럽지만 일단 챙겼다.")
                item = item + ['love']
                return inputs2(item)
            else:
                print("더 볼 것은 없는것 같다......")

                return inputs2(item)
        elif a2 == '3':
            if item == ['key'] or item == ['love', 'key']:
                print("왜 열쇠가 여기있던거지.....?")
                return inputs2(item)
            else:
                item = item + ['key']
                print("어제까지 정말 잘 자던 침대다......!!!")
                time.sleep(1)
                print("열쇠를 입수했습니다!")
                print("뭐지 이게 왜....여기?")
                print("일단 나가자. 뭐 놓고온것은 없겠지?")
                return inputs2(item)
        elif a2 == '4':
            if item == [] or item == ['love']:
                print("그래도 열리지 않는다......")
                print("모든 곳을 다 찾아봐야 할것같다.")
                return inputs2(item)
            elif item == ['key']:
                print("........")
                time.sleep(0.5)
                print("왜인지 차마 발이 떨어지지 않는다.")
                time.sleep(0.5)
                print("아주 중요한걸 나둔 기분이 들어....")
                time.sleep(0.5)
                print("더 찾아볼때가 있는거 아닐까? '서랍'이라든가..")
                return inputs2(item)
            else:
                print("어 열렸다!")
                time.sleep(1)
                print("순간 하얀 빛을 본 기분이었다.")
        else:
            print("4숫자 중에서만 선택해 주세요.")
            return inputs2(item)

    def inputs(a, item):
        if a == '1':
            print("......")
            time.sleep(2)
            print("역시 방문을 열어야 겠다.")
            time.sleep(1)
            a = input("선택지로 돌아간다.:")
            return inputs(a, item)
        elif a == '2':
            print("방문을 잡아 당겼지만 방문이 열리지 않는다. 왠지 모르겠지만….")
            time.sleep(0.5)
            print("근데 내 방문은 안에서만 잠글 수 있는거 아니었나?")
            time.sleep(0.5)
            print("일단 열쇠를 찾아보는것이 좋을 것 같다.")
            return inputs2(item)
        else:
            print("1과 2 중에서만 선택해 주세요")
            a = input("선택해주세요:")
            return inputs(a, item)
    print("내 방인것 같다.")
    time.sleep(0.5)
    print("                   휴대폰 문자")
    time.sleep(0.5)
    print("   엄마 - 지금 대체 왜 이리된건지 모르겠구나…. 가능한 빠르게 연락주렴")
    time.sleep(0.5)
    print("통화권에서 벗어나있다. 아마 이게 마지막 문자였을것 같다.")
    time.sleep(0.5)
    print("익숙한 곳이다 내방 같은데? 근데 통화권 밖인건왜지?")
    time.sleep(0.5)
    print("일단 방문을 열어보는것이 좋을것 같다.")
    time.sleep(0.5)
    print("선택 1 그냥 기다린다.\n    2 방문을 연다.")
    a = input("     선택해주세요:")
    item = []
    inputs(a, item)


def MINE2():
    time.sleep(2)
    print("엔터를 눌러주세요")
    u = input()
    # Mine-2 (벚꽃핀 봄에)
    # -*- coding: utf-8 -*-
    # UTF-8 encoding when using korean
    item = []

    def school():
        print("분명히 문을 연건데……?")
        print("나 왜 교실에 있는거지?")
        print("친구1 - 야 뭐하냐, 오늘 고백한다더니 넋이 나가셨구만?")
        print("어 어어….")
        print("친구1 - 허허 야 나 먼저 나간다. 빨리 나와!")
        print("친구1은 교실문을 닫고 나간다.")
        print(" ")
        print("엔터를 눌러주세요")
        u = input()

        print("뭐야 이건? 아 나 고백하기로 했었지...나가봐야 겠다")
        print("덜컹!")
        print("응??? 문이 왜 안 열리는 거야?")
        print("아니 교실문은 누가 밖에서 열쇠로 잠궈야 하는 거 아닌가?")
        print("일단.. 주위를 살펴보자")

    def school1(item):
        answer1 = input("   무엇을 살펴볼까?\n   1.거울   2.사물함   3.책상   4.교실문")
        if (answer1 == '1'):
            if ('uniform' in item):
                print("오케이!완벽해!")
                return school1(item)
            else:
                print("거울이다 근데…")
                print("나 체육복이네...?")
                print("아 지금 체육시간이었는데 음….")
                print("고백하러 갈때 ‘체육복’은 좀 아닌것 같은데……")
                return school1(item)

        if (answer1 == '2'):
            if ('uniform' in item):
                print("교복으로 이미 갈아입었다.")
                return school1(item)
            else:
                answer = input("‘교복’이 있다 갈아입으시겠습니까?(o/x)")
                if (answer == 'o' or answer == 'O'):
                    item = item + ['uniform']
                    print("교복을 입었다. 역시 나의 핏은 최고다.")
                    return school1(item)
                elif (answer == 'x' or answer == 'X'):
                    print("남자는 역시 체육복…진정한 남자가 된 듯 하다.")
                    return school1(item)
                else:
                    print("o/x를 입력해주세요.")
                    return school1(item)
        elif (answer1 == '3'):
            if ('flower' in item):
                print("봄이다.")
                return school1(item)
            else:
                print("내 책상이고 옆은 ‘그애’의 자리다. 그래 여기서 계속 옆에 있던 그애가 좋아진것 같다…… 왠지 그립다. 왜 이런 기분이 들지?")
                print("어!?")
                print("‘벚꽃잎’을 입수했습니다.")
                item = item + ['flower']
                print("밖에서 벚꽃잎이 날아왔다. 그래 봄이었구나 지금은….")
                return school1(item)

        if (answer1 == '4'):
            if (len(item) != 2):
                print("역시 열리지 않는다……")
                return school1(item)

            else:
                print("응? 열린다. 일단 빨리 밖으로 나가자.")
                print("교실 밖 벚꽃나무 아래")

                print(" ")
                print("엔터를 눌러주세요")
                u = input()

                print("그애 - 음…. 왜 불렀어?")
                print("저기….. 어 …. 나. 니가…")
                print("순간 벚꽃이 휘날리는듯한 ")
                print("아니 정말 벚꽃이 휘날리면서 내 시야를 가렸다.")
        else:
            print("잘 생각해서 다시 입력하자")
            return school1(item)

    school()
    school1(item)


def MINE3():
    time.sleep(2)
    import pygame
    pyblo5 = pygame.image.load("mine2.jpeg")
    pygame.init()
    pygame.mixer.Sound.play(dog)

    display_width = 800
    display_height = 800

    ourScreen = pygame.display.set_mode((display_width, display_height))

    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            ourScreen.blit(pyblo5, (0, 0))
        pygame.display.flip()
    pygame.quit()
    print("엔터를 눌러주세요")
    u = input()
    # Mine-3  (그 여름 친구들과 계곡에 갔다)
    # (벚꽃잎은 인벤토리에 있으면 좋겠다.)
    item = []

    def trip():
        print("??? 여긴 또 어디지?")
        print("      휴대폰 문자")
        print("   재경 - 니가 그리워……")
        print("통화권에서 이탈된 것 같다. 이게 마지막 문자다.")
        print("태현 - 너 뭐하냐? 후딱 나가자고! 모처럼 우리끼리 놀러온거잖아.")

        print(" ")
        print("엔터를 눌러주세요")
        u = input()

        print("그렇다. 모처럼 아는 지인이 별장을 대여해줘서 주위에 사람이라곤 우리밖에 없다.")
        print("아….아! 그랬지 모처럼 정말 친한 친구들하고 여행 계획을 짜다가")
        print("아는 지인덕에 별장을 구해서 계곡에 놀러온거였다.")
        print("태현 - 모처럼 주위엔 우리밖에 없는 정말 놀기 좋은 공간에서 넋을 놓다니…….")
        print("      야! 난 물에 들어가 있을게! 짐 다 챙겨서 나와!")
        print("태현은 문을 닫고 나갔다.")
        print("음….. 잠깐! 왜 짐을 나 혼자 챙겨?!")
        print("문을 열려고 했지만 잠겨있다.")

        print(" ")
        print("엔터를 눌러주세요")
        u = input()

        print("뭐야.. 대체 뭐가 어떻게 되고있는건지는 모르겠지만 문이 잠겼는데?")
        print("?? 뭐야 이건 키패드??")
        print("뭐라고 적혀있는……")
        print("당신은 몇명이서 여행을 왔나요?")  # (이거 사진으로 낚을수 있을까요?)
        print("숫자를 입력해야 되는거야????")

    def trip2(item):
        print("   어디를 조사해 보시겠습니까?(숫자로만 입력)")
        f = input("    1.가방   2.짐들   3.이불   4.문")
        if (f == '1'):
            if ('bag' in item):
                print("아까 봤던 곳이다.")
                return trip2(item)
            else:
                print("음…. 별것 없는것 같은..!!")
                print("‘사진기’를 입수했다.")
                print("친구들이랑 사진 한 장 찍으려고 가져온 사진기다")
                print("챙겨가야겠지?")
                item = item + ['bag']
                return trip2(item)

        elif (f == '2'):
            if ('baggage' in item):
                print("아까 봤던 곳이다.")
                return trip2(item)
            else:
                print("…… 이걸 내가 챙겨가야 하나…..?")
                print("그래 내가 인심쓴다.")
                print("‘짐들’을 입수했다.")
                item = item + ['baggage']
                print("오늘 술을 내가 사나봐라")
                return trip2(item)

        elif (f == '3'):
            if ('picture' in item):
                print("아까 봤던 곳이다.")
                print("그래도 사진을 한 번 더볼까..")
                import pygame
                pyblo5 = pygame.image.load("사진.jpeg")
                pygame.init()

                display_width = 800
                display_height = 800

                ourScreen = pygame.display.set_mode((display_width, display_height))

                finished = False
                while not finished:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            finished = True
                        ourScreen.blit(pyblo5, (0, 0))
                    pygame.display.flip()
                pygame.quit()

                return trip2(item)
            else:
                print("이불이다.")
                print("술 마시고 자던 이불이라 잘 기억은 나지 않지만….. 그랬다.")
                print("어젠 잠 안 자고 놀았으니…..근데 쟤들은 체력도 좋다.")
                print("어제 그렇게 놀고 나서 저렇다니…")
                print("응?")
                print("‘찍은 사진’을 입수했다.")
                import pygame
                pyblo5 = pygame.image.load("사진.jpeg")
                pygame.init()

                display_width = 800
                display_height = 800

                ourScreen = pygame.display.set_mode((display_width, display_height))

                finished = False
                while not finished:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            finished = True
                        ourScreen.blit(pyblo5, (0, 0))
                    pygame.display.flip()
                pygame.quit()
                item = item + ['picture']
                print("아…..애들과 찍은 사진이다.")
                # (날짜가 오늘)
                print("내가 중앙에 있고 주위로 애들이 같이 뛰면서 찍혀있다.")
                print("근데 이거 언제 찍은 거지? 찍은 기억이 있는듯 없는듯 한데?")
                return trip2(item)
        elif (f == '4'):
            if (len(item) != 3):
                print("……")
                print("나는 여기서 더 해야할 것이 있다.")
                return trip2(item)
            else:
                while (len(item) == 3):
                    f1 = input("당신은 몇명이서 여행을 왔나요?")
                    if (f1 == '6'):
                        break
                    else:
                        print("틀렸습니다.")
                        print("단서를 다시 한 번 살펴보세요.")
                        return trip2(item)
        else:
            print("4개의 숫자중에서만 선택해주세요.")
            return trip2(item)

    trip()
    trip2(item)


def MINE4():
    time.sleep(2)
    print("엔터를 눌러주세요")
    u = input()
    item = []

    def valley():
        print("문만 열었는데.. 계곡이네?")
        print("태현 - 야 뭐 기어오냐? 빨리 짐들고 와!")
        print("어.. 어! 지금 갈게!")
        print("일단 놀자! 간만에 친구들하고 놀러온건데 재미있게 놀지 않으면 손해니까")
        print("현창 - 야 빠트려 이거!")
        print("이게 뭐하는 어어어어")

        print(" ")
        print("엔터를 눌러주세요")
        u = input()

        print("풍덩!")
        print("물에 시원하게 빠져 버렸다…..")
        print("바로 나왔지만 다들 벌써 멀찍이 물에서 떨어져있다.")
        print("준혁 - 야 사진이나 찍자 모여봐!")
        print("태현 - 야 후딱와! 센터 세워줄게!")
        print("그래…..봐준다.")
        print("준혁 - 찍는다!")
        print("근데 이거…. 찍은 사진 아닌가?")

        print(" ")
        print("엔터를 눌러주세요")
        u = input()

        print("사진찍는 소리가 나면서 순간 정신이 멍해졌다.")
        print("태현 - 야 뺄거야? 빨리 술마셔!")
        print("응? 첫날부터 계속 먹으니 지치는데….")
        print("태현 - 넌 내 두배는 마시면서 왜 그리 빼냐?")
        print("동진 - 근데 우리 모레 아침 일찍 가야 하잖아. 슬슬 그만 마실 때 되지 않았냐?")
        print("현창 - 마셔 마셔 먹고 뒤져!")
        print("승환 - 각자 주량만큼 매일 밤 마실 거 맞춰서 술 산거야.")
        print("      죽을때까지 먹어보기로 했잖아!")
        print("      각자 자기 마실만큼은 마셔!")
        print("아 알았어!!")

        print(" ")
        print("엔터를 눌러주세요")
        u = input()

        print("그렇게 정신없이 마시다보니…..")
        print("어찌어찌 오늘 마시자고 했던 것만큼은 마신것 같다…")
        print("승환 - 야 태현이 간 것 같은데? 현창이는 나랑 똑같이 마시면서…..왜 내꺼까지 마신거지….. ")
        print("준혁 - 꼭 이렇게 남 술먹이는 놈들이 가장 먼저 간다니까….. ")
        print("동진 - 야 먼저 얘 데리고 가야겠다. 나머지 들고와! ")


        print(" ")
        print("엔터를 눌러주세요")
        u = input()

        print("짐 정리를 해야... 아 근데 왜 이리 정신이 아득하지?")
        print("들어가야하는데……")
        print("겨우겨우 문까지는 걸어왔는데...")
        print("이거 뭐냐? 정신 차리고 어……")
        # (이거 사진을 흐릿하게 보이게 할 수는 없을까요?)
        print("키…패…드..??!!!!")
        print("#Day-우리 총 여행일은 몇일이지?(집가는날 포함)")
        print("이게….뭔…..")

    def valley1():
        print("   어디를 조사해 보시겠습니까?(숫자로만 입력)")
        v = input("   1.식탁   2.쓰레기장   3.계곡   4.문")
        if (v == '1'):
            print("술병이 어지럽게 어질러져 있다.")
            print("이걸 다 치워야 하나….? 하오…..")
            import pygame
            pyblo5 = pygame.image.load("식탁.jpeg")
            pygame.init()

            display_width = 800
            display_height = 800

            ourScreen = pygame.display.set_mode((display_width, display_height))

            finished = False
            while not finished:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        finished = True
                    ourScreen.blit(pyblo5, (0, 0))
                pygame.display.flip()
            pygame.quit()
            # (술병 나와있는 사진이 필요합니다!7병)
            return valley1()

        elif (v == '2'):
            print("이런… 여긴 버릴 자리가 없네… 상관없나?")
            print("여긴 궤짝 채로 버려져있네….")
            import pygame
            pyblo5 = pygame.image.load("쓰레기장.jpeg")
            pygame.init()

            display_width = 800
            display_height = 800

            ourScreen = pygame.display.set_mode((display_width, display_height))

            finished = False
            while not finished:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        finished = True
                    ourScreen.blit(pyblo5, (0, 0))
                pygame.display.flip()
            pygame.quit()
            # (이것도 사진!)
            # print("8병")
            print("어라 그리고 이거는….")
            import pygame
            pyblo5 = pygame.image.load("메모.jpeg")
            pygame.init()

            display_width = 800
            display_height = 800

            ourScreen = pygame.display.set_mode((display_width, display_height))

            finished = False
            while not finished:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        finished = True
                    ourScreen.blit(pyblo5, (0, 0))
                pygame.display.flip()
            pygame.quit()
            print("메모다. 일부분이 찢겨져 있다.")
            print("근데 이게 뭐더라…? 마트 갈 때 챙겼던 것 같은데…")
            return valley1()

        elif (v == '3'):
            print("엊그젠 여기서 마셨나….?")
            print("우리가 마신 소주병 다 여기있네")  # (소주 계곡에 담가 놓기도 하죠?)
            print("여기서 몇일을 보낸거야……")
            import pygame
            pyblo5 = pygame.image.load("밤계곡.jpeg")
            pygame.init()

            display_width = 800
            display_height = 800

            ourScreen = pygame.display.set_mode((display_width, display_height))

            finished = False
            while not finished:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        finished = True
                    ourScreen.blit(pyblo5, (0, 0))
                pygame.display.flip()
            pygame.quit()
            print("애들이랑 이렇게 다시 여행 올 수 있으려나? 이젠 다들 바쁘게 사니까 힘들겠지….. ")
            print("그래 이렇게 추억이라도 쌓아야지!")

            return valley1()

            # 여행은 5박 6일 입니다.
            # 지금은 넷쨰날 밤
            # 그리고 총 주량은 9병 입니다.
            # 그러니까 대화에서
            # ‘먹을 만큼 샀다고 했으니까 술병 개수로 몇박 머물 작정이었는지 알아야하고 day니까 거기에 1을 더해야 하죠 집가는 날도 있으니까요.
            # 여행은 총 6일이죠

        elif (v == '4'):
            while (v == '4'):
                v1 = input("#Day-우리 총 여행일은 몇일이지?(집가는날 포함)")
                if (v1 == '6'):
                    print("“아 열었다!”")
                    print("“야 뭐하냐? 가야지!!”")
                    print("“어..어어”")
                    print("맞다 5박6일의 여행이 끝났다.")
                    print("진짜 친한 친구들하고 같이 와서 즐거웠던 것 같다.")
                    print("이젠 각자의 일이 바빠서 힘들겠지만… 우린 다시 모일 수 있는 거겠지?")

                    print(" ")
                    print("엔터를 눌러주세요")
                    u = input()

                    print("“야 다같이 마지막으로 사진찍자!“")
                    print("“그래! 다들 모여봐!”")
                    print("“자 찍는다 하나.. 둘…”")
                    print("그래 언젠가 또 이런 추억을 쌓을 수 있겠지.")
                    print("“셋!”")
                    print("카메라 셔터에서 눈부신 빛이 터져나왔다.")
                    print("그리고 또 의식이 아득해져 갔다.")
                    break
                else:
                    print("틀렸습니다.")
                    print("단서를 다시 한 번 살펴보세요.")
                    return valley1()
        else:
            print("4개의 숫자중에서만 선택해주세요.")
            return valley1()

    valley()
    valley1()


def MINE5():
    time.sleep(2)
    import pygame
    pyblo5 = pygame.image.load("mine3.jpeg")
    pygame.init()
    pygame.mixer.Sound.play(memory)

    display_width = 800
    display_height = 800

    ourScreen = pygame.display.set_mode((display_width, display_height))

    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            ourScreen.blit(pyblo5, (0, 0))
        pygame.display.flip()
    pygame.quit()
    print("엔터를 눌러주세요")
    u = input()

    def friends():
        print("         휴대폰 문자-")
        print("   친구 - “후딱 일어나지 그러냐…..”")
        print("전화가 꺼졌다….")
        print("“네 끝난 분은 바로 집에 가셔도 됩니다.”")
        print("어라? 그러니까 여기는….")
        print("“그럼 실습을 시작하겠습니다.”")
        print("아 그래 프로그래밍 실습 시간이다.")

        print(" ")
        print("엔터를 눌러주세요")
        u = input()

        print("“문제는 재귀 함수 입니다.”")
        print("문제")
        print("Return 뒤에 뭐가 들어가야 할까요?(띄어 쓰기 없이 작성해 주세요.)")
        print("def fac0(n):")
        print("    def loop(n,sum):")
        print("         if n>0:")
        print("              return loop(n-1,sum*n)")
        print("          else:")
        print("              return ??")
        print("     return loop(n,1)")
        i = 0
        while True:
            a = input("return ??")
            if (a == 'sum'):
                break
            elif (i == 2):
                print("hidden ending!!!!!!!!!!!!")
                time.sleep(2)
                import pygame
                pyblo5 = pygame.image.load("f.jpeg")
                pygame.init()
                pygame.mixer.Sound.play(give)

                display_width = 800
                display_height = 800

                ourScreen = pygame.display.set_mode((display_width, display_height))

                finished = False
                while not finished:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            finished = True
                        ourScreen.blit(pyblo5, (0, 0))
                    pygame.display.flip()
                pygame.quit()
                print("난 그 수업에서 f를 받고 말았다.")
                print("이런 내가 뭘 할수 있을까....")
                print("공부할 의욕이 없어지고 많은 의욕이 떨어져 버렸다.")
                print("??-쩝......")
                print("??-선택지로 갔다오라고")
                print("??-가능하면 다시 보길 바라")
                choice()
            else:
                print("f가 보인다…(틀렸어요!)")
                i = i + 1

        print(" ")
        print("엔터를 눌러주세요")
        u = input()

        print("“다 풀었다!”")
        print("“야 다 풀었으면 밥먹으러 가자!”")
        print("“뭐 먹으러 갈건데?”")
        print("“고기 먹자 고기! 프기끝날때 마다 너무 힘들어……”")
        print("“그래 가자!”")

        print(" ")
        print("엔터를 눌러주세요")
        u = input()

        print("우리끼리 고기집으로 왔다.")
        print("“아… 자퇴하고 싶다…..”")
        print("“정신차려! 우리 아직 별로 겪지도 않았잖아….”")
        print("다들 그런것 같다. 누군가는 자신의 적성에 맞고 누군가는 맞지 않는다.")
        print("그 가운데에 나는…")
        print("“넌 할만하냐?”")
        print("“넌 할만하냐고 코딩”")
        print("“나도 뭐 잘하지는 않으니까……”")
        print("“그러냐…… 하아….”")
        print("다들 그런 것 같다. 자기가 이 학과에 맞다고 느끼는 애들이 있고, 아닌 애들이 있다.")
        print("그 와중에 나는 어떤 걸까……?")
        print("내가 하고 싶은 것은 무엇일까?")

        print(" ")
        print("엔터를 눌러주세요")
        u = input()

        print("“야 얘 취한 것 같은데...?”")
        print("“어휴….. 내가 데리고 갈게, 슬슬 일어나자.”")
        print("밖으로 나와서 애들을 보내고 혼자 집에 걸어가는 길이다.")
        print("“내가 하고 싶은 것이라……”")
        print("늘 생각하라 하지만, 늘 딜레마에 빠져버리고 마는 주제다.")
        print("그런 생각을 하던 사이에, 어느새 방에 도착해 버렸다.")

        print(" ")
        print("엔터를 눌러주세요")
        u = input()

        print("“내 꿈은 뭐였으려나…”")
        print("“찰캌!”")
        print("………음??")
        print("문을 확인해보니까 문이…잠겼다?")
        print("뭐야 이거….")

    def friends2(item):
        print("  어디를 조사해 보시겠습니까?(숫자로만 입력)")
        f = input("    1.옷장   2.책장   3.침대   4.문")

        if (f == '1'):
            if ('boy' in item):
                print("아까 봤던 곳이다.")
                return friends2(item)
            else:
                print("내 옷장이다. 참 옛날 옷까지 별의별게 다 있다.")
                print("어라? 이건….. ‘보이 스카우트 복장’을 발견했습니다.")
                item = item + ['boy']
                print('"그러고 보니 초등학교 때 이런 것도 했었구나…"')
                print("그 때 내 꿈은 경찰관이었던가?")
                print("경찰관이 되겠다던 꿈은 어느샌가 사라져버렸다.")
                return friends2(item)

        elif (f == '2'):
            if ('album' in item):
                print("아까 봤던 곳이다.")
                return friends2(item)
            else:
                print("음…!")
                print("'졸업앨범세트'를 입수했습니다.")
                item = item + ['album']
                print("졸업앨범을 열어보면서 초,중,고 시절의 내 꿈을 볼 수 있었다.")
                print("난 참 꿈이 많았었구나…")
                print("하지만 고등학교의 꿈을 보면 드는 생각은…")
                print("내가 정말 하고싶었던 일이라기보다는 현실과 타협한 느낌이다.")
                return friends2(item)
        elif (f == '3'):
            if ('key' in item):
                print("아까 봤던 곳이다.")
                return friends2(item)
            else:
                print("왠지…")
                print("'열쇠'를 발견했습니다.")
                item = item + ['key']
                print("난 왠지 여기서 열쇠를 찾을 것을 알고 있었던 기분이다.")
                print("뭔가 익숙해진 것 같다…")
                return friends2(item)
        elif (f == '4'):
            if (len(item) != 3):
                print("……")
                print("여기서 나는 더 해야할 것이 있다.")
                return friends2(item)
            else:
                print("내가 참 많은 꿈을 가지고 잃어가며 살았던 삶을 되돌아보았다.")
                print("그렇게 내가 다가간 결론은…")

                print(" ")
                print("엔터를 눌러주세요")
                u = input()

                print("내겐 '지금'밖에 남아있지 않다는 것이다.")
                print("앞으로 내가 어떤 일을 하던간에…")
                print("내가 변화시킬 수 있는 것은 그거 하나밖에 없었다.")
                print("그렇게 나는 문을 열었다.")
        else:
            print("4개의 숫자중에서만 선택해주세요.")
            return friends2(item)

    friends()
    item = []
    friends2(item)


def MINE6():
    time.sleep(2)
    print("엔터를 눌러주세요")
    u = input()
    # -*- coding: utf-8 -*-
    # UTF-8 encoding when using korean
    # Mine-6
    item = []

    def hackathon(item):
        print("여기는…..")
        print("“야 정신차려! 이제곧 시작이잖아!”")
        print("아… 알것같다. 바쁜 분위기, 모두의 긴장한 모습, 그리고 내가 ‘지금’에 집중하다가 오게된 과정")

        print(" ")
        print("엔터를 눌러주세요")
        u = input()

        print("“후딱 준비해!”")
        print("해커톤 대회다.  일단.. 시작해보자.")
        # 점수 뺏기 게임 같은 알고리즘 없으려나?
        # 일단 여기서는 생각해 보는걸로
        print("해커톤을 시작합니다! (우승하세요!)")
        import random

        def num1(one):
            while not (
                                                            one == '2' or one == '1' or one == '3' or one == '4' or one == '5' or one == '6' or one == '7' or one == '8' or one == '9' or one == '0'):
                one = input("숫자만! 그리고 0과9사이에서 중복되지 않게!!!:")
            return one

        print("자 게임을 시작하죠!")
        print("코인은 55개 스트라이크 수와 볼수에 관련해서 코인이 차감됩니다!!")
        print("(코인이 차감되는건 규칙은 알아서 알아내세요 하!하!하!)")
        print("숫자 외에는 눌러도 되지만 재입력을 요구드릴 겁니다.")
        print("숫자는 0부터 9까지!! 중복없이!!!!")

        class get_number(object):
            def __init__(self, name):
                self.name = name

        class decision(object):
            def __init__(self, name, tnumber, inumber, coin):
                self.name = name
                self.tnumber = tnumber
                self.inumber = inumber
                self.coin = coin

            def results(self):
                self.count = 0
                self.strike = 0
                sum = 0
                for k in range(4):
                    if self.tnumber[k] == self.inumber[k]:
                        self.strike = self.strike + 1
                for i in self.tnumber:
                    for j in self.inumber:
                        if i == j:
                            self.count = self.count + 1
                self.count = self.count - self.strike
                print(self.strike, "스트라이크!!")
                print(self.count, "볼!")
                if (self.strike == 4):
                    self.coin = self.coin + 100000
                else:
                    self.coin = self.coin - (4 - self.strike) * 2 - (4 - self.strike - self.count) * 1
                print(self.coin, "남은코인")
                print(self.inumber, "이숫자를 입력하셨습니다")
                return self.coin

        class Reader:
            def get_name():
                name = input("숫자야구로 플레이 하겠습니다(엔터를 눌러주세요)")
                return name

            def input_number():
                inumber = []
                one = input("첫번째 숫자!:")
                one = num1(one)
                one = int(one)
                two = input("두번째 숫자!:")
                two = num1(two)
                two = int(two)
                while (one == two):
                    two = num1(two)
                    two = int(two)
                three = input("세번째 숫지:")
                three = num1(three)
                three = int(three)
                while (two == three or one == three) or three > 9 or three < 0:
                    three = num1(three)
                    three = int(three)
                four = input("네번째 숫자!!:")
                four = num1(four)
                four = int(four)
                while (one == four or two == four or three == four) or four > 9 or four < 0:
                    four = num1(four)
                    four = int(four)

                inumber.append(one)
                inumber.append(two)
                inumber.append(three)
                inumber.append(four)
                return inumber

        class numbercontroller(object):
            def __init__(self, pname, coin):
                self.pname = pname
                self.coin = coin

            def play(self, t_number_list):
                print("새게임!!")
                get_number(self.pname)
                self.tnumber = t_number_list
                self.inumber = Reader.input_number()
                return decision.results(self)

        def main():
            print("해커톤 대회에 온 당신 코인이 다되기 전에 답을 찾아내세요(숫자야구!")
            player_name = Reader.get_name()
            t_number_list = random.sample(range(0, 10), 4)

            game = numbercontroller(player_name, 60)
            while True:
                c = game.play(t_number_list)
                if c > 100:
                    print("당신이 우승했습니다!")
                    break
                elif c == 50:
                    print("Hidden ending!!!!!!!!!!!!!!!!!!!!")
                    time.sleep(1)
                    import pygame
                    pyblo5 = pygame.image.load("카지노.jpeg")
                    pygame.init()
                    pygame.mixer.Sound.play(aa)

                    display_width = 800
                    display_height = 800

                    ourScreen = pygame.display.set_mode((display_width, display_height))

                    finished = False
                    while not finished:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                finished = True
                            ourScreen.blit(pyblo5, (0, 0))
                        pygame.display.flip()
                    pygame.quit()
                    print("운명마저 바꿔버릴 운")
                    print("나- 난 알고보니 도박에 천부적 재능이 있던 것일까?")
                    print("그렇게 나는 라스 베거스로 떠나고 다른 길을 찾았다.")
                    print("내운은 운명마저 바꿔버릴수 있었던 걸까???")
                    time.sleep(3)
                    print("??-이렇게 될줄이야...")
                    print("??-처음 save 에서 돌아오라고 기다릴테니")
                    quit()
                elif c <= 0:
                    print("당신이 졌어요……")
                    import pygame
                    pyblo5 = pygame.image.load("트로피.jpeg")
                    pygame.init()
                    pygame.mixer.Sound.play(give)

                    display_width = 800
                    display_height = 800

                    ourScreen = pygame.display.set_mode((display_width, display_height))

                    finished = False
                    while not finished:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                finished = True
                            ourScreen.blit(pyblo5, (0, 0))
                        pygame.display.flip()
                    pygame.quit()
                    print("재도전 하실거죠?")
                    a = str(input("o,x로 입력해 주세요."))
                    while not (a == 'o' or a == 'x'):
                        a = str(input("o,x로 입력해 주세요!!!!"))
                    if (a == 'o'):
                        print("??-이번엔 통과해 보라고")
                        print("??-처음 선택지 에서 하면 될거야")
                        choice()
                    else:
                        quit()

        main()

        # 숫자야구 알고리즘 짜놓은거 쓰죠!

        print("아….. 끝났다….")
        print("“야…….. 이겼다!!”")
        print("“와…. 끝났다!!!!!!")
        print("기뻐하는 우리…..")
        print("기쁘다. 내가 무언가를 해내고 성취해 냈다는 것이")
        print("그래, 이 땐 정말로 기뻤던 것 같다.")

        print("엔터를 눌러주세요")
        u = input()

        print("“트로피다!”")
        print("“야 이거 니가 들어라!”")
        print("“트로피 들고 두손 올려봐!”")
        item = item + ['트로피']
        print("내가 해왔던 일, 그저 최선을 다 할 수 있었던 일이었기에 더욱이 그랬다.")
        print("난 이 느낌을 잊고 있었다.")
        print("분명히 ‘그땐’……..어?")
        print("“야 붙어 붙어!”")
        print("잠깐 분명히… 그래 ‘하얀 빛’이 있던 기억이….")
        print("“하나, 둘,셋 !”")
        print("난 셔터 빛, 흰빛에 빨려 들어가는 느낌을 받았다.")

    hackathon(item)


def MINE7():
    time.sleep(2)
    import pygame
    pyblo5 = pygame.image.load("mine4.jpeg")
    pygame.init()
    pygame.mixer.Sound.play(home)

    display_width = 800
    display_height = 800

    ourScreen = pygame.display.set_mode((display_width, display_height))

    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            ourScreen.blit(pyblo5, (0, 0))
        pygame.display.flip()
    pygame.quit()
    print("엔터를 눌러주세요")
    u = input()

    def parents():
        print("“뭐해?”")
        print("어, 그러니까….엄마?")
        print("“잠시 쉬고 단체 사진 찍도록 하겠습니다!”")
        print("사진사 복장을 하고있는 사람이 나간다.")
        print("“왜 정신줄을 놓고있어?,어디 아파?”")
        print("“아….아니요, 괜찮아요.”")

        print(" ")
        print("엔터를 눌러주세요")
        u = input()

        print("그..래 나는 아직 8살, 어린애다.")
        print("그리고 이분은… 엄마")
        print("“가족사진 찍어야지~ 어서오렴.”")
        print("“…네”")
        print("우리 가족이 모두 모여있다.")
        print("“네 찍겠습니다. 다들 웃어주세요.”")
        print("우리 가족이 모두 모여있다.")
        print("“찰칵!”")
        print("“와서 사진좀 확인해 주세요.”")
        print("“네~~ 아들 잠시만, 자! 여기 엄마 휴대폰 줄테니까 게임이라도 하고있어.”")

        print(" ")
        print("엔터를 눌러주세요")
        u = input()
        print("                  휴대폰 문자")
        print("   '우리는 당신의 프로젝트가 아직 가능성이 있다고 생각합니다.")
        print("          연락 주시면 감사하겠습니다.'")
        print("휴대폰이 꺼졌다.")
        print("“네 사진은 이정도면 된 것 같아요! 감사합니다.”")
        print("“네, 앨범은 곧 만들어서 댁으로 보내드리겠습니다.”")
        print("“자 사진 다 찍었으니 밥 먹으러 가자!”")
        print("문을 열고 나갔더니….")

        print("엔터를 눌러주세요")
        u = input()

        print("“가족 앨범이 나왔네!”")
        print("“우리 막내 사진이 가장 잘 나온 것 같네!”")
        print("“뭐야… 나도 잘 나왔단 말이야!”")
        print("“그래,알았어 우리딸.”")
        print("이 앨범….")
        print("우리 가족의 다양한 추억들과 각자의 사진을 담아서 만든 앨범이다.")

        print(" ")
        print("엔터를 눌러주세요")
        u = input()

        print("하지만……..")
        print("“이 앨범… 무슨 내용이었지?”")
        print("어느새 주위의 가족들이 사라졌다.")
        print("난 지금 기억을 잃은 앨범앞에 혼자 앉아있다.")

    item = ['1.머리띠', '2.TV', '3.사자', '4.음료수', '5.조약돌']

    def picture():
        i = 0
        s = []
        while (len(s) < 4):
            print("아이템들을 조합해서 추억을 찾으세요")
            print(item)
            print("숫자만 입력해 주세요")
            a = str(input("첫번째 아이템"))
            b = str(input("두번째 아이템"))
            if (a == '1' and b == '3') or (a == '3' and b == '1'):
                if ('1' in s):
                    print("그 때 처음으로 사자를 봤었지..?")
                    print("그 외에도 처음보는 것들이 가득했었지?")
                    print("첫 동물원의 추억은 아직도 즐거운것 같다.")
                else:
                    print("나는 토끼 머리띠를 했다.")
                    print("손에는 풍선을 들고..")
                    print("사자를 보았다....")
                    print("처음에 사자를 보았을 때는 너무 무서웠던 것 같다.")
                    print("그래서 더욱더 손을 꽉 잡았던 것 같다")
                    print("그래도 확실했던건..")
                    print("재밌었다 확실히!")
                    print("앨범이 채워졌습니다!!")
                    s = s + ['1']
            elif (a == '1' and b == '4') or (a == '4' and b == '1'):
                if ('2' in s):
                    print("온 가족이 운동회에서 웃고 떠들던 기억이다.")
                    print("가족 다 같이 소풍온 것 같아 기뻤었다.")
                else:
                    print("이건...8살때였나?")
                    print("첫 초등학교 운동회였다")
                    print("청팀 백팀을 나누는 머리띠를 하고 뛰고있었고...")
                    print("'빨리뛰어 어서!!'")
                    print("가족들이 응원하는 모습이 스쳐 지나갔다")

                    print(" ")
                    print("엔터를 눌러주세요")
                    u = input()

                    print("난 3등도 하지 못해서 우울해 했고..")
                    print("아버지가 괜찮다면서 음료수를 사줬던것 같다.")
                    print("그러곤 다같이 모여앉아 점심을 먹었다..")
                    print("행복했었다.")
                    print("앨범이 채워졌습니다!!!")
                    s = s + ['2']
            elif (a == '2' and b == '4') or (a == '4' and b == '2'):
                if ('3' in s):
                    print("어렸을때는 '짱x'를 보던 추억이다")
                    print("그때 혼나던 것마저도 추억이 되는걸까....?")
                else:
                    print("한 6살땐가? tv에서 짱구가 했던 것 같다")
                    print("짱구가 음료수를 못 마시는 내용이었나?")
                    print("그리고 항상 이럴때면......")
                    print("'엄마가 tv 그만보라고 했지!!!!'")
                    print("엄마가 잔소리를 했던 것 같다.....'")
                    print("그리고 나는 떼를 썼겠지?")
                    print("그랬던 어린시절이다.......")
                    print("앨범이 채워졌습니다!!!")
                    s = s + ['3']
            elif (a == '2' and b == '5') or (a == '5' and b == '2'):
                if ('4' in s):
                    print("그렇게 즉석으로 떠날줄은 몰랐지만")
                    print("그래도 바다를 볼 수 있어서 좋았다.")
                else:
                    print("6살땐가? tv를 보고 있었는데")
                    print("'와 바다다!!")
                    print("tv에 바다가 나왔던것 같다.")
                    print("그런데 그때....")
                    print("'보러갈까?'")
                    print("갑자기 어머니가 나한테 바다를 보러가자고 했고.")

                    print(" ")
                    print("엔터를 눌러주세요")
                    u = input()

                    print("'그래!'")
                    print("나는 설레는 마음에 좋다고 했다")
                    print("그리고 장장 2시간동안 차를 타고 가서 바다를 보았고")
                    print("그곳에서 추억이랍시고 돌을 주어왔다.")
                    print("그리고 회는 너무 맛이 없었다...")
                    print("앨범이 채워졌습니다")
                    s = s + ['4']
            elif (i == 5):
                print("왠지 더이상 틀리면 안될것 같다..")
                print("신경써서 생각해보자 막해선 안될것같다.")
                i = i + 1
            elif (i == 10):
                print("hidden ending!!")
                import pygame
                pyblo5 = pygame.image.load("깨진액자.jpeg")
                pygame.init()
                pygame.mixer.Sound.play(give)

                display_width = 800
                display_height = 800

                ourScreen = pygame.display.set_mode((display_width, display_height))

                finished = False
                while not finished:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            finished = True
                        ourScreen.blit(pyblo5, (0, 0))
                    pygame.display.flip()
                pygame.quit()
                print("아......뭔가 난 더이상 기억해낼 수 없을것 같다..")
                print("이렇게 끝나는건가..?")
                print("재도전 하시겠습니까?")
                print("o x 로 입력해주세요")
                a = input("")
                if a == 'o':
                    choice()
                else:
                    quit()
            else:
                print("연관성을 생각해서 다시 조합해보세요…")
                i = i + 1

        print("그랬다… 내겐 누구와도 바꿀수 없는… 가족이 있었다.")

    parents()
    picture()


def MINE8():
    time.sleep(2)
    print("엔터를 눌러주세요")
    u = input()

    def album():
        print("“우리앨범 잘나왔다 그치?”")
        print("“그러게”")
        print("“뭐야…? 안기뻐? 왜이리 답이 시큰둥해?”")
        print("“어?…아 어어”")
        print("그렇다 우리 가족의 앨범이 나왔다.")
        print("“우리 결혼 기념일때랑… 우리 첫째 낳았을 때랑 다 나와있다!”")

        print(" ")
        print("엔터를 눌러주세요")

        u = input()
        print("“어… 그러네!!!”")
        print("“재경 - 뭐야? 왜 이렇게 반응이 늦어?”")
        print("“어…어…..”")
        print("“재경 - 참…. 먼저 나가있을게! 빨리 따라나와!”")
        print("그래. 나에겐 가족이 있었고 지금도 가족이 있다.")
        print("하지만 나는 이 앨범의 내용도 잘 기억나지 않는다.")
        print("나는 또 기억잃은 앨범 앞에서 추억을 찾는다.")

        print(" ")
        print("엔터를 눌러주세요")
        u = input()

        print("앨범을 열어보니")
        print("예전에 아내가 나에게 준 것 같은 쪽지가 있었다.")
        print("펼쳐보니…")
        import pygame
        pyblo5 = pygame.image.load("이혼문제.jpeg")
        pygame.init()
        pygame.mixer.Sound.play(finale)
        

        display_width = 800
        display_height = 800

        ourScreen = pygame.display.set_mode((display_width, display_height))

        finished = False
        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                ourScreen.blit(pyblo5, (0, 0))
            pygame.display.flip()
        pygame.quit()

        print("결혼기념일은??(숫자만 입력해주세요!)")
        c = []
        while (len(c) < 2):
            a = str(input("몇 월?"))
            b = str(input("몇 일?"))
            if (a == '8' and b == '19'):
                print("재경 - 문제는 다 풀었어? 빨리 나와!!")
                print("어 알았어!")
                print("결혼 기념일의 날짜와 사진이 떠올랐다.")
                print("그리고 오늘은 가족끼리 다같이 보낼만한 시간인")
                print("크리스마스 이브다")
                print("재경 - 뭐해 안 나와?")

                print(" ")
                print("엔터를 눌러주세요")
                u = input()

                print("“어! 지금 나갈게!”")
                print("그렇게 우리는 바깥으로 나왔다")
                print("이런 여유가 얼마만인걸까?")
                print("최근 살아가기에 바빴었다.")
                print("이것 저것 할게 많아서,")
                print("부인을 신경쓰지 못했다.")
                print("친구들에게 연락하지 못했다.")
                print("프로젝트 준비가 소홀했을지도 모른다.")
                print("가족과 시간을 덜 보냈을지도 모른다……")
                print("난 왜 그렇게 열심히 산거지?")
                print("나에게 소중했던건…")

                print(" ")
                print("엔터를 눌러주세요")
                u = input()

                print("재경 - 와 트리다!!")
                print("그래 오늘은 크리스마스 이브다.")
                print("그리고....")
                print("'눈'을 휙득했습니다!")
                print("와 눈이다!!!")
                print("아들이 하늘을 보며 눈이 온다고 외쳤다.")
                print("우린 다같이 눈이 오는 하늘을 보았다.")
                print("그리고 손을 더 꽉 잡았다.")
                print("행복했다. 아니, 행복한 중이었다.")
                break
            else:
                if (c == []):
                    c = c + ['1']
                    print("이 날이 아닌 것 같은데…")
                    print("한 번 더 틀리면 왠지 큰일이 생길 것 같은 예감이…")
                    print("신중하자...신중")
                    import pygame
                    pyblo5 = pygame.image.load("이혼문제.jpeg")
                    pygame.init()

                    display_width = 800
                    display_height = 800

                    ourScreen = pygame.display.set_mode((display_width, display_height))

                    finished = False
                    while not finished:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                finished = True
                            ourScreen.blit(pyblo5, (0, 0))
                        pygame.display.flip()

                else:
                    print("hidden ending!!!!!!")
                    time.sleep(1)
                    
                    pyblo5 = pygame.image.load("이혼.jpeg")
                    pygame.init()
                    pygame.mixer.Sound.play(give)

                    display_width = 800
                    display_height = 800

                    ourScreen = pygame.display.set_mode((display_width, display_height))

                    finished = False
                    while not finished:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                finished = True
                            ourScreen.blit(pyblo5, (0, 0))
                        pygame.display.flip()
                    pygame.quit()
                    print("결혼 기념일도 잘 알지 못하는 남편과 살기는 힘들었겠지")
                    print("그렇게 쌓이던 감정은 어느날 터지고")
                    print("결국 우리는 이혼하게 되버렸다.")
                    print("?? - 돌아올때 힘들 너를 위해")
                    print("?? - 1,3/1,4/2,4/2,5")
                    print("?? - 그리고 색깔과 숫자의 연관!!")
                    print("?? - 얼마 안남아서 더힘든거야 꼭 끝내라고!")
                    quit()

    album()


def MINE9():
    time.sleep(2)
    import pygame
    pyblo5 = pygame.image.load("mine5.jpeg")
    pygame.init()
    pygame.mixer.Sound.play(snow)

    display_width = 800
    display_height = 800

    ourScreen = pygame.display.set_mode((display_width, display_height))

    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            ourScreen.blit(pyblo5, (0, 0))
        pygame.display.flip()
    pygame.quit()
    print(" ")
    print("엔터를 눌러주세요")
    u = input()

    def company():
        print("?? - 어이 일어나")
        print("어..어?")
        print("회사였다. 늘 다니던 그 회사 그 자리였다.")
        print("광민(회사상사) - 깜빡 졸았던 거야? 뭔 정신을 놓고있어?")
        print("아… 죄송합니다.")
        print("광민 - 후딱 정신차리고 일어나!")

        print(" ")
        print("엔터를 눌러주세요")
        u = input()

        print("어…음…..")
        print("그러니까 회사구나...")
        print("난 별일없이 회사에서 일하던 중이었고")
        print("졸다가 상사한테 혼난거고")
        print("평소와 똑같은 하루를 보내던 중이었다.")
        print("그리고 아마 이제 곧…..")
        print("상민 - “어이 뭘 자고 있어?”")
        print("아…. 좀 피곤했나보네")
        print("상민 - 뭔… 마치고 한잔 하러갈래?")
        print("그럴까?")

        print(" ")
        print("엔터를 눌러주세요")
        u = input()

        print("이러곤 늘 일상이 반복될거다")
        print("기획안을 들고 가고")
        print("상사한테 깨지고")
        print("거래처에 연락하고")
        print("지쳐서 커피한잔먹으면서")
        print("해가 질거다")
        print("그리곤 술자리에 앉아서")
        print("상민 - 하….사는게 왜이렇게 힘드냐….")
        print("늘 하던 핀잔을 듣겠지.")
        print("그리곤 나도 힘들어서")
        print("그러게…")
        print("라고 말하겠지")

        print(" ")
        print("엔터를 눌러주세요")
        u = input()

        print("유난히 이날따라 힘들어서 더 마시겠지")
        print("그리곤 취할대로 취한 동료를 집으로 데려다 줄거다.")
        print("그러곤 하늘을 올려다보면서")
        print("왠지 세상일이 무료함을 느낄거다.")
        print("그리곤 지하철에서 앉아서 졸다가 집 근처 역에 도착하고")

        print(" ")
        print("엔터를 눌러주세요")
        u = input()
        print(" ")

        print("횡단보도 앞…")

        print(" ")
        print("엔터를 눌러주세요")
        u = input()
        print(" ")

        print("?? - “가끔 생각하잖아? 인생참 별거 없이 지나간다고..그냥 이냥 저냥”")
        print("횡단보도 불을 확인하고 걸어가다가")

        print(" ")
        print("엔터를 눌러주세요")
        u = input()
        print(" ")

        print("?? - “그런데 누구나 잃을것은 있어 잃기 전까지 모르는거지”")
        print("난 취한 상태라 옆을 잘 볼 수 없었고")

        print(" ")
        print("엔터를 눌러주세요")
        u = input()
        print(" ")

        print("?? - “행복이란게 참 모르겠는거야 그렇지?”")
        print("눈도 잘뜨지 못하는 가운데")

        print(" ")
        print("엔터를 눌러주세요")
        u = input()
        print(" ")

        print("?? - “막상 손에 쥐고 있었을 지도 모르는건데 말이야”")

        print(" ")
        print("엔터를 눌러주세요")
        u = input()
        print(" ")

        print("난 옆에서 흰빛이 내게 달려오는걸 느꼈다.")
        time.sleep(2)

    company()

    # Mine-10
    # (gui를 쓰려다 재한계를 느끼고 갑니다….)
    item = []


def MINE10():
    time.sleep(2)
    print(" ")
    print("엔터를 눌러주세요")
    u = input()
    print("?? - 꺳어?")
    print("어…..")
    print("아주 익숙한 곳이다.")
    print("우리집이다.")

    print(" ")
    print("엔터를 눌러주세요")
    u = input()
    print(" ")

    print("?? - 그럼 다 기억났겠네?")
    print("그러니까 분명히 횡단보도에서")
    print("?? - 옆에서 음주운전 하던 차와 부딪혔지.")
    print("음 그랬구나….")
    print("?? - 그다음 부터는 기억이 없지?")
    print("그런것 같네…")
    print("난 주마등을 체험한걸까?")

    print(" ")
    print("엔터를 눌러주세요")
    u = input()
    print(" ")

    print("?? - 주마등이긴 하지")
    print("그럼 난 죽은건가?")
    print("?? - 글쎄……살 수 있는 방법이 있는데?")

    print(" ")
    print("엔터를 눌러주세요")
    u = input()
    print(" ")

    print("뭔데?")
    print("?? - 내가 누군지 맞춰봐! 그럼 살수 있을걸?")
    print("너가 누군지라….")
    print("?? - 힌트를 줄까? 여기있어")
    print("item = [??,??,??,??]")
    print("자 이 4개를 ‘순서대로’ 맞춰봐. 그럼 답이 보일껄?")
    item = []
    while (item == []):
        a = str(input("첫번째 item"))
        if (a == '벚꽃잎'):
            print("?? - 봄에 새학기에 벚꽃나무 밑에서……")
            print("?? - 어떤 기억이라도 아름다운 추억이되고")
            print("?? - 아무리 시간이 흘러도 가끔 생각나게 되는")
            print("?? - 그런 설렘이었지..")
            print("?? - 첫사랑이니까")
            item = item + ['a']
            break
        else:
            print("MINE1에서 무슨 일이 있었는지 잘 생각해보세요.")
            k=str(input("처음 선택지로 돌아가기겠습니까?:(o,x로 입력해주세요)"))
            while not(k=='o' or k=='x'):
                k = str(input("처음 선택지로 돌아가기겠습니까?:(o,x로 입력해주세요)"))
            if(k=='o'):
                choice()


    while (item == ['a']):
        b = str(input("두번째 item"))
        if (b == '사진기'):
            print("?? - 참 별것도 아닌게 인생에는 기억되게 된단 말이지?")
            print("?? - 친구들과 놀러가게 되면")
            print("?? - 참 이상한짓도 많이하고…")
            print("?? - 쓸데없이 오기부리게 되고")
            print("?? - 그러면서 남는 추억은 사진기에 담기고")
            print("?? - 언젠가 그땐 재밌었다며 술안주가 되어주겠지?")
            item = item + ['b']
            break
        else:
            print("MINE2에서 무슨 일이 있었는지 잘 생각해보세요.")
            k = str(input("처음 선택지로 돌아가기겠습니까?:(o,x로 입력해주세요)"))
            while not (k == 'o' or k == 'x'):
                k = str(input("처음 선택지로 돌아가기겠습니까?:(o,x로 입력해주세요)"))
            if (k == 'o'):
                choice()

    while (item == ['a', 'b']):
        c = str(input("세번째 item"))
        if (c == '트로피'):
            print("?? - 꿈에 다가가는 그 느낌이라…")
            print("?? - 노력이란게 배신하지 않는다고는 하지만")
            print("?? - 결과가 나올때 까지는 결국 알 수 없는거잖아?")
            print("?? - 하지만 그렇기에 더욱더")
            print("?? - 인생에서 성취를 이룬 순간은 값진거야")
            item = item + ['c']
            break
        else:
            print("MINE3에서 무슨 일이 있었는지 잘 생각해보세요.")
            k = str(input("처음 선택지로 돌아가기겠습니까?:(o,x로 입력해주세요)"))
            while not (k == 'o' or k == 'x'):
                k = str(input("처음 선택지로 돌아가기겠습니까?:(o,x로 입력해주세요)"))
            if (k == 'o'):
                choice()

    while (item == ['a', 'b', 'c']):
        d = str(input("네번째 item"))
        if (d == '눈'):
            print("?? - 가족…..")
            print("?? - 태어난 순간부터 끝나는 순간까지")
            print("?? - 가장 많은 시간을 같이 보내게 되는…")
            print("?? - 너무나 많은 행복을 언제나 받고 있지만")
            print("?? - 너무나 일상적이라 눈치 챌수가 없지")
            print("?? - 하지만 잃게 되었을떄의 허전함은.")
            print("?? - ……..")
            break
        else:
            print("MINE4에서 무슨 일이 있었는지 잘 생각해보세요.")
            k = str(input("처음 선택지로 돌아가기겠습니까?:(o,x로 입력해주세요)"))
            while not (k == 'o' or k == 'x'):
                k = str(input("처음 선택지로 돌아가기겠습니까?:(o,x로 입력해주세요)"))
            if (k == 'o'):
                choice()

            # 기회 한번으로 해버릴까요 그냥? 아니면 마지막이니 그냥 살려주는걸로?

    print("?? - 일단 4개를 전부 다 맞히긴 했구나")
    print("?? - 그럼 이제 맞춰봐. 내가 누굴까?")

    print("엔터를 눌러주세요")
    u = input()

    print("……..")  # (이건 문제 아니에요)
    print("?? - 그래 ‘나’지")
    print("정확히는 ‘과거의 나’ 또는 ‘행복했던 기억의 나’지")
    print("음….")
    print("사고가 날때의 난 말이지 인생이 참 별거 없이 무료하다고 생각했던것 같아")
    print("딱히 행복하진 않다고 말이지…")
    print("….")

    print(" ")
    print("엔터를 눌러주세요")
    u = input()

    print("그런데 재밌는 건")
    print("중학생이 되었을즈음, 넌 어린 시절이 행복하다고 느꼈을꺼야.")
    print("스무살이 되었을때, 대학생의 너는 고등학교 생활, 10대를행복하다고 느낄거고")
    print("서른 즈음에? 스무살의 빛나던 너를 행복하다고 생각할거야")
    print("그리고 지금 너는 서른의 너를 행복하다고 느낄지도 몰라")
    print("….")

    print(" ")
    print("엔터를 눌러주세요")
    u = input()

    print("결국 하고 싶은 말은...")
    print("난")
    print("내 인생의 모든순간은")
    print("행복했었어")
    print("죽을 때 되서야 느낄 수 있는거지만")
    print("‘행복은 내가 이미 가지고 있던 것’ 이라는 거지")

    print("엔터를 눌러주세요")
    u = input()

    print("물론 현실에 불만을 가지고 살 수도 있지만")
    print("언젠가 그 순간마저도 행복했음을 깨달을 수 있을거야..")
    print("지금 역시도…")

    print(" ")
    print("엔터를 눌러주세요")
    u = input()

    print("자 슬슬 여기서 '탈출'할때라")
    print("내 인생 몇 안되는 극적으로 행복할 순간 중 하나거든")
    print("지금 마침 주위에 아주 많은 사람이 있고 말이지")
    print("마지막 문제야.")
    print("글귀를 완성해줘")
    print("‘행복은 나의 것이었다.’")
    while (item == ['a', 'b', 'c']):
        e = str(input("‘Happy is ????’(소문자로 작성해주세요!)"))
        if (e == 'mine'):
            import pygame
            pyblo5 = pygame.image.load("마지막.jpeg")
            pygame.init()
            pygame.mixer.Sound.play(memory)

            display_width = 800
            display_height = 800

            ourScreen = pygame.display.set_mode((display_width, display_height))

            finished = False
            while not finished:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        finished = True
                    ourScreen.blit(pyblo5, (0, 0))
                pygame.display.flip()
            pygame.quit()

            import pygame

            pyblo5 = pygame.image.load("크레딧.jpeg")
            pygame.init()
            pygame.mixer.Sound.play(aa)

            display_width = 800
            display_height = 800

            ourScreen = pygame.display.set_mode((display_width, display_height))

            finished = False
            while not finished:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        finished = True
                    ourScreen.blit(pyblo5, (0, 0))
                pygame.display.flip()
            pygame.quit()
            quit()
            break
        else:
            print("..........")
            print("안 일어날 셈이야??")


def choice():
    d = str(input("어느 장부터 읽으시겠습니까?1,2,3,4,5 중에서 선택해 주십시오"))
    while not (d == '1' or d == '2' or d == '3' or d == '4' or d == '5'):
        d = str(input("어느 장부터 읽으시겠습니까?1,2,3,4,5 중에서만!! 선택해 주십시오"))
    if d == '1':
        MINE1()
        MINE2()
        MINE3()
        MINE4()
        MINE5()
        MINE6()
        MINE7()
        MINE8()
        MINE9()
        MINE10()
    if d == '2':
        print("?? - 꼭 이거 부터 봤어야 했니?")
        time.sleep(2)
        print("?? - 2초 있다 실행 될거야")
        print("?? - 좀있다 스크롤을 내려보라고")
        time.sleep(2)

        MINE3()
        MINE4()
        MINE5()
        MINE6()
        MINE7()
        MINE8()
        MINE9()
        MINE10()

    if d == '3':
        print("?? - 시험볼때 책 중간 부터 보면 잘볼 수 있어?")
        time.sleep(2)
        print("?? - 2초 있다 실행 될거야")
        print("?? - 좀있다 스크롤을 내려보라고")
        time.sleep(2)

        MINE5()
        MINE6()
        MINE7()
        MINE8()
        MINE9()
        MINE10()
    if d == '4':
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(2)
        print("?? - 네가 두번째가 아니라면..... ")
        time.sleep(2)
        print("?? - 거참 너무하는구만......")
        time.sleep(2)
        print("?? - 확 꺼버릴가 싶지만....")
        time.sleep(2)
        print("?? - 5초 뒤엔 실행 될테니 알아서 해봐")
        time.sleep(2)
        print("?? - 가아아급적 돌아가줬으면 하지만")
        print("?? - 좀있다 스크롤을 내려보라고")
        time.sleep(3)

        MINE7()
        MINE8()
        MINE9()
        MINE10()
    if d == '5':
        print("?? - 하아.......")
        time.sleep(2)
        print("?? - 네가 두번째이길 바라면서..... ")
        time.sleep(2)
        print("?? - 거참 너무하네......")
        time.sleep(2)
        print("?? - 확 꺼버릴가 싶네 진짜 아오....")
        time.sleep(2)
        print("?? - 어차피 풀지도 못할테지만...")
        time.sleep(2)
        print("?? - 5초 뒤엔 실행 될테니 알아서 해봐")
        time.sleep(2)
        print("?? - 가아아급적 돌아가줬으면 하지만")
        print("?? - 좀있다 스크롤을 내려보라고")
        time.sleep(3)

        MINE9()
        MINE10()


def start():
    time.sleep(0.5)
    print("?? - 음!")
    print("?? - 아마 일어나면 방에 갇혀있을거야.")
    time.sleep(0.5)
    print("?? - 뭐 그건 네가 알아서 할일이고")
    time.sleep(0.5)
    print("?? - 이 이야기는 한편의 소설같은 이야기거든.")
    time.sleep(0.5)
    print("?? - 그러니 가급적 읽으면서 진행해주길 바래….")
    time.sleep(0.5)
    print("?? - 그리고 글을 다 읽었으면 'enter'를 눌러줘!")
    print("?? - enter는 제위치에 '신중히' 눌러달라고~")
    k = input()
    print("?? - 잘했어")
    print("?? - 가끔씩 enter를 눌러야 진행이 될거야.")
    time.sleep(0.5)
    print("?? - 그럴땐 'enter'를 누르란 말을 해줄게")
    print("?? - 그럴땐 'enter'를 누르란 말을 해줄게")
    time.sleep(0.5)
    print("?? - 중요한거라 두번 말했어")
    time.sleep(0.5)
    print("?? - 뭐 읽기 싫어서 연타할수도 있지만..")
    time.sleep(0.5)
    print("?? - 그러다 '히든엔딩'이라는 무서운 세계로 가버릴수도 있으니까 조심하라고")
    time.sleep(0.5)
    print("?? - '히든엔딩'을 보는 방법은 여러가지지만..")
    time.sleep(0.5)
    print("?? - 네가 직접 체험해볼 일이지")
    time.sleep(0.5)
    print("?? - 덤으로 게임이 끝나버리니까 조심하라고…")
    time.sleep(0.5)
    print("?? - 뭐 혹시 질문있어?")
    time.sleep(0.5)
    print("?? - 응? 나??")
    time.sleep(0.5)
    print("……")
    time.sleep(0.5)
    print("?? - 뭐 어차피 네가 딴길로 새지만 않는다면 만나게 될거야")
    time.sleep(0.5)
    print("?? - 또 말해줘야 할게 뭐있더라….")
    time.sleep(0.5)
    print("?? - 아!!! 아마 이제 곧 창이 뜰거거든?")
    time.sleep(0.5)
    print("??-노래와 함께....")
    time.sleep(0.5)
    print("?? - 그럴때 마다 위의 'x'를 눌러서 그 창을 꺼야 진행이 될가야 ")
    print("…….")
    pyblo5 = pygame.image.load("mine.jpeg")
    pygame.init()
    pygame.mixer.Sound.play(door)

    display_width = 800
    display_height = 800

    ourScreen = pygame.display.set_mode((display_width, display_height))

    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            ourScreen.blit(pyblo5, (0, 0))
        pygame.display.flip()
    pygame.quit()

    print("?? - 음… 그거말고는 딱히 없는건가?")
    time.sleep(1)
    print("?? - 혹시 버그가 나오면 'anan7940@naver.com' 으로 연락줘")
    time.sleep(1)
    print("?? - 그리고 이 책의 뒷장부터 읽을 수도 있지만")
    time.sleep(1)
    print("?? - 그러다간 문제를 못 푸는 무서운 일이 일어날거야")
    time.sleep(1)
    print("?? - 자, 정리하자고 'enter'는 신중히! ")
    time.sleep(1)
    print("?? - 그리고 장이 넘어갈때마다 한 2초정도 기다리게 될거야")
    time.sleep(1)
    print("?? - 나중에 보자고")
    choice()

def init():
    global aa,home,once,door,give,dog,snow,memory,finale
    
    pygame.init()
    finale=pygame.mixer.Sound("finale.wav")
    aa=pygame.mixer.Sound("a.wav")
    home = pygame.mixer.Sound("home.wav")
    once = pygame.mixer.Sound("once.wav")
    door = pygame.mixer.Sound("door.wav")
    give = pygame.mixer.Sound("give.wav")
    dog = pygame.mixer.Sound("dog.wav")
    snow = pygame.mixer.Sound("snow.wav")
    memory = pygame.mixer.Sound("memory.wav")
    
    start()

init()
