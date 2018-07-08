from collections import deque

class Queue(deque):
	enqueue = deque.append
	dequeue = deque.popleft
	def front(self):
		return self[-1]
	def size(self):
		return len(self)

class Stack(deque):
	push = deque.append
	def is_empty(self):
		return not self
		
		
def main():
	stack = Stack()
	stack.push(3)
	print(stack)
	stack.pop()
	print(stack)
	
if __name__ == "__main__":
	main()