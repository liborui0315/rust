const (
default_program_name = "default"
program_init_size = 100
min_token_index = 0
)


pub trait RewriteOperation {
    fn execute(&self, buffer: * bytes.Buffer) -> isize;
    fn String(&self) -> String;
    get_instruction_index()        int
    get_index()            int
    get_text()            String
    get_op_name()            String
    get_tokens()            TokenStream
    set_instruction_index(val isize)
    set_index(isize)
    set_text(String)
    set_op_name(String)
    set_tokens(TokenStream)
}

pub struct BaseRewriteOperation {
    instruction_index: isize,
    index: isize,
    text: String,
    op_name: String,
    tokens: TokenStream,
}

impl BaseRewriteOperation {
    fn (op * BaseRewriteOperation)GetInstructionIndex() int { unimplemented ! () }

    fn (op * BaseRewriteOperation)GetIndex() int { unimplemented ! () }

    fn (op * BaseRewriteOperation)GetText() String { unimplemented ! () }

    fn (op * BaseRewriteOperation)GetOpName() String { unimplemented ! () }

    fn (op * BaseRewriteOperation)GetTokens() TokenStream { unimplemented ! () }

    fn (op * BaseRewriteOperation)SetInstructionIndex(val isize) { unimplemented ! () }

    fn (op * BaseRewriteOperation)SetIndex(val isize)  { unimplemented ! () }

    fn (op * BaseRewriteOperation)SetText(val String) { unimplemented ! () }

    fn (op * BaseRewriteOperation)SetOpName(val String) { unimplemented ! () }

    fn (op * BaseRewriteOperation)SetTokens(val TokenStream)   { unimplemented ! () }


    fn execute(&self, buffer: * bytes.Buffer) -> int { unimplemented!() }

    fn String(&self) -> String { unimplemented!() }


    pub struct InsertBeforeOp {
    base: base_rewrite_operation,
    }

    fn new_insert_before_op(index isize, text: String, stream: TokenStream) -> * InsertBeforeOp { unimplemented!() }

    fn execute(&self, buffer: * bytes.Buffer) -> int { unimplemented!() }

    fn String(&self) -> String { unimplemented!() }


    pub struct InsertAfterOp {
    base: base_rewrite_operation,
    }

    fn new_insert_after_op(index isize, text: String, stream: TokenStream) -> * InsertAfterOp { unimplemented!() }

    fn execute(&self, buffer: * bytes.Buffer) -> int { unimplemented!() }

    fn String(&self) -> String { unimplemented!() }

    pub struct ReplaceOp{
    base: base_rewrite_operation,
    last_index: isize,
    }

    fn new_replace_op(from, to: isize, text: String, stream: TokenStream) -> * ReplaceOp { unimplemented!() }

    fn (op * ReplaceOp)Execute(buffer * bytes.Buffer) int { unimplemented ! () }

    fn String(&self) -> String { unimplemented!() }


    pub struct TokenStreamRewriter {
    tokens: TokenStream,
    programs: map[String]Vec < RewriteOperation >,
    last_rewrite_token_indexes: map[String]isize,
    }

    fn new_token_stream_rewriter(tokens TokenStream) -> * TokenStreamRewriter { unimplemented!() }

    fn get_token_stream(&self) -> TokenStream { unimplemented!() }

    fn rollback(&self, program_name: String, instruction_index: isize) { unimplemented!() }

    fn rollback_default(&self, instruction_index: isize) { unimplemented!() }
    fn delete_program(&self, program_name: String) { unimplemented!() }

    fn delete_program_default(&self) { unimplemented!() }

    fn insert_after(&self, program_name: String, index: isize, text: String) { unimplemented!() }

    fn insert_after_default(&self, index: isize, text: String) { unimplemented!() }

    fn insert_after_token(&self, program_name: String, token: Token, text: String) { unimplemented!() }

    fn insert_before(&self, program_name: String, index: isize, text: String) { unimplemented!() }

    fn insert_before_default(&self, index: isize, text: String) { unimplemented!() }

    fn insert_before_token(&self, program_name: String, token Token, text: String) { unimplemented!() }

    fn replace(&self, program_name: String, from: isize, to: isize, text: String) { unimplemented!() }

    fn (tsr * TokenStreamRewriter)ReplaceDefault(from, to: isize, text: String)   { unimplemented ! () }

    fn (tsr * TokenStreamRewriter)ReplaceDefaultPos(index isize, text: String) { unimplemented ! () }

    fn (tsr * TokenStreamRewriter)ReplaceToken(program_name String, from: Token, to: Token, text: String) { unimplemented ! () }

    fn (tsr * TokenStreamRewriter)ReplaceTokenDefault(from, to: Token, text: String) { unimplemented ! () }

    fn (tsr * TokenStreamRewriter)ReplaceTokenDefaultPos(index Token, text: String) { unimplemented ! () }

    fn (tsr * TokenStreamRewriter)Delete(program_name String, from: isize, to: isize) { unimplemented ! () }

    fn (tsr * TokenStreamRewriter)DeleteDefault(from, to: isize) { unimplemented ! () }

    fn (tsr * TokenStreamRewriter)DeleteDefaultPos(index isize) { unimplemented ! () }

    fn (tsr * TokenStreamRewriter)DeleteToken(program_name String, from: Token, to: Token)   { unimplemented ! () }

    fn (tsr * TokenStreamRewriter)DeleteTokenDefault(from, to Token) { unimplemented ! () }

    fn (tsr * TokenStreamRewriter)GetLastRewriteTokenIndex(program_name String)int   { unimplemented ! () }

    fn (tsr * TokenStreamRewriter)GetLastRewriteTokenIndexDefault()int { unimplemented ! () }

    fn (tsr * TokenStreamRewriter)SetLastRewriteTokenIndex(program_name String, i: isize) { unimplemented ! () }

    fn (tsr * TokenStreamRewriter)InitializeProgram(name String)Vec< RewriteOperation >  { unimplemented ! () }

    fn (tsr * TokenStreamRewriter)AddToProgram(name String, op: RewriteOperation) { unimplemented ! () }

    fn (tsr * TokenStreamRewriter)GetProgram(name String) Vec< RewriteOperation >    { unimplemented ! () }
    fn (tsr * TokenStreamRewriter)GetTextDefault() String { unimplemented ! () }
    fn (tsr * TokenStreamRewriter)GetText(program_name String, interval: * Interval) String   { unimplemented ! () }

    fn reduce_to_single_operation_per_index(rewrites Vec<RewriteOperation>) -> map[int]RewriteOperation { unimplemented ! () }


    /*
        quick fixing Go lack of: overloads,
     */

    fn max(a, b isize) -> int { unimplemented!() }
    fn min(a, b isize) -> int { unimplemented!() }
}
 