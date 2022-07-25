[![Tests](https://github.com/TimMeiwald/PackratParserGenerator/actions/workflows/PackratParserGenerator.yml/badge.svg)](https://github.com/TimMeiwald/PackratParserGenerator/actions/workflows/PackratParserGenerator.yml)
# PackratParserGenerator
TODO: QOL Feature Use uint[0-255] to get all ASCII chars as opposed to current solution           
TODO: Implement Pylint/MyPy/Black      
TODO: Error handling, halt start at top level rule and step in find longest match and then return associated error. Generate error framework    
TODO: Implement Parser Generation    
TODO: Generate ParserGenerators Parser with ParserGenerator and Test    
DEFECT: Known issue between string inputs and string from file read. Unsure how to solve or what even the issue is.     


TODO: Return Tuples of Nodes, this would allow me to get rid of _SEQUENCE, _ZERO_OR_MORE and _ONE OR MORE without doing significant extra computation as opposed to currently(dominates parsing time ~ 140% raw parsing time).      
TODO: Do Delete and Passthrough during parsing to minimize compiler time dedicated to rationalizing 
redundant var_names ~ 70% raw parse time.       
TODO: FUTURE: String based inputs, whilst using (a lot)more memory it means you can keep the cache between parsing which should drastically speed up repeated compiles with only minor changes. (If I do this replace LRU_Cache with maxsize with Cache with no size despite being slower(when cache is never filled on LRU cache) per se as it can cache everything). Then test if it is even faster.            