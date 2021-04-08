from stack_class import Stack


s = Stack()

print("Is the stack empty?", s.its_empty())

s.push('first')
s.push(2)

print("First item from the stack is:", s.top_stack())

s.push('three')
print("the size of the stack is: ", s.height())

s.push(4.0)
s.show_stack()

print("pop in stack is: ", s.pop())
print("pop in stack is: ", s.pop())

print("the size of the stack is: ", s.height())
print("Is the stack empty?", s.its_empty())

