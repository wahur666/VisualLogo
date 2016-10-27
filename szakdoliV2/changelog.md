# Changelog / Fejlesztői napló

## TODO List
+ __PythonApplication1__ át kell alakítani egy osztályá, és minimalizálni a kódot ebben a fájlban
+ A *Logo Moduls* még csak a szerkezeti felépítést tartalmazza, amit le kell implementálni!
+ Az UML diagrammot napra készre tenni!
+ *Etc.dt_example.py* egy DeltaTime implementáció, további feldolgozásra vár
+  ~~*Etc* FontAwesome tesztelélsek, a __t . py__ fájlban~~
+ A maradék ikonok ~~beszerzése és helyfoglalók~~ kicserélése. Továbbá a parancsok implementálása
+  A __Tab__ osztály újratervezést igényel nem maradhat így sokkal tovább, mert csak hátráltat, kódban feltüntetve a kritikus helyek, __alacsony prioritás__
+ ~~Az event handert még be kell állítani, hogy értlems műveletet végezzen.~~ 
+ ~~__ConfigParser__ ez nem maradhat így, vagy vissza kell hogy kerüljön a fő programba, vagy teljesen elvetni a külső konigurációs fájl használatát, jelenleg hátráltatja a gyors és dinamukus változtatás lehetőségét.~~
+ ~~A mainpanel átméretezése az elemek számától függően, és annak mozgatása fel-le irányban a görgőtől függően,~~ és húzás bal egérgombbal


## 2016.10.27. (Update 36)
+ Kisebb elíráok javítása
+ __AbstractDrawable__ kapott egy *ResetPosition* funkciót ami visszaállítja a konstruktorban megadott paramtéretben adott értékekre az objektumot, ez azért szükséges, hogy mikor váltunk Tab-ot akkor mindig a kezdőállípotba álljon vissza
+ __Poligon__ kapott egy felüldefiniált ResetPosition függvényt
+ __Tab__ kapott egy felüldefiniált ResetPosition függvényt, hogy ne használja a __Poligon__-ét, mivel technikai problémák miatt nem volt a kettő kompatibilis egymással
+ __ScrollingPlane__ Drag 'n Drop rész teljesen működő képessé lett téve, már csak a __Loop__  Utasítás vár elkészítésre.
+ __Button__ megkapta a Font Awesome implementációt, továbbra is támogatott a kép megadása
+ __GUI__ változott a kirajzolás szerkezete, külön lettek véve a gombok amik elrejtésre kerülnek
+ __Constans__ minden szükséges kép, és Font Awesome kapott egy konstans értéket, hogy könnyen lehessen hivatkozni az előre kiválasztott ikonokra
+ Új osztály:
    + __TextIcon__ funckiója: ez tartalmazza a Font Awesome előkészítését, és kirajzolásást
+ *Resources* ide került a FontAwesome.otf font fájl


### 2016.10.18. (Update 35)
+ __Command__ implementáció a drag 'n drop funckióra
+ Háttér szín miatt több panel mapott szolid fehér hátteret
+ __GUI__ események kezelése átkerült ide a __PythonApplication1__-ből, így minden esemény megkapja az egész esemény struktúrát, amiből majd lehet válogatni mi lesz felhasználva, ezzel könnyíve a fejlesztést. 
+ __Tab__ felcserlétem a színeket, sötét a kijelölt világos a nem aktív tabok színe
+ __Constants__ közkívánatra adtam még hozzá tesztelés során különböző színeket, hogy ne legyen fekete fehér egyhangú a program
+ __SupportFunctions__, új fájl, funkciója olyan függvények nyilvántartása, ami nem kötődik dirket a projekthez, de szügséges pár kritikus helyen
+ *Unittests* kapott még teszteket a __SupportFunctions__ fájl függvényeinek a tesztelésére
+ __ScrollingPlane__, sok sok új dolog, rendre:
    1. IsInside implementáció változott, és elkülöníthetőek a csoportosító elemektől
    2. OnClick() implementáció változott, mostmár külön eseménykezelés történik akkor mikor egy __Command__ osztály leszármazottjára kattintunk. Ugyanis akkor lemásolódik a parancs, és azt már a forráskódok közé tudjuk húzni.
    3. OnDrag() ez a mozgatás eseményeit dolgozza fel, adja hozzá a forráskód panelhez, rendezi át azt, és vesz el belőle elemet
    4. OnRelease() a parancs elegedése implementációja található itt, lényegében takarítás ha még nem történt meg az OnDrag() után, vagy az elem helyrerakása, ha még nem került át az új helyére
    5. Továbbá segédfunckiók, a parancsok elhelyezésére és szép formázására.
    6. Felcseréltem a Jobb és Bal nyilat esztétikai és logikai okokból



