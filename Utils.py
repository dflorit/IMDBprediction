from numpy import *
from math import *
import matplotlib.pyplot as plt

#------------------------------Variables---------------------------------------
position_to_director = {0: 'James Cameron', 1: 'Gore Verbinski', 2: 'Christopher Nolan', 3: 'Doug Walker', 4: 'Sam Raimi', 5: 'Zack Snyder', 6: 'Bryan Singer', 7: 'Peter Jackson', 8: 'Marc Webb', 9: 'Ridley Scott', 10: 'Anthony Russo', 11: 'Peter Berg', 12: 'Colin Trevorrow', 13: 'Sam Mendes', 14: 'Tim Burton', 15: 'Brett Ratner', 16: 'Dan Scanlon', 17: 'Michael Bay', 18: 'Joseph Kosinski', 19: 'John Lasseter', 20: 'McG', 21: 'James Wan', 22: 'Marc Forster', 23: 'J.J. Abrams', 24: 'Guillermo del Toro', 25: 'Peter Sohn', 26: 'Mark Andrews', 27: 'Andrew Stanton', 28: 'Roland Emmerich', 29: 'Robert Zemeckis', 30: 'Martin Scorsese', 31: 'Tom Shadyac', 32: 'Kevin Reynolds', 33: 'Jon Favreau', 34: 'Rupert Sanders', 35: 'Matt Reeves', 36: 'Don Hall', 37: 'Dean DeBlois', 38: 'Jonathan Mostow', 39: 'Hideaki Anno', 40: 'Jon Turteltaub', 41: 'Wolfgang Petersen', 42: 'Duncan Jones', 43: 'Francis Lawrence', 44: 'Brad Bird', 45: 'Eric Darnell', 46: 'Gavin Hood', 47: 'Lana Wachowski', 48: 'Chris Buck', 49: 'George Miller', 50: 'Byron Howard', 51: 'Hoyt Yeatman', 52: 'Jonathan Liebesman', 53: 'Christopher McQuarrie', 54: 'Joe Johnston', 55: 'Steve Hickner', 56: 'Jennifer Yuh Nelson', 57: 'M. Night Shyamalan', 58: 'Simon Wells', 59: 'David Bowers', 60: 'Lee Tamahori', 61: 'Alessandro Carloni', 62: 'Peter Ramsey', 63: 'Rob Cohen', 64: 'Ang Lee', 65: 'Louis Leterrier', 66: 'Steven Spielberg', 67: 'Alejandro G. I\xed\xb1\xed\xe7rritu', 68: 'David Soren', 69: 'Paul Greengrass', 70: 'Mark Osborne', 71: 'Tim Johnson', 72: 'Chris Miller', 73: 'Baz Luhrmann', 74: 'Carlos Saldanha', 75: 'Paul Verhoeven', 76: 'Tony Gilroy', 77: 'Ron Howard', 78: 'John Woo', 79: 'Rob Minkoff', 80: 'Neill Blomkamp', 81: 'David Twohy', 82: 'Jos\xed\xa9 Padilha', 83: 'James Mangold', 84: 'Pete Docter', 85: 'Alfonso Cuar\xed_n', 86: 'Brad Peyton', 87: 'Steven Soderbergh', 88: 'Robert Schwentke', 89: 'Michel Gondry', 90: 'Noam Murro', 91: 'Will Finn', 92: 'Jan de Bont', 93: 'Frank Coraci', 94: 'Ron Clements', 95: 'Christopher Barnard', 96: 'Peter Chelsom', 97: 'Gary Trousdale', 98: 'Stefen Fangmeier', 99: 'Spike Jonze', 100: 'Florian Henckel von Donnersmarck', 101: 'Peter Hyams', 102: 'Edward Zwick', 103: 'Pitof', 104: 'Lawrence Guterman', 105: 'Steve Martino', 106: 'David Mamet', 107: 'Ash Brannon', 108: 'Jay Roach', 109: 'Rupert Wyatt', 110: 'Mark Waters', 111: 'John Lee Hancock', 112: 'Chris Columbus', 113: 'Barry Sonnenfeld', 114: 'Tony Bancroft', 115: 'Walt Becker', 116: 'Dennis Dugan', 117: 'Thor Freudenthal', 118: 'Phillip Noyce', 119: 'Brian De Palma', 120: 'Mick Jackson', 121: 'Alan J. Pakula', 122: 'John Milius', 123: 'Andrey Konchalovskiy', 124: 'Gary Ross', 125: 'Martin Brest', 126: 'Bob Fosse', 127: 'Edgar Wright', 128: 'Jon Amiel', 129: 'Pete Travis', 130: 'George A. Romero', 131: 'Doug Liman', 132: 'David Fincher', 133: 'Todd Phillips', 134: 'Gary Winick', 135: 'Mimi Leder', 136: 'Mike Mitchell', 137: 'Adam Shankman', 138: '', 139: 'Albert Hughes', 140: 'Shawn Levy', 141: 'Scott Derrickson', 142: 'Eric Brevig', 143: 'Kelly Asbury', 144: 'Stephen Hopkins', 145: 'Henry Jaglom', 146: 'Genndy Tartakovsky', 147: 'James Algar', 148: 'Ron Underwood', 149: 'Steven Brill', 150: 'Lucile Hadzihalilovic', 151: 'Barry Cook', 152: 'Roger Christian', 153: 'Richard Donner', 154: 'Breck Eisner', 155: 'Luc Besson', 156: 'Jacques Perrin', 157: 'Paul W.S. Anderson', 158: 'Andr\xed\xa9s Couturier', 159: 'Roger Allers', 160: 'Cody Cameron', 161: 'Des McAnuff', 162: 'Yarrow Cheney', 163: 'Pierre Coffin', 164: 'Timur Bekmambetov', 165: 'Renny Harlin', 166: 'David Kellogg', 167: 'Martin Campbell', 168: 'Bibo Bergeron', 169: 'Bill Condon', 170: 'Gil Kenan', 171: 'Florent-Emilio Siri', 172: 'Don Bluth', 173: 'David Pastor', 174: 'Henry Selick', 175: 'Kyle Balda', 176: 'Clay Kaytis', 177: 'Andy Tennant', 178: 'Steve Carr', 179: 'David Silverman', 180: 'Jean-Jacques Annaud', 181: 'Betty Thomas', 182: 'Paul Tibbitt', 183: 'Randall Wallace', 184: 'Jonathan Frakes', 185: 'Andrzej Bartkowiak', 186: 'Gregory Hoblit', 187: 'Mikael Salomon', 188: 'Bobby Farrelly', 189: 'Phil Alden Robinson', 190: 'Frank Oz', 191: 'Seth MacFarlane', 192: 'Craig Gillespie', 193: 'Rob Bowman', 194: 'Doug Lefler', 195: 'Chris Wedge', 196: 'Michael Lembeck', 197: 'Angelina Jolie Pitt', 198: 'Oliver Stone', 199: 'Larry Charles', 200: 'Glenn Ficarra', 201: 'David S. Goyer', 202: 'Mike Nichols', 203: 'Michael Lehmann', 204: 'Stuart Beattie', 205: 'Roman Polanski', 206: 'Baltasar Korm\xed\xe7kur', 207: 'Tom Tykwer', 208: 'Lawrence Kasdan', 209: 'Rob Reiner', 210: 'Tim Hill', 211: 'David Frankel', 212: 'Frank Darabont', 213: 'Mark Dindal', 214: 'Simon West', 215: 'Tony Scott', 216: 'Wes Ball', 217: 'Robert Redford', 218: 'Michael Mann', 219: 'Kenny Ortega', 220: 'David McNally', 221: 'Brian Robbins', 222: 'Chris Butler', 223: 'Michael Caton-Jones', 224: 'Sam Fell', 225: 'Jean-Pierre Jeunet', 226: 'Antoine Fuqua', 227: 'Phil Lord', 228: 'Clark Johnson', 229: 'Stuart Baird', 230: 'Robert Lorenz', 231: 'Joe Wright', 232: 'Scott Stewart', 233: 'Patrick Gilmore', 234: 'Walter Hill', 235: 'Akiva Goldsman', 236: 'John Dahl', 237: 'Tim Miller', 238: 'Clint Eastwood', 239: 'Brian Levant', 240: 'Anthony Hemingway', 241: 'Sam Weisman', 242: 'Brad Silberling', 243: 'Gabriele Muccino', 244: 'Barry Levinson', 245: 'Quentin Tarantino', 246: 'Paul King', 247: 'Peter Lord', 248: 'Joel Schumacher', 249: 'Karyn Kusama', 250: 'Ron Maxwell', 251: 'Robert Butler', 252: 'Stanley Kubrick', 253: 'Cameron Crowe', 254: 'Steven Zaillian', 255: 'John Singleton', 256: 'F. Gary Gray', 257: 'Robert Rodriguez', 258: 'Kathryn Bigelow', 259: 'Terrence Malick', 260: 'John Whitesell', 261: 'James L. Brooks', 262: 'Neil Jordan', 263: 'Frank Marshall', 264: 'Alex Proyas', 265: 'Hideo Nakata', 266: 'Peter Hewitt', 267: 'Jaume Collet-Serra', 268: "Matthew O'Callaghan", 269: 'Gary Fleder', 270: 'Adrian Lyne', 271: 'Stephen Gaghan', 272: 'Christophe Gans', 273: 'Steven Quale', 274: 'Joe Dante', 275: 'Danny Boyle', 276: 'James McTeigue', 277: 'Tom Dey', 278: 'Barbet Schroeder', 279: 'Peter Webber', 280: 'John McTiernan', 281: 'John Carpenter', 282: 'Alan Parker', 283: 'Jim Sheridan', 284: 'William Friedkin', 285: 'Chuck Bowman', 286: 'Olivier Megaton', 287: 'Deepa Mehta', 288: 'Andrei Tarkovsky', 289: 'Robert Luketic', 290: 'Thomas Carter', 291: 'Roger Michell', 292: 'Luis Llosa', 293: 'Ron Shelton', 294: 'Melville Shavelson', 295: 'Garth Jennings', 296: 'Julie Taymor', 297: 'Mathieu Kassovitz', 298: 'Harold Ramis', 299: 'Sean Penn', 300: 'Simon Wincer', 301: 'Stephen Sommers', 302: 'Spike Lee', 303: 'Mike Newell', 304: 'Lawrence Kasanoff', 305: 'George P. Cosmatos', 306: 'Norman Ferguson', 307: 'Michael Cimino', 308: 'Sydney Pollack', 309: 'Barbra Streisand', 310: 'Mark Pellington', 311: 'John Glen', 312: 'Annabel Jankel', 313: 'Curtis Hanson', 314: 'Jamel Debbouze', 315: 'John G. Avildsen', 316: 'Bruce Beresford', 317: 'Sam Taylor-Johnson', 318: 'Francis Ford Coppola', 319: 'Brian Helgeland', 320: 'Tim Story', 321: 'Taylor Hackford', 322: 'David R. Ellis', 323: 'Mark A.Z. Dipp\xed\xa9', 324: 'Mel Gibson', 325: 'Nimr\xed_d Antal', 326: 'Alejandro Agresti', 327: 'Iain Softley', 328: 'Peter Hedges', 329: 'Colin Strause', 330: 'Greg Mottola', 331: 'Wes Craven', 332: 'Russell Mulcahy', 333: 'Christian Duguay', 334: 'Chuck Russell', 335: 'Frederik Du Chau', 336: 'Joseph Kahn', 337: 'J.A. Bayona', 338: 'Wes Anderson', 339: 'Danny DeVito', 340: 'Jerry Jameson', 341: 'Mic Rodgers', 342: 'Christian Alvart', 343: 'Pierre Morel', 344: 'D.J. Caruso', 345: 'Sergey Bodrov', 346: 'Joss Whedon', 347: 'David Carson', 348: 'Yuefeng Song', 349: 'Norman Jewison', 350: 'Luis Mandoki', 351: 'Michael Apted', 352: 'Stephen Herek', 353: 'Lee Daniels', 354: 'J Blakeson', 355: 'Ethan Coen', 356: 'Fedor Bondarchuk', 357: 'Charles Martin Smith', 358: 'John Frankenheimer', 359: 'Andrew Bergman', 360: 'Kirk De Micco', 361: 'Wilson Yip', 362: 'Roland Joff\xed\xa9', 363: 'Anthony Minghella', 364: 'Roger Donaldson', 365: 'Kevin Munroe', 366: 'Nicholas Stoller', 367: 'Tobe Hooper', 368: 'Alan Poul', 369: 'Catherine Hardwicke', 370: 'Alexandre Aja', 371: 'Hugh Wilson', 372: 'Chris Carter', 373: 'Peter Landesman', 374: 'Gary Chapman', 375: 'David Koepp', 376: 'Hark Tsui', 377: 'Ronny Yu', 378: 'Moustapha Akkad', 379: 'Tony Kaye', 380: 'Darren Aronofsky', 381: 'Hugh Johnson', 382: 'Hayao Miyazaki', 383: 'George Tillman Jr.', 384: 'Rand Ravich', 385: 'Warren Beatty', 386: 'Jeremy Degruson', 387: 'Chris Gorak', 388: 'Scott Speer', 389: 'Joe Charbanic', 390: 'Danny Cannon', 391: 'Richard Marquand', 392: 'Stephen Daldry', 393: 'Rupert Wainwright', 394: 'Miguel Sapochnik', 395: 'Hyung-rae Shim', 396: 'Nanette Burstein', 397: 'Rob Marshall', 398: 'J.B. Rogers', 399: 'Michael Sucsy', 400: 'Rawson Marshall Thurber', 401: 'Steve Oedekerk', 402: 'Stephen Hillenburg', 403: 'Nick Cassavetes', 404: 'Stig Bergqvist', 405: 'Jason Reitman', 406: 'Jonathan Levine', 407: 'Rian Johnson', 408: 'Chris Noonan', 409: 'Peter Lepeniotis', 410: 'Steve Box', 411: 'Jon M. Chu', 412: 'David Slade', 413: 'Drew Goddard', 414: 'Jason Friedberg', 415: 'John R. Leonetti', 416: 'Tom Hanks', 417: 'Liz Friedlander', 418: 'Shane Acker', 419: 'Stephen J. Anderson', 420: 'Troy Miller', 421: 'Tate Taylor', 422: 'Alister Grierson', 423: 'Paul Haggis', 424: 'Vincenzo Natali', 425: "Gavin O'Connor", 426: 'Bruce Hunt', 427: 'Paul McGuigan', 428: 'James Wong', 429: 'Andy Cadiff', 430: 'Mike Disa', 431: 'Kaige Chen', 432: 'Andrew Dominik', 433: 'Li Zhang', 434: 'Reinhard Klooss', 435: 'Liliana Cavani', 436: 'Greg Tiernan', 437: 'George Clooney', 438: 'Richard Attenborough', 439: 'Don Mancini', 440: 'John Maybury', 441: 'Igor Kovalyov', 442: 'Shinji Aramaki', 443: 'Ben Stiller', 444: 'Lasse Hallstr\xed_m', 445: 'Patrick Lussier', 446: 'Burr Steers', 447: 'Jeff Wadlow', 448: 'David Lean', 449: 'Richard Eyre', 450: 'Nicholas Meyer', 451: 'Chris Weitz', 452: 'Steve Miner', 453: 'Philip Kaufman', 454: 'Walter Murch', 455: 'E. Elias Merhige', 456: 'Menno Meyjes', 457: 'John Madden', 458: 'Scott Frank', 459: 'Kevin Costner', 460: 'Andrew Morahan', 461: 'Woody Allen', 462: 'Tarsem Singh', 463: 'Fernando Meirelles', 464: 'Michael Hoffman', 465: 'Raja Gosnell', 466: 'John A. Davis', 467: 'Michael Pressman', 468: 'Scott Hicks', 469: 'Tyler Perry', 470: 'John Polson', 471: 'Kirk Jones', 472: 'Bernardo Bertolucci', 473: 'Paul Thomas Anderson', 474: 'Cathy Malkasian', 475: 'John Eng', 476: 'Ken Kwapis', 477: 'Victor Salva', 478: 'Andy Fickman', 479: 'Steve Bendelack', 480: 'Dwight H. Little', 481: 'Kirsten Sheridan', 482: 'Richard Fleischer', 483: 'Damien Dante Wayans', 484: 'Philip G. Atwell', 485: 'Don Michael Paul', 486: 'James Bridges', 487: 'Carter Smith', 488: 'Jonathan Kaplan', 489: 'Ole Bornedal', 490: 'Rachel Talalay', 491: 'Andrew Adamson', 492: 'Robert Towne', 493: 'J\xed\xa9r\xed\xc7me Deschamps', 494: 'Inna Evlannikova', 495: 'Mario Van Peebles', 496: 'Sylvester Stallone', 497: 'Herbert Ross', 498: 'Grant Heslov', 499: 'Sidney Lumet', 500: 'Douglas McGrath', 501: 'Richard Williams', 502: 'Irvin Kershner', 503: 'Joseph Sargent', 504: 'Teddy Chan', 505: 'Mikael H\xed\xabfstr\xed_m', 506: 'Russell Crowe', 507: 'Jerry Zucker', 508: 'John Pasquin', 509: 'Irwin Winkler', 510: 'Jessie Nelson', 511: 'Len Wiseman', 512: 'Mike Bigelow', 513: 'Harry Elfont', 514: 'Fred Dekker', 515: 'Brian Trenchard-Smith', 516: 'Camille Delamarre', 517: 'Christian Carion', 518: 'Scott Cooper', 519: 'Stuart Gillard', 520: 'David O. Russell', 521: 'Jodie Foster', 522: 'David Cronenberg', 523: 'Jim Sonzero', 524: 'Jonathan Demme', 525: 'Jeannot Szwarc', 526: 'Ben Falcone', 527: 'Alexander Payne', 528: 'Andrew Davis', 529: 'Steve McQueen', 530: 'Charles Stone III', 531: 'Thea Sharrock', 532: 'Aaron Seltzer', 533: 'Ava DuVernay', 534: 'Steve Trenbirth', 535: 'Stephen Kay', 536: 'Mennan Yapo', 537: 'Jun Falkenstein', 538: 'Boaz Yakin', 539: 'Takashi Shimizu', 540: 'Gary Nelson', 541: 'John Patrick Shanley', 542: 'John Luessenhop', 543: 'Steve Beck', 544: 'Nelson McCormick', 545: 'Stephen Frears', 546: 'Michael Spierig', 547: 'William Brent Bell', 548: 'Anthony Bell', 549: 'Gus Van Sant', 550: 'Henry Joost', 551: 'Ed Harris', 552: 'Shana Feste', 553: 'Steve Rash', 554: 'Michael J. Bassett', 555: 'Frank Nissen', 556: 'Paul Abascal', 557: 'Michael Moore', 558: 'Billy Ray', 559: 'Mark Neveldine', 560: 'Michael O. Sajbel', 561: 'Charles T. Kanganis', 562: 'Dave Borthwick', 563: 'Glen Morgan', 564: 'Alejandro Monteverde', 565: 'Richard Linklater', 566: 'Uwe Boll', 567: 'J.C. Chandor', 568: 'Paul Gross', 569: 'Marc Abraham', 570: 'Todd Haynes', 571: 'Charlie Kaufman', 572: 'Nancy Walker', 573: 'Matthew Diamond', 574: 'David Anspaugh', 575: 'Jean-Marie Poir\xed\xa9', 576: 'Jane Clark', 577: 'Wayne Thornley', 578: 'Gnana Rajasekaran', 579: 'Jonathan Jakubowicz', 580: 'John Curran', 581: 'Jake Kasdan', 582: 'William Malone', 583: 'Anthony Mann', 584: 'Emile Ardolino', 585: 'James Schamus', 586: 'Andrew Douglas', 587: 'Terry Gilliam', 588: 'Thomas Bezucha', 589: 'Milos Forman', 590: 'Robert Altman', 591: 'Brandon Camp', 592: 'Kevin Tancharoen', 593: 'Bart Freundlich', 594: 'William A. Fraker', 595: 'John Boorman', 596: 'Matthew Robbins', 597: 'Kenneth Branagh', 598: 'Jeff Nichols', 599: 'Michael Haneke', 600: 'Zack Ward', 601: 'Tran Anh Hung', 602: 'Christian Volckman', 603: 'Matt Dillon', 604: 'Alejandro Amen\xed\xe7bar', 605: 'Joe Carnahan', 606: 'Kevin Greutert', 607: 'Niki Caro', 608: 'Chris Robinson', 609: 'Robert Harmon', 610: 'Gary Halvorson', 611: 'Fede Alvarez', 612: 'Ian Iqbal Rashid', 613: 'Jim Goddard', 614: 'Noel Marshall', 615: 'Guillaume Ivernel', 616: 'Jack Smight', 617: 'Vadim Perelman', 618: 'Peter Weir', 619: 'Michel Hazanavicius', 620: 'Cyrus Nowrasteh', 621: 'Dennie Gordon', 622: 'Peter Kosminsky', 623: 'Nick Gomez', 624: 'Allen Coulter', 625: 'Richard Benjamin', 626: 'Josef Rusnak', 627: 'Bruce Paltrow', 628: 'Adam Rifkin', 629: 'James Ivory', 630: 'Gaspar No\xed\xa9', 631: 'J\xed\xa9r\xed\xc7me Salle', 632: 'William Bindley', 633: 'Wayne Beach', 634: 'James Gunn', 635: 'Tom Hooper', 636: 'Jeff Tremaine', 637: 'James Watkins', 638: 'Michael Dougherty', 639: 'Brian Gibson', 640: 'Joel Gallen', 641: 'James Marsh', 642: 'Rob Zombie', 643: 'Dennis Iliadis', 644: 'Clare Kilner', 645: 'Nicolas Winding Refn', 646: 'Nicholas Hytner', 647: 'Gina Prince-Bythewood', 648: 'Joe Berlinger', 649: 'Andrew Fleming', 650: 'Michael Mayer', 651: 'Martin Weisz', 652: 'Mike Nawrocki', 653: 'Catherine Owens', 654: 'Lone Scherfig', 655: 'Steve Gomer', 656: 'Sean McNamara', 657: 'Craig Brewer', 658: 'Michael Winterbottom', 659: 'Wil Shriner', 660: 'Rodman Flender', 661: 'Katja von Garnier', 662: 'Mark Romanek', 663: 'Brad Anderson', 664: 'Michael Chapman', 665: 'Antonio Banderas', 666: 'Khalil Sullins', 667: 'Atom Egoyan', 668: 'Andrey Zvyagintsev', 669: 'Tony Jaa', 670: 'Neil Marshall', 671: 'Ry\xed\xe9hei Kitamura', 672: 'Anthony Silverston', 673: 'Gabe Ib\xed\xe7\xed\xb1ez', 674: 'Gerry Lively', 675: 'Daniele Luchetti', 676: 'Vidhu Vinod Chopra', 677: 'Sylvain White', 678: 'Courtney Solomon', 679: 'Alan Cohn', 680: 'Tom Holland', 681: 'Emilio Estevez', 682: 'Todd Field', 683: 'James Fargo', 684: 'Mike Leigh', 685: 'Alain Resnais', 686: 'Neil Burger', 687: 'Kasi Lemmons', 688: 'Oliver Hirschbiegel', 689: 'Jonathan Glazer', 690: 'Patricia Riggen', 691: 'Eric Bress', 692: 'John Lafia', 693: 'Alex Garland', 694: 'Dave Green', 695: 'Michael Polish', 696: 'Daisy von Scherler Mayer', 697: 'Lenny Abrahamson', 698: 'Bob Saget', 699: 'Niels Arden Oplev', 700: 'Blair Hayes', 701: 'Jon Lucas', 702: 'Olivier Assayas', 703: 'John Stainton', 704: 'Denzel Washington', 705: 'Mark Herman', 706: 'Lars von Trier', 707: 'William Dear', 708: 'St\xed\xa9phane Aubier', 709: 'John Badham', 710: 'Mike McCoy', 711: 'Anne Fletcher', 712: 'Mike Judge', 713: 'Josh Trank', 714: 'Nima Nourizadeh', 715: 'Franklin J. Schaffner', 716: 'John Erick Dowdle', 717: 'Brian Henson', 718: 'Dan Cutforth', 719: 'Josh Boone', 720: 'Bob Rafelson', 721: 'Dean Israelite', 722: 'Scott Alexander', 723: 'Stuart Gordon', 724: 'Christopher Guest', 725: 'Ryan Murphy', 726: 'Jane Campion', 727: 'James Gray', 728: 'Joon-ho Bong', 729: 'Roger Spottiswoode', 730: 'Antonia Bird', 731: 'Kar-Wai Wong', 732: 'Carroll Ballard', 733: 'Takeshi Kitano', 734: 'Marco Kreuzpaintner', 735: 'Lajos Koltai', 736: 'Chuan Lu', 737: 'Lijun Sun', 738: 'Takashi Yamazaki', 739: 'Mary Lambert', 740: 'Akira Kurosawa', 741: 'Tim Robbins', 742: 'Mel Brooks', 743: 'Brendan Malloy', 744: 'Gregory Poirier', 745: 'Bill Paxton', 746: 'Martin Ritt', 747: 'John Turturro', 748: 'Agnieszka Holland', 749: 'David Hackl', 750: 'Giuliano Montaldo', 751: 'Ruairi Robinson', 752: 'Jaume Balaguer\xed_', 753: 'Jon Kasdan', 754: 'Christopher Cain', 755: 'Darren Lynn Bousman', 756: 'Geoffrey Sax', 757: 'Chuck Sheetz', 758: 'Mark L. Lester', 759: 'Marcus Raboy', 760: 'Leigh Whannell', 761: 'Brett Leonard', 762: 'David Lowery', 763: 'Ciar\xed\xe7n Foy', 764: 'Olatunde Osunsanmi', 765: 'Malcolm D. Lee', 766: 'Tuck Tucker', 767: 'Richard Shepard', 768: 'Theodore Witcher', 769: 'Michael Patrick Jann', 770: 'Jeff Lowell', 771: 'Marcus Dunstan', 772: 'Timothy Bj\xed_rklund', 773: 'David Lynch', 774: 'Jason Bateman', 775: 'David Schwimmer', 776: 'Allan Arkush', 777: 'Werner Herzog', 778: 'Dan Fogelman', 779: 'John Putch', 780: 'Terence Davies', 781: 'Eric Blakeney', 782: 'Rakesh Roshan', 783: 'Guy Ritchie', 784: 'Vincent Gallo', 785: 'Claude Chabrol', 786: 'Jon Stewart', 787: 'Ralph Fiennes', 788: 'Christopher Smith', 789: 'Alan Metter', 790: 'Jeb Stuart', 791: 'Michael Radford', 792: 'Arthur Hiller', 793: 'Kim Farrant', 794: 'Andrew Traucki', 795: 'Robert Adetuyi', 796: 'Taedong Park', 797: 'Benedikt Erlingsson', 798: 'Jee-woon Kim', 799: 'Douglas Aarniokoski', 800: 'Andy Garcia', 801: 'Lewis Gilbert', 802: 'Gary Sherman', 803: 'Valeri Milev', 804: 'Stanley Kramer', 805: 'Gerald Potterton', 806: 'Anurag Basu', 807: 'Kriv Stenders', 808: 'James DeMonaco', 809: 'Rod Lurie', 810: 'Tamara Jenkins', 811: 'Hong-jin Na', 812: 'Peter Cattaneo', 813: 'Julian Jarrold', 814: 'Martyn Pick', 815: 'Joby Harold', 816: 'Mark Rydell', 817: 'Tom Elkins', 818: 'Woo-Suk Kang', 819: 'John Sayles', 820: 'Mervyn LeRoy', 821: 'James Frawley', 822: 'Chris Stokes', 823: 'Don Siegel', 824: 'Doug Atchison', 825: 'Tamra Davis', 826: 'Troy Duffy', 827: 'Matty Rich', 828: 'Joe Nussbaum', 829: 'Fina Torres', 830: 'Duke Johnson', 831: 'Michael Winner', 832: 'Tomm Moore', 833: 'Marc Sch\xed_lermann', 834: 'Thomas Vinterberg', 835: 'Katsuhiro \xed\xeetomo', 836: 'Charles Binam\xed\xa9', 837: 'Ol Parker', 838: 'Fran\xed_ois Ozon', 839: 'Michael Winnick', 840: 'David Oelhoffen', 841: 'Eli Roth', 842: 'Tony Richardson', 843: 'Claude Miller', 844: 'Vincent Paronnaud', 845: 'Dennis Gansel', 846: 'Robert Marcarelli', 847: 'Ernie Barbarash', 848: 'Jay Russell', 849: 'Don Kempf', 850: 'Matt Bettinelli-Olpin', 851: 'Sharron Miller', 852: 'Tony Maylam', 853: 'Yash Chopra', 854: 'Kevin Brodie', 855: 'George Hickenlooper', 856: 'Lynne Ramsay', 857: 'John Stephenson', 858: 'Sofia Coppola', 859: 'Spencer Susser', 860: 'Peter Sollett', 861: 'Aleksey German', 862: 'Richard Rich', 863: 'Kim Nguyen', 864: 'Denis Villeneuve', 865: 'Robert Wise', 866: 'Louis Morneau', 867: 'Caroline Link', 868: 'Hans Petter Moland', 869: 'Oren Moverman', 870: 'Ian Sharp', 871: "Dan O'Bannon", 872: 'Jerome Robbins', 873: 'Rick Famuyiwa', 874: 'King Vidor', 875: 'Rusty Cundieff', 876: 'Jean-Jacques Mantello', 877: 'John Michael McDonagh', 878: 'Deb Hagan', 879: 'John Cameron Mitchell', 880: 'Jon Knautz', 881: 'Wayne Wang', 882: 'Joey Lauren Adams', 883: 'S.R. Bindler', 884: 'C\xed\xa9dric Klapisch', 885: 'Charles Matthau', 886: 'Prachya Pinkaew', 887: 'Gurinder Chadha', 888: 'George Roy Hill', 889: 'Hugh Hudson', 890: 'Darren Grant', 891: 'Terry Zwigoff', 892: 'William Sachs', 893: 'Christophe Barratier', 894: '\xed\x8amile Gaudreault', 895: 'James Cox', 896: 'Hitoshi Matsumoto', 897: 'Rakeysh Omprakash Mehra', 898: 'Collin Schiffli', 899: 'Jon Wright', 900: 'Rohan Sippy', 901: 'Dan Trachtenberg', 902: 'David F. Sandberg', 903: 'Stiles White', 904: 'Blake Edwards', 905: 'Christopher Landon', 906: 'Jean-Marc Vall\xed\xa9e', 907: 'David Gelb', 908: 'Mike Flanagan', 909: 'George Jackson', 910: 'Bille Woodruff', 911: 'Michael Curtiz', 912: 'Rob Hedden', 913: 'Joe Chappelle', 914: 'Fred Walton', 915: 'Steve Carver', 916: 'Gonzalo L\xed_pez-Gallego', 917: 'Christine Jeffs', 918: 'Don Coscarelli', 919: 'Mamoru Hosoda', 920: 'Nicholaus Goossen', 921: 'Scott Marshall', 922: 'Ronan Chapalain', 923: 'Xavier Beauvois', 924: 'Randall Miller', 925: 'Jerry Belson', 926: 'Paul Schrader', 927: 'Jeremy Saulnier', 928: 'Billy Kent', 929: 'James Manera', 930: 'Feroz Abbas Khan', 931: 'Errol Morris', 932: 'Nicholas Fackler', 933: 'Matthew Hastings', 934: 'Klaus Menzel', 935: 'Oren Peli', 936: 'Paul Andrew Williams', 937: 'Billy Bob Thornton', 938: 'Frank LaLoggia', 939: 'Jeremy Brock', 940: 'Sam Peckinpah', 941: 'Christophe Ali', 942: 'Shona Auerbach', 943: 'Robert Sarkies', 944: 'Randal Kleiser', 945: 'John Huston', 946: 'Jonas \xed\x83kerlund', 947: 'Chan-wook Park', 948: 'Johnnie To', 949: 'Mateo Gil', 950: 'R. Balki', 951: 'Ivan Engler', 952: 'Bob Clark', 953: 'Cecil B. DeMille', 954: 'Mike Figgis', 955: 'Duane Journey', 956: 'Carol Reed', 957: 'John Sturges', 958: 'William Arntz', 959: 'Ed Gass-Donnelly', 960: 'Patrick Stettner', 961: 'James Melkonian', 962: 'Alfred Hitchcock', 963: 'Bob Odenkirk', 964: 'Mike Mills', 965: 'Kevin Smith', 966: 'Dave McKean', 967: 'Ron Fricke', 968: 'Ruggero Deodato', 969: 'Mora Stephens', 970: 'Leos Carax', 971: 'Jorge Ram\xed_rez Su\xed\xe7rez', 972: 'Anne Fontaine', 973: 'Dan Ireland', 974: 'Aleksandr Veledinskiy', 975: 'Peter H. Hunt', 976: 'Fred Zinnemann', 977: 'Richard Raymond', 978: 'George Sidney', 979: 'Christopher Morris', 980: 'Peter Stebbings', 981: 'Vincente Minnelli', 982: 'Jim Abrahams', 983: 'Michael Gornick', 984: 'Robert Eggers', 985: 'Juan Jos\xed\xa9 Campanella', 986: 'Louis C.K.', 987: 'Anthony C. Ferrante', 988: 'Salvador Carrasco', 989: 'Andr\xed\xa9 \xed\xd6vredal', 990: 'Warren P. Sonoda', 991: 'Amanda Gusack', 992: 'Charles Adelman', 993: 'Jay Oliva', 994: 'Charles Ferguson', 995: 'Daniel Petrie Jr.', 996: 'Luc Jacquet', 997: 'Clark Gregg', 998: 'Damien Chazelle', 999: 'Karen Moncrieff', 1000: 'Eric Styles', 1001: 'Max Mayer', 1002: 'Joshua Marston', 1003: 'John Gulager', 1004: 'Brandon Cronenberg', 1005: 'Frank Capra', 1006: 'Tod Williams', 1007: 'Jack Sholder', 1008: 'Richard Brooks', 1009: 'Ted Post', 1010: 'Kunihiko Yuyama', 1011: 'Tom McLoughlin', 1012: 'Adam Marcus', 1013: 'Michael Schultz', 1014: 'Howard Hawks', 1015: 'Nnegest Likk\xed\xa9', 1016: "Damien O'Donnell", 1017: 'Mira Nair', 1018: 'Nicole Holofcener', 1019: 'Anthony Hickox', 1020: 'Tom Schulman', 1021: 'Noah Baumbach', 1022: 'David Nixon', 1023: 'Michael Landon Jr.', 1024: 'Andrea Arnold', 1025: 'Deon Taylor', 1026: 'Conor McPherson', 1027: 'Craig Moss', 1028: 'Paolo Monico', 1029: 'Youssef Delara', 1030: 'Walter Salles', 1031: 'Heidi Ewing', 1032: 'Hank Braxtan', 1033: 'John Carl Buechler', 1034: 'Rajkumar Hirani', 1035: 'Thorbj\xed\x9frn Christoffersen', 1036: 'Alex van Warmerdam', 1037: 'Victor Fleming', 1038: 'Joseph Zito', 1039: 'Nacho Vigalondo', 1040: 'Stanley Donen', 1041: "Dinesh D'Souza", 1042: 'Tommy Lee Wallace', 1043: 'Don Taylor', 1044: 'Leslie Small', 1045: '\xed\x8aric Tessier', 1046: 'Alice Wu', 1047: 'Joshua Tickell', 1048: 'Reed Cowan', 1049: 'Stefan Ruzowitzky', 1050: 'Alex Rivera', 1051: 'Benni Diez', 1052: 'Robby Henson', 1053: 'Zackary Adler', 1054: 'Shane Meadows', 1055: 'Dominic Burns', 1056: 'Carmen Marron', 1057: 'Tim McCanlies', 1058: 'Jerry Rees', 1059: 'Danny Steinmann', 1060: 'Tay Garnett', 1061: 'Larry Clark', 1062: 'Petter N\xed_ss', 1063: 'Robert Fontaine', 1064: 'Dan Perri', 1065: 'Neil Mcenery-West', 1066: 'Terence Young', 1067: 'David Robert Mitchell', 1068: 'Robert Mulligan', 1069: 'Kimberly Peirce', 1070: 'Chris Kentis', 1071: 'Sylvain Chomet', 1072: 'Shari Springer Berman', 1073: 'Kevin Macdonald', 1074: 'Miranda July', 1075: 'Max Joseph', 1076: 'Ari Folman', 1077: 'David Sington', 1078: 'Fenton Bailey', 1079: 'Huck Botko', 1080: 'Jugal Hansraj', 1081: 'Aaron Hann', 1082: 'Colin Minihan', 1083: 'Conor McMahon', 1084: 'Chris Shadley', 1085: 'Simon Napier-Bell', 1086: 'Simon Yin', 1087: 'Dave Payne', 1088: 'Harald Reinl', 1089: 'Richard Lester', 1090: 'Scott Dow', 1091: 'Jerry Dugan', 1092: 'Rodrigo Cort\xed\xa9s', 1093: 'Jehane Noujaim', 1094: 'Daniel Stamm', 1095: 'Elia Kazan', 1096: 'Carlos Carrera', 1097: 'Benh Zeitlin', 1098: 'Vera Farmiga', 1099: 'Jonathan Wacks', 1100: 'Khyentse Norbu', 1101: 'Tony Krantz', 1102: 'Mitchell Altieri', 1103: 'W.D. Hogan', 1104: 'David Hunt', 1105: 'J. Lee Thompson', 1106: 'Steven R. Monroe', 1107: 'Pawel Pawlikowski', 1108: 'Sally Potter', 1109: 'Brad J. Silverman', 1110: 'Dave Meyers', 1111: 'Nadine Labaki', 1112: 'Eytan Fox', 1113: 'Fran\xed_ois Truffaut', 1114: 'Travis Zariwny', 1115: 'Fabi\xed\xe7n Bielinsky', 1116: 'Roger Avary', 1117: 'Henry Bean', 1118: 'David Gordon Green', 1119: 'Jeff Garlin', 1120: 'Adam Green', 1121: 'Adam Carolla', 1122: 'Ira Sachs', 1123: 'Bruce McDonald', 1124: 'Robert Greenwald', 1125: 'David Winning', 1126: 'Lucrecia Martel', 1127: 'Zak Penn', 1128: 'Mathieu Amalric', 1129: 'David Worth', 1130: 'Robert M. Young', 1131: 'Boris Rodriguez', 1132: 'Paul Donovan', 1133: 'Douglas Cheek', 1134: 'Deryck Broom', 1135: 'Henry Hathaway', 1136: 'Jay Chandrasekhar', 1137: 'Claudia Sainte-Luce', 1138: 'Kenneth Lonergan', 1139: 'Steve Taylor', 1140: 'Kurt Voss', 1141: 'L\xed\xa9a Pool', 1142: 'Brenton Spencer', 1143: 'Jay Alaimo', 1144: 'Jeff Burr', 1145: 'Harry Gantz', 1146: 'Gareth Evans', 1147: 'Joe Marino', 1148: 'Joel Anderson', 1149: 'Levan Gabriadze', 1150: 'Bradley Parker', 1151: 'Clive Barker', 1152: 'Takao Okawara', 1153: 'Derek Cianfrance', 1154: 'Davis Guggenheim', 1155: 'Allan Dwan', 1156: 'Andrew Steggall', 1157: 'Robert Kenner', 1158: 'Sean Durkin', 1159: 'Morgan Neville', 1160: 'Chris Paine', 1161: 'Marc Levin', 1162: 'Richard Dutcher', 1163: 'Trey Parker', 1164: 'Finn Taylor', 1165: 'Gia Coppola', 1166: 'Mike Cahill', 1167: 'Alex Gibney', 1168: 'Paul Crowder', 1169: 'Rohit Jagessar', 1170: 'Kief Davidson', 1171: 'Ti West', 1172: 'John Hamburg', 1173: 'Craig Mazin', 1174: 'Eric Nicholas', 1175: 'Hal Haberman', 1176: 'Amat Escalante', 1177: 'Katherine Brooks', 1178: 'Kevin Hamedani', 1179: 'Mikel Rueda', 1180: 'D. Stevens', 1181: 'Robert Hall', 1182: 'Jonathan Meyers', 1183: 'Ralph Nelson', 1184: 'Sanjay Rawal', 1185: 'Cristian Mungiu', 1186: 'Brian Dorton', 1187: 'Jamie Babbit', 1188: 'Ryan Coogler', 1189: 'Jamie Travis', 1190: 'Jorge Gaggero', 1191: 'Catherine Jelski', 1192: 'Tommy Wirkola', 1193: 'Ryan Little', 1194: 'Matt Maiellaro', 1195: 'Ben Wheatley', 1196: 'Oliver Blackburn', 1197: 'Christopher Hutson', 1198: 'Steve James', 1199: 'David LaChapelle', 1200: 'Emily Dell', 1201: 'Randy Moore', 1202: 'Chris Atkins', 1203: 'Ryan Smith', 1204: 'Daniel Myrick', 1205: 'Michael Wadleigh', 1206: 'John Landis', 1207: 'Scott Ziehl', 1208: 'Richard Montoya', 1209: 'William Gazecki', 1210: 'Lance McDaniel', 1211: 'Michael Walker', 1212: 'U. Roberto Romano', 1213: 'Alex Kendrick', 1214: 'Joe Camp', 1215: "John 'Bud' Cardos", 1216: 'Tom McCarthy', 1217: 'Patrick Creadon', 1218: 'Kurt Hale', 1219: 'Greg Harrison', 1220: 'Jacob Aaron Estes', 1221: 'Steve Buscemi', 1222: 'Molly Bernstein', 1223: 'Tom DiCillo', 1224: 'Justin Lin', 1225: 'Quentin Dupieux', 1226: 'Gareth Edwards', 1227: 'Stephen Kijak', 1228: 'Andrew Niccol', 1229: 'Daston Kalili', 1230: 'Patrick Gilles', 1231: 'Georgia Hilton', 1232: 'Warren Sheppard', 1233: 'Justin Paul Miller', 1234: 'Michael Herz', 1235: 'Hans Canosa', 1236: 'Lloyd Kaufman', 1237: 'Joe Kenemore', 1238: 'Eric England', 1239: 'Jared Hess', 1240: 'Stacy Peralta', 1241: 'Ray Griggs', 1242: 'Lucio Fulci', 1243: 'Paul Fox', 1244: 'Ari Kirschenbaum', 1245: 'Cassandra Nicolaou', 1246: 'Ingmar Bergman', 1247: 'Franck Khalfoun', 1248: 'Mor Loushy', 1249: 'Sam Firstenberg', 1250: 'Paul Fierlinger', 1251: 'Yorgos Lanthimos', 1252: 'Lauren Lazin', 1253: 'Gregory Widen', 1254: 'Niall Johnson', 1255: 'Eric Mendelsohn', 1256: 'Pan Nalin', 1257: 'Jesse Peretz', 1258: "Eddie O'Flaherty", 1259: 'Babar Ahmed', 1260: 'John D. Hancock', 1261: 'Paul Bartel', 1262: 'Pece Dingo', 1263: '\xed\x8atienne Faure', 1264: 'Herb Freed', 1265: 'Craig Zobel', 1266: 'Maria Maggenti', 1267: 'Miguel Arteta', 1268: 'Daniel Columbie', 1269: 'Bill Plympton', 1270: 'Al Franklin', 1271: 'Stuart Hazeldine', 1272: 'Hilary Brougher', 1273: 'Rachel Goldenberg', 1274: 'Jamin Winans', 1275: 'Matt Cimber', 1276: 'Kristin Rizzo', 1277: 'Ward Roberts', 1278: "James O'Brien", 1279: 'Tom Putnam', 1280: 'Al Silliman Jr.', 1281: 'Eug\xed\xc2ne Louri\xed\xa9', 1282: 'Maurizio Benazzo', 1283: 'Sherman Alexie', 1284: 'Stevan Mena', 1285: 'Eric Valette', 1286: 'Jay Duplass', 1287: 'Livingston Oden', 1288: 'Chris Marker', 1289: 'Carl Theodor Dreyer', 1290: 'Marianna Palka', 1291: 'Richard Schenkman', 1292: 'Ricki Stern', 1293: 'C. Fraser Press', 1294: 'Rania Attieh', 1295: 'Majid Majidi', 1296: 'Andrew Haigh', 1297: 'Cary Bell', 1298: 'John Carney', 1299: 'Robinson Devor', 1300: 'Michel Orion Scott', 1301: 'Pat Holden', 1302: 'Eric Bugbee', 1303: 'Bill Melendez', 1304: 'Dena Seidel', 1305: 'Deborah Anderson', 1306: 'Sara Newens', 1307: 'Sai Varadan', 1308: 'Zal Batmanglij', 1309: 'Jean-Luc Godard', 1310: 'Nathan Smith Jones', 1311: 'Travis Cluff', 1312: 'Stephen Langford', 1313: 'Lisanne Pajot', 1314: 'Jason Miller', 1315: 'Myles Berkowitz', 1316: 'Brett Piper', 1317: 'Brandon Trost', 1318: 'Daniel Schechter', 1319: 'Edward Burns', 1320: 'Matt Johnson', 1321: 'Bruno Barreto', 1322: 'Lena Dunham', 1323: 'Terron R. Parsons', 1324: 'Daniel Mellitz', 1325: 'Jem Cohen', 1326: 'Andrew Leman', 1327: 'Dave Carroll', 1328: 'William Eubank', 1329: 'Chad Hartigan', 1330: 'Kirk Loudon', 1331: 'Travis Legge', 1332: 'Collin Joseph Neal', 1333: 'Bradley Rust Gray', 1334: 'Mike Bruce', 1335: 'Andrew Bujalski', 1336: 'Damir Catic', 1337: 'Neil LaBute', 1338: 'Eric Eason', 1339: 'Marcus Nispel', 1340: 'Brandon Landers', 1341: 'Jim Chuchu', 1342: 'Jason Trost', 1343: 'Jafar Panahi', 1344: 'Ivan Kavanagh', 1345: 'Kiyoshi Kurosawa', 1346: 'Shane Carruth', 1347: 'Neill Dela Llana', 1348: 'Anthony Vallone', 1349: 'Benjamin Roberds', 1350: 'Jon Gunn', 1351: 'Nathan Greno', 1352: 'Rich Moore', 1353: 'James Bobin', 1354: 'Dean Parisot', 1355: 'Hironobu Sakaguchi', 1356: 'Eric Leighton', 1357: 'Matt Birch', 1358: 'Mark Steven Johnson', 1359: 'George Lucas', 1360: 'Fr\xed\xa9d\xed\xa9ric Forestier', 1361: 'Rob Letterman', 1362: 'Bo Welch', 1363: 'Dominic Sena', 1364: 'Ericson Core', 1365: 'Wally Pfister', 1366: 'Daniel Espinosa', 1367: 'Kevin Lima', 1368: 'Sarah Smith', 1369: 'Peter Segal', 1370: 'Nancy Meyers', 1371: 'Les Mayfield', 1372: 'Joe Pytka', 1373: 'Vincent Ward', 1374: 'Antony Hoffman', 1375: 'Judd Apatow', 1376: 'Gary Shore', 1377: 'M\xed\xabns M\xed\xabrlind', 1378: 'Wych Kaosayananda', 1379: 'Joseph Ruben', 1380: 'Scott Waugh', 1381: 'Nora Ephron', 1382: 'Keenen Ivory Wayans', 1383: 'Geoff Murphy', 1384: 'Griffin Dunne', 1385: 'Jorge Blanco', 1386: 'Joel Coen', 1387: 'Harold Becker', 1388: 'Tony Bill', 1389: 'Frank Miller', 1390: 'Pou-Soi Cheang', 1391: 'Peter MacDonald', 1392: 'Kevin Bray', 1393: 'Mike Gabriel', 1394: 'Jimmy Hayward', 1395: 'Shekhar Kapur', 1396: 'Steve Antin', 1397: 'Jim Gillespie', 1398: 'Peyton Reed', 1399: 'Phyllida Lloyd', 1400: 'Joe Roth', 1401: 'Bennett Miller', 1402: 'Angela Robinson', 1403: 'Jorge R. Guti\xed\xa9rrez', 1404: 'Richard Loncraine', 1405: 'Howard Deutch', 1406: 'David Dobkin', 1407: 'Alexander Witt', 1408: 'Beeban Kidron', 1409: 'Steven Seagal', 1410: 'Garry Marshall', 1411: 'Patrick Read Johnson', 1412: 'Penny Marshall', 1413: 'Ted Kotcheff', 1414: 'P.J. Hogan', 1415: 'Brad Furman', 1416: 'Donald Petrie', 1417: 'Stephen Norrington', 1418: 'Jesse Dylan', 1419: 'Joel Zwick', 1420: 'Peter Howitt', 1421: 'John Gray', 1422: 'Danny Pang', 1423: 'Oliver Parker', 1424: 'Ben Affleck', 1425: 'Reginald Hudlin', 1426: 'Carl Franklin', 1427: 'John Herzfeld', 1428: 'Julie Anne Robinson', 1429: 'Sngmoo Lee', 1430: 'Gordon Chan', 1431: 'Kelly Makin', 1432: "Pat O'Connor", 1433: 'Ulu Grosbard', 1434: 'Marc F. Adler', 1435: 'S.S. Rajamouli', 1436: 'Chris Rock', 1437: 'Michael Tollin', 1438: 'Patrick Tatopoulos', 1439: 'John Moore', 1440: 'Gil Junger', 1441: 'Michael Ritchie', 1442: 'Steven E. de Souza', 1443: 'Mike Hodges', 1444: 'Scott Mann', 1445: "Tommy O'Haver", 1446: 'Roger Kumble', 1447: 'Kimble Rendall', 1448: 'Peter Yates', 1449: 'Lexi Alexander', 1450: 'Bille August', 1451: 'Jean-Paul Rappeneau', 1452: 'Justin Chadwick', 1453: 'Jonathan Hensleigh', 1454: 'John Gatins', 1455: 'Forest Whitaker', 1456: 'Ted Demme', 1457: 'William Shatner', 1458: 'Richard LaGravenese', 1459: 'James Gartner', 1460: 'Lee Toland Krieger', 1461: 'Paul Michael Glaser', 1462: 'Phil Joanou', 1463: 'Martha Coolidge', 1464: 'Ivan Reitman', 1465: 'Nick Hurran', 1466: 'Kurt Wimmer', 1467: 'Jean-Fran\xed_ois Richet', 1468: 'Kevin Hooks', 1469: 'Ellory Elkayem', 1470: 'Jon Avnet', 1471: 'Willard Huyck', 1472: 'Nick Hamm', 1473: 'Steve Boyum', 1474: 'Maksim Fadeev', 1475: 'David Wain', 1476: 'Matthew Vaughn', 1477: 'Agust\xed_n D\xed_az Yanes', 1478: 'Michael Cristofer', 1479: 'Alan Shapiro', 1480: 'Oleg Stepchenko', 1481: 'Chris Nahon', 1482: 'Fred Wolf', 1483: 'Mark Helfrich', 1484: 'Bob Spiers', 1485: 'Troy Nixey', 1486: 'Paul Feig', 1487: 'Richard Kelly', 1488: 'John Schlesinger', 1489: 'Ringo Lam', 1490: 'Bruce McCulloch', 1491: 'Craig R. Baxley', 1492: 'John Guillermin', 1493: 'Bonnie Hunt', 1494: 'Kevin Spacey', 1495: 'Jon Cassar', 1496: 'Luke Greenfield', 1497: 'Christopher Spencer', 1498: 'Daniel Sackheim', 1499: 'Uli Edel', 1500: 'Laurence Dunmore', 1501: 'Rowan Joffe', 1502: 'Laurent Tirard', 1503: 'Katt Shea', 1504: 'Joshua Michael Stern', 1505: 'Tomas Alfredson', 1506: 'John Duigan', 1507: 'Robin Budd', 1508: 'Kevin Rodney Sullivan', 1509: 'Anton Corbijn', 1510: 'Gregory Nava', 1511: 'Jim Field Smith', 1512: 'Stephen Chow', 1513: 'Peter Hastings', 1514: 'Mark Mylod', 1515: 'John Wells', 1516: 'John Hillcoat', 1517: 'Mike Barker', 1518: 'Britt Allcroft', 1519: 'Alan Yuen', 1520: 'Brian Percival', 1521: 'Sean Anders', 1522: 'Leonard Nimoy', 1523: 'Vic Armstrong', 1524: 'Audrey Wells', 1525: 'Jody Hill', 1526: 'Jeff Kanew', 1527: 'Gregor Jordan', 1528: 'Cory Edwards', 1529: 'Terry George', 1530: 'Xavier Gens', 1531: 'George Cukor', 1532: 'John Hoffman', 1533: 'Daniel Barnz', 1534: 'Andrea Di Stefano', 1535: 'Todd Lincoln', 1536: 'Howard Zieff', 1537: 'Christian E. Christiansen', 1538: 'Peter Flinth', 1539: 'Lance Rivera', 1540: 'Susanne Bier', 1541: 'Kenneth Johnson', 1542: 'Vicente Amorim', 1543: 'Tommy Lee Jones', 1544: 'G\xed\xa9rard Krawczyk', 1545: 'Udayan Prasad', 1546: 'Morten Tyldum', 1547: 'Andr\xed\xa9s Muschietti', 1548: 'Jim Fall', 1549: 'Ric Roman Waugh', 1550: 'Juan Carlos Fresnadillo', 1551: 'George Armitage', 1552: 'John Bonito', 1553: 'Stephan Elliott', 1554: 'Tom Green', 1555: 'Drew Barrymore', 1556: 'Brian Koppelman', 1557: 'Mark Piznarski', 1558: 'Dan Curtis', 1559: 'Martin McDonagh', 1560: 'Vicky Jenson', 1561: 'Fritz Lang', 1562: 'Hsiao-Hsien Hou', 1563: 'Jake Paltrow', 1564: 'Juraj Jakubisko', 1565: 'Julien Temple', 1566: 'John Cornell', 1567: 'James Isaac', 1568: 'Josh Schwartz', 1569: 'Julian Schnabel', 1570: 'Tony Goldwyn', 1571: 'Amy Heckerling', 1572: 'Ed Decter', 1573: 'Chris Koch', 1574: 'Bronwen Hughes', 1575: 'Jez Butterworth', 1576: 'Patrice Leconte', 1577: 'Jon Hess', 1578: 'John H. Lee', 1579: 'Benedek Fliegauf', 1580: 'James Foley', 1581: 'Ethan Maniquis', 1582: 'David Moreau', 1583: 'Mike Binder', 1584: 'Ernest R. Dickerson', 1585: 'Sanaa Hamri', 1586: 'Richard Curtis', 1587: 'Nicholas Jarecki', 1588: 'Alan Rudolph', 1589: 'Yimou Zhang', 1590: 'Timothy Hines', 1591: 'Mabel Cheung', 1592: 'Dan Mazer', 1593: 'Jonathan Lynn', 1594: 'Rob Pritts', 1595: 'John Crowley', 1596: 'Philip Saville', 1597: 'William A. Graham', 1598: 'Lisa Azuelos', 1599: 'Dean Wright', 1600: 'Rowdy Herrington', 1601: 'Jamie Blanks', 1602: 'Leon Ichaso', 1603: 'Patricia Rozema', 1604: 'Rob Schmidt', 1605: 'Simon Curtis', 1606: 'Joel Edgerton', 1607: 'Scott Kalvert', 1608: 'Luca Guadagnino', 1609: 'Peter Medak', 1610: 'Tom Brady', 1611: 'Jason Zada', 1612: 'Ariel Vromen', 1613: 'Richard Kwietniowski', 1614: 'Bigas Luna', 1615: 'Bobcat Goldthwait', 1616: 'Rafa Lara', 1617: 'Katherine Dieckmann', 1618: 'Kari Skogland', 1619: 'William Phillips', 1620: 'Sarik Andreasyan', 1621: 'Pedro Almod\xed_var', 1622: 'Kris Isacsson', 1623: 'Daniel Taplitz', 1624: 'Dario Argento', 1625: 'Eric Lavaine', 1626: 'Ole Christian Madsen', 1627: 'Andr\xed\xa9 T\xed\xa9chin\xed\xa9', 1628: 'Emily Young', 1629: 'Peter Faiman', 1630: 'Ma\xed\xbfwenn', 1631: 'Vondie Curtis-Hall', 1632: 'Ken Loach', 1633: 'Dan Gilroy', 1634: 'Jonathan Dayton', 1635: 'Masayuki Ochiai', 1636: 'Ken Shapiro', 1637: 'Jonas Elmer', 1638: 'Mary Harron', 1639: 'Will Gluck', 1640: 'Andrew Currie', 1641: 'Claudia Llosa', 1642: 'Stanley Tong', 1643: 'Russell Holt', 1644: 'Daniel Barber', 1645: 'Michael Anderson', 1646: 'Michael Rymer', 1647: 'Aaron Schneider', 1648: 'Dick Richards', 1649: 'Bob Gosse', 1650: 'Alex Zamm', 1651: 'David Lam', 1652: 'Vladlen Barbe', 1653: 'Max F\xed_rberb\xed_ck', 1654: 'Arie Posin', 1655: 'Mark Tonderai', 1656: 'Luis Valdez', 1657: 'Sammo Kam-Bo Hung', 1658: 'Dominique Othenin-Girard', 1659: 'Brian Klugman', 1660: 'Matt Piedmont', 1661: 'Mark Tarlov', 1662: 'Sheldon Lettich', 1663: 'Greg Marcks', 1664: 'Perry Lang', 1665: 'Jake Goldberger', 1666: 'William Kaufman', 1667: 'Kate Barker-Froyland', 1668: 'Martin Koolhoven', 1669: 'Ashish R. Mohan', 1670: 'Joseph Gordon-Levitt', 1671: 'Aki Kaurism\xed_ki', 1672: 'Michael McGowan', 1673: 'Eugenio Derbez', 1674: 'Henry Koster', 1675: 'Nat Faxon', 1676: 'Maurice Joyce', 1677: 'Robert Duvall', 1678: 'Frank Perry', 1679: 'Richard Glatzer', 1680: 'Bill Duke', 1681: 'Frank Borzage', 1682: 'Jay Levey', 1683: 'Sergio Leone', 1684: 'Dan Rush', 1685: 'Michael Cuesta', 1686: 'Dennis Hopper', 1687: 'Eli Craig', 1688: 'Richard Wallace', 1689: 'William H. Macy', 1690: 'Eric Bross', 1691: 'Stanton Barrett', 1692: 'Jir\xed_ Menzel', 1693: 'Nick Murphy', 1694: 'Michel Leclerc', 1695: 'Analeine Cal y Mayor', 1696: 'Tom Kalin', 1697: 'Mike van Diem', 1698: 'Todd Solondz', 1699: 'Barry Skolnick', 1700: 'Lukas Moodysson', 1701: 'Agnieszka Wojtowicz-Vosloo', 1702: 'Raja Menon', 1703: 'Lisa Cholodenko', 1704: 'DJ Pooh', 1705: 'Wayne Kramer', 1706: 'Steven Shainberg', 1707: 'Rick de Oliveira', 1708: 'Gavin Wiesen', 1709: 'Robert Lee King', 1710: 'Kevin Allen', 1711: 'Sam Miller', 1712: 'Fernando Le\xed_n de Aranoa', 1713: 'Jim Mickle', 1714: 'Julian Gilbey', 1715: 'Howard Hughes', 1716: 'Sean Byrne', 1717: 'Bruce Macdonald', 1718: 'Andrucha Waddington', 1719: 'Gideon Raff', 1720: 'Antonio Simoncini', 1721: 'Eldar Rapaport', 1722: 'John Ford', 1723: 'David Raynr', 1724: 'Christopher Leitch', 1725: 'Patricia Cardoso', 1726: 'Peter M. Cohen', 1727: 'Mel Stuart', 1728: 'George Gallo', 1729: 'Matthew Bright', 1730: 'Kate Connor', 1731: 'Jason Alexander', 1732: 'Will Canon', 1733: 'Philip Zlotorynski', 1734: 'Lance Kawas', 1735: 'Monte Hellman', 1736: 'Isaac Florentine', 1737: 'Leon Ford', 1738: 'Victor Nunez', 1739: 'Hao Ning', 1740: 'Tony Giglio', 1741: 'Alison Maclean', 1742: 'Sarah Gavron', 1743: 'Isabel Coixet', 1744: 'James Ponsoldt', 1745: 'Michael D. Sellers', 1746: 'Danny Perez', 1747: 'Jaco Booyens', 1748: "Anthony O'Brien", 1749: 'Chia-Liang Liu', 1750: 'Robert Rossen', 1751: 'Jim Jarmusch', 1752: 'Kevin Tenney', 1753: 'Gary Rogers', 1754: 'Kelly Reichardt', 1755: 'Bob Giraldi', 1756: 'Mitchell Lichtenstein', 1757: 'Lance Mungia', 1758: 'Michael Dowse', 1759: 'Hue Rhodes', 1760: 'Brian Yuzna', 1761: 'Laurie Collyer', 1762: 'John Simpson', 1763: 'Jeff Crook', 1764: 'Orson Welles', 1765: 'Phil Morrison', 1766: 'Tanner Beard', 1767: 'Derick Martini', 1768: 'Richard Ayoade', 1769: 'Maggie Greenwald', 1770: 'Morgan Spurlock', 1771: 'Lucky McKee', 1772: 'Adrienne Shelly', 1773: 'Newt Arnold', 1774: 'Charles Herman-Wurmfeld', 1775: 'Rebecca Miller', 1776: 'Simeon Rice', 1777: 'Qasim Basir', 1778: 'Charles Chaplin', 1779: 'Pete Jones', 1780: 'Bruce Campbell', 1781: 'Jaime Zevallos', 1782: 'Tara Subkoff', 1783: 'William Cottrell', 1784: 'Leslie H. Martinson', 1785: 'Sadyk Sher-Niyaz', 1786: 'Jonathan Kesselman', 1787: 'Tyler Oliver', 1788: 'Walter Lang', 1789: 'Anna Muylaert', 1790: 'Laurent Bouhnik', 1791: 'David Caffrey', 1792: 'Ossie Davis', 1793: 'Dylan Bank', 1794: 'Guy Maddin', 1795: 'Panos Cosmatos', 1796: 'Matthew R. Anderson', 1797: 'Shimit Amin', 1798: 'Douglas Trumbull', 1799: 'Mona Fastvold', 1800: 'Robert D. Webb', 1801: 'Andrew Erwin', 1802: 'Gillian Robespierre', 1803: 'Courtney Hunt', 1804: 'Greg Berlanti', 1805: 'Jos\xed\xa9 Luis Valenzuela', 1806: 'Joshua Oppenheimer', 1807: 'Anthony Powell', 1808: 'Nick Tomnay', 1809: 'Dan Zukovic', 1810: 'Becky Smith', 1811: 'Benjamin Dickinson', 1812: 'David Cross', 1813: 'Guy Hamilton', 1814: 'David DeCoteau', 1815: 'Stefan C. Schaefer', 1816: 'Katie Aselton', 1817: 'Blair Erickson', 1818: 'Allison Burnett', 1819: 'Maryam Keshavarz', 1820: 'Mariette Monpierre', 1821: 'Rich Christiano', 1822: "Natalie Bible'", 1823: 'Justin Molotnikov', 1824: 'Georg Wilhelm Pabst', 1825: 'Michael Burke', 1826: 'Clark Baker', 1827: 'Bill Benenson', 1828: 'Amy Holden Jones', 1829: 'Brian Baugh', 1830: 'Siddiq Barmak', 1831: 'Joseph Dorman', 1832: 'Eric Schaeffer', 1833: 'Marius A. Markevicius', 1834: 'Fernando Baez Mella', 1835: 'Catherine Gund', 1836: 'Matthew Watts', 1837: 'Whit Stillman', 1838: 'D.W. Griffith', 1839: 'Roger Nygard', 1840: 'Henry Alex Rubin', 1841: 'Florence Ayisi', 1842: 'Michael Roemer', 1843: 'Emma-Kate Croghan', 1844: 'Drake Doremus', 1845: 'Michael Kang', 1846: 'Corbin Bernsen', 1847: 'Andrew Hyatt', 1848: 'Jon Shear', 1849: 'Lowell Sherman', 1850: 'Nadia Tass', 1851: 'Sharon Greytak', 1852: 'Nicolae Constantin Tanase', 1853: 'Melvin Van Peebles', 1854: 'Amal Al-Agroobi', 1855: 'Andrew Berends', 1856: 'Nate Parker', 1857: 'Harry F. Millarde', 1858: 'Robert Townsend', 1859: 'Larry Blamire', 1860: 'Dan Reed', 1861: 'Laslo Benedek', 1862: 'Julie Davis', 1863: 'Joseph Green', 1864: 'James Bidgood', 1865: 'Ash Baron-Cohen', 1866: 'David Yates', 1867: 'Robert Stromberg', 1868: 'Carl Rinsch', 1869: 'Alan Taylor', 1870: 'Cedric Nicolas-Troyan', 1871: 'Adam McKay', 1872: 'Seth Gordon', 1873: 'Gary McKendry', 1874: 'Kerry Conran', 1875: 'Demian Lichtenstein', 1876: 'Josh Gordon', 1877: 'Brenda Chapman', 1878: 'Marc Lawrence', 1879: 'Kevin Donovan', 1880: 'Karey Kirkpatrick', 1881: 'George Nolfi', 1882: 'Costa-Gavras', 1883: 'Joseph L. Mankiewicz', 1884: 'Etan Cohen', 1885: 'Cal Brunker', 1886: 'Paul Weiland', 1887: 'Joan Chen', 1888: 'Elaine May', 1889: 'Peter Ho-Sun Chan', 1890: 'Charles S. Dutton', 1891: 'David Leland', 1892: 'Gary David Goldberg', 1893: 'Joachim R\xed\x9fnning', 1894: 'Ken Scott', 1895: 'Tom Vaughan', 1896: 'Michael McCullers', 1897: 'Richard J. Lewis', 1898: 'Janusz Kaminski', 1899: 'Paul Weitz', 1900: 'Michael Cohn', 1901: 'Tim Fywell', 1902: 'Steve Barron', 1903: 'Pascal Chaumeil', 1904: 'Giuseppe Tornatore', 1905: 'Ben Stassen', 1906: 'Jonathan English', 1907: 'Sergey Bondarchuk', 1908: 'Jerry Zaks', 1909: 'Fred Durst', 1910: 'Susanna White', 1911: 'Colin Higgins', 1912: 'Penelope Spheeris', 1913: 'James Mather', 1914: 'Damon Santostefano', 1915: 'David Zucker', 1916: 'Andrew Jarecki', 1917: 'Mark Rosman', 1918: 'Anand Tucker', 1919: 'Rick Friedberg', 1920: 'Istv\xed\xe7n Szab\xed_', 1921: 'Hal Needham', 1922: 'Jonathan Teplitzky', 1923: 'Mike Marvin', 1924: 'Lance Hool', 1925: 'David Hayter', 1926: 'John Fortenberry', 1927: 'Trent Cooper', 1928: 'Peter Farrelly', 1929: 'Perry Andelin Blake', 1930: 'Dany Boon', 1931: 'JK Youn', 1932: 'David Ayer', 1933: 'Matt Williams', 1934: 'Elizabeth Allen Rosenbaum', 1935: 'John Ottman', 1936: 'Peter Atencio', 1937: 'Albert Brooks', 1938: 'Peter Kassovitz', 1939: 'Shane Black', 1940: 'Darrell Roodt', 1941: 'Gilles Paquet-Brenner', 1942: 'Peter Cousens', 1943: 'John Blanchard', 1944: 'Chao-Bin Su', 1945: 'Danny Leiner', 1946: 'Gene Quintano', 1947: 'Mark Brown', 1948: 'John Stockwell', 1949: 'Stephen Chbosky', 1950: 'Stewart Hendler', 1951: 'John Cromwell', 1952: 'Gillian Armstrong', 1953: 'Je-kyu Kang', 1954: 'Jon Hurwitz', 1955: 'Jake Schreier', 1956: 'Lionel C. Martin', 1957: 'Robert Iscove', 1958: 'Paolo Sorrentino', 1959: 'Jamie Thraves', 1960: 'Tim Blake Nelson', 1961: 'Ray Lawrence', 1962: 'Karan Johar', 1963: 'Floyd Mutrux', 1964: 'Bob Dolman', 1965: 'Greg Coolidge', 1966: 'Robert Ben Garant', 1967: 'Lorene Scafaria', 1968: 'John Waters', 1969: 'Dan Harris', 1970: 'Mel Smith', 1971: 'Michael Meredith', 1972: 'Julio DePietro', 1973: 'Vic Sarin', 1974: 'Floria Sigismondi', 1975: 'Roland Suso Richter', 1976: 'Roger Vadim', 1977: 'Nils Gaup', 1978: 'Vipul Amrutlal Shah', 1979: 'Ayan Mukerji', 1980: 'Martin Lawrence', 1981: 'Peter R. Hunt', 1982: 'John Schultz', 1983: 'Erik Canuel', 1984: 'David Jacobson', 1985: 'Edward Hall', 1986: 'Keith Gordon', 1987: 'James Nunn', 1988: 'David Webb Peoples', 1989: 'Charles Robert Carner', 1990: 'Tom Ford', 1991: 'Mitch Davis', 1992: 'Tim Chambers', 1993: 'Stephen Milburn Anderson', 1994: 'Alan Alda', 1995: 'Sterling Van Wagenen', 1996: 'Wolfgang Becker', 1997: 'Robert Stevenson', 1998: 'Fred Savage', 1999: 'Zach Cregger', 2000: 'Michael Crichton', 2001: 'Sylvio Tabet', 2002: 'Rick Bieber', 2003: 'Christopher M. Bessette', 2004: 'Gary Sinyor', 2005: 'Liv Ullmann', 2006: 'Patty Jenkins', 2007: 'Bruce Malmuth', 2008: 'Denys Arcand', 2009: 'Barrett Esposito', 2010: 'Mike Mayhall', 2011: 'Scott Foley', 2012: 'Shekar', 2013: 'Leonard Farlinger', 2014: 'Ren\xed\xa9 F\xed\xa9ret', 2015: 'Henry Hobson', 2016: 'Billy Wilder', 2017: 'Michael Tiddes', 2018: 'Karim A\xed\xbfnouz', 2019: 'Mark Griffiths', 2020: 'Dagur K\xed\xe7ri', 2021: 'Michael Martin', 2022: 'Mark Young', 2023: 'Justin Kerrigan', 2024: 'John Maclean', 2025: 'Jill Sprecher', 2026: 'Enrique Begne', 2027: 'Bobby Roth', 2028: 'Francesca Gregorini', 2029: 'Darin Scott', 2030: "Chris D'Arienzo", 2031: 'Rohit Jugraj', 2032: 'Frank Sebastiano', 2033: 'Joe Cross', 2034: 'James Dodson', 2035: 'John Murlowski', 2036: 'Jason Stone', 2037: 'Hayley Cloake', 2038: 'Shyam Madiraju', 2039: 'Debra Granik', 2040: 'Henry King', 2041: 'David Duchovny', 2042: 'Kundan Shah', 2043: 'Hunter Richards', 2044: 'Ralph Ziman', 2045: 'Paul Bunnell', 2046: 'Tim Hunter', 2047: 'Vijay Chandar', 2048: 'Ritesh Batra', 2049: 'Adam Goldberg', 2050: 'David Ray', 2051: 'Dave Rodriguez', 2052: 'Nae Caranfil', 2053: 'Edward Dmytryk', 2054: 'Ham Tran', 2055: 'Rich Cowan', 2056: 'Arjun Sablok', 2057: 'David Boyd', 2058: 'Justin Thomas Ostensen', 2059: 'Regardt van den Bergh', 2060: 'Duncan Tucker', 2061: 'Craig Johnson', 2062: 'Goran Dukic', 2063: 'Efram Potelle', 2064: 'Nickolas Perry', 2065: 'A. Raven Cruz', 2066: 'Randall Rubin', 2067: 'Mary Pat Kelly', 2068: 'Robert Heath', 2069: 'Jeffrey St. Jules', 2070: 'K. King', 2071: 'Ramaa Mosley', 2072: 'C. Jay Cox', 2073: 'Nick Love', 2074: 'Asghar Farhadi', 2075: 'Daniel Davila', 2076: 'Ryan Fleck', 2077: 'Christopher Scott Cherot', 2078: 'Anna Mastro', 2079: 'Mark Sandrich', 2080: 'Thomas Lilti', 2081: 'Marilyn Agrelo', 2082: 'Alex Smith', 2083: 'Sol Tryon', 2084: 'Michael Hoffman Jr.', 2085: 'Joel Paul Reisig', 2086: 'Luke Dye', 2087: 'Lloyd Bacon', 2088: 'Sue Corcoran', 2089: 'Doug Block', 2090: 'Chad Kapper', 2091: 'Jack Perez', 2092: 'Ken Del Conte', 2093: 'Piyush Dinker Pandya', 2094: 'Allison Anders', 2095: 'Tom Seidman', 2096: 'Sam Martin', 2097: 'Lynn Shelton', 2098: 'Valentine', 2099: 'David Hewlett', 2100: 'Jamaa Fanaka', 2101: 'Patrick Ryan Sims', 2102: 'Wade Gasque', 2103: 'Joseph Mazzella', 2104: 'Daryl Wein', 2105: 'Tadeo Garcia', 2106: 'Scott Smith', 2107: 'Lee Unkrich', 2108: 'Tom McGrath', 2109: 'Daniel Lee', 2110: 'Babak Najafi', 2111: 'Graham Annable', 2112: 'Ruben Fleischer', 2113: 'Harald Zwart', 2114: 'Kent Alterman', 2115: 'Paul Hunter', 2116: 'Paul Bolger', 2117: 'Susan Stroman', 2118: 'Diane Keaton', 2119: 'David Mirkin', 2120: 'Jennifer Flackett', 2121: 'Allen Hughes', 2122: 'Chris Roberts', 2123: 'Olivier Dahan', 2124: 'Edward Norton', 2125: 'Saul Dibb', 2126: 'Sharon Maguire', 2127: 'Gabor Csupo', 2128: 'Nigel Cole', 2129: 'Dexter Fletcher', 2130: 'Jeremy Leven', 2131: 'Marcos Siega', 2132: 'Mary McGuckian', 2133: 'Callie Khouri', 2134: 'Joshua Logan', 2135: 'John McNaughton', 2136: 'Jessica Bendinger', 2137: 'Todd Graff', 2138: 'Mabrouk El Mechri', 2139: 'Daniel Algrant', 2140: 'Scott Walker', 2141: 'Ricky Gervais', 2142: 'Nicholas Ray', 2143: 'Jesse Vaughan', 2144: 'Phil Traill', 2145: 'David Nutter', 2146: 'RZA', 2147: 'Gregory Jacobs', 2148: 'Theodore Melfi', 2149: 'Craig Bolotin', 2150: 'Paul Mazursky', 2151: 'Abel Ferrara', 2152: 'Wallace Wolodarsky', 2153: 'Darnell Martin', 2154: 'R.J. Cutler', 2155: 'David S. Ward', 2156: 'Shintaro Shimosawa', 2157: 'Ken Annakin', 2158: 'Jim Hanon', 2159: 'Jorma Taccone', 2160: 'Fran\xed_ois Girard', 2161: 'Joshua Seftel', 2162: 'Jake Scott', 2163: 'Ben Younger', 2164: 'Linda Mendoza', 2165: 'Hart Bochner', 2166: 'Chatrichalerm Yukol', 2167: 'Marc Forby', 2168: 'Serdar Akar', 2169: 'Tom Gormican', 2170: 'Anna Boden', 2171: 'Michael Corrente', 2172: 'Sacha Bennett', 2173: 'Rodrigo Garc\xed_a', 2174: 'Jeta Amata', 2175: 'Siddharth Anand', 2176: "Thaddeus O'Sullivan", 2177: 'Richard E. Grant', 2178: 'Jackie Earle Haley', 2179: 'David Atkins', 2180: 'James Toback', 2181: 'Morgan J. Freeman', 2182: 'Vicky Jewson', 2183: 'Fatih Akin', 2184: 'Carlos Saura', 2185: 'Peter DeLuise', 2186: 'Jeff Franklin', 2187: 'Stefan Schwartz', 2188: 'Ruba Nadda', 2189: 'Alan Jacobs', 2190: 'Kevin Carraway', 2191: 'Robert Cary', 2192: 'Benny Boom', 2193: 'Darren Stein', 2194: 'Leslye Headland', 2195: 'Tim Heidecker', 2196: 'Marcio Garcia', 2197: 'Michael Jai White', 2198: 'Brian Caunter', 2199: 'Zach Braff', 2200: 'Harmage Singh Kalirai', 2201: 'Chris Eyre', 2202: 'Marielle Heller', 2203: 'Noah Buschel', 2204: 'Phil Claydon', 2205: 'Brad Copeland', 2206: 'Remo', 2207: 'Richard Boddington', 2208: 'Mark Illsley', 2209: 'Llu\xed_s Qu\xed_lez', 2210: 'Alex Cox', 2211: 'Dror Moreh', 2212: 'James Mottern', 2213: 'Gerard Johnstone', 2214: 'Timothy Woodward Jr.', 2215: 'Tom Sanchez', 2216: 'Rob McKittrick', 2217: 'Ben Lewin', 2218: 'Khalid Mohamed', 2219: 'Johnny Remo', 2220: 'Frank Whaley', 2221: 'Lori Petty', 2222: 'H.M. Coakley', 2223: 'Johanna Schwartz', 2224: 'Barry W. Blaustein', 2225: 'Neema Barnette', 2226: 'Jonathan Parker', 2227: 'Jack Heller', 2228: 'Jonathan Caouette', 2229: 'Matt Jackson', 2230: 'Bruce Dellis', 2231: 'Lori Silverbush', 2232: 'Zoran Lisinac', 2233: 'Justin Dillon', 2234: 'James Kerwin', 2235: 'Ken Roht', 2236: 'E.L. Katz', 2237: 'John Reinhardt', 2238: 'Sut Jhally', 2239: 'Joe Swanberg', 2240: 'Michael Patrick King', 2241: 'Kinka Usher', 2242: 'Akiva Schaffer', 2243: 'Evan Goldberg', 2244: 'Charles Shyer', 2245: 'Christian Ditter', 2246: 'Don Scardino', 2247: 'Tom Reeve', 2248: 'John Francis Daley', 2249: 'Corey Yuen', 2250: 'Fr\xed\xa9d\xed\xa9ric Auburtin', 2251: 'Robert B. Weide', 2252: 'Jonathan Newman', 2253: 'Michael Dinner', 2254: 'Todd Strauss-Schulson', 2255: 'Angelo Pizzo', 2256: 'Tom Walsh', 2257: 'Rob Hawk', 2258: 'Brian A Miller', 2259: 'Jason Moore', 2260: 'Diane English', 2261: 'Bryan Barber', 2262: 'Mort Nathan', 2263: 'Tung-Shing Yee', 2264: 'Stephen Carpenter', 2265: 'Steve Pink', 2266: 'Mark Christopher', 2267: 'Peter Care', 2268: 'Dustin Hoffman', 2269: 'Dewey Nicks', 2270: 'Eric Lartigau', 2271: 'Harley Cokeliss', 2272: 'Derrick Borte', 2273: '\xed\x81lex de la Iglesia', 2274: 'Jason Connery', 2275: 'Stewart Raffill', 2276: 'Meiert Avis', 2277: 'Ari Sandel', 2278: 'Andrew Wilson', 2279: 'Gary Hardwick', 2280: 'Harmony Korine', 2281: 'J.S. Cardone', 2282: 'Kabir Sadanand', 2283: 'Mars Callahan', 2284: 'Sam Levinson', 2285: 'Adam Rapp', 2286: 'Jason Eisener', 2287: 'Christian Sesma', 2288: 'Danny Provenzano', 2289: 'Romesh Sharma', 2290: 'Robert Bennett', 2291: 'Tommy Oliver', 2292: 'Shane Dawson', 2293: 'Jennifer Wynne Farmer', 2294: 'Gene Teigland', 2295: 'Jeff Schaffer', 2296: 'David Palmer', 2297: 'Rick Rosenthal', 2298: 'Dito Montiel', 2299: 'Kirk Wong', 2300: 'Christopher Erskin', 2301: 'Cheryl Dunye', 2302: 'Fred Schepisi', 2303: 'Jon Poll', 2304: 'Sajid Khan', 2305: 'Neal Brennan', 2306: 'Jim Issa', 2307: 'Ekachai Uekrongtham', 2308: 'Robert Moresco', 2309: 'Adam Brooks', 2310: 'Robert C. Cooper', 2311: 'Risa Bramon Garcia', 2312: 'George Ratliff', 2313: 'Mickey Liddell', 2314: 'Brian Dannelly', 2315: 'Jennifer Finnigan', 2316: 'Rita Merson', 2317: 'William Wyler', 2318: 'Pascal Arnold', 2319: 'John Laing', 2320: 'David M. Matthews', 2321: 'Vivek Agnihotri', 2322: 'Charlie Levi', 2323: 'Travis Romero', 2324: 'Jason Naumann', 2325: 'Malcolm Goodwin', 2326: 'Kevin Jordan', 2327: 'Daniel Hsia', 2328: 'Marco Schnabel', 2329: 'Peter Billingsley', 2330: 'Asger Leth', 2331: 'Guillaume Canet', 2332: 'George Stevens', 2333: 'Sidney J. Furie', 2334: 'Tina Gordon Chism', 2335: 'Franco Zeffirelli', 2336: 'Joe Cornish', 2337: 'David Winters', 2338: 'Michael Clancy', 2339: 'Keith Parmer', 2340: 'Raymond De Felitta', 2341: 'Preston A. Whitmore II', 2342: 'Jim Amatulli', 2343: 'Gabriela Tagliavini', 2344: 'Beto G\xed_mez', 2345: 'Avi Nesher', 2346: 'Jamal Hill', 2347: 'Giovanni Zelko', 2348: 'Adam Jay Epstein', 2349: 'Scandar Copti', 2350: 'Michael Taliferro', 2351: 'Blaz Zavrsnik', 2352: 'Matt Walsh', 2353: 'Alex Craig Mann', 2354: 'Alec Asten', 2355: 'Jeffrey W. Byrd', 2356: 'Erik White', 2357: 'Ronald Neame', 2358: 'Bo Zenga', 2359: 'Salim Akil', 2360: 'Rachel Perkins', 2361: 'Nathan Frankowski', 2362: 'Laurent Cantet', 2363: 'Tim Boxell', 2364: 'Maggie Carey', 2365: 'Jerome Elston Scott', 2366: 'David G. Evans', 2367: 'Patrick Meaney', 2368: 'Justin Zackham', 2369: 'Elizabeth Banks', 2370: 'Sara Sugarman', 2371: 'Damian Nieman', 2372: 'Ian Fitzgibbon', 2373: 'Susan Seidelman', 2374: 'Jack Conway', 2375: 'Russ Meyer', 2376: 'Kat Coiro', 2377: 'Harry Beaumont', 2378: 'Jessy Terrero', 2379: 'Ferzan Ozpetek', 2380: 'David E. Talbert', 2381: 'Ice Cube', 2382: 'Wajahat Rauf', 2383: 'Jeff Nathanson', 2384: 'James David Pasternak', 2385: 'Harold Cronk', 2386: 'Jeremy Sims', 2387: 'Corey Grant', 2388: 'Patrick Hughes', 2389: 'Marc Bennett', 2390: 'Kay Pollak', 2391: 'Benson Lee', 2392: 'Justin Tipping', 2393: 'Bill Muir', 2394: 'Frank Lotito', 2395: 'Russell Friedenberg', 2396: 'Alex Ranarivelo', 2397: 'Caryn Waechter', 2398: 'Thomas L. Phillips'}


