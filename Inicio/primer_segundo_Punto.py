# primer punto, desarrollo de la lista encadenada
class Node:

	def __init__(self, data):
		# data for node
		self.data = data
		# pointer for nexte element
		self.next = None

class LinkedList:

	def __init__(self):
		# initialize head with node Null
		self.head = None
		self.tail = None

#Devuelve lista enlazada        
	def isEmpty(self):               
		return self.head
		
#Agrega elemento al final            
	def addEnd(self, key):
		nodo = Node(key)
		if not self.isEmpty():
			self.head = nodo
			self.tail = nodo
		else:
			self.tail.next = nodo                
			self.tail = nodo		
			
	def display(self):
		# variable to iterate
		temp_node = self.head
		
		# iterating until we reach the end of the linked list
		while temp_node != None:
			# printing the node data
			print(temp_node.data, end='->')
			# moving to the next node
			temp_node = temp_node.next

		print('Null')

	def delete(self):
		
		current = self.head
		prev = None
		duplicate_dict = dict()
		while current:
			if current.data not in duplicate_dict:
				duplicate_dict[current.data] = None
				prev = current
			else:
				prev.next = current.next
			current = current.next


if __name__ == '__main__':
	# instantiating the linked list
	linked_list = LinkedList()

	phrase = input()
	phrase2 = phrase

	# loop to store string on chars
	for i in phrase:
		linked_list.addEnd(i)

	linked_list.delete()
	linked_list.display()
	
	# list implementation for the same purpouse
	print("USING DYNAMIC ARRAYS = LISTS ON PYTHON")

	listas = []
	newList = []
	for i in phrase2:
		listas.append(i)
	for j in listas:
		if j not in newList:
			newList.append(j)
	print(newList)

# referencias: https://geekflare.com/python-linked-lists/