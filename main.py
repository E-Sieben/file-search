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
                found = await findFile(f"{path}{file}{os.sep}", fileName)
                for i in found:
                    fin.append(i)
            except:
                pass
        if checkFileName(fileName, file):
            fin.append((path, file))
    return fin

if __name__ == "__main__":

    path = input("What is the path you would like to search? (leave blank for base directory) ")
    if path == "":
        path = os.getcwd() + os.sep + ".." + os.sep + ".." + os.sep
        base = True
    fileName = input("What is the file name you are looking for? ")
    foundFiles = asyncio.run(findFile(path = path, fileName = fileName))

    print(f"\nFound {len(foundFiles)} files in {path}:")
    for i in foundFiles:
        print(f"{i[1]} in {f"C:\\{i[0].replace(path, "")}" if base else i[0]}")
    input("Press Enter to close")