imdb_table_path = 'Data/movie_metadata.csv'

#Column Names
color = 'Color'
director_name = 'Director Name'
num_critic_for_reviews = 'Number Critic For Reviews'
duration = 'Duration'
director_facebook_likes = 'Director Facebook Likes'
actor_3_facebook_likes = 'Actor 3 Facebook Likes'
actor_2_name = 'Actor 2 Name'
actor_1_facebook_likes = 'Actor 1 Facebook Likes'
gross = 'Gross'
genres = 'Genres'
actor_1_name = 'Actor 1 Name'
movie_title = 'Movie Title'
num_voted_users = 'Number Voted Users'
cast_total_facebook_likes = 'Cast Total Facebook Likes'
actor_3_name = 'Actor 3 Name'
facenumber_in_poster = 'Facenumber in Poster'
plot_keywords = 'Plot Keywords'	
movie_imdb_link = 'Movie imdb Link'
num_user_for_reviews = 'Number User for Reviews'
language = 'Language'
country = 'Country'
content_rating = 'Content Rating'
budget = 'Budget'
title_year = 'Title Year'
actor_2_facebook_likes = 'Actor 2 Facebook Likes'
imdb_score = 'Imdb Score'
aspect_ratio = 'Aspect Ratio' 
movie_facebook_likes = 'Movie Facebook Likes'

