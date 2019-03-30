from utils import *
import random as rand
import os

line = "-------------------------------------"
game_frame = (
"""
%s
\t\t\tСчёт: %s
Выберите подходящее под маску имя файла
%s
Маска: %s
Варианты ответов:
\t1. %s
\t2. %s
\t3. %s
\t4. %s
%s
""")

inter_frame = (
"""
%s
\t\t\tСчёт: %s
Вариант ответа %s - %s
%s
\t1. %s
\t2. %s
\t3. %s
\t4. %s
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
		"%s + 1" % (score - 1) if right else "%s - 1" % (score + 1),
		inp + 1, "Верный" if right else "Неверный",
		line,
		) + tuple([answ + "  << Верный ответ" if i == inp else answ + "  << Неверный ответ" for i, answ in enumerate(answers)]) +
		tuple([line])))

	inp = input("Нажмите [ENTER], чтобы продолжить или q + [ENTER], чтобы выйти.")

	if inp == "q":
		cprint("Итоговый счет: %s" % score)
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


		


