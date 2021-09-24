import discord
import asyncio, random, os

client = discord.Client()


@client.event
async def on_ready():
    game = discord.Game('?롤덤이 도움말')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "?롤덤이 안녕":
        await message.channel.send("안녕")

    if message.content == "?롤덤이 ㅎㅇ":
        await message.channel.send("안녕")

    if message.content == "?롤덤이 잘가":
        await message.channel.send("잘 가")
  
    if message.content == "?롤덤이 잘 가":
        await message.channel.send("잘 가")



    if message.content == "찌뚜유튜브":
        embed = discord.Embed(title="찌뚜 유튜브 채널", description="https://www.youtube.com/c/찌뚜유튜븝", color=0x00ff00)
        embed.set_footer(text="구독과 좋아요 부탁드려요")
        await message.channel.send(embed=embed)

    if message.content == "?롤덤이 도움말":
        embed = discord.Embed(title="롤랜덤이 사용방법", description=" :bulb: Tip : 밑에 있는 도움말을 보고 이용해주세요 :D", color=0x17164D)
        embed.add_field(name=":newspaper: 봇 패치노트", value=" ``?롤덤노트`` ", inline=False)
        embed.add_field(name=":page_with_curl: 일반 명령어", value=" ``?롤덤이 일반`` ", inline=False)
        embed.add_field(name=":page_with_curl: 추첨 명령어", value=" ``?롤덤이 추첨 안내`` ", inline=False)
        embed.add_field(name=":earth_asia: 문의 명령어", value=" ``?롤덤이 문의`` ", inline=False)
        embed.set_footer(text="문의는 discordbotgang#0010")
        await message.channel.send(embed=embed)

    if message.content == "?롤덤이 추첨 안내":
        embed = discord.Embed(title="롤랜덤이 사용방법", description=" :bulb: Tip : 밑에 있는 도움말을 보고 이용해주세요 :D", color=0x17164D)
        embed.add_field(name=":newspaper: 전체 추첨 명령어", value=" **```?롤덤이 챔피언 전체 추천```** ", inline=False)
        embed.add_field(name=":newspaper: 포지션 별 추첨 명령어", value=" :one: **```?롤덤이 챔피언 암살자 추천```** :two: **```?롤덤이 챔피언 메이지 추천```** :three: **```?롤덤이 챔피언 서포터 추천```** :four: **```?롤덤이 챔피언 전사 추천```** :five: **```?롤덤이 챔피언 탱커 추천```**", inline=False)
        embed.set_footer(text="문의는 discordbotgang#0010")
        await message.channel.send(embed=embed)

    if message.content == "?롤덤이 암살자 목록":
        embed = discord.Embed(title="암살자 목록", description="출처 : 리그 오브 레전드 나무위키", color=0x9c0d06)
        embed.set_image(url="https://postfiles.pstatic.net/MjAyMTA5MjNfMTQ5/MDAxNjMyMzkzODMyMzg1.kejiRlROo9cwl3qFrdIvACBnYYHSHw72kx6CTWFHcFIg.cmO5nkJ2cawK_T2yngs9CXnLCMJHsoMK14jpN92hjUYg.PNG.jjiddoo3003/%EC%95%94%EC%82%B4%EC%9E%90.png?type=w966")
        await message.channel.send(embed=embed)


    if message.content == "?롤덤이":
        embed = discord.Embed(title="롤랜덤이 사용방법", description=" :bulb: Tip : 밑에 있는 도움말을 보고 이용해주세요 :D", color=0x17164D)
        embed.add_field(name="?롤덤이 도움말을 사용 해주세요", value=" ``또는 ?롤덤이 문의`` ", inline=False)
        embed.set_footer(text="문의는 discordbotgang#0010")
        await message.channel.send(embed=embed)

    if message.content == "?롤덤이 추첨":
        embed = discord.Embed(title="롤랜덤이 추첨 명령어", description=" :bulb: Tip : 밑에 있는 도움말을 보고 이용해주세요 :D", color=0x17164D)
        embed.add_field(name="?롤덤이 도움말을 사용 해주세요", value=" ``또는 ?롤덤이 문의`` ", inline=False)
        embed.set_footer(text="문의는 discordbotgang#0010")
        await message.channel.send(embed=embed)
        

    if message.content == "?롤덤노트":
        embed = discord.Embed(title=":newspaper: 롤덤 노트 0.1 ver", description=" **```수정일 : 2021_09_16 롤덤이 봇 바뀐 점을 알려드립니다.```**", color=0x17164D)
        embed.add_field(name=":repeat: 바뀐 점", value=" :tools: 개발자 이야기 : **``` 롤 랜덤 봇 롤덤이가 2021_09_16 에 시작 되었습니다. 이 봇은 단순 제작자가 파이썬 공부 하기 위해서 호기심을 갖다가 만들어진 것 입니다. 관심있는 것 또한 리그오브레전드 이기에 만들게 되었습니다.```** ", inline=False)
        embed.add_field(name=":birthday: 롤덤이 탄생....!!", value=" **```롤덤이 탄생일은 2021_09_16```** ", inline=False)
        embed.set_footer(text="문의는 discordbotgang#0010")
        await message.channel.send(embed=embed)


    if message.content == "?롤덤이 일반":
        embed = discord.Embed(title="롤랜덤이 일반 명령어", description=" :bulb: Tip : 밑에 있는 도움말을 보고 이용해주세요 :D", color=0x17164D)
        embed.add_field(name=":page_with_curl: 일반 명령어", value=" ``?롤덤이 포지션 추천 `` ", inline=False)
        embed.add_field(name=":repeat_one: 추천 명령어", value=" ``?롤덤이 포지션 추천 , ?롤덤이 라인 추천 `` ", inline=False)
        embed.add_field(name=":page_with_curl: 일반 명령어", value=" ``?롤덤이 포지션 추천 `` ", inline=False)
        embed.set_footer(text="문의는 discordbotgang#0010")
        await message.channel.send(embed=embed)

    if message.content == "피즈 룬":
        embed = discord.Embed(title="피즈 룬", description="이 룬은 참고정도로 사용해주세요", color=0x3a92bb)
        embed.set_image(url="https://blog.kakaocdn.net/dn/dMiylU/btqOvR1F1IC/pKGeFVlLynR95eVmkQL7kk/img.png")
        await message.channel.send(embed=embed)

    if message.content == "이즈리얼 룬":
        embed = discord.Embed(title="이즈리얼 룬",description="이 룬은 참고정도로 사용해주세요", color=0xf0ff00)
        embed.set_image(url="https://mblogthumb-phinf.pstatic.net/MjAyMDA3MjhfODgg/MDAxNTk1OTM5NzU4MTA5._nglujglK3Cf9iPiq5sMr6WcyckcWcGCeT0LgxRG5-Ug.FHTmaQgpYsb_rMMhofxjDUx28_LsPflOC5yu3nn_eVMg.JPEG.dbsgns2011/%EC%9D%B4%EC%A6%88%EB%A6%AC%EC%96%BC_%EB%A3%AC.jpg?type=w800")
        await message.channel.send(embed=embed)

    if message.content == "라이즈 룬":
        embed = discord.Embed(title="라이즈 룬",description="이 룬은 참고정도로 사용해주세요", color=0x4f37a1)
        embed.set_image(url="https://lh3.googleusercontent.com/proxy/HmfNiPi7FaRskklloMzoBmKzw7yC8J51sSgTwfTzOpSre5k_WPLxALN1MItXNBXJrFFvT4zrEBMXWEP2JLqnM6C8ezIEddDH4M3YQ7s9g9RMuM1JMo_BR20")
        await message.channel.send(embed=embed)

    if message.content == "갈리오 룬":
        embed = discord.Embed(title="갈리오 룬",description="이 룬은 참고정도로 사용해주세요", color=0xffffff)
        embed.set_image(url="https://mblogthumb-phinf.pstatic.net/MjAyMDA0MDVfMTQw/MDAxNTg2MDk3MzM4MzQy.93w7aoogehUi_L_rJpATZMAYco24WuQ7JPq53eBoSnsg.0uA4VyfpVd-2ogSWGS1fntWCEoBloyWfS-bACGvaCzMg.JPEG.dbsgns2011/%EB%A1%A4_%EC%8B%9C%EC%A6%8C10_%EA%B0%88%EB%A6%AC%EC%98%A4_%EB%A3%AC.jpg?type=w800")
        await message.channel.send(embed=embed)

    if message.content == "유미 룬":
        embed = discord.Embed(title="유미 룬",description="이 룬은 참고정도로 사용해주세요", color=0x5b43df)
        embed.set_image(url="https://blog.kakaocdn.net/dn/2BOAU/btqQhLZ5gpq/ryboqdJgVOK6kcynMGt6BK/img.png")
        await message.channel.send(embed=embed)




    if message.content == "신짜오 룬":
        embed = discord.Embed(title="신짜오 룬", description="이 룬은 참고정도로 사용해주세요", color=0xeded94)
        embed.set_image(url="https://blog.kakaocdn.net/dn/UJWtR/btqAJOwTVFt/hEE2GJ37K8LWzQsEkmU6h0/img.png")
        await message.channel.send(embed=embed)

    if message.content == "이렐리아 룬":
        embed = discord.Embed(title="이렐리아 룬",description="이 룬은 참고정도로 사용해주세요", color=0xeea5cd)
        embed.set_image(url="https://blog.kakaocdn.net/dn/bQ66L9/btqAQlgS5pH/L4XgHAAY6ZiOuRKD3APF41/img.png")
        await message.channel.send(embed=embed)

    if message.content == "클레드 룬":
        embed = discord.Embed(title="클레드 룬",description="이 룬은 참고정도로 사용해주세요", color=0x6e130e)
        embed.set_image(url="https://blog.kakaocdn.net/dn/cfoeay/btqYusrj3tO/y3VWVCetPqGKTEvjJFzAy1/img.png")
        await message.channel.send(embed=embed)

    if message.content == "리븐 룬":
        embed = discord.Embed(title="리븐 룬",description="이 룬은 참고정도로 사용해주세요", color=0x168d14)
        embed.set_image(url="https://blog.kakaocdn.net/dn/Hs1wp/btqNVBEN4Xu/smR4ojI5h9JQykrPKjKha0/img.png")
        await message.channel.send(embed=embed)

    if message.content == "마스터이 룬":
        embed = discord.Embed(title="마스터이 룬",description="이 룬은 참고정도로 사용해주세요", color=0x837d2a)
        embed.set_image(url="https://blog.kakaocdn.net/dn/bzbjBS/btqO6g10lkN/CXAhsWmjbLVrl9c1ZCmPsK/img.png")
        await message.channel.send(embed=embed)

    






    if message.content == "?롤덤이 라인 추천":
        ran = random.randint(0,5)
        if ran == 0:
            d = "탑"
        if ran == 2:
            d = "정글"
        if ran == 3:
            d = "미드"
        if ran == 4:
            d = "원딜"
        if ran == 5:
            d = "서폿"
        await message.channel.send(d)

      
    if message.content == "?롤덤이 포지션 추천":
        ran = random.randint(0,5)
        if ran == 0:
            d = "탑"
        if ran == 2:
            d = "정글"
        if ran == 3:
            d = "미드"
        if ran == 4:
            d = "원딜"
        if ran == 5:
            d = "서폿"
        await message.channel.send(d)
        
        
    if message.content == "?롤덤이 챔피언 암살자 추천":
        cham = random.randint(0,39)
        if cham == 0:
            d = "녹턴"
        if cham == 1:
            d = "니달리"    
        if cham == 2:
            d = "렝가"
        if cham == 3:
            d = "르블랑"
        if cham == 4:
            d = "마스터 이"
        if cham == 5:
            d = "비에고"
        if cham == 6:
            d = "샤코"
        if cham == 7:
            d = "아칼리"
        if cham == 8:
            d = "에코"
        if cham == 9:
            d = "요네"
        if cham == 10:
            d = "이블린"
        if cham == 11:
            d = "제드"
        if cham == 12:
            d = "카사딘"
        if cham == 13:
            d = "카직스"
        if cham == 14:
            d = "카타리나"
        if cham == 15:
            d = "키아나"
        if cham == 16:
            d = "탈론"
        if cham == 17:
            d = "피즈"  # 여기 까지 주 역할 암살자
        if cham == 18:  
            d = "그웬"  # 여기 부터 부 역할 암살자
        if cham == 19:
            d = "리신"
        if cham == 20:
            d = "리븐"
        if cham == 21:
            d = "말자하"
        if cham == 22:
            d = "바이"
        if cham == 23:
            d = "베인"
        if cham == 24:
            d = "사일러스"
        if cham == 25:
            d = "신짜오"
        if cham == 26:
            d = "아리"
        if cham == 27:
            d = "아크샨"
        if cham == 28:
            d = "야스오"
        if cham == 29:
            d = "이렐리아"
        if cham == 30:
            d = "잭스"
        if cham == 31:
            d = "케인"
        if cham == 32:
            d = "퀸"
        if cham == 33:
            d = "트리스타나"
        if cham == 34:
            d = "트린다미어"
        if cham == 35:
            d = "트위치"
        if cham == 36:
            d = "티모"
        if cham == 37:
            d = "파이크"
        if cham == 38:
            d = "판테온"
        if cham == 39:
            d = "피오라"
        await message.channel.send(d)

    if message.content == "?롤덤이 챔피언 전체 추천":
        cham = random.randint(0,39)
        if cham == 0:
            d = "녹턴"
        if cham == 1:
            d = "니달리"    
        if cham == 2:
            d = "렝가"
        if cham == 3:
            d = "르블랑"
        if cham == 4:
            d = "마스터 이"
        if cham == 5:
            d = "비에고"
        if cham == 6:
            d = "샤코"
        if cham == 7:
            d = "아칼리"
        if cham == 8:
            d = "에코"
        if cham == 9:
            d = "요네"
        if cham == 10:
            d = "이블린"
        if cham == 11:
            d = "제드"
        if cham == 12:
            d = "카사딘"
        if cham == 13:
            d = "카직스"
        if cham == 14:
            d = "카타리나"
        if cham == 15:
            d = "키아나"
        if cham == 16:
            d = "탈론"
        if cham == 17:
            d = "피즈"  # 여기 까지 주 역할 암살자
        if cham == 18:  
            d = "그웬"  # 여기 부터 부 역할 암살자
        if cham == 19:
            d = "리신"
        if cham == 20:
            d = "리븐"
        if cham == 21:
            d = "말자하"
        if cham == 22:
            d = "바이"
        if cham == 23:
            d = "베인"
        if cham == 24:
            d = "사일러스"
        if cham == 25:
            d = "신짜오"
        if cham == 26:
            d = "아리"
        if cham == 27:
            d = "아크샨"
        if cham == 28:
            d = "야스오"
        if cham == 29:
            d = "이렐리아"
        if cham == 30:
            d = "잭스"
        if cham == 31:
            d = "케인"
        if cham == 32:
            d = "퀸"
        if cham == 33:
            d = "트리스타나"
        if cham == 34:
            d = "트린다미어"
        if cham == 35:
            d = "트위치"
        if cham == 36:
            d = "티모"
        if cham == 37:
            d = "파이크"
        if cham == 38:
            d = "판테온"
        if cham == 39:
            d = "피오라" # 까지가 암살자 
        if cham == 40:  # 부터가 전사
            d = "가렌"
        if cham == 41:
            d = "갱플랭크"    
        if cham == 42:
            d = "그라가스"
        if cham == 43:
            d = "나르"
        if cham == 44:
            d = "나서스"
        if cham == 45:
            d = "다리우스"
        if cham == 46:
            d = "다이애나"
        if cham == 47:
            d = "럼블"
        if cham == 48:
            d = "레넥톤"
        if cham == 49:
            d = "렉사이"
        if cham == 50:
            d = "릴리아"
        if cham == 51:
            d = "모데카이저"
        if cham == 52:
            d = "문도박사"
        if cham == 53:
            d = "볼리베어"
        if cham == 54:
            d = "세트"
        if cham == 55:
            d = "쉬바나"
        if cham == 56:
            d = "스카너"
        if cham == 57:
            d = "아트록스" 
        if cham == 58:  
            d = "오공"  
        if cham == 59:
            d = "올라프"
        if cham == 60:
            d = "요릭"
        if cham == 61:
            d = "우디르"
        if cham == 62:
            d = "우르곳"
        if cham == 63:
            d = "워윅"
        if cham == 64:
            d = "일라오이"
        if cham == 65:
            d = "제이스"
        if cham == 66:
            d = "카밀"
        if cham == 67:
            d = "케일"
        if cham == 68:
            d = "클레드"
        if cham == 69:
            d = "트런들"
        if cham == 70:
            d = "헤카림"
        if cham == 71:
            d = "노틸러스"
        if cham == 72:
            d = "누누와 윌럼프"
        if cham == 73:
            d = "라이즈"
        if cham == 74:
            d = "람머스"
        if cham == 75:
            d = "말파이트"
        if cham == 76:
            d = "블리츠크랭크"
        if cham == 77:
            d = "뽀삐"
        if cham == 78:
            d = "사이온"
        if cham == 79:
            d = "세주아니"
        await message.channel.send(d)



access_token = os.environ['BOT_TOKEN']
client.run(access_token)