#column names
feature_list = [color, director_name, num_critic_for_reviews, duration,
						director_facebook_likes, actor_3_facebook_likes, actor_2_name,
						actor_1_facebook_likes, gross, genres, actor_1_name, movie_title,
						num_voted_users, cast_total_facebook_likes, actor_3_name,
						facenumber_in_poster, plot_keywords, movie_imdb_link,
						num_user_for_reviews, language, country, content_rating, budget,
						title_year, actor_2_facebook_likes, imdb_score,	aspect_ratio, 
						movie_facebook_likes]

feature_name_to_number = {color:0, director_name:1, num_critic_for_reviews:2, duration:3,
						director_facebook_likes:4, actor_3_facebook_likes:5, actor_2_name:6,
						actor_1_facebook_likes:7, gross:8, genres:9, actor_1_name:10, movie_title:11,
						num_voted_users:12, cast_total_facebook_likes:13, actor_3_name:14,
						facenumber_in_poster:15, plot_keywords:16, movie_imdb_link:17,
						num_user_for_reviews:18, language:19, country:20, content_rating:21, budget:22,
						title_year:23, actor_2_facebook_likes:24, imdb_score:25, aspect_ratio:26, 
						movie_facebook_likes:27}


#posible labels
posible_labels = [x for x in range(1,11)]

