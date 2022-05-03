# import os
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
#
# driver = webdriver.Firefox(executable_path=os.getenv("geckodriver_path"),service_log_path=os.devnull)
# driver.get('https://google.com')
#
# input('pause')
#
# count = 1
# in_a_row = 0
# print('vocab_set = {')
# while True:
#     element = f'div.SetPageTerms-term:nth-child({count})'
#     try:
#         driver.find_element_by_css_selector(element)
#     except NoSuchElementException:
#         count += 1
#         if in_a_row > 5:
#             break
#         in_a_row += 1
#         continue
#     key = driver.find_element_by_css_selector(element + ' > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)')
#     value = driver.find_element_by_css_selector(element + ' > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1) > span:nth-child(1)')
#     print(f'    "{key.text}": "{value.text}",   # {count}')
#     count += 1
#     in_a_row = 0
# print('}')

import pickle

vocab_set = {
    "frūstrā, adv.": "in vain, to no avail",   # 1
    "trānseō, -īre, -īvī/iī, -ītum": "to cross, go across",   # 2
    "portitor, portitōris, m.": "ferryman, tollkeeper (here, Charon, boatman of the river Styx)",   # 3
    "arceō, -ēre, arcuī, —-": "to contain, restrain; to keep away, drive back",   # 5
    "septem, indecl. adj.": "seven",   # 6
    "squālidus, -a, -um": "rough; filthy, unbathed, unkempt",   # 7
    "rīpa, -ae, f.": "riverbank",   # 8
    "Cerēs, Cereris, f.": "Ceres (goddess of grain, mother of Persephone)",   # 9
    "mūnus, mūneris, n.": "owed gift, duty",   # 10
    "sedeō, -ēre, sēdī, sessum": "to sit, be seated",   # 11
    "cūra, -ae, f.": "care, anxiety, worry, concern",   # 12
    "dolor, dolōris, m.": "sorrow, grief, pain",   # 13
    "alimentum, -ī, n.": "food, nourishment",   # 15
    "Erebus, -ī, m.": "Erebus (a name for the Underworld)",   # 16
    "crūdēlis, crūdēle, adj.": "cruel; bloody",   # 17
    "altus, -a, -um": "high, lofty; deep",   # 18
    "Rhodopē, -ēs, (acc. -ēn), f.": "Mt. Rhodope (a Thracian mountain)",   # 19
    "pellō, -ere, pepulī, pulsum": "to beat, strike, push",   # 20
    "aquilō, -ōnis, m.": "north wind",   # 21
    "Haemus, -ī, m.": "Mt. Haemus (a Thracian mountain)",   # 22
    "revolvō, revolvere, revoluī, revolūtum": "to roll back, return; (pass.) to fall back again",   # 23
    "rūrsus, adv.": "back again",   # 25
    "aliter, adv.": "otherwise",   # 26
    "geminus, -a, -um": "twin, double",   # 27
    "nex, necis, f.": "death, murder",   # 28
    "trēs, tria, adj.": "three",   # 29
    "medius, -a, -um": "middle, (the) middle (of the)",   # 30
    "catēna, -ae, f.": "chain; pl., chains, fetters",   # 31
    "portō (1)": "carry, bear",   # 32
    "collum, -ī, n.": "neck",   # 33
    "canis, canis, m./f.": "dog",   # 35
    "pavor, pavōris, m.": "sudden fear, terror",   # 36
    "ante...quam = antequam, conj.": "before",   # 37
    "relinquō, -ere, relīquī, relictum": "to leave, leave behind, abandon",   # 38
    "prior, prius, adj.": "first (of two), previous; earlier, prior, former",   # 39
    "corpus, corporis, n.": "body, corpse",   # 40
    "oborior, oborīrī, obortus sum": "to rise up, spring up",   # 41
    "crīmen, crīminis, n.": "charge, accusation; misdeed, crime",   # 42
    "trahō, -ere, trāxī, tractum": "to drag, pull",   # 43
    "Ōlenos, -ī, m.": "Olenos (an obscure, minor figure; perhaps a mistrel and composer of hymns)",   # 45
    "nocēns, gen. nocentis": "harmful; guilty",   # 46
    "cōnfīdō, -ere, cōnfīsus sum + dat.": "to trust in, have confidence in, be sure of",   # 47
    "figūra, -ae, f.": "form, composition; outward appearance; beauty",   # 48
    "Lēthaea, -ae, f.": "Lethaea (an otherwise unknown figure)",   # 49
    "iungō, -ere, iunxī, iūnctum": "to join, unite",   # 50
    "quondam, adv.": "once, formerly",   # 51
    "pectus, pectoris, n.": "chest, breast, heart",   # 52
    "lapis, lapidis, m.": "stone",   # 53
    "ūmidus, -a, -um": "wet, moist; rainy",   # 54
    "Īdē, Īdēs, f.": "Mt. Ida (name of both a mountain in Crete and a mountain in Troy)",   # 55
    "arduus, -a, -um": "tall, towering; steep, precipitous",   # 56
    "obscūrus, -a, -um": "dark",   # 57
    "cālīgō, cālīginis, f.": "darkness; gloom",   # 58
    "dēnsus, -a, -um": "thick, dense; frequent",   # 59
    "procul, adv.": "in the distance, far off",   # 60
    "absum, abesse, āfuī, āfutūrum": "to be absent, be away, be distant",   # 61
    "tellūs, tellūris, f.": "land, earth",   # 62
    "margō, marginis, m.": "wall; border, edge, margin",   # 63
    "dēficiō, -ere, dēfēcī, dēfectum": "to fail; to lose strength, collapse, faint, give out",   # 64
    "metuō, metuere, metuī, metūtum": "to fear, be afraid of",   # 65
    "avidus, -a, -um": "greedy; desirous (of), eager (for) + gen.",   # 66
    "prōtinus, adv.": "immediately, straightaway",   # 67
    "relābor, relābī, relāpsus sum": "to fall/slip backward",   # 68
    "bracchium, -iī, n.": "arm",   # 69
    "intendō, -ere, intendī, intentum": "to stretch; to stretch forth, hold out",   # 70
    "prēndō, prēndere, prēndī, prēnsum": "to grasp, seize, take hold of; to catch, capture",   # 71
    "certō (1)": "to contend, strive, struggle",   # 72
    "nīl = nihil, indecl. (n.)": "nothing",   # 73
    "cēdō, -ere, cessī, cessūrum": "to go, proceed; (+ dat.) to yield to , be inferior to",   # 74
    "īnfēlīx, gen. īnfēlīcis": "unfortunate, unhappy",   # 75
    "arripiō, -ere, arripuī, arreptum": "tro grasp, take hold of, embrace",   # 76
    "iterum, adv.": "again, once again",   # 77
    "morior, morī, mortuus sum": "to die, be dead",   # 78
    "quicquam, adv.": "in any respect, at all",   # 79
    "queror, querī, questus sum": "to complain (about), protest",   # 80
    "suprēmus, -a, -um": "last, final",   # 81
    "vīx, adv.": "scarcely",   # 82
    "auris, auris, f.": "ear",   # 83
    "Bēlis, Bēlidos (nom. pl. Bēlides), f.": "descendants of Belus; the Danaids",   # 84
    "sedeō, sedēre, sēdī, sessurum": "to sit, be seated",   # 85
    "Sīsyphus, -ī, m.": "Sisyphus (king of Corinth punished in Hades by being made to roll a rock up a hill)",   # 86
    "saxum, -ī, n.": "stone, rock, boulder",   # 87
    "tunc, adv.": "then; next",   # 88
    "prīmum, adv.": "first, at first",   # 89
    "lacrima, -ae, f.": "tear, weeping",   # 90
    "vincō, -ere, vīcī, victum": "to conquer, defeat",   # 91
    "Eumenis, Eumenidos (gen. pl. Eumenidum), f. (usu. pl.)": "one of the Eumenides/Furies (goddesses of vengeance)",   # 92
    "madescō, madescere, maduī, —-": "to become wet",   # 93
    "gena, -ae, f.": "cheek",   # 94
    "rēgius, -a, -um": "royal, of the king",   # 95
    "sustineō, -ēre, sustinuī, sustentum": "to hold up, support; sustain",   # 96
    "regō, -ere, rēxī, rēctum": "to rule, direct",   # 97
    "īmus, -a, -um": "deepest",   # 98
    "recēns, gen. recentis": "recent, new; newly arrived; fresh",   # 99
    "inter + acc.": "between, among",   # 100
    "incēdō, -ere, incessī, incessūrum": "to march, go, proceed (often in a stately manner)",   # 101
    "passus, -ūs, m.": "step, tread, footsteep, gait",   # 102
    "vulnus, vulneris, n.": "wound, injury",   # 103
    "tardus, -a, -um": "slow",   # 104
    "simul, adv.": "together, at the same time",   # 105
    "lēx, lēgis, f.": "law; rule, regulation, order; restriction",   # 106
    "accipiō, -ere, accēpī, acceptum": "to accept",   # 107
    "hērōs, hērōos, m. (Greek declension)": "hero",   # 108
    "flectō, -ere, flexī, flectum": "to (cause to) bend, turn, sway",   # 109
    "retrō, adv.": "backwards",   # 110
    "lūmen, lūminis, n.": "light; eye (idiom.)",   # 111
    "dōnec, conj.": "until",   # 112
    "Avernus, -a, -um": "Avernan, of the Underworld, infernal (Lake Avernus near Naples was an entrance to the underworld)",   # 113
    "exeō, exīre, exiī/exīvī, exitum": "to go out, exit",   # 114
    "vallēs, vallis, f.": "valley; the abyss",   # 115
    "irritus, -a, -um": "nullified, void",   # 116
    "carpo, -ere, carpsī, carptum": "to pluck, gather; pursue (a path)",   # 117
    "acclīvis, acclīve, adj.": "inclined, sloping upwards",   # 118
    "mūtus, -a, -um": "mute, soundless, speechless",   # 119
    "trāmes, trāmitis, m.": "footpath, trail",   # 120
    "iūs, iūris, n.": "law, legal sanction; legal authority, right",   # 121
    "mūnus, muneris, n.": "a required task; tributek offering (to a deity); gift; favor, service",   # 122
    "poscō, poscere, poposcī, —-": "to ask for, demand",   # 123
    "ūsus, -ūs, m.": "use, employment; the right to use/enjoy (esp. w/ ref. to another's property); potential for use, utility; marriage",   # 124
    "fātum, -ī, n": "prophecy; destiny, fate; Fate (as deity); doom, death (oft. pl. for sg.)",   # 125
    "venia, -ae, f.": "favor, kindness, blessing (esp. in religious sense); forgiveness, pardon; reprieve, remission",   # 126
    "nōlō, nōlle, nōluī, —-": "to not want, be unwilling",   # 127
    "redeō, -īre, redivī/rediī, reditum": "to return, go back",   # 128
    "lētum, -ī, n.": "death, destruction",   # 129
    "gaudeō, -ēre, gāvīsus sum": "to rejoice, be glad",   # 130
    "duo, duae, duo": "two",   # 131
    "tālis, tāle, adj.": "such, such a, of such a kind",   # 132
    "moveō, -ēre, mōvī, mōtum": "to move, set in motion",   # 133
    "exsanguis, -e, adj.": "bloodless; pale, lifeless",   # 134
    "fleō, -ēre, flēvī, flētum": "to weep, cry; to weep for, lament",   # 135
    "anima, -ae, f.": "air, breath; soul, life; spirit, ghost",   # 136
    "Tantalus, -ī, m.": "Tantalus (a Lydian king, son of Zeus and father of Pelops)",   # 137
    "unda, -ae, f.": "wave",   # 138
    "captō (1)": "to try to seize; to hunt",   # 139
    "refugus, -a, -um": "fleeing receding",   # 140
    "stupeō, -ēre, stupuī, stupitum": "to be amazed, gape; to be paralyzed",   # 141
    "Ixīōn, Ixīonis, m.": "Ixion (king of the Lapiths, punished by being tied to a turning wheel in Hades for trying to seduce Juno)",   # 142
    "orbs, orbis, m.": "wheel; orb",   # 143
    "carpō, -ere, carpsī, carptum": "to pluck, gather; to tear at; to travel, pursue (a path)",   # 144
    "iecur, iecoris, n.": "the liver",   # 145
    "volucris, -is, f.": "winged creature, bird",   # 146
    "urna, -ae, f.": "urn; water vessel",   # 147
    "vacō (1)": "to be empty, unfilled; to be free (from), take a rest (from)",   # 148
    "nōtus, -a, -um": "known, well-known",   # 149
    "an, conj.": "whether, or, if",   # 150
    "dubitō (1)": "hesitate, doubt, be unsure",   # 151
    "hīc, adv.": "here",   # 152
    "auguror, -ārī, -ātus sum": "to fortell by augury; to intuit, sense, surmise",   # 153
    "fāma, -ae, f.": "news, report; tradition, story",   # 154
    "vetus, gen. veteris": "old",   # 155
    "mentior, mentīrī, mentītus sum": "to lie; invent, fabricate",   # 156
    "rapīna, -ae, f.": "plunder; kidnapping",   # 157
    "iungō, iungere, iūnxī, iūnctum": "to join, unite",   # 158
    "timor, timōris, m.": "fear",   # 159
    "Chaos, Chaī, n.": "Chaos (the formless state of the universe before creation); the Underworld",   # 160
    "ingēns, gen. ingentis": "huge",   # 161
    "vāstus, -a, -um": "desolate, lifeless; huge, immense",   # 162
    "silentium, -iī, n.": "silence",   # 163
    "Eurydicē, Eurydicēs (acc. Eurydicēn), f.": "Eurydice (a Thracian nymph, wife of Orpheus)",   # 164
    "ōrō (1)": "to pray, beg, beseech",   # 165
    "properō (1)": "to rush, act with haste, be quick, hurry, hasten",   # 166
    "retexō, -ere, retexuī, retextum": "to unweave",   # 167
    "fātum, -ī, n.": "prophecy; destiny, fate; Fate (as a deity); doom death (often pl. for sg.)",   # 168
    "paulum, adv.": "a little, little",   # 169
    "moror, -ārī, -ātus sum": "to delay",   # 170
    "sērō, adv.": "late",   # 171
    "citō, adv.": "quickly, rapidly, speedily",   # 172
    "sēdēs, -is, f.": "seat; home; place, position",   # 173
    "domus, -ī/-ūs, f.": "home, house",   # 174
    "ultimus, -a, -um": "last, final, furthest",   # 175
    "genus, generis, n.": "kind, type, race",   # 176
    "iūstus, -a, -um": "lawful, legitimate; rightful, proper, deserved",   # 177
    "mātūrus, -a, -um": "ripe; advanced in age",   # 178
    "peragō, -ere, perēgī, perāctum": "to chase; complete; go through (space or time); live out, complete (a period of time)",   # 179
    "occidō, -ere, occidī, occāsūrum": "to fall, collapse; to die",   # 180
    "tālus, -ī, m.": "ankle-bone, ankle",   # 181
    "serpēns, -entis, m.": "snake, serpent",   # 182
    "dēns, dentis, m.": "tooth, fang",   # 183
    "recipiō, -ere, recēpī, receptum": "to receive, take in",   # 184
    "superus, -a, -um": "upper, (those) above",   # 185
    "postquam, adv.": "afterwards",   # 186
    "Rhodopēius, -a, -um": "Rhodopeian, of/pertaining to Mt. Rhodope (a mountain in Thrace); Thracian",   # 187
    "aura, -ae, f.": "breeze, air",   # 188
    "dēfleō, -ēre, dēflēvī, dēflētum": "to weep for, mourn",   # 189
    "vātēs, -is, m.": "prophet; bard, poet",   # 190
    "umbra, -ae, f.": "shadow, shade; ghost, shade of the dead",   # 191
    "Styx, Stygis (acc. Styga), f.": "the river Styx (principal river of the Underworld); by metonomy, the Underworld",   # 192
    "Taenarius, -a, -um": "of Taenarius (a South Peloponnese cave leading into Hades)",   # 193
    "audeō, audēre, ausus sum": "to dare",   # 194
    "dēscendō, -ere, dēscendī, dēscēnsūrum": "to go/come down, descend'",   # 195
    "porta, -ae, f.": "gate, entrance",   # 196
    "levis, leve, adj.": "light, slight, weightless",   # 197
    "simulacrum, -ī, n.": "likeness; image, statue; phantom, ghost",   # 198
    "fungor, fungī, fūnctus sum + abl.": "to perform; to experience, suffer",   # 199
    "sepulcrum, -ī, n.": "tomb (by metonomy, death)",   # 200
    "Persephonē, Persephonēs (acc. Persephonēn), f.": "Persephone (Proserpina in Latin), queen of the Underworld",   # 201
    "adeō, -īre, -īvī/iī, -ītum": "to approach, come to, go to",   # 202
    "inamoenus, -a, -um": "unpleasant, unlovely",   # 203
    "rēgnum, -ī, n.": "kingdom, realm",   # 204
    "teneō, -ēre, tenuī, tentum": "to hold, have, possess",   # 205
    "pellō, pellere, pepulī, pulsum": "to beat against, strike; drive away, banish, expel",   # 206
    "nervus, -ī, m.": "sinew; string (of a lyre); strength",   # 207
    "inde, adv.": "from there, then, thence",   # 208
    "immēnsus, -a, -um": "boundless, vast",   # 209
    "croceus, -a, -um": "of saffron; saffron-colored, yellow (the color worn by Roman brides in weddings)",   # 210
    "vēlō (1)": "to cover, clothe",   # 211
    "amictus, -ūs, m.": "cloak, mantle",   # 212
    "aethēr, aetheris (acc. aethera), n.": "the upper regionsof space, heaven",   # 213
    "dīgredior, dīgredī, dīgressus sum": "to go away, depart",   # 214
    "Ciconēs, Ciconum, m. pl.": "the Cicones (a tribe of southern Thrace)",   # 215
    "Hymenaeus, -ī, m.": "Hymenaus (Greek god of weddings; also a wedding refrain)",   # 216
    "ōra, -ae, f.": "shore, coast",   # 217
    "tendō, -ere, tetendī, tentum": "to extend, stretch forth; to proceed",   # 218
    "Orphēus, -a, -um": "of/belonging to Orpheus",   # 219
    "nēquīquam, adv.": "futilely, in vain, to no avail",   # 220
    "adsum, adesse, adfuī, adfutūrum": "to be present",   # 221
    "sollemnis, sollemne, adj.": "ceremonial, ritual; traditional",   # 222
    "laetus, -a, -um": "happy",   # 223
    "vultus, -ūs, m.": "face, countenance, visage",   # 224
    "fēlīx, gen. fēlīcis": "happy, fortunate",   # 225
    "afferō, -ferre, attulī, allātum": "to bring, bring to, bring in",   # 226
    "ōmen, ōminis, n.": "omen, augury, sign",   # 227
    "fax, facis, f.": "torch, material used for a torch, flame of love; wedding torch",   # 228
    "lacrimōsus, -a, -um": "tearful; causing tears",   # 229
    "strīdulus, -a, -um": "shrill, high-pitched",   # 230
    "fūmus, -ī, m.": "smoke",   # 231
    "ūsque, adv.": "all the way to/from; continuously",   # 232
    "mōtus, -ūs, m.": "movement, motion",   # 233
    "ignis, -is, m.": "fire, flame",   # 234
    "exitus, -ūs, m.": "departure, exit; outcome",   # 235
    "ausipicium, -iī, n.": "omen, augury",   # 236
    "gravis, grave, adj.": "grave, serious",   # 237
    "nūpta, -ae, f.": "married woman, bride",   # 238
    "herba, -ae, f.": "grass",   # 239
    "Nāias, Nāiadis, f.": "Naiad (river nymph)",   # 240
    "turba, -ae, f.": "crowd",   # 241
    "comitō (1)": "to accompany",   # 242
    "vagor, -ārī, -ātus sum": "to wander, roam",   # 243
    "sīc, adv.": "thus, in this way",   # 244
    "ait (irreg.)": "s/he speaks, s/he spoke",   # 245
    "ponō, ponere, posuī, positum": "to place, put",   # 246
    "nūmen, nūminis, n.": "divinity, deity, divine presence, god/dess",   # 247
    "mundus, -ī, m.": "world, universe",   # 248
    "reccidō, -ere, reccidī, reccāsūrum": "to fall back, sink back",   # 249
    "quisquis, quidquid": "whoever, whatever",   # 250
    "mortālis, -e, adj.": "subject to death; mortal",   # 251
    "creō (1)": "to beget, create",   # 252
    "licet, impersonal": "it is permitted",   # 253
    "falsus, -a, -um": "untrue, false; misleading, deceptive",   # 254
    "ambāgēs, ambāgum, f. pl.": "a circuitous path; long-winded/obscure/evasive speech",   # 255
    "ōs, ōris, n.": "mouth; face",   # 256
    "vērus, -a, -um": "TRUE",   # 257
    "sinō, -ere, sīvī, situm": "to allow, permit",   # 258
    "hūc, adv.": "to this point, here, to here",   # 259
    "opācus, -a, -um": "shaded; shadowy, dark, dim",   # 260
    "Tartara, -ōrum": "Tartarus (the Underworld)",   # 261
    "dēscendō, -ere, dēscendī, dēscēnsum": "to descend, go/come down",   # 262
    "utī, conj. (= ut)": "that, so that",   # 263
    "villōsus, -a, -um": "shaggy, hairy",   # 264
    "colubra, -ae, f.": "serpent, snake",   # 265
    "ternī, -ae, -a": "three each, three at a time, three in succession",   # 266
    "Medūsaeus, -a, -um": "Medusa-like; of or pertaining to Medusa (a Gorgon whose hair resembled snakes)",   # 267
    "guttur, gutturis, n.": "throat",   # 268
    "mōnstrum, -ī, n.": "omen, portent; monster",   # 269
    "coniūnx, coniugis, m./f.": "spouse",   # 270
    "calcō (1)": "to trample, tread (on), step on",   # 271
    "venēnum, -ī, n.": "poison, venom",   # 272
    "vīpera, -ae, f.": "viper, serpent",   # 273
    "diffundō, -ere, diffūdī, diffūsus": "to pour into, pour widely, diffuse",   # 274
    "crēscō, -ere, crēvī, crētūrum": "to be born, arise; increase, change into (by growing),); to grow, bud",   # 275
    "auferō, auferre, abstulī, ablātum": "to carry away, take away",   # 276
    "patior, patī, passus sum": "to suffer, experience",   # 277
    "volō, velle, voluī, —-": "to want, wish, be willing",   # 278
    "temptō (1)": "try, test, attempt",   # 279
    "negō (1)": "to deny, say that not",   # 280
}

# with open('./vocab_set.pickle', 'wb') as file:
#     pickle.dump(vocab_set, file)

with open('./vocab_set.pickle', 'rb') as file:
    vocab_set = pickle.load(file)
    # out = ""
    # for key in vocab_set.keys():
    #     out += f'{key} || {vocab_set[key]}\n'
    # print(out)
    print(len(vocab_set.keys()))