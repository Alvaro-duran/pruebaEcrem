import requests
import json

def topic_id (text):
    #print(text)
    if text=="ML":
        topic_idR=1
    elif text =="SAP":
        topic_idR=2
    elif text =="Mathematics":
        topic_idR=3
    elif text =="Web development":
        topic_idR=4
    elif text =="DB development":
        topic_idR=5
    elif text =="Programming":
        topic_idR=6
    elif text =="Software":
        topic_idR=7
    elif text =="Irrelevant":
        topic_idR=8
    else:
        topic_idR=8
    
    return topic_idR
    



def sendTopic(title):
        url = 'http://127.0.0.1:8000/topic'

        headers = {
            'Content-type': 'application/x-www-form-urlencoded'
        }

        params = {
            'text': title
        }

        r = requests.post(url, headers=headers, data=params)

        print(f'Status http: {r.status_code}')

        print(f' {r.json()}')
        topic=str((f' {r.json()}'))
        topic=topic.strip()
        topic=topic.replace(".","")
        print(topic)
        topic_idr=topic_id(topic)


        return topic_idr



#a = sendTopic("Playground - OpenAI API")
#print(a)

'''

 this paragraph have diferent topic:
- Build a machine learning Model with Python. Topic: ML.
- Alvaro - Chat. Topic: Irrelevant.
- English course from the beginning COMPLETE AND FREE for BEGINNERS to ADVANCED. Topic: Irrelevant. 
- Introductory Calculus: Oxford Mathematics 1st Year Student Lecture- YouTube. Topic: Mathematics. 
- DUKI || BZRP Music Sessions #50. Topic: Irrelevant.
- Taylor Swift - Anti-Hero (Official Music Video). Topic: Irrelevant.
- Bad Gyal - Sin Carné (Video Oficial) - YouTube. Topic: Irrelevant.
- General | Microsoft Teams. Topic: Corporative Chat. - docker_quick_start.pdf . Topic: Irrelevant. 
- Injured France forward Christopher Nkunku defends Eduardo Camavinga for tackle in training that ruled him out of the World Cup after Real Madrid midfielder was targeted with racist abuse. Topic: Irrelevant. 
- Mail : Alvaro Duran Damian Outlook. Topic: Irrelevant. 
- Curso SAP FI Completo | Udemy. Topic: SAP. 
- Cursos de SAP - educaweb.com. Topic: SAP.
- Curso de Consultor SAP en Finanzas y Tesorería (Módulos FI TR) on-line por Esneca Business School - educaweb.com Topic: SAP.
- Certificado profesional de SAP Technology Consultant | Coursera. Topic: SAP.
- Software Engineering MasterTrack® Certificate | Coursera. Topic: Software.
- UK Home | Daily Mail Online. Topic: Irrelevant. 
- Curso de C++ desde CERO (Completo) - Nivel JUNIOR - YouTube. Topic: Programming.
-Complete Mathematics Masterclass: College & University Level | Udemy. Topic: Mathematics.
-Machine Learning y Data Science: Curso Completo con Python | Udemy. Topic: ML.
-Software Testing desde cero : MasterClass todo en 1 (2022) | Udemy. Topic: ML.
-The Mainframe Development Course : IMS-DB | Udemy. Topic: DB development.
-Modern Application Development with Python on AWS | Coursera. Topic:  DB development.
-Responsive Website Development and Design | Coursera. Topic: Web development.
-The Web Developer Bootcamp: Learn HTML, CSS, Node, and More! | Udemy. Topic: Web development.
-Learn Python Programming Masterclass | Udemy. Topic. Programming.
-HTML, CSS, and Javascript for Web Developers | Coursera. Topic: Web development.
-Cutting-Edge AI: Deep Reinforcement Learning in Python | Udemy. Topic: ML.
-Fundamentals of Database Engineering | Udemy. Topic: DB development.
-Digital Signal Processing (DSP) From Ground Up™ in Python | Udemy. Topic: Software.
-Digital Signal Processing with MATLAB Applications | Udemy: Topic: Software.
-Nueva pestaña. Topic: Irrelevant.

Playground - OpenAI API
https://beta.openai.com/playground
 We have only this Topics: ML, SAP, Mathematics,DB development,Web development,Mathematics,Web development,DB development,Programming,Software and Irrelevant (everything that is not with the previous labels).

What topic have this paragraph?

Angular: De cero a experto | Udemy


Topic:


Web development.

'''


