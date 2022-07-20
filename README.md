[![Tests](https://github.com/TimMeiwald/PackratParserGenerator/actions/workflows/PackratParserGenerator.yml/badge.svg)](https://github.com/TimMeiwald/PackratParserGenerator/actions/workflows/PackratParserGenerator.yml)
# GPG3
GPG3
TODO: QOL Feature Use uint[0-255] to get all ASCII chars as opposed to current solution  


# [Reproduction Steps]
git clone <repo>  
run commands in BuildInstructions.txt   
Navigate to tests\test_grammar_parser\test_Var_Name.py  
Run pytest, note how only "FAILED tests/test_grammar_parser/test_Sequence.py::Test_Sequence::test_Sequence[<This_is_a_name>, <Another_Name>-answer5]" fails
Remove the """ around the parameterized test. 
Run pytest, note how 
   FAILED tests/test_grammar_parser/test_Var_Name.py::Test_Var_Name::test_A - as...
   FAILED tests/test_grammar_parser/test_Var_Name.py::Test_Var_Name::test_B - as...
These tests previously passed when the parameterized test was commented out. 
  
 On windows 10, version "10.0.19041.1806"

