[kattio].

main :-
    repeat,
    read_int(X),
    calcDartScore(X).

/* Calculate - Arbetsh�sten i denna uppgift                                             */
/* F�r den h�r uppgiften �r det viktigt att inse att det finns olike "ranges".          */
/* F�r X = [1, 140] kan vi alltid k�ra standardfallet, att "lyfta" upp X med antingen   */
/* en eller tv� trippel och sen avsluta med en single. Alternativt f�r sm� X kan vi l�sa*/
/* direkt.                                                                              */
/* -------------------------------------------------------------------------------------*/
/* Exempel, X = 68:  trippel 20, singel 8.                                              */
/* Exempel, X = 138: tripple 20, trippel 20, single 18.                                 */

/* F�r X = [141, 157] kan vi inte lyfta upp och avsluta med singel. H�r �r det lite     */
/* sv�rare. Vi m�ste antingen lyfta upp och avsluta med dubbel, eller g�ra konvertering */
/* Konvertering g�rs om X - 120 �r udda, d� f�r vi ist�llet g�ra X - 117 dvs T 20 T 19. */
/* Genom att subtrahera med en udda trippel f�r vi d� en j�mn rest att k�ra dubbel p�.  */
/* -------------------------------------------------------------------------------------*/
/* Exempel: X = 144: trippel 20 trippel 20 double 12.                                   */
/* Exempel(Konvertering till j�mn): X = 143: trippel 20 trippel 19 dubbel 13.           */
/* (Notera att trippel 20 trippel 20 hade gett rest = 23, inte delbart med tv�)         */

/* F�r X = [158 180] kan vi bara kolla delbarhet med 3 vilket g�rs enkelt genom mod 3   */
/* eller genom att se ifall siffersumman �r delbar med 3 (Om man vill g�ra huvudr�kning)*/

calculate(X) :- X < 1.
calculate(X) :- X < 157, X > 140, (X-120) mod 2 > 0, (X-120) mod 3 > 0, nl, X1 is (X-57), write("triple 19"), nl, calculate(X1).
calculate(X) :- X > 60, X1 is (X-60), write("triple 20"), nl, calculate(X1).
calculate(X) :- X =< 60, X mod 3 < 1, X1 is X/3, write("triple "), write(X1).
calculate(X) :- X > 40, X1 is (X-40), write("double 20"), nl, calculate(X1).
calculate(X) :- X > 20, X =< 40, X mod 2 < 1, X1 is (X/2),  write("double "), write(X1).
calculate(X) :- X > 20, X =< 60, X1 is (X-20), write("single 20"), nl, calculate(X1).
calculate(X) :- X =< 20, write("single "), write(X).

impossible(X) :- X > 140, (X - 120) mod 3 > 0, (X - 117) mod 2 > 0, write("impossible").
impossible(X) :- X > 160, (X - 120) mod 3 > 0, write("impossible").

possible(X, Z) :- (\+impossible(X)),
    calculate(X).

calcDartScore(X) :- impossible(X).
calcDartScore(X) :- possible(X, Z).



















