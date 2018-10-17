class Node:
	def __init__(self, key, value, upPointer, downPointer, col):
		self.col = col #is red or black, false==black red==true
		self.upPointer = upPointer
		self.downPointer = downPointer
		self.key = key
		self.value = value
		self.size = 0

	def __repr__(self):
		RB = "Black"
		if(self.col):
			RB = "Red"
		return "Node{"+"key="+str(self.getKey())+", value="+str(self.getValue())+", color="+ RB + "}"
	def getKey(self):
		return self.key
	def isRed(self):
		return self.col()
	def setKey(self, key):
		self.key = key
	def getValue(self):
		return self.value
	def setValue(self, newVal):
		self.value = newVal
	def setUp(self, x):
		self.upPointer = x
	def getUp(self):
		return self.upPointer
	def getDown(self):
		return self.downPointer
	def setDown(self, x):
		self.downPointer = x
	def setSize(self, newSize):
		self.size = newSize
	def setCol(self, newCol):
		self.col = newCol
	def getSize(self):
		self.size = 1
		if(self.getDown()!=None):
			self.size += self.getDown().getSize()
		if(self.getUp()!=None):
			self.size += self.getUp().getSize()
		return self.size
	def verifyBlackHeight(self,height):
		if(not self.isRed):
			height-=1;
		if(self.getUp() is None and height is not 0):
			return False
		if(self.getDown is None and height is not 0):
			return False
		if(self.getUp() is not None and self.getUp().verifyBlackHeight(height) is False):
			return False
		if(self.getDown() is not None and self.getDown().verifyBlackHeight(height) is False):
			return False
		return True

