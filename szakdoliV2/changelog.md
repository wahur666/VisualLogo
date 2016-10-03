# Changelog

### 2016.10.03. (Commit 32)
+ Törött linkek és elírások javítása a readme és changelog fájlokban, továbbá további hivatkozások hozzáadása
+ Optimalizált importok, *Pycharm* segtítségével
+ Kisebb átnevezések az osztályokban
+ __AbstractDrawable__, kapott egy konstruktor, abból a célból, hogy a típus ellenőrzés megtörténjen, mivel Pythonban nem támogatott a függvény túlterhelés ezért kellett így csinálni. Ezentúl ami osztály az ebből származik, tudja használni majd ezt, így két féle módon meg lehet majd adni a helyzetét és nagyságát az elemeknek. Explicit (x, y, w, h) és Implicit a _size=tuple(w,h)_ és _vec2_pos=__Vector2(x, y)___ segítségével
+ __Button__, felbontva az osztály, a kép része átkerült egy saját osztályba (__Sprite__), ezzel az erőforrásokat könnyebben tudjuk nyilvántartani, és majd a paracsoknál és a teknős rajzolásánál is használható lesz
+ A __Tab__ osztály, TODO újratervezést igényel nem maradhat így sokkal tovább, mert csak hátráltat, kódban feltüntetve a kritikus helyek
+ *System* könyvtár létrehozása, ide átkerült a __Constants__ osztály.
+ *Util* könyvtárban már csak a __Configparser__ maradt, ami egy függvény külön véve. TODO: ez nem maradhat így, vagy vissza kell hogy kerüljön a fő programba, vagy teljesen elvetni a külső konigurációs fájl használatát, jelenleg hátráltatja a gyors és dinamukus változtatás lehetőségét.
+ Új osztályok létrehozása
    + __Spirte__, funkciója: a képekért felelős osztály, ez tölti be és jeleníti meg a képet. Mivel még a megjelenítési felület előbb jön létre mint a *pygame* maga, ezért csak akkor kerül betöltésre a kép, mikor először kirajzolásra kerül. Ez az első kirajzolást lassítja, és a fő program átírása szükséges!
    + __Vector__, funkciója: megadni tömören és egyértelműen a helyét az elemeknek. Továbbá majd szükség lesz a *Lerp(Lineáris interpoláció)* funkcióra a __Scrollplane__ elemei mozgatásakor
    + *Unittests* könyvtár létrehozása, ide került egy __test__ osztály, ami jelenleg a __Vector__ oszály műveleteit teszteli
### 2016.09.27 (Commit 31)

+ *Changelog létrehozása*
+ Readme hozzáadása, hogy mindig az akutális információk is látszódjonak
+ UTF-8 kódolási beállítás hozzáadása a fájlokhoz
+ Drawable.\_\_init__.py importok elkészítés
+ GUI folyamatos bővítése a panelokkal, és eseményvezérlés kiépítésének folyamata
+ Rect: *IsInside* fix, visszatérési érték módosítása (bool, string)-ről (bool)-ra
+ Új osztályok létrehozása
    + __Polygon__, funkciója : bármi alakzat kirjazolása a képernyőre, örökölt műveletek többnyire leimplementálva, hiányzik még a __*IsInside*__, ami valószínüleg Raycast módszerrel fog működni
    + __Tab__, funkciója : füleken való elemek megjelenítése, így lehet majd csoportosítani a kódokat. Működnek az örökölt funckciók. Minden tab rendelkezik egy Id mezővel, amit majd a *ScrollingPlane* fog hasznosítani a csoportosításkor. 
*TODO:* A rajzolást újra gondolni, kódban jelezve, két arc és kettő rect segítségével!*
    + __ScrollingPlane__, funkciója : ez fogja tárolni a parancsokat amit majd a felhasználó fog elheyezni a panelen, majd futtatni. Működik minden örökölt funkció. A fülek külön külön tárolják a parancsokat, és mindig csak az aktív fülön lévő rajzolódik ki. Az event handert még be kell állítani, hogy értlems műveletet végezzen. 





[Created with Dillinger](http://dillinger.io)