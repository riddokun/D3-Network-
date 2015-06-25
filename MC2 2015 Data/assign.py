import json

for each row csv
read from, to
if(exist(from, node))
{
	link[i].source = node_index(from)
	if(exist(to, node))
		link[i].target = node_index(to)
	else
	{
		node.push(to)
		link[i].target = node_index(to)
	}
}
else
	node.push(from)
	link[i].source = node_index(from)
	if(exist(to, node))
		link[i].target = node_index(to)
	else
	{
		node.push(to)
		link[i].target = node_index(to)
	}
}
write row in new csv
end