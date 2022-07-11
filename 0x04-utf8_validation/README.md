### 0x04. UTF-8 Validation
<p>This project covers the following aspects:</p>
<h6>Write a method that determines if a given data set represents a valid UTF-8 encoding.</h6>
<li>Prototype: def validUTF8(data)
<li>Return: True if data is a valid UTF-8 encoding, else return False
<li>A character in UTF-8 can be 1 to 4 bytes long
T<li>he data set can contain multiple characters
<li>The data will be represented by a list of integers
<li>Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer