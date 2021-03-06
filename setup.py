from setuptools import setup

setup(
      name='my_custom_sklearn_transforms',
      version='1.0',
      description='''
            This is a sample python package for encapsulating custom
            tranforms from scikit-learn into Watson Machine Learning
      ''',
      url='https://github.com/JaMinsane/sklearn_transforms/',
      author='James Jaramillo',
      author_email='james.jh03@gmail.com',
      license='BSD',
      packages=[
            'my_custom_sklearn_transforms'
      ],
      install_requires=[
         'impyute==0.0.8'
      ],
      zip_safe=False
)
