from fastapi import FastAPI
from fastapi import Form
import openai
import os
#uvicorn main:app --reload   

app = FastAPI()

@app.post("/topic")
async def contact(text: str = Form(...)):

    TopicStructure="""
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
- Tab name: Responsive Website Development and Design | Coursera. Topic: Web development.
- Tab name: The Web Developer Bootcamp: Learn HTML, CSS, Node, and More! | Udemy. Topic: Web development.
- Tab name: Learn Python Programming Masterclass | Udemy. Topic. Programming.
- Tab name: HTML, CSS, and Javascript for Web Developers | Coursera. Topic: Web development.
- Tab name: Cutting-Edge AI: Deep Reinforcement Learning in Python | Udemy. Topic: ML.
- Tab name: Fundamentals of Database Engineering | Udemy. Topic: DB development.
- Tab name: Digital Signal Processing (DSP) From Ground Up™ in Python | Udemy. Topic: Software.
- Tab name: Digital Signal Processing with MATLAB Applications | Udemy: Topic: Software.
- Tab name: Nueva pestaña. Topic: Irrelevant.
- Tab name: Angular: De cero a experto | Udemy
- Tab name: Node: De cero a experto | Udemy. Topic: Programming.
- Tab name: """ +text+". Topic: "

    openai.api_key = "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"




    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=TopicStructure,
    temperature=0.5,
    max_tokens=48,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop="- Tab name:"
  
    )

    textTopic=response['choices'][0]['text']

    return textTopic