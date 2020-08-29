import numpy as np
import random
import time
from gtts import gTTS
import os
import requests


#leitura dos alunos
def getAlunos():
	r = requests.get('https://lincolnmr.github.io/agent/students.json')
	data = r.json()
	alunos = data['students']
	return alunos

def playVoice(aluno):
  language = 'pt-br'
  output = gTTS(text=aluno, lang=language, slow=False)
  output.save('output.mp3')
  os.system("start output.mp3")
  print(aluno)

#gera um número randomico para definir o tempo entre cada chamada
def timeRandom():
  time = random.randint(1,15) # como a duracaoAula é 100 e considerando que o random da quantidadeChamada e do time 
                              # seja respectivamente 6 e 15, ainda não iria ultrapassar o tempo de aula
  return time

#gera o horário para definir o intervalo entre os nomes dos alunos
def getHorario(numAlunos, quantidadeChamada, duracaoAula):
  horario = (duracaoAula / numAlunos) / quantidadeChamada
  return horario

alunos = getAlunos()

#função que faz a chamada
def chamada():

  numAlunos = len(alunos)
  quantidadeChamada = random.randint(2,6) #gera um inteiro randômico entre 2 e 6 para definir a quantidade de chamadas realizadas na aula
                                          #haverá pelo menos duas chamadas por padrão
  duracaoAula = 100

  horario = getHorario(numAlunos, quantidadeChamada, duracaoAula)
  
  alunosChamados = []
  
  init = 2 #esta variável ira ajudar na comparação com à quantidade de chamadas para finalizar o while
  while init <= quantidadeChamada: #loop onde as chamadas serão realizadas

    time.sleep(timeRandom()) #gera a pausa entre as chamadas

    print('!! Chamada !!\n')
    
    calltime = 0
    while calltime < numAlunos: #aqui os nomes serão chamados
      
      aluno = random.choice(alunos) 

      if aluno in alunosChamados:
        continue
      else:
        time.sleep(horario)
        playVoice(aluno)
        alunosChamados.append(aluno)
        calltime += 1

    alunosChamados[:] = [] #depois do while finalizado, o array é zerado para a próxima chamada
    init += 1

chamada()