from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(name='nb_pdf_template',
      version='2.0.2',
      description='LaTeX templates for jupyter notebook conversion to pdf',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/t-makaro/nb_pdf_template',
      author='Tyler Makaro',
      author_email='',
      license='MIT',
      packages=['nb_pdf_template'],
      include_package_data=True,
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Development Status :: 5 - Production/Stable',
          'Topic :: Text Processing :: Markup :: LaTeX',
          'Programming Language :: Python',
      ],
      entry_points={'pygments.styles': [
            'jupyter_python = nb_pdf_template:Jupyter_PythonStyle']},
      zip_safe=False)
