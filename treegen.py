space_between_nodes = 4

#input is represented as a list, the first entry is the node itself, the second entry is a list of children
tree = [
	'if', [
		['name x', []],
		['then subtree', [
			['operator =', [
				['y', []],
				['2', []],
			]],
		]],
		['else subtree', [
			['operator =', [
				['y', []],
				['3', []],
			]],
		]],
	]
]

#first generate a level order traversal of the tree
def get_levels(levels, node, depth):
	if len(node) != 0:
		if depth == len(levels):
			levels.append([])
		levels[depth].append(node[0])

		for child in node[1]:
			get_levels(levels, child, depth + 1)

levels = []
get_levels(levels, tree, 0)
print(str(levels))

def get_level_string_length(level):
	total_length = 0
	for inode in range(len(level)):
		total_length += len(level[inode])
		if inode != (len(level) - 1):
			total_length += space_between_nodes

	return total_length

tree_x_size = get_level_string_length(levels[len(levels) - 1])
for level in levels:
	level_x_size = get_level_string_length(level)
	# this will put our string in the center
	prefix_space = int((tree_x_size - level_x_size) / 2)
	level_string = ' ' * prefix_space
	for inode in range(len(level)):
		level_string += level[inode]
		if inode != (len(level) - 1):
			level_string += (' ' * space_between_nodes)
	print(level_string)