### 2016.10.10. (Update 34)
+ Kisebb hibák javítása
+ __Base.AbstarctDrawbale__ kapott egy SetPosition metódust, dinamikus elrendezés esetére, ahol nincs meg a fix pozíció, bár kötelező paramétere minden ebből származtatott osztálynak
+ __Base.Command__ feljebb lettek hozva a különböző metódusok implementációi, mivel megyeznek többnyire, a spciális eseteket majd külön kell kezelni, pl. __Loop__
+ __LogoModul.DrawableCommands__ oszályból ki lettek véve a fent kiemelet függvények implementációi
+ __Polygon__ oszály kapott egy háttérszínt, ha nem kívánjuk hogy áttetsző legyen
+ __Rectangle__ osztály is kapott egy háttérszínt, ez mellett kapott egy új attributumot, ami ki tudja kapocsolni, hogy mikor kattintunk az objektumra, annak ellenére hogy benne van hamisat adunk vissza, ez azért szükséges hogy ne a gyűjtő panel legyen mindig kattintva, hanem a rajta szereplő elemek. Ez még egy kisérleti funkció, további tesztelést és finomítást igényel.
+ __ScrollingPlane__ megkapta az oldalpanelt, amire fogom rátenni a Logó parancsokat, majd ezek után ezek segítségével lehet összerakni a Logó kódot, a fő panelben
+ __Tab__ osztály kapott háttérszínt, és attól függően, hogy épp ki van jelölve más színe van a háttérnek. Világos a kijelölt, sötét a nem. Az új kirajzolás elhalasztva határozatlan időre.



## 2016.10.04. (Update 33)
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



### 2016.10.03. (Commit 32)
+ Törött linkek és elírások javítása a readme és changelog fájlokban, továbbá további hivatkozások hozzáadása
+ Optimalizált importok, *Pycharm* segtítségével
+ Kisebb átnevezések az osztályokban
+ __AbstractDrawable__, kapott egy konstruktor, abból a célból, hogy a típus ellenőrzés megtörténjen, mivel Pythonban nem támogatott a függvény túlterhelés ezért kellett így csinálni. Ezentúl ami osztály az ebből származik, tudja használni majd ezt, így két féle módon meg lehet majd adni a helyzetét és nagyságát az elemeknek. Explicit (x, y, w, h) és Implicit a _size=tuple(w,h)_ és _vec2_pos=__Vector2(x, y)___ segítségével
+ __Button__, felbontva az osztály, a kép része átkerült egy saját osztályba (__Sprite__), ezzel az erőforrásokat könnyebben tudjuk nyilvántartani, és majd a paracsoknál és a teknős rajzolásánál is használható lesz
+ *System* könyvtár létrehozása, ide átkerült a __Constants__ osztály.
+ *Util* könyvtárban már csak a __Configparser__ maradt, ami egy függvény külön véve. 
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
    + __ScrollingPlane__, funkciója : ez fogja tárolni a parancsokat amit majd a felhasználó fog elheyezni a panelen, majd futtatni. Működik minden örökölt funkció. A fülek külön külön tárolják a parancsokat, és mindig csak az aktív fülön lévő rajzolódik ki.





[Created with Dillinger](http://dillinger.io)