import os
import shutil
import nbconvert
from warnings import warn

if nbconvert.__version__ < '5.5':
    warn('Template may not work with your version of nbconvert. '
         'Please either upgrade nbconvert to version >=5.5 '
         'or downgrade nb_pdf_template to <4.')

TEMPLATES = {"classic.tplx", "classicm.tplx"}


def install():
    """Copies the templates into the necessary location to be
    globally accessible to nbconvert.
    """
    nbconvert_path = os.path.dirname(nbconvert.__file__)
    dst = os.path.abspath(os.path.join(nbconvert_path, "templates", "latex"))
    if not os.path.isdir(dst):
        raise OSError("Directory: %s not found." % dst)

    module_path = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.abspath(os.path.join(module_path, "templates"))
    found_templates = os.listdir(template_path)
    if TEMPLATES != set(found_templates):
        raise ValueError("Templates not found")

    for template in TEMPLATES:
        src = os.path.join(template_path, template)
        shutil.copy(src, dst)

    print("Success")


if __name__ == "__main__":
    install()
