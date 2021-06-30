[kattio].

main :-
    repeat,
    read_int(X),
    calcDartScore(X).

/* Calculate - Arbetshästen i denna uppgift                                             */
/* För den här uppgiften är det viktigt att inse att det finns olike "ranges".          */
/* För X = [1, 140] kan vi alltid köra standardfallet, att "lyfta" upp X med antingen   */
/* en eller två trippel och sen avsluta med en single. Alternativt för små X kan vi lösa*/
/* direkt.                                                                              */
/* -------------------------------------------------------------------------------------*/
/* Exempel, X = 68:  trippel 20, singel 8.                                              */
/* Exempel, X = 138: tripple 20, trippel 20, single 18.                                 */

/* För X = [141, 157] kan vi inte lyfta upp och avsluta med singel. Här är det lite     */
/* svårare. Vi måste antingen lyfta upp och avsluta med dubbel, eller göra konvertering */
/* Konvertering görs om X - 120 är udda, då får vi istället göra X - 117 dvs T 20 T 19. */
/* Genom att subtrahera med en udda trippel får vi då en jämn rest att köra dubbel på.  */
/* -------------------------------------------------------------------------------------*/
/* Exempel: X = 144: trippel 20 trippel 20 double 12.                                   */
/* Exempel(Konvertering till jämn): X = 143: trippel 20 trippel 19 dubbel 13.           */
/* (Notera att trippel 20 trippel 20 hade gett rest = 23, inte delbart med två)         */

/* För X = [158 180] kan vi bara kolla delbarhet med 3 vilket görs enkelt genom mod 3   */
/* eller genom att se ifall siffersumman är delbar med 3 (Om man vill göra huvudräkning)*/

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



















