from django.shortcuts import render


# Create your views here.
def game_info(request):
    return render(request, 'gameplay/game_info.html')


def main_menu(request):
    return render(request, 'gameplay/main_menu.html')


def character_temp():
    area1='''
    <html>
    <body>
    <div id="main_menu" style="position:absolute; z-index:-1;">
        <div id="stat">
            <div>통솔
                <span id="통솔"></span>
            </div>
            <div>무력
                <span id="무력"></span>
            </div>
            <div>지력
                <span id="지력"></span>
            </div>
            <div>정치
                <span id="정치"></span>
            </div>
            <div>
                <button id="statbtn" type="button">장수 스탯 정하기</button>
            </div>
        </div>

        <div id="내정특기">
            <div id="trait1"></div>
            <div>
                <button id="btn2" type="button">내정특기</button>
            </div>
        </div>
        <div id="전투특기">
            <div id="trait2"></div>
            <div>
                <button id="btn3" type="button">전투특기</button>
            </div>
        </div>
        <div id="전술">
            <div id="trait3"></div>
            <div>
                <button id="btn4" type="button">전술</button>
            </div>
        </div>
        <div id="장수" class="img1"></div>
        <div id="next" class="mainui">
            <a href="/story2" target="_self">다음</a>
        </div>
    </div>
    </body>
    </html>
    '''
    return area1



def character(request):
    return HttpResponse(character_temp())


def story1(request):
    return render(request, 'gameplay/story1.html')


def story2(request):
    return render(request, 'gameplay/story2.html')


def story3(request):
    return render(request, 'gameplay/story3.html')


def 내정(request):
    return render(request, 'gameplay/내정.html')


def 전투(request):
    return render(request, 'gameplay/전투.html')
