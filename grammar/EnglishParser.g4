parser grammar EnglishParser;

options {
    tokenVocab=EnglishLexer;
}

english: basicSentence* EOF
       ;

basicSentence: withVerb noun?
             | withoutVerb
             ;

withVerb: (subject1 | subject2) verb1
        | subject3 verb1SorEsSuffix
        ;

withoutVerb: subject1 auxiliaryVerb1 noVerb
           | subject2 auxiliaryVerb2 noVerb
           | subject3 auxiliaryVerb3 noVerb
           ;

subject1: I ;
subject2: YOU | WE | THEY ;
subject3: HE | SHE | IT ;

auxiliaryVerb1: AM ;
auxiliaryVerb2: ARE ;
auxiliaryVerb3: IS ;

verb1: STUDY | WORK ;

verb1SorEsSuffix: STUDIES | WORKS ;

noVerb: SMART ;

noun: ENGLISH ;