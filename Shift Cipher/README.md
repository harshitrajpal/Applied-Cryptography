The program implements a monoalphabetic substitution cipher with a customizable shift, enabling both encryption and decryption of text, with an option for brute force decryption attempts.

Program brief:
0. The program implements "First cipher" (as per class slides, it comes after Caesar's cipher) where shift is modifiable by the user
1. The  program provides a menu based context to encrypt and decrypt English characters
2. The user chooses option 1 to encrypt English text.
3. They then provide the sentence/words/characters to encrypt
4. Then they choose how much to shift. For example, 13 (for ROT-13) or 3 (Caesar's cipher)
5. Program gives the output.
6. Alternately a user can provide a ciphertext to deecrypt. They can either input the shift they want to decrypt or input 0 to bruteforce usign 1 to 25 shifts
7. Upon an invalid shift, program exits

------------------------------------------------------------------------------------------------------------------------------------------

Example run:
 1. In this run a text "HELLO" is encrypted using shift 3 and then bruteforced using option 0
 
 ┌──(root㉿kali)-[~/cryptography]
└─# python3 rajpal-shift.py 
Choose operation:
1. Encrypt
2. Decrypt
Enter choice (1 or 2): 1
Enter the text to encrypt: HELLO
Enter the shift amount: 3
Encrypted text: KHOOR
                                                                                            
┌──(root㉿kali)-[~/cryptography]
└─# python3 rajpal-shift.py
Choose operation:
1. Encrypt
2. Decrypt
Enter choice (1 or 2): 2
Enter the text to decrypt: KHOOR
Enter the shift amount (0 for bruteforce): 0
Bruteforcing all shifts:
Shift 1: JGNNQ
Shift 2: IFMMP
Shift 3: HELLO
Shift 4: GDKKN
Shift 5: FCJJM
Shift 6: EBIIL
Shift 7: DAHHK
Shift 8: CZGGJ
Shift 9: BYFFI
Shift 10: AXEEH
Shift 11: ZWDDG
Shift 12: YVCCF
Shift 13: XUBBE
Shift 14: WTAAD
Shift 15: VSZZC
Shift 16: URYYB
Shift 17: TQXXA
Shift 18: SPWWZ
Shift 19: ROVVY
Shift 20: QNUUX
Shift 21: PMTTW
Shift 22: OLSSV
Shift 23: NKRRU
Shift 24: MJQQT
Shift 25: LIPPS


2. In this run, a sentence in English is input to be decrypted

┌──(root㉿kali)-[~/cryptography]
└─# python3 rajpal-shift.py
Choose operation:
1. Encrypt
2. Decrypt
Enter choice (1 or 2): 2
Enter the text to decrypt: G waoiq hxuct lud muky natzotm lux gt Krkvngtz cnork pasvotm ut skgjucy....
Enter the shift amount (0 for bruteforce): 0
Bruteforcing all shifts:
Shift 1: F vznhp gwtbs ktc ltjx mzsynsl ktw fs Jqjumfsy bmnqj ozrunsl ts rjfitbx....
Shift 2: E uymgo fvsar jsb ksiw lyrxmrk jsv er Ipitlerx almpi nyqtmrk sr qiehsaw....
Shift 3: D txlfn eurzq ira jrhv kxqwlqj iru dq Hohskdqw zkloh mxpslqj rq phdgrzv....
Shift 4: C swkem dtqyp hqz iqgu jwpvkpi hqt cp Gngrjcpv yjkng lworkpi qp ogcfqyu....
Shift 5: B rvjdl cspxo gpy hpft ivoujoh gps bo Fmfqibou xijmf kvnqjoh po nfbepxt....
Shift 6: A quick brown fox goes hunting for an Elephant while jumping on meadows....
Shift 7: Z pthbj aqnvm enw fndr gtmshmf enq zm Dkdogzms vghkd itlohmf nm ldzcnvr....
Shift 8: Y osgai zpmul dmv emcq fslrgle dmp yl Cjcnfylr ufgjc hskngle ml kcybmuq....
Shift 9: X nrfzh yoltk clu dlbp erkqfkd clo xk Bibmexkq tefib grjmfkd lk jbxaltp....
Shift 10: W mqeyg xnksj bkt ckao dqjpejc bkn wj Ahaldwjp sdeha fqilejc kj iawzkso....
Shift 11: V lpdxf wmjri ajs bjzn cpiodib ajm vi Zgzkcvio rcdgz ephkdib ji hzvyjrn....
Shift 12: U kocwe vliqh zir aiym bohncha zil uh Yfyjbuhn qbcfy dogjcha ih gyuxiqm....
Shift 13: T jnbvd ukhpg yhq zhxl angmbgz yhk tg Xexiatgm pabex cnfibgz hg fxtwhpl....
Shift 14: S imauc tjgof xgp ygwk zmflafy xgj sf Wdwhzsfl ozadw bmehafy gf ewsvgok....
Shift 15: R hlztb sifne wfo xfvj ylekzex wfi re Vcvgyrek nyzcv aldgzex fe dvrufnj....
Shift 16: Q gkysa rhemd ven weui xkdjydw veh qd Ubufxqdj mxybu zkcfydw ed cuqtemi....
Shift 17: P fjxrz qgdlc udm vdth wjcixcv udg pc Tatewpci lwxat yjbexcv dc btpsdlh....
Shift 18: O eiwqy pfckb tcl ucsg vibhwbu tcf ob Szsdvobh kvwzs xiadwbu cb asorckg....
Shift 19: N dhvpx oebja sbk tbrf uhagvat sbe na Ryrcunag juvyr whzcvat ba zrnqbjf....
Shift 20: M cguow ndaiz raj saqe tgzfuzs rad mz Qxqbtmzf ituxq vgybuzs az yqmpaie....
Shift 21: L bftnv mczhy qzi rzpd sfyetyr qzc ly Pwpaslye hstwp ufxatyr zy xplozhd....
Shift 22: K aesmu lbygx pyh qyoc rexdsxq pyb kx Ovozrkxd grsvo tewzsxq yx woknygc....
Shift 23: J zdrlt kaxfw oxg pxnb qdwcrwp oxa jw Nunyqjwc fqrun sdvyrwp xw vnjmxfb....
Shift 24: I ycqks jzwev nwf owma pcvbqvo nwz iv Mtmxpivb epqtm rcuxqvo wv umilwea....
Shift 25: H xbpjr iyvdu mve nvlz obuapun mvy hu Lslwohua dopsl qbtwpun vu tlhkvdz....

3. In this run, a simple sentence is input and a fixed shift is given to decrypt to demonstrate ROT-13

┌──(root㉿kali)-[~/cryptography]
└─# python3 rajpal-shift.py                       
Choose operation:
1. Encrypt
2. Decrypt
Enter choice (1 or 2): 1
Enter the text to encrypt: Hello, professor and TAs. Here is my code :D
Enter the shift amount: 13
Encrypted text: Uryyb, cebsrffbe naq GNf. Urer vf zl pbqr :Q
                                                                                            
┌──(root㉿kali)-[~/cryptography]
└─# python3 rajpal-shift.py
Choose operation:
1. Encrypt
2. Decrypt
Enter choice (1 or 2): 2
Enter the text to decrypt: Uryyb, cebsrffbe naq GNf. Urer vf zl pbqr :Q
Enter the shift amount (0 for bruteforce): 13
Decrypted text: Hello, professor and TAs. Here is my code :D

------------------------------------------------------------------------------------------------------------------------------------------
