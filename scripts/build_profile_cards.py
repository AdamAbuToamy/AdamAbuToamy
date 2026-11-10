#!/usr/bin/env python3
"""Compose real repository GIF frames into self-contained dark project cards."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageSequence
import io, os, urllib.request

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "profile-v3"
OUT.mkdir(parents=True, exist_ok=True)
W,H=1100,365
BG=(10,19,33); ORANGE=(255,150,62); WHITE=(246,248,250); MUTED=(191,206,222)

def font(sz,bold=False):
    candidates=["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
    for p in candidates:
        if os.path.exists(p):return ImageFont.truetype(p,sz)
    return ImageFont.load_default()

def rounded(draw,box,fill,r=18,outline=None,width=1):
    draw.rounded_rectangle(box,radius=r,fill=fill,outline=outline,width=width)

def base(title,eyebrow,desc,tools,bullets):
    im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
    rounded(d,(2,2,W-3,H-3),BG,24,ORANGE,2)
    d.line((30,32,112,32),fill=ORANGE,width=5)
    d.line((30,32,30,62),fill=ORANGE,width=5)
    d.text((40,49),eyebrow,font=font(17,True),fill=ORANGE)
    d.text((40,90),title,font=font(41,True),fill=WHITE)
    d.line((40,148,169,148),fill=ORANGE,width=4)
    d.text((40,169),desc,font=font(19),fill=MUTED)
    x=40
    for tech in tools[:3]:
        tfont=font(15,True)
        b=d.textbbox((0,0),tech,font=tfont); width=b[2]+27
        rounded(d,(x,216,x+width,249),(21,42,63),13,(56,94,124),1)
        d.text((x+13,222),tech,font=tfont,fill=WHITE)
        x+=width+9
    y=274
    for bullet in bullets[:2]:
        d.ellipse((42,y+7,49,y+14),fill=ORANGE)
        d.text((61,y),bullet,font=font(17),fill=MUTED)
        y+=31
    rounded(d,(562,26,1074,339),(17,29,45),17,(93,106,124),2)
    return im

def source_frames(local_path,remote=None):
    if local_path and local_path.exists():
        im=Image.open(local_path)
    elif remote:
        with urllib.request.urlopen(remote,timeout=35) as r: data=r.read()
        im=Image.open(io.BytesIO(data))
    else:
        raise RuntimeError("Missing original media: "+str(local_path))
    frames=[];duration=[]
    if getattr(im,"is_animated",False):
        n=getattr(im,"n_frames",1)
        picks=sorted(set(round(i*(n-1)/min(17,n-1)) for i in range(min(18,n)))) if n>1 else [0]
        for index in picks:
            im.seek(index)
            frames.append(im.convert("RGB").copy())
            duration.append(max(80,min(350,int(im.info.get("duration",120) or 120))))
    else:
        frames=[im.convert("RGB").copy()]
        duration=[2400]
    return frames,duration

def compose(name,title,eyebrow,desc,tools,bullets,media,remote=None):
    frames,durations=source_frames(ROOT/media if media else None,remote)
    target=(492,291)
    out=[]
    for frame in frames:
        image=base(title,eyebrow,desc,tools,bullets)
        draw=ImageDraw.Draw(image)
        thumb=frame.copy()
        thumb.thumbnail(target,Image.Resampling.LANCZOS)
        px=572+(492-thumb.width)//2;py=37+(291-thumb.height)//2
        image.paste(thumb,(px,py))
        out.append(image)
    target_file=OUT/(name+".gif")
    out[0].save(target_file,save_all=True,append_images=out[1:],duration=durations,loop=0,optimize=True)
    print(name,target_file.stat().st_size,len(out))

compose("wilo-card","WILO","01 / LIVE PRODUCT","Projects & university workspace",
        ["React","TypeScript","Firebase"],["Offline edits & account sync","Real multi-device web application"],
        "assets/wilo-preview.gif")
compose("postmark-card","PostMark AI","02 / EMAIL AUTOMATION","AI-assisted inbox organization",
        ["Python","FastAPI","SQLite"],["Multi-account categorization","Backend APIs & persistence"],
        None,"https://raw.githubusercontent.com/AdamAbuToamy/PostMark-ai-email-agent/main/assets/inbox-live.png")
compose("robot-card","Robot Arm Studio","03 / ROBOTICS","Physical robotic-arm prototype",
        ["Hardware","Robotics","Motion"],["Real assembled prototype","Original motion demonstration"],
        "assets/robot-motion.gif")
compose("drone-card","FPV Drone","04 / DRONE ENGINEERING","FPV build & flight diagnostics",
        ["Betaflight","Hardware","Testing"],["Original orientation test","Controller integration & build"],
        "assets/drone-betaflight.gif")


def build_tech_animation():
    categories=[
      ("LANGUAGES",["Python","TypeScript","JavaScript","C#","Java","C++"]),
      ("FRAMEWORKS & APIs",["React","FastAPI",".NET","REST APIs"]),
      ("DATA & DEV TOOLS",["Firebase","SQLite","Git","GitHub Actions","Linux / WSL","VS Code"])]
    frames=[]
    for step in range(18):
        im=Image.new("RGB",(1100,400),(10,19,33))
        d=ImageDraw.Draw(im)
        rounded(d,(2,2,1097,397),(11,21,36),24,ORANGE,2)
        d.text((42,26),"LANGUAGES & TECHNOLOGIES",font=font(33,True),fill=WHITE)
        d.text((43,74),"Organized by what I use in real projects",font=font(19),fill=MUTED)
        counter=0
        for j,(heading,items) in enumerate(categories):
            y=116+j*94
            d.text((43,y),heading,font=font(19,True),fill=ORANGE)
            x=43
            for item in items:
                w=max(104,len(item)*12+29)
                shown=counter<step
                rounded(d,(x,y+32,x+w,y+71),(24,47,71) if shown else (14,29,44),13,(60,111,150) if shown else (31,56,76))
                d.text((x+13,y+43),item,font=font(17,True),fill=WHITE if shown else (66,92,115))
                x+=w+10
                counter+=1
        frames.append(im)
    frames[0].save(OUT/"tech-stack.gif",save_all=True,append_images=frames[1:],duration=[190]*17+[1100],loop=0,optimize=True)
    print("tech-stack", (OUT/"tech-stack.gif").stat().st_size)

def build_contributions():
    # Source is the real data-derived GitHub contributions graphic in this repository.
    import cairosvg
    svg=(ROOT/"profile-3d-contrib/recent-16-weeks.svg").read_bytes()
    png=cairosvg.svg2png(bytestring=svg)
    src=Image.open(io.BytesIO(png)).convert("RGB")
    src.thumbnail((1040,440),Image.Resampling.LANCZOS)
    frames=[]
    for i in range(14):
        im=Image.new("RGB",(1100,495),(9,18,31))
        d=ImageDraw.Draw(im)
        rounded(d,(2,2,1097,492),(10,20,34),24,ORANGE,2)
        d.text((35,22),"GITHUB CONTRIBUTIONS / LAST 16 WEEKS",font=font(24,True),fill=WHITE)
        extent=round(src.width*(i+1)/14)
        strip=src.crop((0,0,extent,src.height))
        im.paste(strip,(30,65))
        frames.append(im)
    frames[0].save(OUT/"contributions.gif",save_all=True,append_images=frames[1:],duration=[150]*13+[1100],loop=0,optimize=True)
    print("contributions", (OUT/"contributions.gif").stat().st_size)

build_tech_animation()
build_contributions()
