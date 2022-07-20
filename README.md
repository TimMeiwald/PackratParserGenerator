[![Tests](https://github.com/TimMeiwald/PackratParserGenerator/actions/workflows/PackratParserGenerator.yml/badge.svg)](https://github.com/TimMeiwald/PackratParserGenerator/actions/workflows/PackratParserGenerator.yml)
# PackratParserGenerator
PackratParserGenerator
TODO: QOL Feature Use uint[0-255] to get all ASCII chars as opposed to current solution  


# [Reproduction Steps]
git clone <repo>    
create venv
pip install pytest
run commands in BuildInstructions.txt      
Navigate to tests\test_grammar_parser\test_Var_Name.py     
Run pytest, note how only "FAILED tests/test_grammar_parser/test_Sequence.py::Test_Sequence::test_Sequence[<This_is_a_name>, <Another_Name>-answer5]" fails    
Remove the """ around the parameterized test.     
Run pytest, note how     
   FAILED tests/test_grammar_parser/test_Var_Name.py::Test_Var_Name::test_A - as...    
   FAILED tests/test_grammar_parser/test_Var_Name.py::Test_Var_Name::test_B - as...    
These tests previously passed when the parameterized test was commented out.     

Also note how running the copy of the code beneath the if __name__ == "__main__" works fine.    
Have also checked that the functools lru_cache is getting cleared by using
print(<method>.cache_info())
Should also clear in _set_src and also added a seperate clear_cache in the test. 
 
 
On windows 10, version "10.0.19041.1806"    
Also fails on Githubs Ubuntu runner    

See Github actions test runs "Commented" and "Uncommented" for evidence of Ubuntu runners failure. 

Have tried rolling back pytest to 7.0.0, didn't work    
Have tried setting up venv again and reinstalling pytest, didn't work    
 