#This is the color on the table
colors_to_numbers = {' Black and White':0, 'Color':1, '':2}

#This is for the purpose of plotting
colors = {1:'black', 2:'lightcoral', 3:'maroon', 4:'orangered', 5:'saddlebrown', 7:'purple', 8:'navy', 9:'skyblue', 6:'green', 10:'yellow'}

#------------------------------Math Tools---------------------------------------

def normalize(l):
	m = 1.0*max(l)
	return list(array(l)/m)
	

#precondition: The 2 vectors have the same dimensions
#This function calculates the dot product of vectors v1 and v2. The same index on v1 and
#v2 represents the same dimension
#v1 is a vector represented as numpy array.
#v2 is a vector represented as numpy array.
#returns a scalar = the value of the dot product
def dot_product(v1, v2):
	dot_product_scalar = 1.0*sum(v1*v2)
	return dot_product_scalar
	
#precondition: The 2 vectors have the same dimensions
#This function calculates the sum of vectors v1 and v2
#v1 is a vector represented as a numpy array.
#v2 is a vector represented as a numpy array.
#returns a vector which is the sum of v1 and v2
def sum_vectors(v1, v2):
	sum_vector = v1 + v2
	return sum_vector

#This function multiplies a vector times a constant
#v is a vector
#c is a constant
#returns a new vector = c*v
def scalar_multiplication(v, c):
	scalar_mult_vector = c*v
	return scalar_mult_vector		

