import socket
import random
import time
import re
import string
import traceback
import json

server = ('irc.orderofthetilde.net', 6667)
username = "gamebot" 
#+ str(random.randrange(1,69))
hoppy = '#Battlearena'

s = socket.socket()
s.connect(server)
s.send('NICK '+ username + '\r\n')
s.send('USER ' + username + ' . . :retard\r\n')

possible_monsters = ['Bee','BluePoring','Poring','Lost_Soul', 'orb_fountain','Wild_Rabbit','Jester', 'Ding_Bats', 'Brauner', 'Tiamat', 'Dirt_Eater', 'Orcish_Impaler', 'Strolling_Sapling', 'HealSlime', 'GreenSlime', 'BlueSlime', 'Stone_Eater']




with open('data.txt') as json_file:  
    possible_monsters = json.load(json_file)


readbuffer = ""
monsters = []
monster = ''
hit = ' !attack '
me = ' :\x01ACTION'
techH = ' uses his chargedshot on '
techF = ' uses his doublepunch on '
idk = 'PRIVMSG ' + hoppy + " I don't know who to fight. Use !gamebot load <monster> then !gamebot fight to teach me" + '\r\n'
lo = 1

current_weapon = 'fists'	
while 1:
    readbuffer = s.recv(2048)
    lines = readbuffer.split('\n')

    for line in lines: 
        line = line.rstrip()
        feed = line
        feed = re.sub(r'[\x02\x1F\x0F\x16]|\x03(\d\d?(,\d\d?)?)?', '', feed)
        feed = re.sub(r'\,','' , feed)
        feed = re.sub(r'\]','' , feed)
        print 'this is feed' + feed
        terms = feed.split()
        if not terms: continue
        print terms
	
	
	 
	
	
	
        # put comamnds and checks after this comment. Everything above this is all that is needed.
        try:
            
            if len(terms) >= 0 and terms[0] == 'PING':
                s.send('PONG '+terms[1]+'\r\n')

            elif len(terms) >= 1 and '376' == terms[1]:
                s.send('JOIN ' + hoppy +'\r\n')
                s.send('PRIVMSG ' + hoppy + ' !id 54321' + '\r\n')

            if len(terms) >= 3 and ':!test' == terms[3]:
                s.send('PRIVMSG ' + hoppy + ' test' + '\r\n')
            elif len(terms) > 4 and 'dimensional'== terms[4]: 
                s.send('PRIVMSG ' + hoppy + ' !enter' + '\r\n')
            elif len(terms) > 5 and 'dimensional'== terms[5] and terms[4] == 'powerful': 
                s.send('PRIVMSG ' + hoppy + ' !enter' + '\r\n')

            elif len(terms) > 7 and terms[4] == 'Allied' and terms[5] == 'Forces' and terms[7] == 'detected':
                s.send('PRIVMSG ' + hoppy + ' !enter' + '\r\n')
            elif terms[3] == ':!gamebot' and terms[4] == 'say' and terms[5] != ':/me':
                print terms[5:]
                say = str(terms[5:]).strip('[]')
                say = say.strip(',')
                say = say.strip("'")
                say = re.sub(r"\'\,\s\'",' ', say)
                s.send('PRIVMSG ' + hoppy + ' ' + say + '\r\n')
            elif terms[3] == ':!gamebot' and terms[4] == 'say' and terms[5] == ':/me':
                print terms[6:]
                say = str(terms[5:]).strip('[]')
                say = say.strip(',')
                say = say.strip("'")
                say = re.sub(r"\'\,\s\'",' ', say)
                s.send('PRIVMSG ' + hoppy + ' ' + me + ' ' + say + '\r\n')
            elif len(terms) >= 3 and ':!printmonsters' == terms[3]:
                s.send('PRIVMSG ' + hoppy + ' the monsters are ' + str(monsters) + '\r\n')
                s.send('PRIVMSG ' + hoppy + ' hello ' + str(PM) + '\r\n')
                print 'the cmd is working'
            elif ':!gamebot' == terms[3] and 'help' == terms[4]:
                s.send('PRIVMSG ' + hoppy + ' Gamebot Help' + '\r\n')
                s.send('PRIVMSG ' + hoppy + ' Gamebot not playing its turn? !gamebot load <monster> will tell gamebot what monster you are fighting, !gamebot fight will make gamebot attack' + '\r\n')
                s.send('PRIVMSG ' + hoppy + ' Want gamebot to say a cmd? !gamebot say <msg> will say anything you want it too' + '\r\n')
            if len(terms)>= 7 and terms[3] == ':!gamebot' and terms[4] == 'redorbs' and terms[7] == 'maddux1':
                s.send('PRIVMSG ' + hoppy + me + ' gives ' + terms[5] + ' redorbs to ' + terms[6] + '\r\n')
        except:
            print traceback.print_exc()
        try:
            if current_weapon == 'fists' and len(terms) > 6 and terms[3] == ':gamebot' and terms[4] != 'has' and terms[4] != 'gets' and terms[5] != 'another' and terms[4] != 'steps':
                time.sleep(1)
                s.send('PRIVMSG ' + hoppy + ' !equip handgun' + '\r\n')
                time.sleep(2)
                current_weapon = 'handgun'
                print current_weapon
            elif current_weapon == 'handgun' and len(terms) > 11 and terms[4] != 'has' and terms[3] == ':gamebot' and terms[4] != 'gets' and terms[5] != 'another' and terms[4] != 'steps':
                time.sleep(1) 
                s.send('PRIVMSG ' + hoppy + ' !equip fists' + '\r\n')
                time.sleep(2)
                current_weapon = 'fists' 
                print current_weapon
           
                
           
            if len(terms) > 4 and 'Order:' == terms[4]:
                for term in terms:
                    if term in possible_monsters:
                        monsters.append(term) 
                        print monsters
            if monsters == []:
                if len(terms) > 4 and ':gamebot' == terms[3] and 'steps' == terms[4]:
                    s.send(idk)
                if len(terms) > 5 and "gamebot" == terms[3] and terms[5]== 'another':
                    s.send(idk)
                if len(terms) > 5 and "gamebot's" == terms[5]:
                    s.send(idk)
                if len(terms) >= 8 and ':Error:' == terms[3] and 'gamebot' == terms[4] and 'turn!' == terms[8]:
                    s.send(idk)
            if len(monsters) >= 1:       
                monster = random.choice(monsters)
                print monster
                attack = 'PRIVMSG ' + hoppy + hit + monster + '\r\n'
                if current_weapon == 'handgun':
                    attack = 'PRIVMSG ' + hoppy + me + techH + monster + '\x01\n'
                if current_weapon == 'fists':
                    attack = 'PRIVMSG ' + hoppy + me + techF + monster + '\x01\n'
                if len(terms) > 16 and terms[3] == ':gamebot' and terms[6] == 'allowed' and terms[10] == 'action' and terms[16] == 'conditions!':
                    attack = 'PRIVMSG ' + hoppy + hit + monster + '\r\n'
                    time.sleep(5)
                    s.send(attack)
                if terms[3] == ':Error:' and terms[7] == 'technique':
                    s.send(attack)
                if len(terms) >= 8 and ':Error:' == terms[3] and 'gamebot' == terms[4] and 'turn!' == terms[8]:
                    s.send(attack)
                if len(terms) > 4 and ':gamebot' == terms[3] and 'steps' == terms[4]:
                    time.sleep(1)
                    s.send(attack)
                elif len(terms) >= 4 and terms[3] == ':!gamebot' and terms[4] == 'fight':
                    time.sleep(1)
                    s.send(attack)    
                elif len(terms) > 5 and ":gamebot" == terms[3] and terms[5]== 'another':
                    time.sleep(1)    
                    s.send(attack)     
                elif len(terms) > 5 and "gamebot's" == terms[5]:
                    time.sleep(1)
                    s.send(attack)
                elif len(terms) > 4 and terms[3] == ':gamebot' and terms[4] == 'gets':
                    time.sleep(1)
                    s.send(attack)   
                elif len(terms) >= 4 and terms[3] == ':!gamebot' and terms[4] == 'fight':
                    time.sleep(3)
                    s.send(attack)
                elif terms[3] == ':Error:' and terms[4] == 'gamebot' and terms[9] == 'weapon.':
                    time.sleep(3)
                    s.send(attack)
                    #Error: gamebot is already using that weapon.
                elif terms[3] == ':Error:' and terms[4] in monsters:
                    monsters.remove(terms[4])
                    time.sleep(2)
                    s.send(attack)
           
                       
            if len(terms) > 5 and 'their' == terms[4] and 'victory' == terms[5]: 
                monsters = []
            if len(terms) > 5 and 'their' == terms[4] and 'efforts' == terms[5]:
                monsters = []     
        except:
            print traceback.print_exc()
        try:
            if len(terms) >= 5 and terms[3] == ':!gamebot' and terms[4] == 'load':
                possible_monsters.append(terms[5])
                monsters = []
                monsters.append(terms[5]) 
                with open('data.txt', 'w') as outfile:  
                    json.dump(possible_monsters, outfile)          
        except:
            print traceback.print_exc()
with open('data.txt', 'a') as outfile:  
    json.dump(possible_monsters, outfile)
