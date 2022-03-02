// Student's ID : 1713964

grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}


// 2 PROGRAM STRUCTURE
program: class_declaration+ EOF;

// 2.1 CLASS DECLARATION
class_declaration: CLASS ID (COLON ID)? LCP memberlist RCP;
memberlist: member nextmember |;
nextmember: member nextmember |;
member: attribute | method;
// val a,b,c : int = 1,2,3
// [a,b,c]
// [1,2,3]
// 2.2 ATTRIBUTE DECLARATION
attribute: (VAL | VAR) list_of_attribute_names COLON type_name (ASSIGN list_of_exp)? SEMI;
list_of_attribute_names: attribute_name next_attribute_name;
next_attribute_name: COMMA attribute_name next_attribute_name | ;
attribute_name: ID | DOLLAR_ID;
type_name: primitive_type;

// 2.3 METHOD DECLARATION
method: (ID | DOLLAR_ID) LP list_of_parameters RP block_statement | constructor | destructor;
list_of_parameters: parameter_dec next_parameter_dec | ;
next_parameter_dec : SEMI parameter_dec next_parameter_dec | ;
parameter_dec: id_list COLON typ;
id_list: ID next_id;
next_id: COMMA ID next_id | ;
typ: primitive_type;
//calculate_sum(a,b : Int; c,d: Float)

// constructor co return
constructor : CONSTRUCTOR LP list_of_parameters RP block_statement;
// constructor khong return
destructor : DESTRUCTOR LP RP block_statement;


// INDEXED ARRAY

indexed_array: ARRAY LP list_of_exp RP;
list_of_exp: exp next_exp;
next_exp: COMMA exp next_exp | ;


// MULTI-DEMENSIONAL ARRAY

multi_dimen_arr: ARRAY LP array_list RP;
array_list : indexed_array next_array;
next_array: COMMA indexed_array next_array | ;

// 4 TYPE AND VALUE
// 4.1 PRIMITIVE TYPES
// 4.1.1 BOOLEAN TYPE
primitive_type: BOOLEAN | INT | FLOAT | STRING | array_type | class_type;


// 4.2 ARRAY TYPE
array_type: ARRAY LSP element_type COMMA size RSP;
element_type: primitive_type | array_type;
size : INTEGER_LITERAL;


// 4.3 CLASS TYPE

class_type : ID;


// 5. EXPRESSIONS
// 5.5 INDEX OPERATOR
index_operator : LSP exp RSP | LSP exp RSP index_operator;


//5.6 MEMBER ACCESS

member_access   : instance_att_acc
                | static_att_acc
                | static_met_inv
				| instance_met_inv;

instance_att_acc: DOT ID;

static_att_acc  : ID DOUBLE_COLON DOLLAR_ID;

instance_met_inv: DOT ID LP list_of_exp RP;

static_met_inv  : ID DOUBLE_COLON DOLLAR_ID LP list_of_exp? RP;


//5.7 OBJECT CREATION

object_creation : NEW ID LP list_of_exp RP;


// 5.9 Operator precedence and associativity

exp: exp STRING_CONCAT exp
    | exp STRING_EQUAL exp
    | exp1;
exp1: exp1 EQUAL exp1
    | exp1 NOT_EQUAL exp1
    | exp1 LESS exp1
    | exp1 GREATER exp1
    | exp1 LESS_OR_EQUAL exp1
    | exp1 GREATER_OR_EQUAL exp1
    | exp2;
exp2: exp2 AND exp3
    | exp2 OR exp3
    | exp3;
exp3: exp3 ADD exp4
    | exp3 SUB exp4
    | exp4;
exp4: exp4 MUL exp5
    | exp4 DIV exp5
    | exp4 MOD exp5
    | exp5;
exp5: NOT exp5
    |exp6;
exp6: SUB exp6
    |exp7;
exp7: exp7 index_operator
    | exp8;
exp8: exp8 instance_att_acc | exp8 instance_met_inv
    | exp9;
exp9: static_att_acc | static_met_inv
    | exp10;
exp10: object_creation | operand;
operand: ID
        | DOLLAR_ID
        | SELF
        | NULL
        | INTEGER_LITERAL
        | BOOLEAN_LITERAL
        | FLOAT_LITERAL
        | STRING_LITERAL
        | indexed_array
        | multi_dimen_arr
        | subexp;
subexp: LP exp RP;


// 6. STATEMENT

statement   : variable_dec
            | constant_dec
            | assign_statement
            | if_statement
            | for_in_statement
            | break_statement
            | continue_statement
            | return_statement
            | method_inv_statement
            | block_statement
            ;


// 6.1 Variable and Constant Declaration Statement

variable_dec: VAR list_of_variable_names COLON type_name (ASSIGN list_of_exp)? SEMI;
list_of_variable_names: variable_name next_variable_name;
next_variable_name: COMMA variable_name next_variable_name | ;
variable_name: ID;

