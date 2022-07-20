from core_parser import Rules

def generate_ordered_choice_terminals(func_name: str, args:list):
    nested_binary_ops = ""
    nested_binary_ops += f"args = {args}\n"
    bin_op = "self._ORDERED_CHOICE(position, "
    terminal = "self._TERMINAL"
    nested_binary_ops += "for val in range(0,len(args)-1):\n"
    nested_binary_ops += f"\targ1, arg2 = ({terminal}, args[val]), ({terminal}, args[val+1])\n"
    nested_binary_ops += f"\tposition, bool, node = {bin_op}(arg1, arg2))\n"
    nested_binary_ops += f"\tif(bool == True):\n"
    nested_binary_ops += f"\t\t {func_name}_node = Node('{func_name}')\n"
    nested_binary_ops += f"\t\t {func_name}_node.children.append(node)\n"
    nested_binary_ops += f"\t\t return position, bool, {func_name}_node\n"
    nested_binary_ops += f"\t return position, False, None\n"
    nested_binary_ops = nested_binary_ops.replace("\t", "  ")
    return nested_binary_ops

if __name__ == "__main__":
    args =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    x = generate_ordered_choice_terminals("Alphabet_Upper", args)
    print(x)