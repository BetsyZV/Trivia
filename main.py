#TRIVIAAA##
import random 
import time
#Constantes para el color del texto
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
NEGRI='\033[1m'
RAYA='\033[4m'
END='\033[0m'

# Iniciamos la variable en True
iniciar_trivia = True  
intentos = 0
#BIENVENIDA************************
print (RAYA+ NEGRI+RED+"\nBIENVENIDO A MI " +RESET+WHITE+"TRIVIA SOBRE "+RESET+RED+"FIESTAS PATRIAS"+RESET+END)
time.sleep(2)
print (WHITE+"\n En este juego pondremos a prueba tus conocimientos")
print(" En breve iniciará el juego, estás listo!!"+RESET)
time.sleep(4)
for numero_carga in range (5,0,-1):
  print (numero_carga)
  time.sleep(0.5) #Tiempo de espera
#Ingresa el nombre del jugador
nombre= input(GREEN+"\n Ingresa tu nombre: "+RESET)
#INICIAR BLUCLE DE TRIVIA 
while iniciar_trivia == True: #  Mientras iniciar_trivia sea True, repite:
  intentos += 1
  #Otorgar puntaje de entrada al usuario
  puntos=random.randint(1,5) 
  r=0 #conteo de respuestas correctas
  print(MAGENTA+NEGRI+"\nINTENTO NÚMERO", intentos)
  # Instrucciones sobre cómo jugar:
  print (END+WHITE+"\nHola ",nombre, "Responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"+RESET)
  time.sleep(4)
  print(YELLOW+NEGRI+"Inicias la trivia con", puntos, "puntos a favor en..."+END)
  for numero_carga in range (5,0,-1):
    print (numero_carga)
    time.sleep(0.5)
  
  # Pregunta 1
  print (BLUE+NEGRI+"\n1) ¿Quién se tiró del morro de Arica con la bandera del Perú?"+END)
  print (BLUE+"a) Miguel Grau")
  print ("b) Alfonso Ugarte")
  print ("c) Jose Olaya")
  print ("d) Francisco Bolognesi"+RESET)
  time.sleep(2) #Tiempo de espera
  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input(GREEN+"\nTu respuesta: "+RESET).lower()
  #Validamos las letras de la alternativa
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input(CYAN+"\nDebes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET).lower()
  #Comprovamos la respuesta
  if respuesta_1== "b":
    puntos +=10
    print(YELLOW+"\nEs correcto",nombre,". Haz alcanzado",puntos, "puntos"+RESET)
  elif respuesta_1== "a": 
    print (RED+"\nIncorrecto", nombre, ". Miguel Grau fue un gran almirante de la Marina de Guerra del Perú."+RESET)
    print(YELLOW+nombre, "llevas", puntos, "puntos"+RESET)
  elif respuesta_1== "c": 
    print (RED+"\nIncorrecto", nombre, ". José Olaya fue un mártir en la lucha por la Independencia del Perú."+RESET)
    print(YELLOW+nombre, "llevas", puntos, "puntos"+RESET)
  elif respuesta_1== "d": 
    print (RED+"\nIncorrecto", nombre, ". Francisco Bolognesi fue un militar peruano conocido por su participación en la Guerra del Pacífico."+RESET)
    print(YELLOW+nombre, "llevas", puntos, "puntos"+RESET)
  time.sleep(3) #Tiempo de espera
  
    # Pregunta 2
  print (BLUE+ NEGRI+"\n \n2) ¿En que región del Perú se encuentra un de las 7 maravillas del mundo?"+END)
  print (BLUE+"a) Piura")
  print ("b) Lima")
  print ("c) Cajamarca")
  print ("d) Cusco"+RESET)
  time.sleep(3) #Tiempo de espera
  
  respuesta_2 = input(GREEN+"\nTu respuesta: "+RESET).lower()
  while respuesta_2 not in ("a", "b", "c", "d", "h"):
    respuesta_2 = input(CYAN+"\nDebes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET).lower()
  if respuesta_2== "d":
    puntos += 10
    print(YELLOW+"\nEs correcto", nombre, ". Haz alcanzado", puntos, "puntos"+RESET)
  elif respuesta_2== "a": 
    print (RED+"\nIncorrecto", nombre, ". Piura es el mejor destino turistico del Perú para veranear en sus playas"+RESET)
    print(YELLOW+nombre, "llevas", puntos, "puntos"+RESET)
  elif respuesta_2== "b":
    print (RED+"\nIncorrecto", nombre, ". Lima es la capital del Perú."+RESET)
    print(YELLOW+nombre, "llevas", puntos, "puntos"+RESET)
  elif respuesta_2== "c": 
    print (RED+"\nIncorrecto", nombre, ". Cajamarca es conocida porque alberga los famasos baños del inca"+RESET)
    print(YELLOW+nombre, "llevas", puntos, "puntos"+RESET)
  time.sleep(3)
  
  # Pregunta 3
  print (BLUE+NEGRI+"\n \n3) ¿Cuál es el plato bandera del Perú?"+END)
  print (BLUE+"a) Juane")
  print ("b) Seco de chavelo")
  print ("c) Ceviche")
  print ("d) Pozole"+RESET)
  time.sleep(3) #Tiempo de espera
  
  respuesta_3 = input(GREEN+"\nTu respuesta: "+RESET).lower()
  
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input (CYAN+"\nDebes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET).lower()
  
  if respuesta_3 == "a":
    print (RED+ "\nIncorrecto!! El juane es como un tamal, típico de la gastronomía de la selva peruana"+RESET)
    puntos = puntos + 3
    print(YELLOW+nombre, "llevas", puntos, "puntos"+RESET)
  elif respuesta_3 == "b":
    print (RED+"\nIncorrecto!! El Seco de Chavelo, es un plato tipico del norte del Perú"+RESET)
    puntos = puntos + 3
    print(YELLOW+nombre, "llevas", puntos, "puntos"+RESET)
  elif respuesta_3 == "d":
    print (RED+"\nTotalmente incorrecto!! El Pozole es una sopa tradicional mexicana..."+RESET)
    puntos = puntos - 5
    print(YELLOW+nombre, "llevas", puntos, "puntos"+RESET)
  else:
    print (YELLOW+"\nCorrecto!! El ceviche es plato bandera del Perú!"+RESET)
    puntos +=10
    print(YELLOW+nombre, "llevas", puntos, "puntos"+RESET)
  
  time.sleep(3)
  # Pregunta 4
  print (BLUE+NEGRI+"\n \n4) ¿En qué año se proclamo la independencia del Perú?"+END)
  print (BLUE+"a) 1821")
  print ("b) 1824")
  print ("c) 1879")
  print ("d) 1880"+RESET)
  time.sleep(3) #Tiempo de espera
  
  respuesta_4 = input(GREEN+"\nTu respuesta: "+RESET).lower()
  while respuesta_4 not in ("a", "b", "c", "d"):
    respuesta_4 = input (CYAN+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "+RESET).lower()
  
  if respuesta_4 == "b":
    print (RED+ "\nIncorrecto!! El 6 de agosto de 1824 se desarrollo la Batalla de Junín"+RESET)
    print(YELLOW+nombre, "llevas", puntos, "puntos"+RESET)
  elif respuesta_4 == "c":
    print (RED+"\nIncorrecto!! 8 de octubre de 1879 se desarrollo el Combate de Angamos"+RESET)
    print(YELLOW+nombre, "llevas", puntos, "puntos"+RESET)
  elif respuesta_4 == "d":
    print (RED+"\nIncorrecto!! El 7 de junio de 1880 se desarrollo la Batalla de Arica"+RESET)
    print(YELLOW+nombre, "llevas", puntos, "puntos"+RESET)
  else:
    print (YELLOW+"\nCorrecto!! El 28 de Julio de 1821, el general José de San Martín proclamo la independencia del Perú!"+RESET)
    puntos += 10
    print(YELLOW+nombre, "llevas", puntos, "puntos"+RESET)

  #conteo de respuestas correctas
  if respuesta_1== "b":
    r= r+1
  if respuesta_2== "d":
    r= r+1
  if respuesta_3== "c":
    r = r+1
  if respuesta_4== "a":
    r =r+1
    
  
  time.sleep(3)
  #FIN DE TRIVIA
  print (MAGENTA+ NEGRI+"\nGracias", nombre, "por jugar mi trivia, alcanzaste ", puntos, "puntos"+END)

  print (MAGENTA+ NEGRI+"\nObtuviste", r, "respuestas correctas "+END)
  r=4-r
  print (MAGENTA+ NEGRI+"\nObtuviste", r, "respuestas incorrectas "+END)
  #INTENTAR TRIVIA NUEVAMENTE
  print(GREEN+NEGRI+"\n¿Deseas intentar la trivia nuevamente?"+END)
  repetir_trivia = input(GREEN+"Ingresa 'si' para repetir, o cualquier tecla para finalizar: "+RESET).lower()

  if repetir_trivia != "si":  # != significa "distinto"
   print(MAGENTA+NEGRI+"\nEspero",nombre, "que lo hayas pasado bien, hasta pronto!"+END)
   iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.
