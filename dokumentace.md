**Zadání:** <br>
Vytvořte hru piškvorky, která se bude střídavě ptát hráčů na souřadnice jejich tahu. Hrá má tyto podmínky:
* Pokud dojde k zadání souřadnic mimo herní plán, program vyzve hráče k novému zadání souřadnic. 
* Není potřeba vyhodnocovat vítězství jednoho hráče
* Není potřeba zavádět kontrolu zajišťující obsazení pole právě jednou 

Bonusové úkoly:
* možnost zadat volitelné rozměry hracího pole
* síť bude tvořena šestiúhelníky
* odevzdejte úkol přes GitHub.

**Vypracování:**<br>
Program se nejprve uživatele zeptá, jakou délku má mít jedna strana šestiúhleníku a jaké rozměry má mít šestiúhelníková síť. Po zadání těchto údajů dojde k vykreslení sítě pomocí *želví grafiky*. *Želva* poté přestane kreslit a přesune se na počáteční bod, tj. levý dolní roh sítě. 
V dalším kroku se program zeptá na souřadnice pole, kam si první hráč přeje zakreslit svoji značku. Po zadání se *želva* přesune do prostředka zadaného pole a vykreslí křížek. Následně přestane kreslit a přesune se na počáteční bod. Program se poté zeptá druhého hráče na souřadnice pole. Postup se opakuje (střídá se vykreslení křížku a kolečka) do té doby, než jsou všechna pole obsazena. Program pak hru ukončí a oznámí to uživateli.