import string, math, json
import random as rand

default_settings = {"MAX_NAME_LEN" : 5, 
					"MAX_EXT_LEN" : 5, 
					"MAX_STAR_LEN" : 3, 
					"ANSWER_OPTS" : 4, 
					"ANSWERS_COUNT" : 10}


def writeSettings(setts=default_settings):
	with open("settings.json", 'w') as settings:
		settings.write(json.dumps(setts))

def readSettings():
	try:
		settings = json.loads(open("settings.json", "r").read())
		if all([key in settings.keys() and type(settings[key]) == int for key in default_settings.keys()]):
			return settings
		else:
			raise FileNotFoundError

	except FileNotFoundError:
		writeSettings()
		return readSettings()

class Stage:
		def __init__(self, StageGenerator):
			self.mask = StageGenerator.generate_mask()
			self.answers = [StageGenerator.get_invalid_txt_by_mask(self.mask) for i in range(StageGenerator.ANSWER_OPTS-1)]
			self.valid_answer = StageGenerator.get_valid_txt_by_mask(self.mask)
			self.answers.append(self.valid_answer)
			rand.shuffle(self.answers)

class StageGenerator:
	def __init__(self, settings):
		self.settings = settings

		self.SALPH = "?*" # Алфавит специальных символов
		self.ALPH = string.ascii_letters+string.digits+"_" # Алфавит используемый в генерации имени файла

		self.MIN_NAME_LEN = 3 # Минимальная длина имени(нельзя ставить меньше 3)
		self.MAX_NAME_LEN = self.settings["MAX_NAME_LEN"] # Максимальная длина имени
		self.MIN_EXT_LEN = 3 # Минимальная длина расширения(нельзя ставить меньше 3)
		self.MAX_EXT_LEN = self.settings["MAX_EXT_LEN"] # Максимальная длина расширения

		self.MAX_STAR_LEN = self.settings["MAX_STAR_LEN"] # Максимальная длина последовательности на месте *
		self.ANSWER_OPTS = self.settings["ANSWER_OPTS"]

	def generate_mask(self):
		name = [rand.choice(self.ALPH) for i in range(self.MAX_NAME_LEN-rand.randint(0, self.MAX_NAME_LEN-self.MIN_NAME_LEN))]
		ext = [rand.choice(self.ALPH.lower()) for i in range(self.MAX_EXT_LEN-rand.randint(0, self.MAX_EXT_LEN-self.MIN_EXT_LEN))]

		sps_in_name = rand.choice([i for i in range(1, len(name) - 1)])
		sps_in_ext = rand.choice([i for i in range(1, len(ext) - 1)])

		for i in range(sps_in_name): name[rand.randint(0, len(name)-1)] =  rand.choice(self.SALPH)
		for i in range(sps_in_ext): ext[rand.randint(0, len(ext)-1)] =  rand.choice(self.SALPH)

		return "".join(name) + "." + "".join(ext)

	def get_valid_txt_by_mask(self, mask, ALPH=string.ascii_letters+string.digits+"_"):
		mask = list(mask)
		for i, s in enumerate(mask):
			if s == "?":
				mask[i] = rand.choice(ALPH)
			elif s == "*":
				mask[i] = "".join(rand.choice(ALPH) for j in range(rand.randint(0, self.MAX_STAR_LEN)))
			else:
				continue

		return "".join(mask)

	def get_invalid_txt_by_mask(self, file_mask):
		nALPH = self.ALPH
		while True in [file_mask.find(i) > -1 for i in ["*?*", "?*", "*?"]]:
			file_mask = file_mask.replace("*?*", "?").replace("?*", "?").replace("*?", "?")

		sp_indxs = []
		for i, s in enumerate(file_mask):
			if s in self.SALPH:
				if s == "*":
					if  i != len(file_mask) - 1 and file_mask[i+1] not in self.SALPH and file_mask[i+1] != ".":
						sp_indxs.append([i, 1])
					elif i > 0 and file_mask[i-1] not in self.SALPH and file_mask[i-1] != ".":
						sp_indxs.append([i, -1])
					else:
						continue
				else:
					sp_indxs.append([i, None])

		name, ext = file_mask.split(".")
		name, ext = list(name), list(ext)
		bad_sp_ind = rand.choice(sp_indxs)

		if bad_sp_ind[0] <= len(name)-1:
			if name[bad_sp_ind[0]] == "?":
				name.pop(bad_sp_ind[0])
			else:
				nALPH = nALPH.replace(name[bad_sp_ind[0]+bad_sp_ind[1]], "")
				name[bad_sp_ind[0]+bad_sp_ind[1]] = rand.choice(nALPH)
		else:
			bad_sp_ind[0] -= len(name) + 1
			if ext[bad_sp_ind[0]] == "?":
				ext.pop(bad_sp_ind[0])
			else:
				nALPH = nALPH.replace(ext[bad_sp_ind[0]+bad_sp_ind[1]], "")
				ext[bad_sp_ind[0]+bad_sp_ind[1]] = rand.choice(nALPH)

		return self.get_valid_txt_by_mask("".join(name)+"."+"".join(ext), nALPH)