#This function finds the norm of a vector
#v is a vector
#returns the value of the norm of v
def norm(v):
	norm = sqrt(sum(v**2))
	return norm


#applies the sigmoid function to either a constant of a numpy array
def sigmoid_function(x, theta):
	#print x
	#print theta
	return 1.0/(1+e**(-1.0*sum(theta*x)))

'''
def dJ(xs, ys, h, j, thetas):
	der = 0.0
	m = 1.0*len(xs)
	
	
	for i in range(len(xs)):
		x_vect = xs[i]
		h_x_vec = h(x_vect, thetas)
		#print "Evaluation = " + str(h_x_vec)
		der += (h_x_vec - ys[i])*xs[i][j]	

	#print "Derivative = " + str(der)
	return der/m
	
	
def gradient_descent(xs, ys, h, alpha=0.01, iterations=10000):
	thetas = array([0]*len(xs[0]))
	
	for iteration in range(iterations):
		for j in range(len(thetas)):
			#print 'AAAAAA ' + str(alpha*dJ(xs,ys,h,j,thetas))
			thetas[j] = thetas[j] - alpha*dJ(xs,ys,h,j,thetas)
			print thetas[j]
	
	return thetas
'''	

def derivative_J(xs, ys, thetas, j):
	cost = 0.0
	
	for i in range(len(xs)):
		cost += xs[i][j] * (sigmoid_function(xs[i], thetas) - ys[i])
	
	return cost/(1.0 * len(xs))


