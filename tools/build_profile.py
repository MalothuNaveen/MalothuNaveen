from pathlib import Path
from html import escape
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
PALETTES={
'dark':dict(bg='#0b1118',surface='#111d27',ink='#f0f5f4',muted='#92a6b0',line='#263b47',accent='#84e1bc',soft='#182f2c',blue='#89bde3'),
'light':dict(bg='#f5f7f4',surface='#ffffff',ink='#172a2d',muted='#62797d',line='#d4e0dc',accent='#21745d',soft='#e4f0e8',blue='#397a9e')}
def text(x,y,value,size=16,color='ink',weight=400,mono=False,extra=''):
 return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{{{color}}}" class="{ "mono" if mono else "sans"}" {extra}>{escape(value)}</text>'
def rect(x,y,w,h,fill='surface',rx=16,extra=''):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{{{fill}}}" {extra}/>'
def wrap(body,w,h,title,theme):
 palette=PALETTES[theme]
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title>
<style>.sans{{{{font-family:Arial,Helvetica,sans-serif}}}}.mono{{{{font-family:monospace;white-space:pre}}}}.route{{{{stroke-dasharray:5 8;animation:route 12s linear infinite}}}}.pulse{{{{animation:pulse 3s ease-in-out infinite}}}}@keyframes route{{{{to{{{{stroke-dashoffset:-130}}}}}}}}@keyframes pulse{{{{50%{{{{opacity:.35}}}}}}}}@media(prefers-reduced-motion:reduce){{{{.route,.pulse{{{{animation:none}}}}}}}}</style>{body}</svg>'''
 svg=svg.format(**palette);ET.fromstring(svg);return svg
def save(name,body,w,h,title):
 for theme in PALETTES:(ROOT/'assets'/f'{name}-{theme}.svg').write_text(wrap(body,w,h,title,theme))
# Hero: stable readable identity, quiet animated system connections.
b=rect(1,1,1198,638,'bg',22,'stroke="{line}"')
b+='<path d="M35 66H1165" stroke="{line}"/>'
b+=text(38,42,'N / M',17,'accent',700,True)+text(120,41,'NAVEEN MALOTHU',12,'muted',400,True, 'letter-spacing="2"')
b+='<circle cx="929" cy="37" r="4" fill="{accent}" class="pulse"/>'+text(943,41,'OPEN TO COLLABORATION',11,'accent',400,True)
b+=text(42,119,'AI INFRASTRUCTURE · CLOUD · PRODUCT',12,'accent',400,True,'letter-spacing="1.5"')
b+=text(36,203,'Naveen',80,'ink',700,False,'letter-spacing="-4"')+text(36,284,'Malothu.',80,'ink',700,False,'letter-spacing="-4"')
b+=text(42,344,'I build the systems behind',27,'ink',400)+text(42,381,'intelligent products.',27,'accent',400)
b+=text(42,429,'Engineer. Architect. Founder.',16,'muted')
b+=rect(42,461,335,43,'soft',9)+text(59,487,'FROM FIRST IDEA → PRODUCTION',12,'accent',400,True)
# Architecture viewport
b+=rect(633,102,526,412,'surface',18,'stroke="{line}"')+text(656,132,'SYSTEMS / THINKING IN LAYERS',11,'muted',400,True,'letter-spacing="1"')
b+='<path d="M660 151H1132" stroke="{line}"/>'
# nodes and centered routing
nodes=[(682,180,177,82,'01 / INTELLIGENCE','Agents + models'),(929,180,177,82,'02 / APPLICATION','APIs + products'),(682,343,177,82,'03 / PLATFORM','Cloud + compute'),(929,343,177,82,'04 / RELIABILITY','Signals + delivery')]
for x,y,w,h,k,v in nodes:
 b+=rect(x,y,w,h,'bg',10,'stroke="{line}"')+text(x+15,y+26,k,9,'accent',400,True)+text(x+15,y+53,v,15,'ink',700)
b+='<g fill="none" stroke="{accent}" stroke-width="1.5"><path d="M859 221H929" class="route"/><path d="M770 262V343" class="route"/><path d="M1017 262V343" class="route"/><path d="M859 384H929" class="route"/></g>'
b+='<circle cx="894" cy="302" r="24" fill="{soft}" stroke="{accent}" stroke-opacity=".5"/>'+text(884,308,'<>',16,'accent',700,True)
b+=text(657,486,'DESIGN → BUILD → OPERATE → IMPROVE',11,'muted',400,True)
b+='<path d="M35 547H1165" stroke="{line}"/>'
b+=text(42,578,'CURRENTLY',10,'muted',400,True,'letter-spacing="1.5"')+text(42,607,'Lead AI, Cloud & Platform Engineer · CloudSeals',16,'ink',600)
b+=text(660,578,'BUILDING',10,'muted',400,True,'letter-spacing="1.5"')+text(660,607,'Griffin AI Tech + MyDrivingSchool',16,'ink',600)
save('engineer',b,1200,640,'Naveen Malothu — I build the systems behind intelligent products')
# Project cards: small, tangible, readable at GitHub width.
for ident,num,title,tag,lines,stack in [
 ('griffin','01','Griffin AI Tech','FOUNDER / AI PRODUCTS',['Enterprise AI and agent orchestration.','From product architecture to cloud delivery.'],'LangGraph · OpenAI · Kubernetes · FastAPI'),
 ('driving','02','MyDrivingSchool','FOUNDER / SAAS PRODUCT',['Driving school management, built end to end.','Attendance, fees, and multilingual workflows.'],'React · Node.js · PostgreSQL · Cloud')]:
 b=rect(1,1,598,308,'surface',17,'stroke="{line}"')+text(27,36,f'{num} / SELECTED WORK',10,'muted',400,True,'letter-spacing="1.5"')
 b+=text(26,94,title,34,'ink',700,False,'letter-spacing="-1"')+text(28,126,tag,10,'accent',400,True,'letter-spacing="1"')
 b+=text(28,177,lines[0],15,'muted')+text(28,204,lines[1],15,'muted')
 b+='<path d="M28 231H572" stroke="{line}"/>'+text(28,262,stack,11,'muted',400,True)+text(28,291,'EXPLORE PROJECT ↗',11,'accent',600,True)
 save(ident,b,600,310,title+' — selected work by Naveen Malothu')
# Toolkit four deliberate capability groups.
b=rect(1,1,1198,359,'bg',17,'stroke="{line}"')
items=[(30,30,'01','AI & AGENT SYSTEMS','Python · FastAPI · LangChain','LangGraph · OpenAI · RAG'),(625,30,'02','CLOUD & PLATFORM','AWS · Google Cloud · Azure','Kubernetes · Docker · Terraform'),(30,190,'03','DELIVERY & OBSERVABILITY','GitHub Actions · ArgoCD · Helm','Prometheus · Grafana · OpenTelemetry'),(625,190,'04','PRODUCT ENGINEERING','React · Next.js · TypeScript','Node.js · PostgreSQL')]
for x,y,n,label,l1,l2 in items:
 b+=text(x,y+23,n,12,'accent',700,True)+text(x+40,y+23,label,12,'ink',700,True,'letter-spacing=".6"')
 b+=text(x+40,y+65,l1,17,'muted')+text(x+40,y+94,l2,17,'muted')
b+='<path d="M30 173H1170M600 30V330" stroke="{line}"/>'
save('toolkit',b,1200,360,'Naveen’s toolkit: AI, cloud, delivery, observability and product engineering')
# System operating principles, carefully framed as approach, not invented outcomes.
b=rect(1,1,1198,239,'surface',17,'stroke="{line}"')
for x,n,heading,l1,l2 in [(32,'01','Clarity before complexity','Understand the failure modes.','Choose the smallest sound design.'),(432,'02','Reliability is a feature','Instrument what matters.','Make delivery repeatable.'),(832,'03','Ownership end to end','Connect product to infrastructure.','Build, operate, learn, improve.')]:
 b+=text(x,43,n,12,'accent',700,True)+text(x,86,heading,21,'ink',700)+text(x,134,l1,16,'muted')+text(x,162,l2,16,'muted')
b+='<path d="M400 30V210M800 30V210" stroke="{line}"/>'+text(32,211,'ENGINEERING APPROACH / PRINCIPLES, NOT SHORTCUTS',10,'accent',400,True,'letter-spacing="1"')
save('principles',b,1200,240,'Engineering approach: clarity, reliability and ownership')
print('Generated and XML-validated ten themed SVG assets.')
