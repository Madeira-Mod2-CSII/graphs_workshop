def bfs(network, source):
    '''
    Purpose: Perform a breadth-first search on network starting
    from the source.

    Parameters:
        network - a graph adjacency list; dict
        source - the node in the network from which to start
        the BFS.

    Return Values:
        distance - the distance from the source to any other node; dict
        predecessor - the predecessor for each note resulting from 
        a BFS run; dict
    '''
    # Dictionaries to track which nodes have been visited,
    # the distance from the source, and the predecessors

    visited = {}
    distance = {}
    predecessor = {}

    # Setup: For each node
    # visited is set to False
    # distance is set to infinity
    # there are no predecessors at this point

    for node in network:
        visited[node] = False
        distance[node] = float("inf")
        predecessor[node] = None
    
    # We now do the setup for the source
    visited[source] = True
    distance[source] = 0
    queue = [source]

    # While the queue has something on it, we will update the
    # information and explore the neighbors of the current node

    while queue != []:
        front = queue.pop(0)

        for neighbor in network[front]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[front] + 1
                predecessor[neighbor] = front
                queue.append(neighbor)
    
    return distance, predecessor

def path(network, source, dest):
    '''
    Purpose: Find a shortest path in network from source to
    destination.

    Parameters:
        network - adjacency list for a graph; dict
        source - the node to start the BFS run
        dest - the node where the desired path will end

    Return Value: a list containing a path from soruce to 
    destination.
    '''

def node_query(network, source, dist):
   
    if dist == 0:
        return [source] if source in network else []

    queue = deque([(source, 0)])
    visited = {source}
    result = []

    while queue:
        current, current_dist = queue.popleft()

        if current_dist == dist:
            result.append(current)
            continue
        
        if current_dist > dist:
            break

        for neighbor in network.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, current_dist + 1))

    return result

def is_connected(network):
    '''
    Purpose: To determine if a graph is connected. That is does
    there exist a path between any pair of nodes in network?

    Parameter:
        network - graph adjacency list; dict
    
    Return Value:
        True - the graph is connected
        False - the graph is not connected
    '''