lexer grammar EnglishLexer;

options {
    caseInsensitive=true;
}

WS: [ \t\n\r\f]+ -> skip ;
COMMENT: '#' ~[\r\n]* -> channel(HIDDEN);

// Subject 1
I: 'i' ;

// Subject 2
YOU: 'you' ;
WE: 'we' ;
THEY: 'they' ;

// Subject 3
HE: 'he' ;
SHE: 'she' ;
IT: 'it' ;

// Auxiliary Verb 1
AM: 'am' ;

// Auxiliary Verb 2
ARE: 'are' ;

// Auxiliary Verb 3
IS: 'is' ;

// Verb1
STUDY: 'study' ;
WORK: 'work' ;

// Verb1 with -s or -es suffix
STUDIES: 'studies';
WORKS: 'works';

// NoVerb
SMART: 'smart' ;

// Noun
ENGLISH: 'english' ;

