class Trie:
    def __init__(self):
        self.children = {}
        self.isFile = False
        self.content = []

class FileSystem:

    def __init__(self):
        self.root_node = Trie()

    def ls(self, path: str) -> List[str]:
        temp=self.root_node
        for p in path.strip().split("/"):
            if p:
                temp = temp.children[p]
        
        if temp.isFile:
            return [p]
        
        result = []
        for child in temp.children:
            result.append(child)
        result.sort()
        return result
        

    def mkdir(self, path: str) -> None:
        temp=self.root_node
        for p in path.split("/"):
            if p:
                if p not in temp.children:
                    temp.children[p] = Trie()
                temp = temp.children[p]            
        
    def addContentToFile(self, filePath: str, content: str) -> None:
        segments = filePath.split("/")
        file_name = segments[-1]
        segments = segments[:-1]
        temp = self.root_node
        for segment in segments:
            if segment:
                temp = temp.children[segment]
        if file_name not in temp.children:
            temp.children[file_name] = Trie()
        temp.children[file_name].content.append(content)
        temp.children[file_name].isFile = True
        

    def readContentFromFile(self, filePath: str) -> str:
        temp=self.root_node
        for p in filePath.split("/"):
            if p:
                temp = temp.children[p]
        return "".join(temp.content)

        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)