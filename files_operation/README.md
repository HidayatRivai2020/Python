# Files Operation
Read and manipulate files

## [Open()](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/read_files.py) files
reading file in python use built in function **open()**<br/>
**open()** return value **file object**<br/>
close the file with **close()** method<br/>
<br/>
**open(1, 2)** parameters:
1. filename (mandatory): Path or location of the file
2. mode (optional): combination of the first and second letter
  - First char is how the file will be opened
    - [read (default)](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/read_files.py): read-only mode 
    - [write](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/write_files.py): write in override mode
    - [append](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/write_files.py): write in append mode
    - [read+](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/write_files.py): read and write mode
  - Second char is the type of files
    - text (default): sequence of lines that end with EOL (End Of Line)
    - binary: non-text files 

## [File Objects](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/read_files.py)
#### File Object method:<br/>
- [read()](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/read_files.py): read the value of files and return it as string
  - [size](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/cursor.py) (optional): the number of bytes to return
- [readlines()](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/read_files.py): get the value of file as list and line as item
  - [hint](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/cursor.py) (optional): the limit of line size
- [readline()](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/read_files.py): get one line from the file
  - [size](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/cursor.py) (optional): the limit of line size
- [tell()](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/cursor.py): get the current file position in a file stream
- [seek()](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/cursor.py): set the current file position in a file stream and return the new position
  - [offset](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/cursor.py): number representing the position to set the current file stream position
- [write()](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/write_files.py): set text into file stream
- [close()](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/read_files.py): close the file and set **closed** attribute into **true**

#### File Object attribute:
- [closed](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/read_files.py) (boolean): true if the file is not open

#### [How to read file by line](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/file_by_line.py):
- read file and use **splitlines()** from the **String**
- readlines as List
- readline
- open file and loop the value

## [Cursor](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/read_files.py) <br/>
currently position inside the files<br/>
the position will be updated into "after the last char we read"<br/>
use **tell()** to get the position of cursor<br/>
use **seek()** to set the position of cursor<br/>

## [With](https://github.com/StuAgraricity/python_learning/blob/main/files_operation/with_keyword.py) Keyword
recommended way to read files<br/>
the file will be closed automatically<br/>
the file can't be manipulate outside with block of code<br/>
