from sem_analyze import *

stack = [{}]
new_symbol("foo", stack)
#new_symbol("fii", stack)
begin_block(stack)
new_symbol("foo", stack)
begin_block(stack)
new_symbol("fii", stack)

print_stack(stack)
print "Search foo : " + str(search_symbol("foo", stack))
print "Search fii : " + str(search_symbol("fii", stack))

end_block(stack)

print_stack(stack)
print "Search foo : " + str(search_symbol("foo", stack))
print "Search fii : " + str(search_symbol("fii", stack))

end_block(stack)

print_stack(stack)
print "Search foo : " + str(search_symbol("foo", stack))
