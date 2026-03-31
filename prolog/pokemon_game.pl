:-ensure_loaded("pokemon_list.pl").
:-ensure_loaded("pokemon_info_attacks.pl").
:-ensure_loaded("pokemon_route.pl").

player_starts(0,0).

% TO DO
next_rooms(X,Y,Rooms) :-
    route(M),
    findall(
        [Id,Name,Level,NX,NY,Types], % What we gonna collect
        valid_neighbour(M,X,Y,Id,Name,Level,NX,NY,Types),
        Rooms).

get_element([H|_],0,H).
get_element([_|T],N,E):-
    N > 0,
    N1 is N - 1,
    get_element(T,N1,E).

% right neighbour
valid_neighbour(M,X,Y,Id,Name,Level,NX,NY,Types):-
    NX is X + 1,
    NY = Y,

    %Boundaries check
    NX >= 0,
    NX =< 4,
    NY >= 0,
    NY =< 4,

    %Info from Matrix
    get_element(M,NY,Row),
    get_element(Row,NX,Cell),
    Cell = (Id, Level),

    %Pokemon info
    pokemon(Id,Name,Types).

% left neighbour
valid_neighbour(M,X,Y,Id,Name,Level,NX,NY,Types):-
    NX is X - 1,
    NY = Y,

    NX >= 0,
    NX =< 4,
    NY >= 0,
    NY =< 4,

    get_element(M,NY,Row),
    get_element(Row,NX,Cell),
    Cell = (Id,Level),

    pokemon(Id,Name,Types).

% up neighbour
valid_neighbour(M,X,Y,Id,Name,Level,NX,NY,Types):-
    NX = X,
    NY is Y - 1,

    NX >= 0,
    NX =< 4,
    NY >= 0,
    NY =< 4,

    get_element(M,NY,Row),
    get_element(Row,NX,Cell),
    Cell = (Id,Level),

    pokemon(Id,Name,Types).

% down neighbour
valid_neighbour(M,X,Y,Id,Name,Level,NX,NY,Types):-
    NX = X,
    NY is Y + 1,

    NX >= 0,
    NX =< 4,
    NY >= 0,
    NY =< 4,

    get_element(M,NY,Row),
    get_element(Row,NX,Cell),
    Cell = (Id,Level),

    pokemon(Id,Name,Types).
