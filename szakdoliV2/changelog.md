# Changelog / Fejlesztői napló


## 2016.10.10. (Update 34)
+ Kisebb hibák javítása
+ __Base.AbstarctDrawbale__ kapott egy SetPosition metódust, dinamikus elrendezés esetére, ahol nincs meg a fix pozíció, bár kötelező paramétere minden ebből származtatott osztálynak
+ __Base.Command__ feljebb lettek hozva a különböző metódusok implementációi, mivel megyeznek többnyire, a spciális eseteket majd külön kell kezelni, pl. __Loop__
+ __LogoModul.DrawableCommands__ oszályból ki lettek véve a fent kiemelet függvények implementációi, *TODO:* a maradék ikonok beszerzése és helyfoglalók kicserélése. Továbbá a parancsok implementálása
+ __Polygon__ oszály kapott egy háttérszínt, ha nem kívánjuk hogy áttetsző legyen
+ __Rectangle__ osztály is kapott egy háttérszínt, ez mellett kapott egy új attributumot, ami ki tudja kapocsolni, hogy mikor kattintunk az objektumra, annak ellenére hogy benne van hamisat adunk vissza, ez azért szükséges hogy ne a gyűjtő panel legyen mindig kattintva, hanem a rajta szereplő elemek. Ez még egy kisérleti funkció, további tesztelést és finomítást igényel.
+ __ScrollingPlane__ megkapta az oldalpanelt, amire fogom rátenni a Logó parancsokat, majd ezek után ezek segítségével lehet összerakni a Logó kódot, a fő panelben
+ __Tab__ osztály kapott háttérszínt, és attól függően, hogy épp ki van jelölve más színe van a háttérnek. Világos a kijelölt, sötét a nem. Az új kirajzolás elhalasztva határozatlan időre.
+ *Etc.dt_example.py* egy DeltaTime implementáció, további feldolgozásra vár



### 2016.10.04. (Update 33)
+ __ConfigParser__ átkerült az *Etc* mappába, mivel nem volt érdemi haszna ezért került oda, így megszünt a *Utils* mappa. 
+ __PythonApplication1__, a fő program most nem a *settings.ini* fájlból olvassa fel a méreteket, hanem két konstans értéket kapott
+ *Etc* mappa funkciója hogy ott tárolódnak azok az adatok amit már egyszer kikerestem neten, de még nincs berakva a kódba, és további elemzésre vár
+ __Command__ kapott egy konstruktort, és az IsInside művelet is kapott implementációt, mivel mindegyik egy négyzet, és ezzel elkerüljük felesleges kódismétlést
+ *Unittests* kikerült root-ra, mivel nincs szoros kapcsolatban a specifikus verziókkal
+ Új osztályok, és csomag:
    + *LogoModule* csomag, a progarm modulatritására törekvően jött létre. Az osztályok követik a [Model-View-Controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) alapelvet.
    + __Core__, funkciója: Ez a Logo Modulnak a vezérlője, itt dolgozom fel a felhasználó által adott parancsokat, és továbbítom a modelnek
    + __Turtle__, funkciója: Ez a Logo Modulnak a modellje. Minden mező és leírás itt található meg. Ez az osztály *package-private*. (Mivel pythonvan nincs direkt lehetőség elrejteni dolgokat, ezért itt jegyzem fel ezt. ) 
    + __DrawableCommands__, funkciója: ez egy gyüjtő osztály, amiben minden egyes lehetséges (eddig tervezett) parancs megjelenítéséhez szükséges osztályt és annak metódusait tárolja. Mivel a __Command__ megváltozott picit, ezért már az IsInside parancsok készen vannak, kivétel __Loop__ osztály, mert az több darabból fog állni, és ott majd külön kell kézileg lekezelni.
+ A *Logo Moduls* még csak a szerkezeti felépítést tartalmazza, amit le kell implementálni!
+ *TODO:* Az UML diagrammot napra készre tenni!


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