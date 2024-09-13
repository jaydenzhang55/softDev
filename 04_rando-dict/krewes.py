""" Jayden Zhang
JED
SoftDev
K04 -- Python Dictionairies and Random Selection/Intro to Python/To access a random value in a dictionary, you would first get the value of the key:value pair using .get(). To grab a random value, the import random would be used.
2024-09-13
time spent: 0.3 hours """

import random # import for random class

krewes = { # list of student names
           4: [ 
		'DUA','TAWAB','EVA','JACK','VICTOR','EVAN','JASON','COLYI','IVAN','TANZEEM',
		'TAHMIM','STANLEY','LEON','NAOMI','NIA','ANASTASIA','JADY','BRIAN','JACOB',
		'ALEX','CHONGTIAN','DANNY','MARCO','ABIDUR','ANKITA','ANDY','ETHAN','AMANDA',
		'AIDAN','LINDA','QIANJUN','JIAYING','KISHI'
		],
           5: [ 
                'ADITYA','MARGIE','RACHEL','ALEXANDER','ZIYAD','DANNY','ENDRIT','CADEN',
                'VEDANT','SUHANA','KYLE','KEVIN','RAYMOND','CHRISTOPHER','JONATHAN','SASHA',
                'NAFIYU','TIM','WILL','DANIEL','BENJAMIN','CLAIRE','CHLOE','STELLA','TRACY',
                'JESSICA','JACKIE','WEN YUAN','YINWEI','TIFFANY','JAYDEN DANIEL','PRINCEDEN' 
              ]
         }

x = krewes.get(int(random.randint(4,5))) # grabs a random value from the key:value pair.

print (x[random.randint(0,len(x)-1)]) # prints a name using a random index within the value list.