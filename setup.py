from setuptools import setup

setup(name='nb_pdf_template',
      version='1.1.2',
      description='LaTeX templates for jupyter notebook conversion to pdf',
      url='https://github.com/t-makaro/nb_pdf_template',
      author='Tyler Makaro',
      author_email='',
      license='MIT',
      packages=['nb_pdf_template'],
      include_package_data = True,
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
      ],
      zip_safe=False)