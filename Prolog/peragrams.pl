[kattio].

main :-
    repeat,
    read_string(X),
    (X == end_of_file ;
     peragrams(X),
     fail
    ).


/* Nedan, count tagen från Stack Overflow*/
/* Rekursiv algoritm som ser efter om element matchar och inkrementerar den i så fall*/

count(Element,[],0).

    count(Element,[X|List],OccurNum) :-
        Element = X,!,
        count(Element,List,OccurNum1),
        OccurNum is OccurNum1 + 1.

    count(Element,[X|List],OccurNum) :-
        count(Element,List,OccurNum).

zeroShifter(X, 0) :- X == 0.
zeroShifter(X, Y) :- X > 0, Y is X -1.

peragrams(X) :-

    count(97, X, A),
    count(98, X, B),
    count(99, X, C),
    count(100, X, D),
    count(101, X, E),
    count(102, X, F),
    count(103, X, G),
    count(104, X, H),
    count(105, X, I),
    count(106, X, J),
    count(107, X, K),
    count(108, X, L),
    count(109, X, M),
    count(110, X, N),
    count(111, X, O),
    count(112, X, P),
    count(113, X, Q),
    count(114, X, R),
    count(115, X, S),
    count(116, X, T),
    count(117, X, U),
    count(118, X, V),
    count(119, X, W),
    count(120, X, EX),
    count(121, X, Y),
    count(122, X, Z),



    Res is ((A mod 2) + (B mod 2)  + (C mod 2) + (D mod 2) + (E mod 2) + (F mod 2) + (G mod 2) + (H mod 2) + (I mod 2) + (J mod 2) + (K mod 2) + (L mod 2) + (M mod 2) + (N mod 2) + (O mod 2) + (P mod 2) + (Q mod 2) + (R mod 2) + (S mod 2) + (T mod 2) + (U mod 2) + (V mod 2) + (W mod 2) + (EX mod 2) + (Y mod 2) + (Z mod 2)),

    zeroShifter(Res, HandRes),
    write(HandRes), nl.











