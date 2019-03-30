from utils import *
import random as rand
from colorama import init
import os

init()

line = "\033[36m-------------------------------------------\033[0m"
game_frame = (
"""
%s
\033[33;1m\t\t\t\tСчёт: %s
Выберите подходящее под маску имя файла\033[0m
%s
\033[32;1mМаска: %s\033[0m
\033[37;1mВарианты ответов:
\t1. %s
\t2. %s
\t3. %s
\t4. %s\033[0m
%s
""")

inter_frame = (
"""
%s
\033[33;1m\t\t\tСчёт: %s\033[0m
\033[37;1mВариант ответа %s - %s
%s
\t1. %s
\t2. %s
\t3. %s
\t4. %s\033[0m
%s
""")

def cprint(s):
	os.system('cls' if os.name == 'nt' else 'clear')
	print(s)

def intermFrame(inp, valid_answer, answers, mask, score):
	if answers[inp] == valid_answer:
		right = True
		score += 1
	else:
		right = False
		score -= 1

	cprint(inter_frame % 
		((line, 
		"\033[32;1m%s + 1\033[0m" % (score - 1) if right else "\033[31;1m%s - 1\033[0m" % (score + 1),
		inp + 1, "\033[32;1mВерный\033[0m" if right else "\033[31;1mНеверный\033[0m",
		line,
		) + tuple([answ + "  \033[32;1m<< Верный ответ\033[0m" if answ == valid_answer else answ + "  \033[31;1m<< Неверный ответ\033[0m" for answ in answers]) +
		tuple([line])))

	inp = input("\033[33;1mНажмите [ENTER], чтобы продолжить или q + [ENTER], чтобы выйти.\033[0m")

	if inp == "q":
		cprint("\033[33;1mИтоговый счет: %s\033[0m" % score)
		return
	else:
		return gameFrame(score)




def gameFrame(score):
	mask = generate_mask()
	answers = []

	while len(answers) < 3:
		answ = get_invalid_txt_by_mask(mask)
		if answ not in answers:
			answers.append(answ)

	valid_answer = get_valid_txt_by_mask(mask)
	answers.append(valid_answer)
	rand.shuffle(answers)

	cprint(game_frame % ((line, score, line, mask) + tuple(answers) + tuple([line])))
	inp = ""
	while True:
		
		inp = input("Ваш ответ(q - выход): ")

		try:
			inp = int(inp)
			if 1 <= inp <= 4:
				inp -= 1
		except ValueError:
			if inp == "q":
				break
			else:
				inp = ""
				continue

		return intermFrame(inp, valid_answer, answers, mask, score)

	cprint("Итоговый счет: %s" % score)

	

def main():
	score = 0
	gameFrame(score)


		


