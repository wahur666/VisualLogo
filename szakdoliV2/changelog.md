# Changelog

### 2016.09.27 (Commit 31)

+ *Changelog létrehozása*
+ UTF-8 kódolási beállítás hozzáadása a fájlokhoz
+ Drawable.\__init__.py importok elkészítés
+ Új osztályok létrehozása
    + __Polygon__, funkciója : bármi alakzat kirjazolása a képernyőre, örökölt műveletek többnyire leimplementálva, hiányzik még a __*IsInside*__, ami valószínüleg Reycast módszerrel fog működni
    + __Tab__, funkciója : füleken való elemek megjelenítése, így lehet majd csoportosítani a kódokat. Működnek az örökölt funckciók. Minden tab rendelkezik egy Id mezővel, amit majd a *ScrollingPlane* fog hasznosítani a csoportosításkor. 
*TODO: A rajzolást újra gondolni, kódban jelezve, két arc és kettő rect segítségével!*
    + __ScrollingPlane__, funkciója : ez fogja tárolni a parancsokat amit majd a felhasználó fog elheyezni a panelen, majd futtatni. Működik minden örökölt funkció. A fülek külön külön tárolják a parancsokat, és mindig csak az aktív fülön lévő rajzolódik ki. Az event handert még be kell állítani, hogy értlems műveletet végezzen. 
+ GUI folyamatos bővítése a panelokkal, és eseményvezérlés kiépítésének folyamata
+ Rect: *IsInside* fix, visszatérési érték módosítása (bool, string)-ről (bool)-ra




[Created with Dillinger](dillinger.io)