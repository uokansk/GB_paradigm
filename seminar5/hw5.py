% Rules
sum( [ ], 0 ).
sum( [ H | T ], S1 ) :-
	sum( T, S2 ), S1 is S2 + H.


% Query
&- sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], S).