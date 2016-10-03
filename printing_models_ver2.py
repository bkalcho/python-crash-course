# Author: Bojan G. Kalicanin
# Date: 02-Oct-2016
# Print 3D models for submitted designs

import printing_functions

# Start with some designs that need to be printed
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)