class FileNode:
    def __init__(self) -> None:
        self.sons = {}
        self.isFile = False
        self.content = ''
class FileSystem:

    def __init__(self):
        self.root = FileNode()

    def ls(self, path: str) -> List[str]:
        nodes = path.split('/')
        p = self.root
        for node in nodes:
            if node == '':
                continue
            if node not in p.sons:
                p.sons[node] = FileNode()
            p = p.sons[node]
        if p.isFile:
            return [nodes[-1]]
        else:
            result = list(p.sons.keys())
            result.sort()
            return result

    def mkdir(self, path: str) -> None:
        nodes = path.split('/')
        p = self.root
        for node in nodes:
            if node == '':
                continue
            if node not in p.sons:
                p.sons[node] = FileNode()
            p = p.sons[node]
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        nodes = filePath.split('/')
        p = self.root
        for node in nodes:
            if node == '':
                continue
            if node not in p.sons:
                p.sons[node] = FileNode()
            p = p.sons[node]
        p.isFile = True
        p.content += content
        

    def readContentFromFile(self, filePath: str) -> str:
        nodes = filePath.split('/')
        p = self.root
        for node in nodes:
            if node == '':
                continue
            p = p.sons[node]
        return p.content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)