def gradient_descent(xs, ys, h, alpha, iterations, lamda):
	thetas = array([1.0]*len(xs[0]))
	m = len(xs)
	#print 'Sig =', sigmoid_function(array([-0.25, 0.25]), thetas)
	for it in range(iterations):
		for j in range(len(thetas)):
			thetas[j] = thetas[j] - alpha*(derivative_J(xs, ys, thetas, j)+(lamda/m)*thetas[j])
	return thetas
	
#------------------------------------Ploting Tools----------------------------------
def plot_points(xs, ys, labels, labelX, labelY, filename=None):
	dx = {}
	dy = {}
	for i in range(len(xs)):
		key = (labels[i], colors[labels[i]])
		if key in dx:
			dx[key] = dx[key] + [xs[i]]
			dy[key] = dy[key] + [ys[i]]
		else:
			dx[key] = [xs[i]]
			dy[key] = [ys[i]]
	
	for key in dx:
		plt.scatter(dx[key], dy[key], c=key[1], label=key[0]) 
			
	
	#for i in range(len(xs)):
		#plt.scatter(xs[i],ys[i], c=colors[labels[i]], label=labels[i])
	
	
	plt.legend()
	plt.grid(True)
	plt.xlabel(labelX)
	plt.ylabel(labelY)
	plt.title(labelX + ' vs. ' + labelY)
	
	if filename == None:
		plt.show()
	else:
		plt.savefig(filename+'png')


