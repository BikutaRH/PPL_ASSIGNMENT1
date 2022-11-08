// ID: 2120028

grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : classDecle+ EOF ;
/*-------------------Syntax Structure--------------------*/

// 2.1. class declaration
classDecle: 'class' ID inheri? classBody ;
inheri: 'extends' ID;
classBody: LP members? RP;
members: (attribute | method)+ ;

// 2.2.Attribute declaration
attribute: mulable | immutable;
mulable: STATIC? typAttribute nonNullAttlist SEMI;
immutable: ((STATIC? FINAL) | (FINAL STATIC)) typAttribute nonNullAttlist SEMI;
typAttribute: primitive_type | array_type | class_type;
primitive_type: INT | FLOAT | BOOLEAN | STRING;
array_type: primitive_type LSB size RSB;
size: INTLIT;
class_type: ID;
nonNullAttlist: attName (COMMA attName)* ;
attName: ID (EQ exprs)? ;

// 5. Expression
exprs: expr1 (LESS | GREATER | LQ | GQ) expr1 | expr1  ; 
expr1: expr2 (EQUAL | NOTEQUAL) expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADD | SUB) expr4 | expr4;
expr4: expr4 (MUL | FLDIV | INDIV | MOD) expr5 | expr5;
expr5: expr5 CONCA expr6 | expr6 ;
expr6: NOT expr6 | expr7 ;
expr7: (ADD | SUB) expr7 | expr8 ;
expr8: expr8 index_Expr | expr9;
expr9: expr9 DOT ID
		| expr9 DOT ID LB expr_list? RB
 		| expr10;
expr10: NEW ID LB expr_list? RB | operands;
operands: INTLIT | FLOATLIT | BOOLIT | STRINGLIT | ARRLIT | ID | LB exprs RB | THIS | NIL ;
expr_list: exprs (COMMA exprs)*;
index_Expr: LSB exprs RSB ;


// 2.3 Method declaration
method: normalMethod | constructor ;
//// normal method:
normalMethod: static_method | unstatic_method;
static_method: STATIC typMethod ID paramsList block_stmts;
unstatic_method: typMethod ID paramsList block_stmts;
typMethod: primitive_type | array_type | class_type | VOID ;
paramsList: LB params? RB ;
params: param (SEMI param)* ;
param: typAttribute idList ;
idList: ID (COMMA ID)*;
block_stmts: LP ((vardecle*) (stmts*)) RP;
vardecle: FINAL? typAttribute nonNullAttlist SEMI;
stmts: block_stmts
	 | assign_stmts 
	 | if_stmts 
	 | for_stmts 
	 | break_stmts 
	 | continue_stmts 
	 | return_stmts 
	 | invocation_stmts;
/// assignment statement
assign_stmts: lhs ASSIGN exprs SEMI ;
lhs: ID | expr9 DOT ID | index_Expr ;

/// if statement
if_stmts: IF exprs THEN stmts (ELSE stmts)? ;

/// for statement
for_stmts: FOR scalar_var ASSIGN exprs (TO | DOWNTO) exprs DO stmts ;
scalar_var: ID | expr9 DOT ID | index_Expr;

/// Break statements
break_stmts: BREAK SEMI;

/// Continue Statements
continue_stmts: CONTINUE SEMI; 

/// return statements
return_stmts: RETURN exprs SEMI ;

/// invocation statements
invocation_stmts: ID DOT ID LB expr_list? RB SEMI ;

// constructor
constructor: ID paramsList block_stmts ;

/*-------------------Lexical Structure--------------------*/

EQ: '=';
ASSIGN: ':=';

// 3.4 Keyword
BOOLEAN: 'boolean';
BREAK: 'break';
CLASS: 'class';
CONTINUE: 'continue';
DO: 'do';
ELSE:'else';
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

// 3.3 Identifier
ID: [a-zA-Z_][a-zA-Z0-9_]* ;

// 3.5 Operator
ADD: '+';
SUB: '-';
MUL: '*';
FLDIV: '/';
INDIV: '\\';
MOD: '%';
NOTEQUAL: '!=';
EQUAL: '==';
LESS: '<';
GREATER: '>';
LQ: '<=';
GQ: '>=';
OR: '||';
AND: '&&';
NOT: '!';
CONCA: '^';
// 3.6 Separator
LSB: '[';
RSB: ']';
LP: '{';
RP: '}';
LB: '(';
RB: ')';
SEMI: ';';
COLON: ':';
DOT: '.';
COMMA: ',';

// 3.7. Literal
// 3.7.1 Integer Literal
INTLIT: [0-9]+;

// 3.7.2 Float Literal
FLOATLIT: INTPART (FRACPART EXPART? | EXPART) ;
fragment INTPART: [0-9]+;
fragment FRACPART: '.'[0-9]+;
fragment EXPART: [eE] [-+]? [0-9]+;

// 3.7.3 Boolean Literal
BOOLIT: TRUE | FALSE;

// 3.7.4 String Literal
STRINGLIT: '"' CHARACTERS* '"'
{
	self.text = self.text[1:-1]
};
fragment CHARACTERS: ~[\r\n] | ESCAPE;
fragment ESCAPE: '\\' [bfrnt"\\];

// 3.7.5 Array Literals
ARRLIT: LP NONNULL_LIT RP ;
fragment NONNULL_LIT: INTLIT (COMMA INTLIT)*
					| FLOATLIT(COMMA FLOATLIT)*
					| BOOLIT (COMMA BOOLIT)*
					| STRINGLIT (COMMA STRINGLIT)*
					;

// 3.2 Comment
BLOCK_COMMENT:  SL_MU (~[MU_SL])* MU_SL -> skip;
fragment SL_MU: '/*';
fragment MU_SL: '*/';
LINE_COMMENT: '#' (~[\n\r])* -> skip;

WS : [ \f\t\r\n]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING: '"' STR_CHAR* ( [\b\t\n\f\r"'\\] | EOF )
	{
		y = str(self.text)
		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
		if y[-1] in possible:
			raise UncloseString(y[1:-1])
		else:
			raise UncloseString(y[1:])
	}
	;

ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
	{
		y = str(self.text)
		raise IllegalEscape(y[1:])
	}
	;

fragment STR_CHAR: ~[\b\t\n\f\r"'\\] | ESC_SEQ ;

fragment ESC_SEQ: '\\' [btnfr"'\\] ;

fragment ESC_ILLEGAL: '\\' ~[btnfr"'\\] | ~'\\' ;

ERROR_CHAR: .
	{
		raise ErrorToken(self.text)
	}
	;