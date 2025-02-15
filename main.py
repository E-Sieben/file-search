import asyncio
import os

async def findFile (
                    path: str, 
                    fileName: str, 
                    findDifferentNames: bool = False,
                    caseSensitive: bool = False 
                ) -> list[tuple[str, str]]:

    def checkFileName(fileName: str, file: str) -> bool:
        fileName = fileName.split(" ")
        found: bool = False
        for option in fileName:
            if option in file:
                found = True
            elif not findDifferentNames:
                found = False
                break
        return found

    dir: list[str] = os.listdir(path)
    fin: list[tuple[str, str]] = []

    for file in dir:
        if not caseSensitive:
            file = file.lower()
            fileName = fileName.lower()
        if not "." in file:
            try:
                found = await findFile(f"{path}{file}/", fileName)
                for i in found:
                    fin.append(i)
            except:
                pass
        if checkFileName(fileName, file):
            fin.append((path, file))
    return fin

if __name__ == "__main__":
    foundFiles = asyncio.run(findFile(path="./", fileName="main"))
    for i in foundFiles:
        print(f"{i[1]} in {i[0]}")