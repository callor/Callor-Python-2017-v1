def hanoi(nDisks, startreg=1, endreg=3):
   if nDisks:
    hanoi(nDisks - 1, startreg, 6 - startreg - endreg)
    print(startreg,'번기둥--',nDisks,'번원반->',endreg)
    hanoi(nDisks -1, 6-startreg-endreg, endreg)



hanoi(nDisks=8)