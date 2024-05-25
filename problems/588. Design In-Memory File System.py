# link: https://leetcode.com/problems/design-in-memory-file-system/

class FileSystem:

    def __init__(self):
        self.dirs = {}

    def ls(self, path: str) -> List[str]:
        if path == '/':
            return sorted(self.dirs.keys())

        cur = self.dirs
        *paths, final_path = path.split('/')[1:]
        for path in paths:
            cur = cur[path]
        
        if type(cur[final_path]) is str:
            return [final_path]
        else:
            return sorted(cur[final_path].keys())

    def mkdir(self, path: str) -> None:
        folders = path.split('/')[1:]
        cur = self.dirs
        for folder in folders:
            if folder not in cur:
                cur[folder] = {}
            cur = cur[folder]

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self.dirs
        *folders, fileName = filePath.split('/')[1:]
        for folder in folders:
            if folder not in cur:
                cur[folder] = {}
            cur = cur[folder]
        
        if fileName not in cur:
            cur[fileName] = ""
        
        cur[fileName] += content

    def readContentFromFile(self, filePath: str) -> str:
        cur = self.dirs
        *folders, fileName = filePath.split('/')[1:]
        for folder in folders:
            cur = cur[folder]
        
        return cur[fileName]
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)