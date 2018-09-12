from sem_analyze import *

stack = [{}]
new_symbol("foo", stack)
begin_block(stack)
new_symbol("fii", stack)
end_block(stack)
print search_symbol("foo", stack)
print search_symbol("fii", stack)