'''
  this paragraph have diferent topic:
- Build a machine learning Model with Python. Topic: ML.
- Alvaro - Chat. Topic: Irrelevant.
- English course from the beginning COMPLETE AND FREE for BEGINNERS to ADVANCED. Topic: Irrelevant. 
- Introductory Calculus: Oxford Mathematics 1st Year Student Lecture- YouTube. Topic: Mathematics. 
- DUKI || BZRP Music Sessions #50. Topic: Irrelevant.
- Taylor Swift - Anti-Hero (Official Music Video). Topic: Irrelevant.
- Bad Gyal - Sin Carné (Video Oficial) - YouTube. Topic: Irrelevant.
- General | Microsoft Teams. Topic: Corporative Chat. - docker_quick_start.pdf . Topic: Irrelevant. 
- Injured France forward Christopher Nkunku defends Eduardo Camavinga for tackle in training that ruled him out of the World Cup after Real Madrid midfielder was targeted with racist abuse. Topic: Irrelevant. 
- Mail : Alvaro Duran Damian Outlook. Topic: Irrelevant. 
- Curso SAP FI Completo | Udemy. Topic: SAP. 
- Cursos de SAP - educaweb.com. Topic: SAP.
- Curso de Consultor SAP en Finanzas y Tesorería (Módulos FI TR) on-line por Esneca Business School - educaweb.com Topic: SAP.
- Certificado profesional de SAP Technology Consultant | Coursera. Topic: SAP.
- Software Engineering MasterTrack® Certificate | Coursera. Topic: Software.
- UK Home | Daily Mail Online. Topic: Irrelevant. 
- Curso de C++ desde CERO (Completo) - Nivel JUNIOR - YouTube. Topic: Programming.
-Complete Mathematics Masterclass: College & University Level | Udemy. Topic: Mathematics.
-Machine Learning y Data Science: Curso Completo con Python | Udemy. Topic: ML.
-Software Testing desde cero : MasterClass todo en 1 (2022) | Udemy. Topic: ML.
-The Mainframe Development Course : IMS-DB | Udemy. Topic: DB development.
-Modern Application Development with Python on AWS | Coursera. Topic:  DB development.
-Responsive Website Development and Design | Coursera. Topic: Web development.
-The Web Developer Bootcamp: Learn HTML, CSS, Node, and More! | Udemy. Topic: Web development.
-Learn Python Programming Masterclass | Udemy. Topic. Programming.
-HTML, CSS, and Javascript for Web Developers | Coursera. Topic: Web development.
-Cutting-Edge AI: Deep Reinforcement Learning in Python | Udemy. Topic: ML.

What topic have this paragraph? 




'''



'''
 this paragraph have diferent topic:
- Tab name: Build a machine learning Model with Python. Topic: ML.
- Tab name: Alvaro - Chat. Topic: Irrelevant.
- Tab name: English course from the beginning COMPLETE AND FREE for BEGINNERS to ADVANCED. Topic: Irrelevant. 
- Tab name: Introductory Calculus: Oxford Mathematics 1st Year Student Lecture- YouTube. Topic: Mathematics. 
- Tab name: DUKI || BZRP Music Sessions #50. Topic: Irrelevant.
- Tab name: Taylor Swift - Anti-Hero (Official Music Video). Topic: Irrelevant.
- Tab name: Bad Gyal - Sin Carné (Video Oficial) - YouTube. Topic: Irrelevant.
- Tab name: General | Microsoft Teams. Topic: Corporative Chat. - docker_quick_start.pdf . Topic: Irrelevant. 
- Tab name: Injured France forward Christopher Nkunku defends Eduardo Camavinga for tackle in training that ruled him out of the World Cup after Real Madrid midfielder was targeted with racist abuse. Topic:Irrelevant. 
- Tab name: Mail : Alvaro Duran Damian Outlook. Topic: Irrelevant. 
- Tab name: Curso SAP FI Completo | Udemy. Topic: SAP. 
- Tab name: Cursos de SAP - educaweb.com. Topic: SAP.
- Tab name: Curso de Consultor SAP en Finanzas y Tesorería (Módulos FI TR) on-line por Esneca Business School - educaweb.com Topic: SAP.
- Tab name: Certificado profesional de SAP Technology Consultant | Coursera. Topic: SAP.
- Tab name: Software Engineering MasterTrack® Certificate | Coursera. Topic: Software.
- Tab name: UK Home | Daily Mail Online. Topic: Irrelevant. 
- Tab name: Curso de C++ desde CERO (Completo) - Nivel JUNIOR - YouTube. Topic: Programming.
- Tab name: Complete Mathematics Masterclass: College & University Level | Udemy. Topic: Mathematics.
- Tab name: Machine Learning y Data Science: Curso Completo con Python | Udemy. Topic: ML.
- Tab name: Software Testing desde cero : MasterClass todo en 1 (2022) | Udemy. Topic: ML.
- Tab name: The Mainframe Development Course : IMS-DB | Udemy. Topic: DB development.
- Tab name: Modern Application Development with Python on AWS | Coursera. Topic:  DB development.
- Tab name:Responsive Website Development and Design | Coursera. Topic: Web development.
- The Web Developer Bootcamp: Learn HTML, CSS, Node, and More! | Udemy. Topic: Web development.
- Tab name: Learn Python Programming Masterclass | Udemy. Topic. Programming.
- Tab name: HTML, CSS, and Javascript for Web Developers | Coursera. Topic: Web development.
- Tab name: Cutting-Edge AI: Deep Reinforcement Learning in Python | Udemy. Topic: ML.
- Tab name: Fundamentals of Database Engineering | Udemy. Topic: DB development.
- Tab name: Digital Signal Processing (DSP) From Ground Up™ in Python | Udemy. Topic: Software.
- Tab name: Digital Signal Processing with MATLAB Applications | Udemy: Topic: Software.
- Tab name: Nueva pestaña. Topic: Irrelevant.
- Tab name: Angular: De cero a experto | Udemy
- Tab name: Node: De cero a experto | Udemy. Topic: Programming.



'''