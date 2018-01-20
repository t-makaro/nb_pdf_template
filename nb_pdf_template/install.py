import os
import shutil
import nbconvert

templates = {"jupyter.tplx","style_jupyter.tplx","classic.tplx"}
nbconvert_path = os.path.dirname(nbconvert.__file__)
to_path = os.path.abspath(os.path.join(nbconvert_path,"templates","latex"))
if not os.path.isdir(to_path):
    raise OSError("Directory: %s not found." % to_path)

path = os.path.dirname(os.path.realpath(__file__))
from_path = os.path.abspath(os.path.join(path,"templates"))
found_templates = os.listdir(from_path)
if templates != set(found_templates):
    raise ValueError("Templates not found")

for template in templates:
    src = os.path.join(from_path,template)
    shutil.copy(src,to_path)

print("Success")