def plot2D(xs, ys, labelX, labelY):
	plt.plot(xs, ys, 'ro')
	plt.xlabel(labelX)
	plt.ylabel(labelY)
	plt.title(labelX + ' vs. ' + labelY)
	plt.show()

#---------------------------------Managing Files tools--------------------------------
#table_path is the path to the excel_table
#return a Data object with feature vectors and labels included
def read_excel_table(table_path):
	#feature_names = []
	#feature_vectors = []
	#data = Data()
	headers = []
	rows = []
	
	f = open(table_path, 'r')
	
	for line in f:
		line = line.replace('\n', '')
		splited_line = line.split(',')
		splited_line = filter(lambda a: a != '', splited_line)
		splited_line = filter(lambda a: a != '\r', splited_line)
	
		if len(headers) == 0:
			headers = splited_line
		else:
			#feature_vectors.append([float(feature) for feature in splited_line])
			rows.append(splited_line)
	
	f.close()
	
	#data.set_feature_vectors(array(feature_vectors))
	#data.set_feature_names(array(feature_names))
	
	return (headers, rows)
	
	
	
def read_file(filename):
		f = open(filename, 'r')
		file_data = []
		
		
		for line in f:
			#row_dict = {}
			row = []
			splited = line.split(',')
			if len(splited) > 28:
				offset = len(splited) - 28
			else:
				offset = 0
				
			for i in range(len(feature_list)):
				val = splited[i]
				if feature_list[i] == 'Movie Title':
					for iter in range(offset):
						val = ", ".join([val, splited[i+iter+1]])
				elif i > 11:
					val = splited[i + offset]
					if i == (len(feature_list) - 1):
						val = val.split('\r')[0]
			
				#row_dict[self.feature_list[i]] = val
				row.append(val)
		
			#self.file_data.append(row_dict)
			file_data.append(row)
		headers = file_data.pop(0)
		return headers, file_data