constant_dec: VAL list_of_constant_names COLON type_name (ASSIGN list_of_exp)? SEMI;
list_of_constant_names: constant_name next_constant_name;
next_constant_name: COMMA constant_name next_constant_name | ;
constant_name: ID;


// 6.2 Assignment Statement

assign_statement: lhs ASSIGN exp SEMI;
lhs: ID | ID index_operator | exp instance_met_inv | exp instance_att_acc | static_att_acc | static_met_inv;


// 6.3 If statement

if_statement: IF LP exp RP block_statement (ELSEIF LP exp RP block_statement)* (ELSE block_statement)? ;


// 6.4 For/In statement

for_in_statement: FOREACH LP ID IN exp '..' exp (BY exp)? RP block_statement;

// 6.5 Break statement

break_statement: BREAK SEMI;


// 6.6 Continue statement

continue_statement: CONTINUE SEMI;


// 6.7 Return statement

return_statement: RETURN exp? SEMI;


// 6.8 Method Invocation statement

method_inv_statement:  (exp instance_met_inv | static_met_inv) SEMI;


// 6.9 Block statement

block_statement: LCP list_of_statement RCP;
list_of_statement: statement next_statement | ;
next_statement: statement next_statement | ;


//3.2 COMMENT

COMMENT	:'##' .*? '##' -> skip;


//3.7 LITERALS


//INTEGER_LITERAL

INTEGER_LITERAL: ('0' | OCTAL | HEX | BIN | DEC) {self.text = self.text.replace('_','')};
fragment NON_ZERO: [1-9];
fragment DIGIT : [0-9];
fragment OCTAL: '0' [0-7]+ ('_' [0-7]+)*;
fragment HEX: ('0x'|'0X') [0-9A-F]+ ('_' [0-9A-F]+)*;
fragment BIN: ('0b'|'0B') [0-1]+ ('_' [0-1]+)*;
fragment DEC: NON_ZERO DIGIT* ('_' DIGIT+)*;


// FLOAT_LITERAL

FLOAT_LITERAL       : (INT_PART DEC_PART EX_PART?
                    | INT_PART EX_PART
                    | DEC_PART EX_PART) {self.text = self.text.replace('_','')};
fragment INT_PART        : DEC;
fragment DEC_PART        : DOT DIGIT*;
fragment EX_PART       : [eE][-+]? DIGIT+;


// BOOLEAN

BOOLEAN_LITERAL             : TRUE | FALSE;


//3.4 KEYWORD

BREAK:'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';
TRUE: 'True';
FALSE: 'False';
ARRAY: 'Array';
IN: 'In';
INT:'Int';
FLOAT:'Float';
BOOLEAN:'Boolean';
STRING:'String';
RETURN:'Return';
NULL:'Null';
CLASS:'Class';
VAL:'Val';
VAR:'Var';
SELF:'Self';
CONSTRUCTOR:'Constructor';
DESTRUCTOR:'Destructor';
NEW:'New';
BY:'By';

//3.5 OPERATORS

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
ASSIGN: '=';
NOT_EQUAL: '!=';
LESS:'<';
LESS_OR_EQUAL: '<=';
GREATER: '>';
GREATER_OR_EQUAL: '>=';
STRING_EQUAL: '==.';
STRING_CONCAT: '+.';
DOT: '.';
DOUBLE_COLON: '::';


//3.6 SEPERATORS

LP:'(';
RP:')';
LSP:'[';
RSP:']';
LCP:'{';
RCP:'}';
COMMA:',';
SEMI:';';
COLON:':';


//3.3 IDENTIFIERS

ID: (LETTER | '_') (LETTER | '_' | DIGIT)* ;
DOLLAR_ID: '$' (LETTER | '_' | DIGIT)+;
LETTER: [A-Za-z];


//3.1 CHARACTERS SETS

WS: [ \t\b\f\r\n]+ -> skip;


//ERROR

ERROR_CHAR: . {raise ErrorToken(self.text)};

STRING_LITERAL : '"' (ESC_SEQUENCE | ESC_ILLEGAL | '\'"')*? '"' {self.text = self.text[1:-1]};

fragment ESC_SEQUENCE   : '\\' ('b' | 'f' | 'r' | 'n' | 't' | '\'' | '\\');
fragment ESC_ILLEGAL    : ~('\b' | '\f' | '\r' | '\n' | '\t' | '\'' | '\\');

UNCLOSE_STRING: '"' (ESC_SEQUENCE | ESC_ILLEGAL )*? ([\b\f\r\n\t"\\] | EOF)
    {
		y = str(self.text)
		raise UncloseString(y[1:])
	};
ILLEGAL_ESCAPE: '"' (ESC_SEQUENCE | ESC_ILLEGAL )*? '\\' ~[bfrnt\\]
    {
		y = str(self.text)
		raise IllegalEscape(y[1:])
	};





