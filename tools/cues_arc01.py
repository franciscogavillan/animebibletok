"""Arc I cue sheets (VO + captions) for Genesis episodes 02A-10C.

Each cue: (gap_before_seconds, speaker, "caption line 1 / caption line 2").
Cue text must be exact KJV; tools/tracks.py verifies it against scripture/genesis_kjv.json.
Timings are planning estimates at the Bible pace (narrator ~120 wpm); re-time to the recorded VO.
"""
# (gap_before_seconds, speaker, "line1 / line2")
N,G,A,E,S="NARRATOR","GOD","ADAM","EVE","SERPENT"
EP={}
EP["02A"]=("1:6-1:8",[(0.6,N,"And God said,"),(0.3,G,"Let there be a firmament / in the midst of the waters,"),(0.2,G,"and let it divide the waters / from the waters."),
(6.5,N,"And God made the firmament,"),(0.3,N,"and divided the waters / which were under the firmament"),(0.3,N,"from the waters / which were above the firmament:"),(1.0,N,"and it was so."),
(6.0,N,"And God called / the firmament Heaven."),(4.5,N,"And the evening and the morning / were the second day.")])
EP["02B"]=("1:9-1:13",[(0.6,N,"And God said,"),(0.3,G,"Let the waters under the heaven / be gathered together"),(0.2,G,"unto one place, / and let the dry land appear:"),(1.2,N,"and it was so."),
(1.6,N,"And God called / the dry land Earth;"),(0.4,N,"and the gathering together / of the waters called he Seas:"),(0.8,N,"and God saw that it was good."),
(2.0,N,"And God said,"),(0.3,G,"Let the earth bring forth grass, / the herb yielding seed,"),(0.2,G,"and the fruit tree yielding fruit / after his kind,"),(0.2,G,"whose seed is in itself, / upon the earth:"),(1.2,N,"and it was so."),
(1.6,N,"And the earth brought forth grass, / and herb yielding seed"),(0.1,N,"after his kind,"),(0.2,N,"and the tree yielding fruit, / whose seed was in itself,"),(0.2,N,"after his kind:"),(0.5,N,"and God saw that it was good."),
(2.0,N,"And the evening and the morning / were the third day.")])
EP["03A"]=("1:14-1:19",[(0.5,N,"And God said,"),(0.3,G,"Let there be lights / in the firmament of the heaven"),(0.2,G,"to divide the day / from the night;"),(0.4,G,"and let them be for signs, / and for seasons,"),(0.2,G,"and for days, and years:"),
(0.6,G,"And let them be for lights / in the firmament of the heaven"),(0.2,G,"to give light upon the earth:"),(1.0,N,"and it was so."),
(3.0,N,"And God made two great lights;"),(0.4,N,"the greater light / to rule the day,"),(0.6,N,"and the lesser light / to rule the night:"),(1.5,N,"he made the stars also."),
(3.0,N,"And the evening and the morning / were the fourth day.")])
EP["03B"]=("1:20-1:25",[(0.5,N,"And God said,"),(0.3,G,"Let the waters bring forth / abundantly the moving creature"),(0.2,G,"that hath life, and fowl / that may fly above the earth"),(0.1,G,"in the open firmament of heaven."),
(1.6,N,"And God created great whales,"),(0.4,N,"and every living creature / that moveth,"),(0.2,N,"which the waters brought forth / abundantly, after their kind,"),(0.3,N,"and every winged fowl / after his kind:"),(0.6,N,"and God saw that it was good."),
(2.0,N,"And God blessed them, saying,"),(0.3,G,"Be fruitful, and multiply, / and fill the waters in the seas,"),(0.2,G,"and let fowl multiply / in the earth."),
(2.0,N,"And the evening and the morning / were the fifth day."),
(2.0,N,"And God said,"),(0.3,G,"Let the earth bring forth / the living creature"),(0.1,G,"after his kind,"),(0.2,G,"cattle, and creeping thing,"),(0.2,G,"and beast of the earth / after his kind:"),(1.0,N,"and it was so.")])
EP["04A"]=("1:26-1:28",[(2.5,N,"And God said,"),(0.4,G,"Let us make man in our image, / after our likeness:"),(0.8,G,"and let them have dominion / over the fish of the sea,"),(0.2,G,"and over the fowl of the air, / and over the cattle,"),(0.2,G,"and over all the earth,"),(0.2,G,"and over every creeping thing / that creepeth upon the earth."),
(3.0,N,"So God created man / in his own image,"),(0.8,N,"in the image of God / created he him;"),(1.0,N,"male and female / created he them."),
(3.0,N,"And God blessed them, / and God said unto them,"),(0.3,G,"Be fruitful, and multiply, / and replenish the earth,"),(0.2,G,"and subdue it:"),(0.5,G,"and have dominion / over the fish of the sea,"),(0.2,G,"and over the fowl of the air,"),(0.2,G,"and over every living thing / that moveth upon the earth.")])
EP["04B"]=("1:29-1:31",[(0.6,N,"And God said,"),(0.3,G,"Behold, I have given you / every herb bearing seed,"),(0.2,G,"which is upon the face / of all the earth,"),(0.4,G,"and every tree, / in the which is the fruit"),(0.1,G,"of a tree yielding seed;"),(0.4,G,"to you it shall be for meat."),
(1.5,G,"And to every beast of the earth, / and to every fowl of the air,"),(0.2,G,"and to every thing / that creepeth upon the earth,"),(0.2,G,"wherein there is life,"),(0.3,G,"I have given every green herb / for meat:"),(1.0,N,"and it was so."),
(5.0,N,"And God saw every thing / that he had made,"),(1.0,N,"and, behold, / it was very good."),
(3.5,N,"And the evening and the morning / were the sixth day.")])
EP["05"]=("2:1-2:3",[(2.0,N,"Thus the heavens and the earth / were finished,"),(0.4,N,"and all the host of them."),
(6.5,N,"And on the seventh day God ended / his work which he had made;"),(0.8,N,"and he rested on the seventh day"),(0.2,N,"from all his work / which he had made."),
(8.0,N,"And God blessed the seventh day, / and sanctified it:"),(0.8,N,"because that in it he had rested / from all his work"),(0.2,N,"which God created and made.")])
EP["06A"]=("2:4-2:7",[(0.5,N,"These are the generations / of the heavens and of the earth"),(0.2,N,"when they were created,"),(0.4,N,"in the day that the LORD God / made the earth and the heavens,"),
(1.2,N,"And every plant of the field / before it was in the earth,"),(0.3,N,"and every herb of the field / before it grew:"),(0.4,N,"for the LORD God had not caused / it to rain upon the earth,"),(0.4,N,"and there was not a man / to till the ground."),
(2.0,N,"But there went up a mist / from the earth,"),(0.3,N,"and watered the whole face / of the ground."),
(3.0,N,"And the LORD God formed man / of the dust of the ground,"),(2.0,N,"and breathed into his nostrils / the breath of life;"),(3.0,N,"and man became a living soul.")])
EP["06B"]=("2:8-2:15",[(0.5,N,"And the LORD God planted a garden / eastward in Eden;"),(0.4,N,"and there he put the man / whom he had formed."),
(2.5,N,"And out of the ground / made the LORD God to grow"),(0.2,N,"every tree that is pleasant / to the sight, and good for food;"),(1.2,N,"the tree of life also / in the midst of the garden,"),(1.0,N,"and the tree of knowledge / of good and evil."),
(3.0,N,"And a river went out of Eden / to water the garden;"),(0.4,N,"and from thence it was parted, / and became into four heads."),
(3.0,N,"And the LORD God took the man,"),(0.3,N,"and put him into / the garden of Eden"),(0.3,N,"to dress it and to keep it.")])
EP["07A"]=("2:16-2:20",[(0.5,N,"And the LORD God / commanded the man, saying,"),(0.4,G,"Of every tree of the garden / thou mayest freely eat:"),(1.2,G,"But of the tree of the knowledge / of good and evil,"),(0.3,G,"thou shalt not eat of it:"),(1.0,G,"for in the day / that thou eatest thereof"),(0.3,G,"thou shalt surely die."),
(4.0,N,"And the LORD God said,"),(0.3,G,"It is not good that the man / should be alone;"),(0.8,G,"I will make him / an help meet for him."),
(3.5,N,"And Adam gave names / to all cattle,"),(0.3,N,"and to the fowl of the air, / and to every beast of the field;"),(1.5,N,"but for Adam there was not found / an help meet for him.")])
EP["07B"]=("2:21-2:25",[(0.5,N,"And the LORD God caused / a deep sleep to fall upon Adam,"),(0.3,N,"and he slept:"),(1.0,N,"and he took one of his ribs,"),(0.4,N,"and closed up the flesh / instead thereof;"),
(2.0,N,"And the rib, which the LORD God / had taken from man,"),(0.3,N,"made he a woman, / and brought her unto the man."),
(3.0,N,"And Adam said,"),(0.6,A,"This is now bone of my bones, / and flesh of my flesh:"),(0.8,A,"she shall be called Woman,"),(0.3,A,"because she was taken / out of Man."),
(2.5,N,"Therefore shall a man leave / his father and his mother,"),(0.3,N,"and shall cleave unto his wife:"),(0.4,N,"and they shall be one flesh."),
(2.0,N,"And they were both naked, / the man and his wife,"),(0.3,N,"and were not ashamed.")])
EP["08"]=("3:1-3:5",[(0.5,N,"Now the serpent was more subtil / than any beast of the field"),(0.2,N,"which the LORD God had made."),
(1.8,N,"And he said unto the woman,"),(0.6,S,"Yea, hath God said,"),(0.4,S,"Ye shall not eat / of every tree of the garden?"),
(1.8,N,"And the woman said / unto the serpent,"),(0.4,E,"We may eat of the fruit / of the trees of the garden:"),(0.5,E,"But of the fruit of the tree / which is in the midst"),(0.1,E,"of the garden, God hath said,"),(0.2,E,"Ye shall not eat of it, / neither shall ye touch it,"),(0.2,E,"lest ye die."),
(1.5,N,"And the serpent said / unto the woman,"),(0.5,S,"Ye shall not surely die:"),(1.2,S,"For God doth know / that in the day ye eat thereof,"),(0.3,S,"then your eyes shall be opened,"),(0.8,S,"and ye shall be as gods, / knowing good and evil.")])
EP["09A"]=("3:6-3:8",[(0.5,N,"And when the woman saw / that the tree was good for food,"),(0.6,N,"and that it was pleasant / to the eyes,"),(0.6,N,"and a tree to be desired / to make one wise,"),(1.5,N,"she took of the fruit thereof,"),(0.8,N,"and did eat,"),(1.5,N,"and gave also unto her husband / with her;"),(1.0,N,"and he did eat."),
(3.0,N,"And the eyes of them both / were opened,"),(0.6,N,"and they knew / that they were naked;"),(1.2,N,"and they sewed / fig leaves together,"),(0.2,N,"and made themselves aprons."),
(3.0,N,"And they heard the voice / of the LORD God"),(0.2,N,"walking in the garden / in the cool of the day:"),(1.2,N,"and Adam and his wife / hid themselves"),(0.2,N,"from the presence of the LORD God"),(0.2,N,"amongst the trees of the garden.")])
EP["09B"]=("3:9-3:13",[(1.0,N,"And the LORD God / called unto Adam,"),(0.2,N,"and said unto him,"),(0.6,G,"Where art thou?"),
(3.5,N,"And he said,"),(0.4,A,"I heard thy voice in the garden,"),(0.5,A,"and I was afraid, / because I was naked;"),(0.7,A,"and I hid myself."),
(2.5,N,"And he said,"),(0.3,G,"Who told thee / that thou wast naked?"),(1.2,G,"Hast thou eaten of the tree, / whereof I commanded thee"),(0.2,G,"that thou shouldest not eat?"),
(2.2,N,"And the man said,"),(0.3,A,"The woman whom thou gavest / to be with me,"),(0.5,A,"she gave me of the tree, / and I did eat."),
(2.2,N,"And the LORD God said / unto the woman,"),(0.3,G,"What is this that thou hast done?"),(1.8,N,"And the woman said,"),(0.4,E,"The serpent beguiled me, / and I did eat.")])
EP["10A"]=("3:14-3:16",[(0.8,N,"And the LORD God said / unto the serpent,"),(0.5,G,"Because thou hast done this,"),(0.3,G,"thou art cursed above all cattle,"),(0.2,G,"and above every beast / of the field;"),(0.8,G,"upon thy belly shalt thou go,"),(0.5,G,"and dust shalt thou eat / all the days of thy life:"),
(2.0,G,"And I will put enmity / between thee and the woman,"),(0.3,G,"and between thy seed / and her seed;"),(1.0,G,"it shall bruise thy head,"),(0.5,G,"and thou shalt bruise his heel."),
(3.0,N,"Unto the woman he said,"),(0.4,G,"I will greatly multiply / thy sorrow and thy conception;"),(0.5,G,"in sorrow thou shalt / bring forth children;"),(0.8,G,"and thy desire shall be / to thy husband,"),(0.3,G,"and he shall rule over thee.")])
EP["10B"]=("3:17-3:20",[(0.8,N,"And unto Adam he said,"),(0.4,G,"Because thou hast hearkened / unto the voice of thy wife,"),(0.3,G,"and hast eaten of the tree, / of which I commanded thee, saying,"),(0.2,G,"Thou shalt not eat of it:"),(1.0,G,"cursed is the ground / for thy sake;"),(0.4,G,"in sorrow shalt thou eat of it / all the days of thy life;"),
(1.0,G,"Thorns also and thistles / shall it bring forth to thee;"),(0.3,G,"and thou shalt eat / the herb of the field;"),
(1.0,G,"In the sweat of thy face / shalt thou eat bread,"),(0.3,G,"till thou return unto the ground;"),(0.4,G,"for out of it wast thou taken:"),(1.5,G,"for dust thou art,"),(0.8,G,"and unto dust shalt thou return."),
(4.5,N,"And Adam called / his wife's name Eve;"),(1.0,N,"because she was / the mother of all living.")])
EP["10C"]=("3:21-3:24",[(0.8,N,"Unto Adam also and to his wife"),(0.2,N,"did the LORD God make / coats of skins,"),(0.4,N,"and clothed them."),
(3.0,N,"And the LORD God said,"),(0.4,G,"Behold, the man is become / as one of us,"),(0.3,G,"to know good and evil:"),(1.0,G,"and now, lest he put forth / his hand,"),(0.2,G,"and take also / of the tree of life,"),(0.3,G,"and eat, and live for ever:"),
(2.5,N,"Therefore the LORD God / sent him forth"),(0.2,N,"from the garden of Eden,"),(0.3,N,"to till the ground / from whence he was taken."),
(3.0,N,"So he drove out the man;"),(1.5,N,"and he placed at the east / of the garden of Eden"),(0.3,N,"Cherubims,"),(1.0,N,"and a flaming sword / which turned every way,"),(0.5,N,"to keep the way / of the tree of life.")])
OMIT={"03A":["1:17","1:18"],"03B":["1:25"],"06B":["2:11","2:12","2:13","2:14"],"07A":["2:19"]}
TITLE={"02A":"THE HEAVENS","02B":"THE DRY LAND","03A":"SIGNS AND SEASONS","03B":"THE LIVING WORLD","04A":"IN HIS IMAGE","04B":"VERY GOOD","05":"THE SEVENTH DAY","06A":"A LIVING SOUL","06B":"THE GARDEN","07A":"THE COMMAND","07B":"THE WOMAN","08":"THE SERPENT","09A":"THE FALL","09B":"WHERE ART THOU?","10A":"ENMITY","10B":"DUST THOU ART","10C":"EXILE FROM EDEN"}
RATE={N:2.0,G:1.9,A:2.25,E:2.25,S:2.0}
TAIL=6.5
TAILS={"02A":9.5,"05":10.5}
def timed(ep):
    rng,cues=EP[ep]; t=0; out=[]
    for gap,sp,txt in cues:
        w=len(txt.replace(" / "," ").split())
        start=t+gap; dur=max(1.2,w/RATE[sp]+0.25); end=start+dur
        out.append((start,end,sp,txt,w)); t=end
    return rng,out,t
