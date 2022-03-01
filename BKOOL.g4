//1752637
grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}
//2
program: classdecl+ EOF;

//type
typ: (INT|FLOAT|BOOLEAN|STRING|arraytype|classtype);
classtype: ID;

//2.1
classdecl: CLASS ID (EXTENDS ID)? LCP memberlist RCP;
memberlist: member nextmember | ;
nextmember: member nextmember | ;
member:  (methoddecl|attributedecl|constructor);
//2.2
attributedecl: ((STATIC? FINAL?)|(FINAL? STATIC?)) typ attnamelist SMCOLON;
attnamelist: ID (ASM exp)? nextattributename;
nextattributename: COMMA ID (ASM exp)? nextattributename | ;
//attributename: ID (ASM exp)?;
ASM: '=';
//2.3
methoddecl: STATIC? primitivetype ID LB paralist RB blockstmt;
paralist: paradecl nextparadecl | ;
nextparadecl: SMCOLON paradecl nextparadecl | ;
paradecl: typ idlist;
idlist: ID nextid;
nextid: COMMA ID nextid | SMCOLON paradecl nextid | ;
constructor: ID LB paralist RB blockstmt;

//4
//4.1
primitivetype: (INT|FLOAT|BOOLEAN|STRING|VOID);
//4.2
arraytype: (INT|FLOAT|BOOLEAN|STRING) LSB INTLIT RSB;

//exp
exp: exp1 (LESS | GREATER | LESSOE | GREATEROE) exp1 | exp1;
exp1: exp2 (EQ | NEQ) exp2 | exp2;
exp2: exp2 (AND | OR) exp3 | exp3;
exp3: exp3 (ADD | SUB) exp4 | exp4;
exp4: exp4 (MUL | MOD | FDIV | IDIV) exp5 | exp5;
exp5: exp5 CONCAT exp6 | exp6;
exp6: NOT exp6 | exp7;
exp7: (ADD | SUB) exp7 | exp8;
exp8: exp8 index_op | exp9;
exp9: exp9 DOT ID (LB explist RB)? | exp10;
exp10: NEW exp10 LB explist RB | operand;
operand: INTLIT | FLOATLIT | BOOLIT | STRINGLIT | arraylit | ID | THIS ;
index_op: LSB exp RSB;
explist: exp nextexp | ;
nextexp: COMMA exp nextexp | ;

//6
blockstmt: LCP vardecllist stmtlist RCP;
vardecllist: vardec nextvardec | ;
nextvardec: vardec nextvardec | ;
stmtlist: stmt nextstmt | ;
nextstmt: stmt nextstmt | ;
vardec: FINAL? typ attnamelist SMCOLON;
stmt: blockstmt | asmstmt | ifstmt | forstmt | breakstmt | continuestmt | returnstmt | methodinvocstmt;
asmstmt: exp GAN exp SMCOLON;
GAN: ':=';
ifstmt: IF exp THEN stmt (ELSE stmt)? ;
forstmt: FOR ID GAN exp (TO|DOWNTO) exp DO stmt;
breakstmt: BREAK SMCOLON;
continuestmt: CONTINUE SMCOLON;
returnstmt: RETURN exp SMCOLON;
methodinvocstmt: exp DOT ID LB explist RB SMCOLON;

//3.2
BCOMMENT: '/*' .*? '*/' -> skip;
LCOMMENT: '#' .~('\f' | '\r' | '\n')* -> skip;

//3.7
//3.7.1
INTLIT: DIGIT+;
//3.7.2
FLOATLIT: DIGIT+ (DECIMAL EXPONENT?|DECIMAL? EXPONENT);
fragment DIGIT: [0-9];
fragment DECIMAL: '.' DIGIT*;
fragment EXPONENT: ('E'|'e') ('+'|'-')? DIGIT+;
//3.7.3
BOOLIT: (TRUE|FALSE);
//3.7.4
STRINGLIT: '"' ('\\' ('t' | 'b' | 'f' | 'r' | 'n' | '\\') | '\\''"' | ~('\b' | '\f' | '\r' | '\n' | '\t' | '"' | '\\'))* '"'{self.text = self.text[1:-1]};
//3.7.5
arraylit: LCP literals (COMMA literals)* RCP;
literals: INTLIT | FLOATLIT | BOOLIT | STRINGLIT | nulliteral | arraylit;
nulliteral: NIL;
//3.4
BOOLEAN: 'boolean';
BREAK: 'break';
CLASS: 'class';
CONTINUE: 'continue';
DO: 'do';
ELSE: 'else';
EXTENDS: 'extends';
FLOAT: 'float';
IF: 'if';
INT: 'int';
NEW: 'new';
STRING: 'string';
THEN: 'then';
FOR: 'for';
RETURN: 'return';
TRUE: 'true';
FALSE: 'false';
VOID: 'void';
NIL: 'nil';
THIS: 'this';
FINAL: 'final';
STATIC: 'static';
TO: 'to';
DOWNTO: 'downto';

//3.5
ADD: '+';
SUB: '-';
MUL: '*';
FDIV: '/';
IDIV: '\\';
MOD: '%';
NEQ: '!=';
EQ: '==';
LESS: '<';
GREATER: '>';
LESSOE: '<=';
GREATEROE: '>=';
OR: '||';
AND: '&&';
NOT: '!';
CONCAT: '^';

//3.6
LSB: '[';
RSB: ']';
LCP: '{';
RCP: '}';
LB: '(';
RB: ')';
SMCOLON: ';';
COLON: ':';
DOT: '.';
COMMA: ',';

//3.3
ID: (LETTER|UNDERSCORE) (LETTER|UNDERSCORE|DIGIT)*;
fragment LETTER: [a-zA-Z];
fragment UNDERSCORE: '_';

//3.1
WS : ('\t'|'\f'|'\r'|'\n'|' ')+ -> skip ; // skip spaces, tabs, newlines
//ERROR
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' STR_CHAR* ( [\b\t\n\f\r"'\\] | EOF )
	{
		wrong_string = str(self.text)
		esc_squence = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
		if wrong_string[-1] in esc_squence:
			raise UncloseString(wrong_string[1:-1])
		else:
			raise UncloseString(wrong_string[1:])
	};

ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
	{
		wrong_string = str(self.text)
		raise IllegalEscape(wrong_string[1:])
	}
	;

fragment STR_CHAR: ~('\b' | '\t' | '\n' | '\f' | '\r' | '"' | '\\') | ESC_SEQUENCE ;
fragment ESC_SEQUENCE: '\\' ('b' | 't' | 'n' | 'f' | 'r' | '"' | '\\');
fragment ESC_ILLEGAL: '\\' ~('b' | 't' | 'n' | 'f' | 'r' | '"' | '\\') | ~'\\';

//UNCLOSE_STRING: .;
//ILLEGAL_ESCAPE: .;