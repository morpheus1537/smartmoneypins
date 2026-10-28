from PIL import Image, ImageDraw, ImageFont
P="/usr/share/fonts/truetype/sand-box/google/Poppins/"
G=(30,77,53); GOLD=(184,146,72); CREAM=(250,245,234)
def hero(src,out,kicker,lines):
    W,H=1000,1500; im=Image.new("RGB",(W,H),CREAM)
    s=Image.open(src).convert("RGB"); ph=880
    sc=max(W/s.width,ph/s.height); s=s.resize((int(s.width*sc)+1,int(s.height*sc)+1))
    l=(s.width-W)//2; s=s.crop((l,0,l+W,ph)); im.paste(s,(0,0))
    d=ImageDraw.Draw(im); d.rectangle([0,ph,W,ph+10],fill=GOLD)
    fk=ImageFont.truetype(P+"Poppins-SemiBold.ttf",34); fh=ImageFont.truetype(P+"Poppins-ExtraBold.ttf",84); fw=ImageFont.truetype(P+"Poppins-Bold.ttf",30)
    y=ph+60; d.text((W//2,y),kicker.upper(),font=fk,fill=GOLD,anchor="mt"); y+=70
    for t in lines: d.text((W//2,y),t,font=fh,fill=G,anchor="mt"); y+=98
    d.line([(W//2-60,H-95),(W//2+60,H-95)],fill=GOLD,width=4)
    d.text((W//2,H-70),"SMART MONEY PINS",font=fw,fill=G,anchor="mt")
    im.save(out,quality=88)
hero("assets/src-budget.jpg","assets/hero-50-30-20.jpg","Free printable inside",["The 50/30/20","Budget","Made Simple"])
hero("assets/src-side.jpg","assets/hero-side-hustles.jpg","Beginner friendly",["15 Realistic","Side Hustles","From Home"])
hero("assets/src-ef.jpg","assets/hero-emergency-fund.jpg","Step-by-step plan",["Build Your First","$1,000","Emergency Fund"])
l=Image.open("/workspace/smartmoney/logo.png").convert("RGB"); l.resize((200,200)).save("assets/logo.jpg",quality=90); l.resize((64,64)).save("assets/favicon.png")
