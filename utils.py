import random as rand
import string, math
from cfg import *

SALPH = "?*" # Алфавит специальных символов

def generate_mask():
	name = [rand.choice(ALPH) for i in range(MAX_NAME_LEN-rand.randint(0, MAX_NAME_LEN-MIN_NAME_LEN))]
	ext = [rand.choice(ALPH.lower()) for i in range(MAX_EXT_LEN-rand.randint(0, MAX_EXT_LEN-MIN_EXT_LEN))]

	sps_in_name = rand.choice([i for i in range(1, len(name) - 1)])
	sps_in_ext = rand.choice([i for i in range(1, len(ext) - 1)])

	for i in range(sps_in_name): name[rand.randint(0, len(name)-1)] =  rand.choice(SALPH)
	for i in range(sps_in_ext): ext[rand.randint(0, len(ext)-1)] =  rand.choice(SALPH)

	return "".join(name) + "." + "".join(ext)

def get_valid_txt_by_mask(mask, ALPH):
	mask = list(mask)
	for i, s in enumerate(mask):
		if s == "?":
			mask[i] = rand.choice(ALPH)
		elif s == "*":
			mask[i] = "".join(rand.choice(ALPH) for j in range(rand.randint(0, MAX_STAR_LEN)))
		else:
			continue

	return "".join(mask)

def get_invalid_txt_by_mask(file_mask):
	nALPH = ALPH
	sp_indxs = []
	for i, s in enumerate(file_mask):
		if s in SALPH:
			if i != len(file_mask) - 1 and file_mask[i+1] not in SALPH and file_mask[i+1] != ".":
				sp_indxs.append([i, 1])
			elif i > 0 and file_mask[i-1] not in SALPH and file_mask[i-1] != ".":
				sp_indxs.append([i, -1])
			else:
				continue

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

	return get_valid_txt_by_mask("".join(name)+"."+"".join(ext), nALPH)