def get_imdb_score(rows):
	labels = []
	rating_index = feature_name_to_number[imdb_score]
	for row in rows:
		labels.append(int(round(float(row[rating_index]))))
	return labels
		
def get_colors(rows):
	colors = []
	for row in rows:
		colors.append(colors_to_numbers[row[feature_name_to_number[color]]])
	return color, colors

def get_movie_title(rows):
	ids = []
	
	for row in rows:
		ids.append(row[feature_name_to_number[movie_title]])
	
	return ids

	
def get_int_column(rows, column_name):
	output = []
	output_ne = []
	
	for row in rows:
		strg = row[feature_name_to_number[column_name]]
		if strg == '':
			output.append(strg)
		else:
			output.append(int(strg))
			output_ne.append(int(strg))
	
	avg = sum(output_ne)/len(output_ne)
	
	for i in range(len(output)):
		if output[i] == '':
			output[i] = avg
	
	return column_name, output

def get_num_critic_for_reviews(rows):
	return get_int_column(rows, num_critic_for_reviews)

def get_duration(rows):
	return get_int_column(rows, duration)

def get_director_facebook_likes(rows):
	return get_int_column(rows, director_facebook_likes)
	
def get_num_voted_users(rows):
	return get_int_column(rows, num_voted_users)

def get_cast_total_facebook_likes(rows):
	return get_int_column(rows, cast_total_facebook_likes)

def get_facenumber_in_poster(rows):
	return get_int_column(rows, facenumber_in_poster)

def get_num_user_for_reviews(rows):
	return get_int_column(rows, num_user_for_reviews)

def get_budget(rows):
	return get_int_column(rows, budget)
	
def get_title_year(rows):
	return get_int_column(rows, title_year)

def get_movie_facebook_likes(rows):
	return get_int_column(rows, movie_facebook_likes)

def get_direcrors_numeric(rows):
	directors = {}
	pos = 0
	
	for row in rows:
		director = row[feature_name_to_number[director_name]]
		
		if director not in directors:
			directors[director] = pos
			pos += 1
	
	
	#fliping keys and values
	
	fliped_directors = {}
	
	for director in directors:
		fliped_directors[directors[director]] = director
	
	print fliped_directors
	 
		
