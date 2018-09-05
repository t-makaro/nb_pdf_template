import os
import shutil
import nbconvert
import argparse


parser = argparse.ArgumentParser(description='none')
parser.add_argument('--minted', action='store_true')
args = parser.parse_args()

TEMPLATES = {"style_jupyter.tplx", "style_jupyter_minted.tplx",
             "classic.tplx", "classicm.tplx"}


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
        if template == 'style_jupyter_minted.tplx':
            continue
        src = os.path.join(template_path, template)
        shutil.copy(src, dst)

    if args.minted:
        src = os.path.join(template_path, 'style_jupyter_minted.tplx')
        dst_ = os.path.join(dst, 'style_jupyter.tplx')
        shutil.copy(src, dst_)

    print("Success")


if __name__ == "__main__":
    install()