class BST():
	def __init__(self):
		self.root = Node(None, None, None, None, False)
	#Thnx G-RANT
	def printPart(self,node):
		if(node==None):
			 return "X"
		downString=self.printPart(node.getDown())
		upString=self.printPart(node.getUp())
		sideWidth=max(len(leftString.split("\n")[0]),len(rightString.split("\n")[0]))
		width=sideWidth+len(str(node.key))+sideWidth
		halfWidth=math.floor(sideWidth/2)
		string=halfWidth*" "+"|"+(sideWidth-halfWidth-1)*"-"+str(node.isRed)+(sideWidth-halfWidth-1)*"-"+"|"+halfWidth*" "+"\n"
		leftArr=leftString.split('\n')
		rightArr=rightString.split("\n")
		for i in range(0,max(len(leftArr),len(rightArr))):
			if(len(leftArr)>i):
				smallSideWidth=math.floor((sideWidth-len(leftArr[i]))/2)
				string+=smallSideWidth*" "
				string+=leftArr[i]
				string+=(sideWidth-len(leftArr[i])-smallSideWidth)*" "
			else:
				string+=" "*(sideWidth)
			string+=(width-sideWidth*2)*" "
			if(len(rightArr)>i):
				smallSideWidth=math.floor((sideWidth-len(rightArr[i]))/2)
				string+=smallSideWidth*" "
				string+=rightArr[i]
				string+=(sideWidth-len(rightArr[i])-smallSideWidth)*" "
			else:
				string+=" "*(sideWidth)
			string+="\n"
		return string[:-1]
	def size(self):
		return self.__recSize(self.root)
	def __recSize(self, node):
		return node.getSize() + 1
	def isEmpty(self):
		return self.size()==0
	def rotateRight(self, node):
		if(node.getUp() is None):
			return None
		newNode = node.getDown()
		node.setDown(node.getUp())
		newNode.setDown(node)
		return newNode()
	def rotateLeft(self, node):
		if(node.getDown() is None):
			return None
		newNode = node.getUp()
		node.setDown(node.getDown())
		newNode.setUp(node)
		return newNode()
	def isGrandParent(node):
		if(node.getLeft()!=None and (node.getLeft().getLeft()!=None or node.getLeft().getRight()!=None)) or (node.getRight().getRight()!=None and (node.getRight().getLeft()!=None or node.getRight().getRight()!=None))

	def put(self, key, val):
		x = self.__recPut(self.root, key, val)
		self.root = x
	def __recPut(self, node, key, value):
		if(node.getKey() == None):
			node = Node(key, value, None, None)
			return node;
			# node.setKey(key)
			# node.setValue(value)
		else:
			if(key >= node.getKey()):
				if (node.getUp()==None):
					node.setUp(Node(key, value, None, None))
					return node
				else:
					node.setUp(self.__recPut(node.getUp(), key, value))
					return node
			#this will check for all values less than
			else:
				if(node.getDown()==None):
					node.setDown(Node(key, value, None, None))
					return node
				else:
					node.setDown(self.__recPut(node.getDown(), key, value))
					return node
	def get(self, key):
		return self.__recGet(self.root, key)
	def __recGet(self, node, key):
		#checks if equals
		if(key==node.getKey()):
			return node.getValue()
		#checks higher values
		elif(node.getUp() != None and key>node.getKey()):
			return self.__recGet(node.getUp(), key)
		#checks less values
		elif(node.getDown() != None and key<node.getKey()):
			return self.__recGet(node.getDown(), key)
		else:
			return -1

	def contains(self, key):
		return self.get(key) != -1
	def remove(self, key):
		v = self.get(key)
		self.root = self.__recRemove(self.root, key)
		print(self.root)
		return v;
	def __recRemove(self, node, key):
		if(node==None):
			return None
		if(key<node.getKey()):
			node.setDown(self.__recRemove(node.getDown(), key))
		elif(key>node.getKey()):
			node.setUp(self.__recRemove(node.getUp(), key))
		else:
			if(node.getUp()==None):
				return node.getDown()
			if(node.getDown()==None):
				return node.getUp()
			else:
				dwn = node.getDown()
				node = node.getUp()
				node.setDown(dwn)
		#node.setSize(node.getUp().size() + self.node.getDown().size() + 1)
		return node

	def minimum(self):
		return self.__recMin(self.root).getKey()

	def __recMin(self, node):
		if(node.getDown() != None):
			return self.__recMin(node.getDown())
		else:
			return node

	def maximum(self):
		return self.__recMax(self.root).getKey()

	def __recMax(self, node):
		if(node.getUp() != None):
			return self.__recMax(node.getUp())
		else:
			return node

	def __repr__(self):
		return self.printPart(self.root)
	def getRoot(self):
		return self.root
	def setRoot(self, x):
		root.setKey(x)
	def __toString(self, node):
		if(node==None):
			return ""
		else:
			return str(self.__toString(node.getDown())) + str(node.getKey()) + "=" + str(node.getValue()) + ", " + str(self.__toString(node.getUp()))
def isRBBST(bst):
	if(bst.root.isRed()):
		return False
	if(tree.root.verifyBlackHeight(tree.getBlackHeight()) == False):
		return False
	return isRBBSTPart(tree.root)
   def isRBBSTPart(node):
	if(node.isRed):
		if(node.left is not None and node.left.isRed()) or (node.right is not None and node.right.isRed()):
			return False
	if node.getDown() is not None and not isRBBSTPart(node.getDown()):
		return False
	if node.getUp() is not None and not isRBBSTPart(node.getUp()):
		return False
	return True
def main():
	bst = RedBlackBST()
	bst.put(5,1)
	bst.put(2,2)
	bst.put(6,3)
	bst.put(20,4)
	bst.put(1,5)
	bst.put(19,6)
	bst.put(0,7)
	print(str(bst)+"\n\n\n")
	bst.root=rotateRight(bst.root)
	print(str(bst)+"\n\n\n")
	bst.root.right=rotateLeft(bst.root.right)
	print(str(bst)+"\n\n\n")

if __name__ == '__main__':
	main()




